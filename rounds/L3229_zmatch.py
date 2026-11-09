import sys, re, json, numpy as np
sys.argv=['x']; 
exec(open('/home/claude/helix/spec.py').read().split("rows=[")[0])   # reuse proteome(), spectrum()
R0=json.load(open('/home/claude/helix/R.json'))
rich=[a for a in R0 if R0[a]['d']>=0.60]; poor=[a for a in R0 if R0[a]['d']<=0.40]
import glob
loc={}
for d in ['L3181','L3185','L3213','L3221']:
    for f in glob.glob('/home/claude/%s/out/*.gff3'%d): loc[f.split('/')[-1][:-5]]=d
def nb(S,d): return np.mean([S[d-3],S[d-2],S[d],S[d+1]])   # S index = d-1
res={}; posrich=[]
for a in rich+poor:
    d=loc[a]; P=proteome('/home/claude/%s/g/%s.gb'%(d,a),'/home/claude/%s/out/%s.gff3'%(d,a))
    S=spectrum(P,'C',D=62)
    res[a]={k:S[k-1]/nb(S,k) for k in (26,30,56)}
    # base rate: fraction of d in 20..58 with S/nb >= 1.10
    res[a]['base']=np.mean([S[k-1]/nb(S,k)>=1.10 for k in range(20,59)])
    if a in rich:
        for p in P:
            m=re.search(r'C..C',p)
            if m: posrich.append(m.start()+1)
for k in (26,30,56):
    n=sum(res[a][k]>=1.10 for a in rich)
    print("d=%d: rich genomes with >=+10%%: %d of %d  (poor: %d of %d)  ratios rich: %s"%(k,n,len(rich),sum(res[a][k]>=1.10 for a in poor),len(poor),[round(res[a][k],2) for a in rich]))
print("base rate (d 20-58, rich) %.2f, (poor) %.2f"%(np.mean([res[a]['base'] for a in rich]),np.mean([res[a]['base'] for a in poor])))
c=np.bincount(posrich,minlength=40)
print("first-CxxC start position counts 22..30:",{i:int(c[i]) for i in range(22,31)}, "ratio at 26: %.2f"%(c[26]/np.mean([c[24],c[25],c[27],c[28]])))
