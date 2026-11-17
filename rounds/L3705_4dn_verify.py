"""L3705: independent recount of the 4D report's audit numbers from the two Zenodo BEDPE files (argv: H1 file, HFFc6 file). Own code, not the report's."""
import sys,collections,statistics,bisect
def load(p):
    R=[]
    for l in open(p):
        c1,s1,e1,c2,s2,e2,pl=l.rstrip('\n').split('\t'); a=(c1,int(s1),int(e1)); b=(c2,int(s2),int(e2))
        if b<a: a,b=b,a
        R.append((a,b,tuple(sorted(set(pl.split(','))))))
    return R
def q(v,p):
    v=sorted(v); x=p*(len(v)-1); lo=int(x); hi=min(lo+1,len(v)-1); return v[lo]+(x-lo)*(v[hi]-v[lo])
D={}
for name,p in zip(['H1ESC','HFFc6'],sys.argv[1:3]):
    R=load(p); D[name]=R; cis=[r for r in R if r[0][0]==r[1][0]]
    sp=[abs((b[1]+b[2]-a[1]-a[2])/2) for a,b,_ in cis]
    plat=collections.Counter(x for *_,pl in R for x in pl); sup=collections.Counter(len(pl) for *_,pl in R)
    print(name,'loops',len(R),'unique pairs',len({(a,b) for a,b,_ in R}),'cis',len(cis),'trans',len(R)-len(cis))
    print('  span quantiles 0.25/0.5/0.75:',q(sp,.25),q(sp,.5),q(sp,.75),'| <50kb',sum(s<50000 for s in sp),'<100kb',sum(s<100000 for s in sp),'>=1Mb',sum(s>=1e6 for s in sp))
    print('  platforms',dict(sorted(plat.items())),'| support',dict(sorted(sup.items())),'| single-platform %.4f'%(sup[1]/len(R)))
ex=len({(a,b) for a,b,_ in D['H1ESC']}&{(a,b) for a,b,_ in D['HFFc6']}); print('exact shared interval pairs',ex)
def mids(R): return [(a[0],b[0],(a[1]+a[2])/2,(b[1]+b[2])/2) for a,b,_ in R]
def frac(Q,T,tol):
    idx=collections.defaultdict(list)
    for c1,c2,x,y in T: idx[(c1,c2)].append((x,y))
    for k in idx: idx[k].sort()
    m=0
    for c1,c2,x,y in Q:
        L=idx.get((c1,c2),[]); i=bisect.bisect_left(L,(x-tol,-1e18)); f=False
        while i<len(L) and L[i][0]<=x+tol:
            if abs(L[i][1]-y)<=tol: f=True; break
            i+=1
        m+=f
    return m/len(Q)
M={k:mids(v) for k,v in D.items()}
for tol in (2000,5000,10000,15000): print('tol',tol,'H1->HFF %.4f'%frac(M['H1ESC'],M['HFFc6'],tol),'HFF->H1 %.4f'%frac(M['HFFc6'],M['H1ESC'],tol))
