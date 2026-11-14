"""L3489 grading of PREREGISTERED_L3485_navcav V1-V4. Truth: UniProt automatic protein names."""
import gzip,collections
N={}; O={}
for l in gzip.open('/home/claude/L3489/z/navcav.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t')
    if len(f)>=4: N[f[0]]=f[2].lower(); O[f[0]]=f[1]
keep=[l.split('\t')[0] for l in open('/home/claude/L3489/z/navcav_filtered.tsv').read().splitlines()[1:]]
def truth(a):
    n=N[a]
    if 'calcium channel subunit alpha' in n: return 'Ca'
    if 'sodium channel protein' in n and 'calcium' not in n: return 'Na'
    return None
def load(f):
    c={}
    for l in open(f):
        x=l.split()
        if x and x[0] in('Na','Ca'): c[x[1]]=x[0]
    return c
R=[]; out={}
for v,f in [('v7','rounds/L3489_v7_tool.txt'),('v6','rounds/L3489_v6_tool.txt')]:
    c=load(f); T={a:truth(a) for a in keep if truth(a)}
    called=[a for a in T if a in c]; swaps=[a for a in called if c[a]!=T[a]]
    na=[a for a in T if T[a]=='Na']; ca=[a for a in T if T[a]=='Ca']
    nar=sum(c.get(a)=='Na' for a in na); car=sum(c.get(a)=='Ca' for a in ca)
    out[v]=len(swaps)
    print('%s: truth Na %d, Ca %d | called %d | swaps %d (%.2f%%) | Na recall %d/%d = %.1f%% | Ca recall %d/%d = %.1f%%'%(v,len(na),len(ca),len(called),len(swaps),100*len(swaps)/len(called),nar,len(na),100*nar/len(na),car,len(ca),100*car/len(ca)))
    sw=collections.Counter((T[a],c[a],N[a][:55]) for a in swaps)
    for k,n in sw.most_common(12): print('    swap x%d  truth %s -> called %s  | %s'%(n,k[0],k[1],k[2]))
    if v=='v7':
        R+= [('V1','PASS' if len(swaps)/len(called)<=0.01 else 'FAIL'),('V2','PASS' if nar/len(na)>=.9 else 'FAIL'),('V3','PASS' if car/len(ca)>=.9 else 'FAIL')]
R.append(('V4','ungradeable' if out['v6']==0 else ('PASS' if out['v7']<out['v6'] else 'FAIL')))
print('RESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable')
