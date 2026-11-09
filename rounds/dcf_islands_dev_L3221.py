# Label-free Fe-S island finder (development): sliding windows of W consecutive predicted genes, CxxC per 1000 aa;
# flag windows with z >= Z vs the genome's own window distribution; then (grading only) read annotation products in flagged windows.
import sys, re, json, random
CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
comp=str.maketrans('ACGTN','TGCAN')
KEY=re.compile(r'(?<!de)hydrogenase|formate dehydrogenase|ferredoxin|nitrogenase|carbon[- ]monoxide dehydrogenase|sulfite reductase|adenylyl-?sulfate reductase|heterodisulfide|4Fe-4S|2Fe-2S|iron-sulfur|\(Fe-S\)|Fe-S cluster|radical SAM|pyruvate synthase|pyruvate:ferredoxin|2-oxoacid:ferredoxin|Rnf|Fe-only',re.I)
def load(gb,gff):
    t=open(gb).read(); seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
    P=sorted((int(f[3]),int(f[4]),f[6]) for f in (l.split('\t') for l in open(gff)) if len(f)>6 and f[2]=='CDS')
    A=[]
    for m in re.finditer(r'\n     CDS             (complement\()?<?(\d+)\.\.>?(\d+)\)?\n(.*?)(?=\n     \S)',t,re.S):
        pr=re.search(r'/product="([^"]*)"',m.group(4)); A.append((int(m.group(2)),int(m.group(3)),(pr.group(1) if pr else '').replace('\n                     ',' ')))
    return seq,P,A
def prot(seq,a,b,s):
    g=seq[a-1:b] if s=='+' else seq[a-1:b].translate(comp)[::-1]
    return ''.join(CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3))
def windows(seq,P,W):
    cx=[]; ln=[]
    for a,b,s in P:
        p=prot(seq,a,b,s); cx.append(len(re.findall(r'(?=C..C)',p))); ln.append(len(p))
    D=[]
    for i in range(len(P)-W+1):
        D.append(1000*sum(cx[i:i+W])/max(sum(ln[i:i+W]),1))
    return D
def run(gb,gff,W=10,Z=3.0):
    seq,P,A=load(gb,gff); D=windows(seq,P,W)
    mu=sum(D)/len(D); sd=(sum((x-mu)**2 for x in D)/len(D))**.5
    flag=[i for i,x in enumerate(D) if (x-mu)/sd>=Z]
    # merge flagged windows into islands (gene index ranges)
    isl=[]
    for i in flag:
        if isl and i<=isl[-1][1]: isl[-1][1]=i+W-1
        else: isl.append([i,i+W-1])
    def keyfrac(lo,hi):
        a0,b0=P[lo][0],P[hi][1]; prods=[p for a,b,p in A if a<=b0 and b>=a0]
        return prods, sum(bool(KEY.search(p)) for p in prods)
    res=[]
    for lo,hi in isl:
        prods,k=keyfrac(lo,hi); res.append((P[lo][0],P[hi][1],k,len(prods),[p for p in prods if KEY.search(p)][:4]))
    # baseline: random windows of the same gene length
    random.seed(1); base=[]
    for _ in range(300):
        L=random.choice([hi-lo for lo,hi in isl]) if isl else W
        lo=random.randrange(0,len(P)-L-1); prods,k=keyfrac(lo,lo+L); base.append(k>0)
    allk=sum(bool(KEY.search(p)) for a,b,p in A)/max(len(A),1)
    ing=sum(r[2] for r in res); inn=sum(r[3] for r in res)
    return res, sum(base)/len(base), mu, sd, allk, (ing/inn if inn else 0)
if __name__=='__main__':
    out={}
    for gb,gff in zip(sys.argv[1::2],sys.argv[2::2]):
        res,bl,mu,sd,allk,isk=run(gb,gff); a=gb.split('/')[-1][:-3]
        hit=sum(r[2]>0 for r in res)
        print("%s islands %d; with keyword %d (%.0f%%) vs random windows %.0f%% | genes with keyword: islands %.1f%% vs genome %.1f%% (x%.1f)"%(a,len(res),hit,100*hit/max(len(res),1),100*bl,100*isk,100*allk,isk/allk if allk else 0))
        for r in res[:0]: print("   ",r[0],r[1],"kw %d/%d"%(r[2],r[3]),r[4])
