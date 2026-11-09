import re, glob, numpy as np
comp=str.maketrans('ACGTN','TGCAN')
loc={}
for d in ['L3181','L3185','L3213','L3221','L3229','L3241']:
    for f in glob.glob('/home/claude/%s/out/*.gff3'%d): loc[f.split('/')[-1][:-5]]=d
loc.pop('NC_005241',None)
PER=[3,11,12,19,20,23,24,26,29,30,34,39,40,56,63,64]
def ratio(s,p):
    k=round(4100/p); W=p*k
    a=np.frombuffer(s.encode(),np.uint8); n=len(a)//W; a=a[:n*W].reshape(n,W); P=np.zeros(W//2+1)
    for b in b'ACGT':
        x=(a==b).astype(float); x-=x.mean(1,keepdims=True); P+=(np.abs(np.fft.rfft(x,axis=1))**2).mean(0)
    return P[k]/np.mean(np.r_[P[k-8:k-2],P[k+3:k+9]])
cnt={(p,ds):0 for p in PER for ds in 'ab'}; R={(p,ds):[] for p in PER for ds in 'ab'}
for a in sorted(loc):
    d=loc[a]; t=open('/home/claude/%s/g/%s.gb'%(d,a)).read()
    seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
    cds=[]
    for l in open('/home/claude/%s/out/%s.gff3'%(d,a)):
        f=l.split('\t')
        if len(f)>6 and f[2]=='CDS':
            x,y=int(f[3]),int(f[4]); g=seq[x-1:y]; cds.append(g if f[6]=='+' else g.translate(comp)[::-1])
    cd=''.join(cds)
    for p in PER:
        for ds,s in (('a',seq),('b',cd)):
            r=ratio(s,p); cnt[(p,ds)]+=r>1; R[(p,ds)].append(r)
print("period | genome DNA: genomes above / median ratio | coding: genomes above / median ratio")
for p in PER: print("%3d | %2d  %.3f | %2d  %.3f"%(p,cnt[(p,'a')],np.median(R[(p,'a')]),cnt[(p,'b')],np.median(R[(p,'b')])))
