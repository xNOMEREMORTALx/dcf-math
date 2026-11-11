"""L3281 development (seen genomes only): split the L3273 zinc-ribbon matches by knuckle type."""
import sys, re, statistics as st
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
tier={'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_008530':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,
'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4}
def files(a): return (f'/home/claude/L3273/g/{a}.gb',f'/home/claude/L3273/out/{a}.gff3') if a=='NC_008530' else (f'/home/claude/L3269/g/{a}.gb',f'/home/claude/L3269/out/{a}.gff3')
res={}
for a in tier:
    g,f=files(a); seq=R.read_seq(g); n=0; c={'rubG':0,'other':0,'rubredoxin29':0,'CPxCG_any':0}
    for p in R.proteins(seq,f):
        n+=len(p); q=list(p)
        for m in re.finditer(r'(?=C..C..C...C)',p):
            for k in range(m.start(),m.start()+11):
                if q[k]=='C': q[k]='z'
        qs=''.join(q)
        for m in re.finditer(r'(?=(C..C.{9,20}C..C))',qs):
            s=m.group(1)
            if re.match(r'C..CG',s) or re.search(r'CP.C$',s): c['rubG']+=1
            else: c['other']+=1
        c['rubredoxin29']+=len(re.findall(r'(?=C..CG.{24,32}C..CG)',p))
        c['CPxCG_any']+=len(re.findall(r'CP.CG',p))
    res[a]={k:1000*v/n for k,v in c.items()}
for k in ('rubG','other','rubredoxin29','CPxCG_any'):
    meds=[st.median(res[a][k] for a in tier if tier[a]==t) for t in (1,2,3,4)]
    print(k, ' '.join('%.4f'%m for m in meds), ' t4/t1 %.1f'%(meds[3]/meds[0] if meds[0] else float('inf')))
