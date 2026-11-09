import re, glob, numpy as np
from scipy.stats import chi2_contingency
exec(open('/home/claude/helix/spec.py').read().split("rows=[")[0])
loc={}
for d in ['L3181','L3185','L3213','L3221','L3229']:
    for f in glob.glob('/home/claude/%s/out/*.gff3'%d): loc[f.split('/')[-1][:-5]]=d
loc.pop('NC_005241')
T=np.zeros((2,2)); pos=0; per=[]
for a in sorted(loc):
    d=loc[a]; gb='/home/claude/%s/g/%s.gb'%(d,a); t=open(gb).read()
    seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper()); L=len(seq)
    a8=np.frombuffer(seq.encode(),np.uint8); cs=np.cumsum((a8==71).astype(int)-(a8==67).astype(int))
    ori=int(cs.argmin()); ter=int(cs.argmax())
    def inarc(x):   # True if x lies on the clockwise arc ori -> ter
        return (ori<=x<ter) if ori<ter else (x>=ori or x<ter)
    m_lead=m_n=o_lead=o_n=0
    for l in open('/home/claude/%s/out/%s.gff3'%(d,a)):
        f=l.split('\t')
        if len(f)<7 or f[2]!='CDS': continue
        s,e,st=int(f[3]),int(f[4]),f[6]; mid=(s+e)//2
        lead=(st=='+')==inarc(mid)
        g=seq[s-1:e] if st=='+' else seq[s-1:e].translate(comp)[::-1]
        p=''.join(CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3))
        if re.search(r'C..C',p): m_n+=1; m_lead+=lead
        else: o_n+=1; o_lead+=lead
    T+=[[m_lead,m_n-m_lead],[o_lead,o_n-o_lead]]
    diff=100*(m_lead/m_n-o_lead/o_n); per.append(diff); pos+=diff>0
    print("%s ori %d ter %d | leading: metal %.1f%% (n=%d), other %.1f%% | diff %+.1f"%(a,ori,ter,100*m_lead/m_n,m_n,100*o_lead/o_n,diff))
chi=chi2_contingency(T)
print("POOLED metal-gene leading %.2f%% vs other %.2f%%: diff %+.2f pts, chi2 p=%.2g; positive in %d of %d genomes"%(100*T[0,0]/T[0].sum(),100*T[1,0]/T[1].sum(),100*(T[0,0]/T[0].sum()-T[1,0]/T[1].sum()),chi[1],pos,len(per)))
