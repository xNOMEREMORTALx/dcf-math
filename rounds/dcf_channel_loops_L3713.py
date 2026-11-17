"""L3713 frozen: are nerve-metal genes at loop anchors more or less often than other protein-coding genes?
argv: GENCODE GTF (gz), H1 bedpe, HFFc6 bedpe. Genes: gene_type protein_coding, autosomes + X. TSS = gene start (+) or end (-).
Channel set = gene_name matching ^(KCN[A-Z0-9]+|SCN\d+A|CACNA1[A-Z]|HCN[1-4]|NALCN|GRIN[123][A-D]?|ATP1A[1-4]|ATP2A[1-3]|ATP2B[1-4])$ ; controls = all other protein-coding genes.
A gene is "anchored" by a loop class if its TSS +-5 kb overlaps either anchor of a loop carrying that platform label.
Loop classes: CTCF-ChIAPET (structural) and H3K4me3-PLACSeq (active-promoter). One-sided Fisher tests, both directions reported; odds ratio."""
import gzip,re,sys,bisect,collections
from scipy.stats import fisher_exact
CH=re.compile(r'^(KCN[A-Z0-9]+|SCN\d+A|CACNA1[A-Z]|HCN[1-4]|NALCN|GRIN[123][A-D]?|ATP1A[1-4]|ATP2A[1-3]|ATP2B[1-4])$')
G={}
for l in gzip.open(sys.argv[1],'rt'):
    if l.startswith('#'): continue
    x=l.split('\t')
    if x[2]!='gene' or 'gene_type "protein_coding"' not in x[8]: continue
    c=x[0]
    if not re.match(r'^chr([0-9]+|X)$',c): continue
    n=re.search(r'gene_name "([^"]+)"',x[8]).group(1); t=int(x[3]) if x[6]=='+' else int(x[4]); G[n]=(c,t)
print('protein-coding genes',len(G),'channel set',sum(bool(CH.match(n)) for n in G))
for cell,p in [('H1',sys.argv[2]),('HFFc6',sys.argv[3])]:
    for lab in ['CTCF-ChIAPET','H3K4me3-PLACSeq']:
        A=collections.defaultdict(list)
        for l in open(p):
            f=l.rstrip('\n').split('\t')
            if lab in f[6].split(','):
                A[f[0]].append((int(f[1]),int(f[2]))); A[f[3]].append((int(f[4]),int(f[5])))
        for c in A: A[c].sort()
        def hit(c,t):
            L=A.get(c,[]); i=bisect.bisect_left(L,(t-5000-10**7,0))
            while i<len(L) and L[i][0]<=t+5000:
                if L[i][1]>=t-5000: return True
                i+=1
            return False
        tab=collections.Counter((bool(CH.match(n)),hit(c,t)) for n,(c,t) in G.items())
        a,b,cc,d=tab[(True,True)],tab[(True,False)],tab[(False,True)],tab[(False,False)]
        orr,pg=fisher_exact([[a,b],[cc,d]],alternative='greater'); _,pl=fisher_exact([[a,b],[cc,d]],alternative='less')
        print('%-6s %-16s channel %d/%d = %.3f  control %d/%d = %.3f  OR %.2f  p(enriched) %.2g  p(depleted) %.2g'%(cell,lab,a,a+b,a/(a+b),cc,cc+d,cc/(cc+d),orr,pg,pl),flush=True)
