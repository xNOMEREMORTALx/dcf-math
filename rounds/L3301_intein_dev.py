"""L3301 development (seen genomes, annotated translations): label-free intein (Hint domain) signature."""
import re, glob
files=['L3213/g/NC_007514.gb','L3221/g/NC_008095.gb','L3269/g/NC_009718.gb','L3269/g/NC_014532.gb','L3285/g/NC_003551.gb',
       'L3293/g/NC_003272.gb','L3293/g/NC_004113.gb','L3293/g/NC_005125.gb','L3293/g/NC_007604.gb']
PATS={'A_B_G': r'[CS][LIVFAM].{2}[GDE][TSDA].{50,120}T..H.{60,700}[HN]N[CST]',
      'A_B_G_strict': r'C[LIVFAM].{2}[GDE][TS][LIVMFAE][LIVMF].{50,120}T..H.{60,700}HN[CST]',
      'B_G': r'[LIVMFA].{4}T..H.{60,700}HN[CST]'}
recs=[]
for f in files:
    t=open('/home/claude/'+f).read().split('\nORIGIN')[0]
    for feat in re.split(r'\n     CDS             ',t)[1:]:
        block=feat.split('\n     gene   ')[0]
        m=re.search(r'/translation="([^"]+)"',block)
        if not m: continue
        p=re.sub(r'\s','',m.group(1)); pos='intein' in block.lower()
        recs.append((pos,p,f))
P=sum(r[0] for r in recs); print("proteins",len(recs),"annotated intein-related",P)
for k,pat in PATS.items():
    tp=sum(1 for r in recs if r[0] and re.search(pat,r[1])); fp=sum(1 for r in recs if not r[0] and re.search(pat,r[1]))
    print("%-13s recall %d/%d  false hits %d  precision %.2f"%(k,tp,P,fp,tp/max(tp+fp,1)))
