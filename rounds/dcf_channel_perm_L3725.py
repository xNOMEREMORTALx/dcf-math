"""L3725 frozen: genome-shift permutation test of the channel-gene CTCF-anchor excess (L3717). argv: GENCODE GTF, H1 bedpe, HFFc6 bedpe.
Genes, channel regex and the TSS +-5 kb rule as L3713. Statistic D = (share of channel genes whose TSS is at a CTCF-ChIAPET anchor) -
(same share among all other protein-coding genes). Null: for each chromosome, every anchor is shifted by one common offset u ~ U[0, L_c)
(L_c = largest coordinate seen on that chromosome + 1; positions wrap modulo L_c); 1,000 shifts, numpy seed 3725.
p = (1 + #{null D >= observed D}) / (1 + 1000)."""
import gzip,re,sys,collections
import numpy as np
CH=re.compile(r'^(KCN[A-Z0-9]+|SCN\d+A|CACNA1[A-Z]|HCN[1-4]|NALCN|GRIN[123][A-D]?|ATP1A[1-4]|ATP2A[1-3]|ATP2B[1-4])$')
G=[]; Lc=collections.defaultdict(int)
for l in gzip.open(sys.argv[1],'rt'):
    if l.startswith('#'): continue
    x=l.split('\t')
    if x[2]!='gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$',x[0]): continue
    n=re.search(r'gene_name "([^"]+)"',x[8]).group(1); t=int(x[3]) if x[6]=='+' else int(x[4]); G.append((x[0],t,bool(CH.match(n)))); Lc[x[0]]=max(Lc[x[0]],int(x[4]))
def anchors(p):
    A=collections.defaultdict(list)
    for l in open(p):
        f=l.rstrip('\n').split('\t')
        if 'CTCF-ChIAPET' in f[6].split(','): A[f[0]].append((int(f[1]),int(f[2]))); A[f[3]].append((int(f[4]),int(f[5])))
    return A
def hits(A,off):
    H=np.zeros(len(G),bool); byc=collections.defaultdict(list)
    for i,(c,t,_) in enumerate(G): byc[c].append(i)
    for c,idx in byc.items():
        if c not in A: continue
        a=np.array(A[c]); L=Lc[c]; s=(a[:,0]+off.get(c,0))%L; e=s+(a[:,1]-a[:,0])
        o=np.argsort(s); s=s[o]-5000; e=e[o]+5000; me=np.maximum.accumulate(e)
        T=np.array([G[i][1] for i in idx]); k=np.searchsorted(s,T,side='right')-1
        H[idx]=(k>=0)&(me[np.maximum(k,0)]>=T)
    return H
isch=np.array([g[2] for g in G]); rng=np.random.default_rng(3725)
print('genes',len(G),'channel',isch.sum())
for cell,p in [('H1',sys.argv[2]),('HFFc6',sys.argv[3])]:
    A=anchors(p)
    for c in A: Lc[c]=max(Lc[c],max(e for _,e in A[c]))
    D=lambda H:H[isch].mean()-H[~isch].mean()
    d0=D(hits(A,{})); null=np.array([D(hits(A,{c:int(rng.integers(0,Lc[c])) for c in A})) for _ in range(1000)])
    pv=(1+(null>=d0).sum())/1001
    print('%-6s observed D %.4f | null mean %.4f sd %.4f 95th %.4f | p %.4f'%(cell,d0,null.mean(),null.std(),np.percentile(null,95),pv),flush=True)
