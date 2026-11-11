"""dcf_zinc_ribbon_L3273.py - zinc-ribbon (redox-inert, structural Zn(Cys)4) density per 1000 aa of the predicted proteome,
with ferredoxin-ladder cysteines masked first so 2x[4Fe-4S] ferredoxins are not counted.
Motif: C-x2-C-x(9..20)-C-x2-C (overlapping). Prints ribbon and ladder densities.
Usage: python3 -I dcf_zinc_ribbon_L3273.py genome.gb pred.gff3   Author: Gary NOMEREMORTAL Mason (Digital Cosmos Framework). Frozen L3273."""
import re, sys
CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
comp=str.maketrans('ACGTN','TGCAN')
t=open(sys.argv[1]).read(); seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
n=lad=rib=0
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
print("ribbon per 1000 aa %.4f | ladder per 1000 aa %.4f | aa %d"%(1000*rib/n,1000*lad/n,n))
