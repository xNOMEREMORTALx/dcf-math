"""dcf_redoxage_L3257.py - label-free 'redox-age' call from a genome + gene-finder predictions (DCF, Gary NOMEREMORTAL Mason). Frozen L3257.
ladder = C-x2-C-x2-C-x3-C motifs (4Fe-4S ferredoxin) per 1000 aa; CuA = proteins with C-x-E-x-C-x3-H-x2-M (CuA site of cytochrome oxidase II / N2O reductase).
Call: ladder >= 0.06 -> 'Fd' (ferredoxin-based low-potential metabolism); else CuA >= 1 -> 'O2' (oxygen respiration); else 'neither' (e.g. lactic fermenter).
Cut 0.06 set on 12 development genomes only (O2 max 0.025, Fd min 0.099). Usage: python3 -I dcf_redoxage_L3257.py genome.gb pred.gff3"""
import re, sys
CODE={}; b='TCAG'; aa='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i,x in enumerate(b):
  for j,y in enumerate(b):
    for k,z in enumerate(b): CODE[x+y+z]=aa[16*i+4*j+k]
comp=str.maketrans('ACGTN','TGCAN')
t=open(sys.argv[1]).read(); seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
n=lad=cua=0
for l in open(sys.argv[2]):
    f=l.split('\t')
    if len(f)>6 and f[2]=='CDS':
        x,y,s=int(f[3]),int(f[4]),f[6]; g=seq[x-1:y] if s=='+' else seq[x-1:y].translate(comp)[::-1]
        p=''.join(CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3)); n+=len(p)
        lad+=len(re.findall(r'(?=C..C..C...C)',p)); cua+=bool(re.search(r'C.E.C...H..M',p))
L=1000*lad/n; call='Fd' if L>=0.06 else ('O2' if cua>=1 else 'neither')
print("ladder %.4f  CuA %d  call %s"%(L,cua,call))
