import re, glob, numpy as np
exec(open('/home/claude/helix/spec.py').read().split("rows=[")[0])
loc={}
for d in ['L3181','L3185','L3213','L3221','L3229']:
    for f in glob.glob('/home/claude/%s/out/*.gff3'%d): loc[f.split('/')[-1][:-5]]=d
loc.pop('NC_005241'); loc.pop('NC_006448',None) if loc.get('NC_006448')=='L3221' else None
G=sorted(loc); print("genomes",len(G))
M=[('Ni',28,30,'C'),('Cu',29,34,'H'),('Zn',30,34,'C'),('Se',34,46,'C'),('Mo',42,56,'C')]
def nb(S,d): return np.mean([S[d-3],S[d-2],S[d],S[d+1]])
cnt={m[0]:0 for m in M}; detail={m[0]:[] for m in M}
PROT={}
for a in G:
    d=loc[a]; P=proteome('/home/claude/%s/g/%s.gb'%(d,a),'/home/claude/%s/out/%s.gff3'%(d,a)); PROT[a]=P
    SC=spectrum(P,'C',D=60); SH=spectrum(P,'H',D=60)
    for nm,Z,N,r in M:
        S=SC if r=='C' else SH
        rz=S[Z-1]/nb(S,Z); rn=S[N-1]/nb(S,N); ok=(rz>=1.10) or (rn>=1.10)
        cnt[nm]+=ok; detail[nm].append((round(rz,2),round(rn,2)))
for nm,Z,N,r in M: print("%s (Z %d, N %d, %s-%s): genomes clearing +10%% at Z or N: %d of %d"%(nm,Z,N,r,r,cnt[nm],len(G)))
# chance rate of 'either of two distances clears' at random distance pairs d, d' in 20..58
import itertools,random
random.seed(0)
SPC={a:spectrum(PROT[a],'C',D=60) for a in G}
rates=[]
for _ in range(200):
    d1,d2=random.sample(range(22,57),2)
    rates.append(sum((SPC[a][d1-1]/nb(SPC[a],d1)>=1.10) or (SPC[a][d2-1]/nb(SPC[a],d2)>=1.10) for a in G))
print("random distance pairs, Cys-Cys: genomes clearing (median, 5-95%%): %d (%d-%d) of 29"%(np.median(rates),np.percentile(rates,5),np.percentile(rates,95)))
