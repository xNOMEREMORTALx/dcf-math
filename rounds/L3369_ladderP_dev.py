"""L3369 development (graded data only): plain ladder C..C..C...C vs Ladder-P C..C..C...CP."""
import sys, re, gzip, glob, statistics as st
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
from scipy.stats import spearmanr
L, LP = r'(?=C..C..C...C)', r'(?=C..C..C...CP)'
sets={'/home/claude/L3269':{'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4},
 '/home/claude/L3273':{'NC_008530':1},'/home/claude/L3285':{'NC_005362':1,'NC_009785':1,'NC_003551':4,'NC_013223':4},
 '/home/claude/L3293':{'NC_007604':2,'NC_003272':2,'NC_004113':2,'NC_005125':2,'NC_010337':4},
 '/home/claude/L3333':{'NC_010080':1,'NC_013853':1,'NC_015759':1,'NC_003295':2,'NC_007761':2,'NC_009848':2,'NC_008593':3,'NC_009616':3,'NC_014393':3,'NC_013665':4,'NC_015388':4,'NC_014378':4}}
rows=[]
for d,T in sets.items():
    for a,t in T.items():
        aa=x=y=0
        for p in R.proteins(R.read_seq(f'{d}/g/{a}.gb'),f'{d}/out/{a}.gff3'):
            aa+=len(p); x+=len(re.findall(L,p)); y+=len(re.findall(LP,p))
        rows.append((t,1000*x/aa,1000*y/aa))
print("BACTERIA/ARCHAEA (37 graded blind genomes)")
for i,nm in ((1,'plain ladder'),(2,'Ladder-P')):
    med=[st.median(r[i] for r in rows if r[0]==k) for k in (1,2,3,4)]
    v=lambda k:[r[i] for r in rows if r[0]==k]
    print("  %-13s rho %.3f | medians %s | t3/t2 %.2fx t4/t3 %.2fx | overlaps: t2max %.4f vs t3min %.4f, t3max %.4f vs t4min %.4f"%(nm,spearmanr([r[0] for r in rows],[r[i] for r in rows])[0],' '.join('%.4f'%m for m in med),med[2]/med[1],med[3]/med[2],max(v(2)),min(v(3)),max(v(3)),min(v(4))))
def prot(f):
    op=gzip.open if f.endswith('gz') else open; t=op(f,'rt').read(); aa=x=y=0
    for b in t.split('>')[1:]:
        s=b.partition('\n')[2].replace('\n',''); aa+=len(s); x+=len(re.findall(L,s)); y+=len(re.findall(LP,s))
    return 1000*x/aa,1000*y/aa
print("PROTISTS (14 graded; Naegleria special)")
for f in sorted(glob.glob('/home/claude/L3353/z/*.gz'))+['/home/claude/L3357/tvag.fasta.gz']+sorted(glob.glob('/home/claude/L3365/z/*')):
    nm=re.search(r'OS=(\S+ \S+)',gzip.open(f,'rt').read(3000)) if 'L3353' not in f else None
    nm=nm.group(1) if nm else f.split('/')[-1].split('.')[0][:28]
    a,b=prot(f); print("  %-30s plain %.4f | Ladder-P %.4f"%(nm,a,b))
x=y=aa=0; seen=set()
for f in ['/home/claude/L3313/p/human.1.protein.faa.gz','/home/claude/L3313/p/human.2.protein.faa.gz']:
    for b in gzip.open(f,'rt').read().split('>')[1:]:
        h,_,s=b.partition('\n'); k=re.sub(r' isoform.*','',h.split(' ',1)[1].split(' [')[0])
        if k in seen: continue
        seen.add(k); s=s.replace('\n',''); aa+=len(s); x+=len(re.findall(L,s)); y+=len(re.findall(LP,s))
print("HUMAN (5,390 proteins): plain %.4f (%d) | Ladder-P %.4f (%d)"%(1000*x/aa,x,1000*y/aa,y))
