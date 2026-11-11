"""dcf_rubredoxin_L3281.py - per 1000 aa of the predicted proteome: iron 3-3-4 ladder (L3237), zinc ribbon with ladder cysteines masked (L3273),
and the classic RUBREDOXIN knuckle pair C-x2-C-G-x(24..32)-C-x2-C-G (Fe(Cys)4, ~29-residue spacing), counted overlapping on the raw protein.
Usage: python3 -I dcf_rubredoxin_L3281.py genome.gb pred.gff3     Author: Gary NOMEREMORTAL Mason (Digital Cosmos Framework). Frozen L3281."""
import re, sys
CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
comp=str.maketrans('ACGTN','TGCAN')
t=open(sys.argv[1]).read(); seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
n=lad=rib=rub=0
for l in open(sys.argv[2]):
    f=l.split('\t')
    if len(f)>6 and f[2]=='CDS':
        a,e,s=int(f[3]),int(f[4]),f[6]; g=seq[a-1:e] if s=='+' else seq[a-1:e].translate(comp)[::-1]
        p=''.join(CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3)); n+=len(p)
        L=[m.start() for m in re.finditer(r'(?=C..C..C...C)',p)]; lad+=len(L)
        q=list(p)
        for st in L:
            for k in range(st,st+11):
                if q[k]=='C': q[k]='z'
        rib+=len(re.findall(r'(?=C..C.{9,20}C..C)',''.join(q)))
        rub+=len(re.findall(r'(?=C..CG.{24,32}C..CG)',p))
print("ladder %.4f | ribbon %.4f | rubredoxin %.4f | aa %d"%(1000*lad/n,1000*rib/n,1000*rub/n,n))
