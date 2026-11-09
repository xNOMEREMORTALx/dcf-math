import re, glob, numpy as np
comp=str.maketrans('ACGTN','TGCAN')
loc={}
for d in ['L3181','L3185','L3213','L3221','L3229','L3241']:
    for f in glob.glob('/home/claude/%s/out/*.gff3'%d): loc[f.split('/')[-1][:-5]]=d
loc.pop('NC_005241',None)
def power(s,W):
    a=np.frombuffer(s.encode(),np.uint8); n=len(a)//W
    if n==0: return None
    a=a[:n*W].reshape(n,W); P=np.zeros(W//2+1)
    for b in b'ACGT':
        x=(a==b).astype(float); x-=x.mean(1,keepdims=True); P+=(np.abs(np.fft.rfft(x,axis=1))**2).mean(0)
    return P
def above(P,b,lo,hi): return P[b]>np.mean(np.r_[P[lo[0]:lo[1]+1],P[hi[0]:hi[1]+1]])
res={k:0 for k in ['F1','F2','F3','F4','C3']}; ratios={k:[] for k in res}
for a in sorted(loc):
    d=loc[a]; t=open('/home/claude/%s/g/%s.gb'%(d,a)).read()
    seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
    cds=[]
    for l in open('/home/claude/%s/out/%s.gff3'%(d,a)):
        f=l.split('\t')
        if len(f)>6 and f[2]=='CDS':
            x,y=int(f[3]),int(f[4]); g=seq[x-1:y]; cds.append(g if f[6]=='+' else g.translate(comp)[::-1])
    cd=''.join(cds)
    for key,s,W,b,lo,hi in [('F1',seq,4100,820,(810,815),(825,830)),('F2',seq,4100,100,(95,98),(102,105)),
                            ('F3',cd,4100,820,(810,815),(825,830)),('F4',cd,4100,100,(95,98),(102,105)),
                            ('C3',cd,4101,1367,(1357,1362),(1372,1377))]:
        P=power(s,W); res[key]+=above(P,b,lo,hi)
        ratios[key].append(P[b]/np.mean(np.r_[P[lo[0]:lo[1]+1],P[hi[0]:hi[1]+1]]))
for k in res: print(k,"above neighbours in %d of %d genomes; median ratio %.3f"%(res[k],len(loc),np.median(ratios[k])))
