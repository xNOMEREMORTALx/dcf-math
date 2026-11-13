"""L3377 development (graded genomes): 'information iron' (EndoIII/MutY FCL loop C-x6-C-x2-C-x5-C) vs 'energy iron' (3-3-4 ladder), by tier.
Validation afterwards: annotated products of FCL hits (stop-codon match)."""
import sys, re, statistics as st, collections
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
from scipy.stats import spearmanr
sets={'/home/claude/L3269':{'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4},
 '/home/claude/L3273':{'NC_008530':1},'/home/claude/L3285':{'NC_005362':1,'NC_009785':1,'NC_003551':4,'NC_013223':4},
 '/home/claude/L3293':{'NC_007604':2,'NC_003272':2,'NC_004113':2,'NC_005125':2,'NC_010337':4},
 '/home/claude/L3333':{'NC_010080':1,'NC_013853':1,'NC_015759':1,'NC_003295':2,'NC_007761':2,'NC_009848':2,'NC_008593':3,'NC_009616':3,'NC_014393':3,'NC_013665':4,'NC_015388':4,'NC_014378':4}}
FCL=r'C.{6}C..C.{5}C'; rows=[]; prods=collections.Counter()
for d,T in sets.items():
    for a,t in T.items():
        txt=open(f'{d}/g/{a}.gb').read().split('\nORIGIN')[0]; stops={}
        for feat in re.split(r'\n     CDS             ',txt)[1:]:
            loc=feat.split('\n')[0]; m=re.findall(r'\d+',loc)
            if not m: continue
            pr=re.search(r'/product="([^"]+)"',feat.replace('\n                     ',' '))
            stops[(int(m[0]),True) if 'complement' in loc else (int(m[-1]),False)]=pr.group(1) if pr else 'unnamed'
        seq=R.read_seq(f'{d}/g/{a}.gb'); n=lad=fcl=0
        for l in open(f'{d}/out/{a}.gff3'):
            f=l.split('\t')
            if len(f)<7 or f[2]!='CDS': continue
            s,e,sd=int(f[3]),int(f[4]),f[6]; g=seq[s-1:e] if sd=='+' else seq[s-1:e].translate(R.comp)[::-1]
            p=''.join(R.CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3)); n+=1
            lad+=len(re.findall(r'(?=C..C..C...C)',p))
            if re.search(FCL,p):
                fcl+=1; prods[stops.get((s,True) if sd=='-' else (e,False),'(no match)')[:50]]+=1
        rows.append((t,a,1000*lad/n,1000*fcl/n,fcl))
print("per 1000 genes      tier medians (1/2/3/4)             rho with tier   t4/t1")
for i,nm in ((2,'energy ladder'),(3,'FCL information loop')):
    med=[st.median(r[i] for r in rows if r[0]==k) for k in (1,2,3,4)]
    print("%-20s %s   %.3f   %s"%(nm,' '.join('%.3f'%m for m in med),spearmanr([r[0] for r in rows],[r[i] for r in rows])[0],'%.1fx'%(med[3]/med[0]) if med[0] else 'inf'))
for r in rows:
    if r[0]==1: print("  tier1",r[1],"FCL proteins",r[4])
print("genomes with >=1 FCL protein: %d of %d"%(sum(r[4]>0 for r in rows),len(rows)))
print("FCL proteins, annotated products (after counting):"); [print("  %3d %s"%(v,k)) for k,v in prods.most_common(14)]
