"""L3729 frozen: partners of CTCF-ChIAPET loops anchored at nerve-metal gene TSSs (+-5 kb). argv: GENCODE GTF, H1 bedpe, HFFc6 bedpe.
For each such loop, the other anchor is classed: 'channel' (at another channel-gene TSS), 'gene' (at any other protein-coding TSS), 'none'.
Comparison: the same classing for CTCF loops anchored at control-gene TSSs ('channel' and 'gene' merged as 'TSS'). Loops are counted once each."""
import gzip,re,sys,collections,bisect
from scipy.stats import fisher_exact
CH=re.compile(r'^(KCN[A-Z0-9]+|SCN\d+A|CACNA1[A-Z]|HCN[1-4]|NALCN|GRIN[123][A-D]?|ATP1A[1-4]|ATP2A[1-3]|ATP2B[1-4])$')
T=collections.defaultdict(list)
for l in gzip.open(sys.argv[1],'rt'):
    if l.startswith('#'): continue
    x=l.split('\t')
    if x[2]!='gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$',x[0]): continue
    n=re.search(r'gene_name "([^"]+)"',x[8]).group(1); T[x[0]].append((int(x[3]) if x[6]=='+' else int(x[4]),n))
for c in T: T[c].sort()
def at(c,s,e):
    L=T.get(c,[]); i=bisect.bisect_left(L,(s-5000,'')); out=[]
    while i<len(L) and L[i][0]<=e+5000: out.append(L[i][1]); i+=1
    return out
for cell,p in [('H1',sys.argv[2]),('HFFc6',sys.argv[3])]:
    cls=collections.Counter(); ctl=collections.Counter(); pairs=[]; dist=[]
    for l in open(p):
        f=l.rstrip('\n').split('\t')
        if 'CTCF-ChIAPET' not in f[6].split(','): continue
        A=at(f[0],int(f[1]),int(f[2])); B=at(f[3],int(f[4]),int(f[5]))
        for X,Y in ((A,B),(B,A)):
            if any(CH.match(n) for n in X):
                k='channel' if any(CH.match(n) for n in Y if n not in X) else ('gene' if Y else 'none'); cls[k]+=1
                if k=='channel': pairs.append((','.join(n for n in X if CH.match(n)),','.join(n for n in Y if CH.match(n)),int(f[4])-int(f[1])))
            elif X: ctl['TSS' if Y else 'none']+=1
    a=cls['channel']+cls['gene']; b=cls['none']; c=ctl['TSS']; d=ctl['none']; o,pv=fisher_exact([[a,b],[c,d]],alternative='greater')
    print('%s channel-anchored loop ends %d: partner channel %d (%.3f), other gene %d, none %d | control partner-at-TSS %.3f | OR %.2f p %.2g'%(
        cell,sum(cls.values()),cls['channel'],cls['channel']/max(1,sum(cls.values())),cls['gene'],cls['none'],c/(c+d),o,pv),flush=True)
    for x in sorted(set(pairs)): print('   PAIR',cell,*x)
