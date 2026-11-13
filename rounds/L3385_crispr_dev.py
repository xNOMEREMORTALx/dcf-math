"""L3385 [CRISPR] development: label-free CRISPR array finder on graded genomes; validation against GenBank CRISPR annotation."""
import re, glob, collections, statistics as st
from scipy.stats import spearmanr
def arrays(seq, k=23):
    """runs of >= 3 copies of a 23-mer spaced 50-120 bp apart, whose intervening spacers are all different (CRISPR, not tandem repeats)."""
    pos=collections.defaultdict(list)
    for i in range(len(seq)-k):
        w=seq[i:i+k]
        if 'N' not in w: pos[w].append(i)
    found=[]
    def keep(run):
        if len(run)<3: return
        sp=[seq[run[i]+k:run[i+1]] for i in range(len(run)-1)]
        if len(set(x[8:20] for x in sp))==len(sp): found.append((run[0],run[-1],len(run)))
    for w,P in pos.items():
        if len(P)<3 or len(set(w))<3: continue
        run=[P[0]]
        for p in P[1:]:
            if 50<=p-run[-1]<=120: run.append(p)
            else: keep(run); run=[p]
        keep(run)
    found.sort(); merged=[]
    for s_,e_,n_ in found:
        if merged and s_<=merged[-1][1]+120: merged[-1]=(merged[-1][0],max(e_,merged[-1][1]),max(n_,merged[-1][2]))
        else: merged.append((s_,e_,n_))
    return merged
tier={'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_008530':1,'NC_005362':1,'NC_009785':1,'NC_010080':1,'NC_013853':1,'NC_015759':1,'NC_008497':1,'NC_010471':1,'NC_008526':1,'NC_009009':1,
 'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,'NC_003295':2,'NC_007761':2,'NC_009848':2,'NC_007604':2,'NC_003272':2,'NC_004113':2,'NC_005125':2,'NC_006510':2,'NC_009664':2,
 'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_008593':3,'NC_009616':3,'NC_014393':3,
 'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4,'NC_003551':4,'NC_013223':4,'NC_010337':4,'NC_013665':4,'NC_015388':4,'NC_014378':4,'NC_008553':4,'NC_011768':4}
files={}
for f in glob.glob('/home/claude/L3*/g/*.gb'):
    a=f.split('/')[-1][:-3]
    if a in tier and a not in files: files[a]=f
rows=[]; tp=fp=fn=0
for a,f in sorted(files.items()):
    t=open(f).read(); seq=re.sub(r'[^ACGT]','N',''.join(re.findall(r'[A-Za-z]+',t.split('\nORIGIN')[1].split('\n//')[0])).upper())
    A=arrays(seq)
    ann=[(int(m.group(1)),int(m.group(2))) for m in re.finditer(r'repeat_region\s+(?:complement\()?<?(\d+)\.\.>?(\d+)\)?\n(?:\s+/[^\n]*\n)*?\s+/rpt_family="CRISPR"',t)]
    hit=lambda s,e: any(not(e<x-1 or s-1>y) for x,y in ann)
    t_=sum(hit(s,e) for s,e,n in A); tp+=t_; fp+=len(A)-t_
    fn+=sum(not any(not(y<s or x>e) for s,e,n in A) for x,y in ann)
    rows.append((tier[a],a,len(A),sum(n for _,_,n in A),len(ann)))
print("validation vs GenBank CRISPR repeat_region: found-and-annotated %d, found-not-annotated %d, annotated-missed %d"%(tp,fp,fn))
for k in (1,2,3,4):
    R=[r for r in rows if r[0]==k]
    print("tier %d (%2d genomes): genomes with >=1 array %2d | median arrays %s | median repeats %s"%(k,len(R),sum(r[2]>0 for r in R),st.median(r[2] for r in R),st.median(r[3] for r in R)))
print("rho(tier, arrays) %.3f | rho(tier, repeat units) %.3f"%(spearmanr([r[0] for r in rows],[r[2] for r in rows])[0],spearmanr([r[0] for r in rows],[r[3] for r in rows])[0]))
