"""dcf_seven.py (frozen L3261) - rhythm at multiples of 7 nt in human coding sequence. Gary NOMEREMORTAL Mason (Digital Cosmos Framework).
One transcript per gene (lowest NM_ number; gene = symbol in parentheses), CDS = longest ORF, concatenated; Fourier power of the four base indicators,
window W = p*round(4100/p) so period p sits on a bin; ratio = power / mean of bins k-8..k-3, k+3..k+8.
Reports ratios for periods 7..62; multiples of 7 (7,14,21,28,35,42,49,56) vs the 'others' = periods 8..62 not divisible by 7.
Usage: python3 -I dcf_seven.py file.rna.fna.gz [more files]"""
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
best={}
for path in sys.argv[1:]:
    for acc,desc,s in records(path):
        if not acc.startswith('NM_'): continue
        m=re.search(r'\(([A-Za-z0-9\-\.]+)\), ',desc); g=m.group(1) if m else acc
        num=int(re.search(r'NM_(\d+)',acc).group(1))
        if g not in best or num<best[g][0]: best[g]=(num,s)
cds=''.join(s[slice(*longest_orf(s))] for num,s in best.values())
def ratio(s,p):
    k=round(4100/p); W=p*k; a=np.frombuffer(s.encode(),np.uint8); n=len(a)//W; a=a[:n*W].reshape(n,W); P=np.zeros(W//2+1)
    for b in b'ACGT':
        x=(a==b).astype(float); x-=x.mean(1,keepdims=True); P+=(np.abs(np.fft.rfft(x,axis=1))**2).mean(0)
    return P[k]/np.mean(np.r_[P[k-8:k-2],P[k+3:k+9]])
R={p:ratio(cds,p) for p in range(7,63)}
others=[R[p] for p in range(8,63) if p%7]; p95=np.percentile(others,95)
print("genes %d, coding %.1f Mb; others' 95th percentile %.3f, median %.3f"%(len(best),len(cds)/1e6,p95,np.median(others)))
for p in (7,14,21,28,35,42,49,56): print("period %2d ratio %.3f %s"%(p,R[p],'ABOVE' if R[p]>p95 else ''))
print("top 8 overall:",sorted(((round(v,3),p) for p,v in R.items()),reverse=True)[:8])
