"""L3281 development: CCHC zinc knuckle C-x2-C-x4-H-x4-C in human mRNA, one transcript per gene (lowest NM_), longest ORF."""
import gzip, re, sys, collections
CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
def orf(s):
    best=''
    for f in range(3):
        p=''.join(CODE.get(s[i:i+3],'X') for i in range(f,len(s)-2,3))
        for seg in p.split('*'):
            k=seg.find('M')
            if k>=0 and len(seg)-k>len(best): best=seg[k:]
    return best
genes={}
for path in sys.argv[1:]:
    txt=gzip.open(path,'rt').read()
    for blk in txt.split('>')[1:]:
        h,_,s=blk.partition('\n'); acc=h.split()[0]
        if not acc.startswith('NM_'): continue
        m=re.search(r'\(([A-Za-z0-9\-\.]+)\)',h); g=m.group(1) if m else acc
        num=int(re.sub(r'\D','',acc.split('.')[0]))
        if g not in genes or num<genes[g][0]: genes[g]=(num,s.replace('\n','').upper())
hits=[]; n=0
for g,(_,s) in genes.items():
    p=orf(s); n+=len(p); c=len(re.findall(r'(?=C..C....H....C)',p))
    if c: hits.append((c,g))
hits.sort(reverse=True)
print("genes %d, aa %d, CCHC per 1000 aa %.4f, genes with >=1: %d, >=2: %d"%(len(genes),n,1000*sum(c for c,_ in hits)/n,len(hits),sum(c>=2 for c,_ in hits)))
print("top:",hits[:25])
known=[g for g in genes if g.startswith('ZCCHC') or g in ('CNBP','LIN28A','LIN28B','ZCRB1','CPSF4','SF1','RBM4','RBM4B','NANOS1','NANOS2','NANOS3')]
print("known CCHC genes present:",len(known),"with >=1 hit:",sum(any(g==x for _,x in hits) for g in known), sorted(known)[:30])
