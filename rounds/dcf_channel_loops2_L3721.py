"""L3721 frozen: robustness and specificity of the H1 CTCF-anchor enrichment of nerve-metal genes (L3717).
argv: GENCODE GTF, H1 bedpe, HFFc6 bedpe. Same gene parsing, channel regex, TSS +-5 kb rule and CTCF-ChIAPET label as L3713.
P1 cluster-merged: genes of a set whose TSSs lie < 100 kb apart (same chromosome, single-linkage) form one unit; a unit is anchored if any
   member is. Channel units vs control units (controls merged the same way). One-sided Fisher (enriched).
P2 specificity: a non-channel neural set NEUR = ^(NRXN[1-3]|NLGN[1-4]X?|CNTNAP[1-5][AB]?|CNTN[1-6]|LRRTM[1-4]|SHANK[1-3]|DLG[1-4]|SYN[1-3]|SYT([1-9]|1[0-7]))$
   vs controls (all protein-coding genes not in channel or NEUR). One-sided Fisher (enriched).
P3 length-matched: for each channel gene, the 10 non-channel, non-NEUR genes with the closest gene length (no reuse); channel vs matched pool.
Reports H1 (graded) and HFFc6 (descriptive)."""
import gzip,re,sys,bisect,collections
from scipy.stats import fisher_exact
CH=re.compile(r'^(KCN[A-Z0-9]+|SCN\d+A|CACNA1[A-Z]|HCN[1-4]|NALCN|GRIN[123][A-D]?|ATP1A[1-4]|ATP2A[1-3]|ATP2B[1-4])$')
NE=re.compile(r'^(NRXN[1-3]|NLGN[1-4]X?|CNTNAP[1-5][AB]?|CNTN[1-6]|LRRTM[1-4]|SHANK[1-3]|DLG[1-4]|SYN[1-3]|SYT([1-9]|1[0-7]))$')
G={}
for l in gzip.open(sys.argv[1],'rt'):
    if l.startswith('#'): continue
    x=l.split('\t')
    if x[2]!='gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$',x[0]): continue
    n=re.search(r'gene_name "([^"]+)"',x[8]).group(1); G[n]=(x[0],int(x[3]) if x[6]=='+' else int(x[4]),int(x[4])-int(x[3]))
ch=[n for n in G if CH.match(n)]; ne=[n for n in G if NE.match(n)]; ct=[n for n in G if not CH.match(n) and not NE.match(n)]
print('genes',len(G),'channel',len(ch),'neural non-channel',len(ne),'controls',len(ct))
def anchors(p):
    A=collections.defaultdict(list)
    for l in open(p):
        f=l.rstrip('\n').split('\t')
        if 'CTCF-ChIAPET' in f[6].split(','): A[f[0]].append((int(f[1]),int(f[2]))); A[f[3]].append((int(f[4]),int(f[5])))
    for c in A: A[c].sort()
    return A
def hit(A,n):
    c,t,_=G[n]; L=A.get(c,[]); i=bisect.bisect_left(L,(t-5000-10**7,0))
    while i<len(L) and L[i][0]<=t+5000:
        if L[i][1]>=t-5000: return True
        i+=1
    return False
def units(names):
    by=collections.defaultdict(list)
    for n in names: by[G[n][0]].append((G[n][1],n))
    U=[]
    for c,v in by.items():
        v.sort(); cur=[v[0][1]]
        for (t0,_),(t1,n1) in zip(v,v[1:]):
            if t1-t0<100000: cur.append(n1)
            else: U.append(cur); cur=[n1]
        U.append(cur)
    return U
def fisher(A,B,lab):
    a=sum(A);b=len(A)-a;c=sum(B);d=len(B)-c; o,p=fisher_exact([[a,b],[c,d]],alternative='greater')
    print('  %-34s %d/%d = %.3f vs %d/%d = %.3f  OR %.2f  p(enriched) %.2g'%(lab,a,a+b,a/(a+b),c,c+d,c/(c+d),o,p),flush=True); return o,p
srt=sorted(ct,key=lambda n:G[n][2]); L=[G[n][2] for n in srt]; used=set(); pool=[]
for n in ch:
    i=bisect.bisect_left(L,G[n][2]); lo,hi=i-1,i; got=0
    while got<10:
        cand=[]
        if lo>=0: cand.append(lo)
        if hi<len(srt): cand.append(hi)
        j=min(cand,key=lambda k:abs(L[k]-G[n][2]))
        if j==lo: lo-=1
        else: hi+=1
        if srt[j] not in used: used.add(srt[j]); pool.append(srt[j]); got+=1
print('median length: channel %d, matched pool %d, all controls %d'%(sorted(G[n][2] for n in ch)[len(ch)//2],sorted(G[n][2] for n in pool)[len(pool)//2],sorted(L)[len(L)//2]))
for cell,p in [('H1',sys.argv[2]),('HFFc6',sys.argv[3])]:
    A=anchors(p); print('##',cell)
    o1,p1=fisher([any(hit(A,n) for n in u) for u in units(ch)],[any(hit(A,n) for n in u) for u in units(ct)],'P1 cluster-merged units')
    o2,p2=fisher([hit(A,n) for n in ne],[hit(A,n) for n in ct],'P2 neural non-channel vs controls')
    o3,p3=fisher([hit(A,n) for n in ch],[hit(A,n) for n in pool],'P3 channel vs length-matched')
    if cell=='H1': H=(o1,p1,o2,p2,o3,p3)
o1,p1,o2,p2,o3,p3=H
print('RESULT',[('P1','PASS' if o1>1 and p1<0.05 else 'FAIL'),('P2','PASS' if o2>1 and p2<0.05 else 'FAIL'),('P3','PASS' if o3>1 and p3<0.05 else 'FAIL')])
