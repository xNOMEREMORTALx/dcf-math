"""L3349 development (graded genomes only): label-free electron-bifurcation marker = proteins carrying BOTH a 3-3-4 ladder
and a Rossmann FAD/NAD(P)-binding G-x-G-x-x-G, per 1000 proteins; compared with the whole ladder for the tier-3 vs tier-4 split."""
import sys, re, statistics as st
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
from scipy.stats import spearmanr, mannwhitneyu
sets={'/home/claude/L3269':{'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4},
 '/home/claude/L3273':{'NC_008530':1},
 '/home/claude/L3285':{'NC_005362':1,'NC_009785':1,'NC_003551':4,'NC_013223':4},
 '/home/claude/L3333':{'NC_010080':1,'NC_013853':1,'NC_015759':1,'NC_003295':2,'NC_007761':2,'NC_009848':2,'NC_008593':3,'NC_009616':3,'NC_014393':3,'NC_013665':4,'NC_015388':4,'NC_014378':4}}
rows=[]
for d,T in sets.items():
    for a,t in T.items():
        n=aa=lad=bif=bif2=0
        for p in R.proteins(R.read_seq(f'{d}/g/{a}.gb'),f'{d}/out/{a}.gff3'):
            n+=1; aa+=len(p); c=len(re.findall(r'(?=C..C..C...C)',p)); lad+=c
            if c and re.search(r'G.G..G',p): bif+=1
            if c>=2 and re.search(r'G.G..G',p): bif2+=1
        rows.append((a,t,1000*lad/aa,1000*bif/n,1000*bif2/n))
for i,nm in [(2,'whole ladder /1000 aa'),(3,'ladder+GxGxxG proteins /1000 genes'),(4,'>=2 ladders+GxGxxG /1000 genes')]:
    v=lambda k:[r[i] for r in rows if r[1]==k]; med=[st.median(v(k)) for k in (1,2,3,4)]
    lo=max(v(3)); hi=min(v(4)); 
    print("%-38s rho %.3f | medians %s | t4/t3 %.2fx | overlap t3 max %.3f vs t4 min %.3f | MWU p %.3g"%(nm,spearmanr([r[1] for r in rows],[r[i] for r in rows])[0],' '.join('%.3f'%m for m in med),med[3]/med[2],lo,hi,mannwhitneyu(v(4),v(3),alternative='greater').pvalue))
