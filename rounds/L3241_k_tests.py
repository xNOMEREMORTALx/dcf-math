import re, glob, numpy as np
loc={}
for d in ['L3181','L3185','L3213','L3221','L3229','L3241']:
    for f in glob.glob('/home/claude/%s/out/*.gff3'%d): loc[f.split('/')[-1][:-5]]=d
loc.pop('NC_005241',None)
print("genomes",len(loc))
cnt={37:0,41:0,43:0}; N=0
k2=k3=k4=0
for a in sorted(loc):
    d=loc[a]; t=open('/home/claude/%s/g/%s.gb'%(d,a)).read()
    seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
    for l in open('/home/claude/%s/out/%s.gff3'%(d,a)):
        f=l.split('\t')
        if len(f)>6 and f[2]=='CDS':
            L=(int(f[4])-int(f[3])+1)//3-1; N+=1
            for m in cnt: cnt[m]+=(L%m==0)
    s=np.frombuffer(seq.encode(),np.uint8); ok=(s!=78)
    def ident(k): m=ok[:-k]&ok[k:]; return np.mean(s[:-k][m]==s[k:][m])
    def test(k,ctrl): return ident(k)>np.mean([ident(c) for c in ctrl])
    r2=test(41,[35,38,44,47]); r3=test(401,[395,398,404,407]); r4=test(153,[147,150,156,159])
    k2+=r2; k3+=r3; k4+=r4
print("K1 ratio (fraction divisible by m) x m:",{m:round(cnt[m]/N*m,3) for m in cnt},"proteins",N)
print("K2 lag 41 above controls in %d of %d genomes"%(k2,len(loc)))
print("K3 lag 401 above controls in %d of %d"%(k3,len(loc)))
print("K4 lag 153 above controls in %d of %d"%(k4,len(loc)))
