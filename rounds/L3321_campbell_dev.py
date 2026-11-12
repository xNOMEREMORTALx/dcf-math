"""L3321 development (blind_20 genomes, now seen): whole-proteome ladder vs Campbell-style small-ferredoxin count."""
import sys, re, statistics as st
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
from scipy.stats import spearmanr
tier={'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_008530':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,
'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4}
f=lambda a:('/home/claude/L3273' if a=='NC_008530' else '/home/claude/L3269')
rows={}
for a in tier:
    d=f(a); n=aa=lad=small=sm_lad=0
    for p in R.proteins(R.read_seq(f'{d}/g/{a}.gb'),f'{d}/out/{a}.gff3'):
        n+=1; aa+=len(p); c=len(re.findall(r'(?=C..C..C...C)',p)); lad+=c
        if len(p)<=200 and c: small+=1; sm_lad+=c
    rows[a]=(1000*lad/aa, 1000*small/n, 1000*sm_lad/aa, 1000*(lad-sm_lad)/aa)
names=['whole-proteome ladder /1000 aa','small Fd genes (<=200 aa) /1000 genes','ladders in small proteins /1000 aa','ladders in large proteins /1000 aa']
for i,nm in enumerate(names):
    v=[rows[a][i] for a in tier]; t=[tier[a] for a in tier]
    med=[st.median(rows[a][i] for a in tier if tier[a]==k) for k in (1,2,3,4)]
    print("%-40s rho %.3f | tier medians %s | H2-ferm/lactic %.1fx"%(nm,spearmanr(t,v)[0],' '.join('%.4f'%m for m in med),med[2]/max(med[0],1e-9)))
