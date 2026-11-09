import re, glob, numpy as np, json
from scipy.stats import mannwhitneyu
CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
comp=str.maketrans('ACGTN','TGCAN')
FD=re.compile(r'C(?=..C..C...C)')
def proteome(gb,gff):
    t=open(gb).read(); seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
    out=[]
    for l in open(gff):
        f=l.split('\t')
        if len(f)>6 and f[2]=='CDS':
            a,b_,s=int(f[3]),int(f[4]),f[6]; g=seq[a-1:b_] if s=='+' else seq[a-1:b_].translate(comp)[::-1]
            out.append(''.join(CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3)))
    return out
def mask_fd(p):
    p=list(p)
    for m in re.finditer(r'(?=(C..C..C...C))',''.join(p)):
        i=m.start()
        for k in (0,3,6,10): p[i+k]='X'
    return ''.join(p)
def spectrum(P,res,D=24):
    O=np.zeros(D+1); E=np.zeros(D+1)
    for p in P:
        pos=np.array([i for i,c in enumerate(p) if c==res]); L=len(p); n=len(pos)
        if n<2 or L<D+2: continue
        diff=(pos[None,:]-pos[:,None]); diff=diff[diff>0]; diff=diff[diff<=D]
        O+=np.bincount(diff,minlength=D+1)
        npairs=n*(n-1)/2; tot=L*(L-1)/2
        E+=np.array([npairs*(L-d)/tot for d in range(D+1)])
    return O[1:]/np.maximum(E[1:],1e-9)
def power(S,period=3.6):
    d=np.arange(1,len(S)+1); x=S-S.mean(); return abs(np.sum(x*np.exp(2j*np.pi*d/period)))**2
rows=[l.split() for l in open('/home/claude/L3213/tool_numbers.txt').read().splitlines()[2:]]+[l.split() for l in open('/home/claude/L3221/tool_numbers.txt').read().splitlines()[2:]]+[l.split() for l in open('/home/claude/L3185/tool_numbers.txt').read().splitlines()[2:]]
dens={r[0]:float(r[3]) for r in rows}
for l in open('/home/claude/L3181/tool_numbers.txt').read().splitlines()[2:]:
    r=l.split(); dens[r[0]]=float(r[3])
dens.pop('NC_005241',None)
loc={}
for d in ['L3181','L3185','L3213','L3221']:
    for f in glob.glob('/home/claude/%s/out/*.gff3'%d): loc[f.split('/')[-1][:-5]]=d
R={}
for a,v in dens.items():
    d=loc[a]; P=proteome('/home/claude/%s/g/%s.gb'%(d,a),'/home/claude/%s/out/%s.gff3'%(d,a))
    Sc=spectrum(P,'C'); Sm=spectrum([mask_fd(p) for p in P],'C'); Sk=spectrum(P,'K')
    R[a]=dict(d=v,oe6=Sc[5],oe10=Sc[9],oe3=Sc[2],p36=power(Sm),pk=power(Sk),spec=list(Sc),specm=list(Sm))
json.dump(R,open('/home/claude/helix/R.json','w'))
rich=[a for a in R if R[a]['d']>=0.60]; poor=[a for a in R if R[a]['d']<=0.40]
print("rich",len(rich),"poor",len(poor))
for k in ['oe6','oe10','p36','pk','oe3']:
    x=[R[a][k] for a in rich]; y=[R[a][k] for a in poor]
    alt='two-sided' if k=='pk' else 'greater'
    print(k,"rich median %.3f poor median %.3f  MW p(%s)=%.4f"%(np.median(x),np.median(y),alt,mannwhitneyu(x,y,alternative=alt).pvalue))
