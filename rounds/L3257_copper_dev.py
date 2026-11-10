import re, glob, collections
CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
comp=str.maketrans('ACGTN','TGCAN')
MOT={'T1Cu C.{2,4}H.{3,4}M':r'(?=C.{2,4}H.{3,4}M)','CuA C.E.C...H..M':r'(?=C.E.C...H..M)','MCO H.H.{30,120}H.H':None,'HxHxxxxxxxHxH':r'(?=H.H.{6,8}H.H)'}
CU=re.compile(r'azurin|plastocyanin|cupredoxin|copper|cytochrome c oxidase subunit (II|2)|cytochrome c oxidase subunit I\b|multicopper|laccase|nitrosocyanin|amicyanin|CueO|nitrite reductase.{0,10}(NO-forming|copper)|cbb3|heme-copper|nitrous-oxide reductase|NosZ|ammonia monooxygenase|methane monooxygenase|ubiquinol oxidase subunit (II|2)|bo3',re.I)
def load(d,a):
    t=open('/home/claude/%s/g/%s.gb'%(d,a)).read()
    seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
    A=[]
    for m in re.finditer(r'\n     CDS             (complement\()?<?(\d+)\.\.>?(\d+)\)?\n(.*?)(?=\n     \S)',t,re.S):
        pr=re.search(r'/product="([^"]*)"',m.group(4)); A.append((int(m.group(2)),int(m.group(3)),'-' if m.group(1) else '+',(pr.group(1) if pr else '').replace('\n                     ',' ')))
    P=[]
    for l in open('/home/claude/%s/out/%s.gff3'%(d,a)):
        f=l.split('\t')
        if len(f)>6 and f[2]=='CDS':
            x,y,s=int(f[3]),int(f[4]),f[6]; g=seq[x-1:y] if s=='+' else seq[x-1:y].translate(comp)[::-1]
            P.append((x,y,s,''.join(CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3))))
    return P,A
def product(p,A):
    x,y,s,_=p; best=''
    for a,b,t,pr in A:
        if t==s and a<=y and b>=x and min(b,y)-max(a,x)+1>=0.5*(y-x+1): return pr
    return ''
G=[('L3181','NC_004129'),('L3181','NC_002927'),('L3181','NC_008313'),('L3213','NC_009720'),('L3221','NC_008095'),('L3241','NC_009441'),('L3213','NC_007614'),('L3213','NC_013422'),
   ('L3181','NC_012108'),('L3181','NC_016894'),('L3241','NC_007681'),('L3181','NC_008531')]
tot=collections.Counter(); hitcu=collections.Counter(); cuprot_total=0; cuprot_found=collections.Counter()
for d,a in G:
    P,A=load(d,a)
    cuprods=set()
    for p in P:
        pr=product(p,A); iscu=bool(CU.search(pr))
        if iscu: cuprot_total+=1
        for name,rx in MOT.items():
            if rx is None: continue
            if re.search(rx,p[3]):
                tot[name]+=1; hitcu[name]+=iscu
                if iscu: cuprot_found[name]+=1
for name in MOT:
    if MOT[name] is None: continue
    print("%-22s hits %4d  copper-annotated among hits %3d (%.0f%%)  recall of copper-annotated proteins %d/%d"%(name,tot[name],hitcu[name],100*hitcu[name]/max(tot[name],1),cuprot_found[name],cuprot_total))
