"""dcf_seven_znf.py (frozen L3261) - 7-family / 84-nt rhythm in human coding sequence, split by C2H2 zinc-finger genes (>=3 C2H2 motifs).
One transcript per gene (lowest NM_), CDS = longest ORF. Gary NOMEREMORTAL Mason (Digital Cosmos Framework).
Usage: python3 -I dcf_seven_znf.py file.rna.fna.gz"""
import sys, re, numpy as np

import sys, gzip, re, numpy as np
def records(path):
    op=gzip.open if path.endswith('.gz') else open
    txt=op(path,'rt').read()
    for blk in txt.split('>')[1:]:
        h,_,s=blk.partition('\n'); yield h.split()[0], h, re.sub(r'[^ACGT]','N',s.replace('\n','').upper())
def longest_orf(s):
    best=(0,0)
    for f in range(3):
        i=f
        while i<len(s)-2:
            if s[i:i+3]=='ATG':
                j=i
                while j<len(s)-2 and s[j:j+3] not in ('TAA','TAG','TGA'): j+=3
                if j-i>best[1]-best[0]: best=(i,j+3)
                i=j+3
            else: i+=3
    return best

CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
ZF=re.compile(r'C.{2,4}C.{12}H.{3,5}H')
best={}
for path in sys.argv[1:]:
    for acc,desc,s in records(path):
        if not acc.startswith('NM_'): continue
        m=re.search(r'\(([A-Za-z0-9\-\.]+)\), ',desc); g=m.group(1) if m else acc
        num=int(re.search(r'NM_(\d+)',acc).group(1))
        if g not in best or num<best[g][0]: best[g]=(num,s)
zf=[];rest=[]
for num,s in best.values():
    c=s[slice(*longest_orf(s))]; p=''.join(CODE.get(c[i:i+3],'X') for i in range(0,len(c)-2,3))
    (zf if len(ZF.findall(p))>=3 else rest).append(c)
def ratio(s,p):
    k=round(4100/p); W=p*k; a=np.frombuffer(s.encode(),np.uint8); n=len(a)//W; a=a[:n*W].reshape(n,W); P=np.zeros(W//2+1)
    for bb in b'ACGT':
        x=(a==bb).astype(float); x-=x.mean(1,keepdims=True); P+=(np.abs(np.fft.rfft(x,axis=1))**2).mean(0)
    return P[k]/np.mean(np.r_[P[k-8:k-2],P[k+3:k+9]])
for name,S in (('ALL genes',zf+rest),('ZNF genes (>=3 C2H2)',zf),('all other genes',rest)):
    s=''.join(S); R={p:ratio(s,p) for p in range(7,63)}; o=[R[p] for p in range(8,63) if p%7]; p95=np.percentile(o,95)
    print("%s: n=%d, %.2f Mb | others p95 %.3f | 7:%.2f 12:%.2f 14:%.2f 21:%.2f 28:%.2f 42:%.2f"%(name,len(S),len(s)/1e6,p95,R[7],R[12],R[14],R[21],R[28],R[42]))
    print("   period 84 ratio %.2f | top periods 7-100: %s"%(ratio(s,84),sorted(((round(ratio(s,q),2),q) for q in range(7,101)),reverse=True)[:6]))
