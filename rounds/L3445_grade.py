"""L3445 grading X1-X12 on zebrafish XM_ (genes not in NM_ file 1)."""
import gzip,re
Z1='/home/claude/L3441/z/zebrafish.1.rna.fna.gz'; Z2='/home/claude/L3441/z/zebrafish.2.rna.fna.gz'
T={'Ca':r'cacna1','Na':r'scn\d+l?a[ab]?$','K':r'kcn[abcdfghqsv]\d','HCN':r'hcn\d','K2P':r'kcnk\d','iGluR':r'gri[akdn]','NMDA':r'grin[12]','FeHyd2':r'(th|th2|tph1.*|tph2.*|pah.*)$'}
fam=lambda g,c: bool(re.match('(?i)'+T[c],g))
skip=set()
for l in gzip.open(Z1,'rt'):
    if l.startswith('>NM_'):
        m=re.findall(r'\(([A-Za-z0-9\-\.:]+)\)',l); skip.add(m[-1]) if m else None
syms=set()
for l in gzip.open(Z2,'rt'):
    if l.startswith('>XM_'):
        m=re.findall(r'\(([A-Za-z0-9\-\.:]+)\)',l)
        if m and m[-1] not in skip: syms.add(m[-1])
chan=lambda g: next((c for c in('Ca','Na','HCN','K') if fam(g,c)),None)
present={c:sorted(g for g in syms if (chan(g)==c if c in('Ca','Na','K','HCN') else fam(g,c))) for c in T}
rows=[l.split() for l in open('rounds/L3445_grade.txt') if not l.startswith('genes')]
calls={}; other={}
for r in rows:
    if r[0] in('Ca','Na','K','HCN','undecided','other'): calls[r[-1]]=r[0]
    else: other.setdefault(r[0],[]).append(r[-1])
for c in T: print('present',c,len(present[c]),present[c])
R=[]
def P(tag,a,n,minn,bar,extra=''):
    r='ungradeable' if n<minn else ('PASS' if a/n>=bar else 'FAIL'); R.append((tag,r)); print(tag,'%d/%d'%(a,n),r,extra)
for tag,cs,minn,bar in [('X1',['Ca'],2,.9),('X2',['Na'],1,1.0),('X3',['K','HCN'],2,.9)]:
    L=[g for g,c in calls.items() if c in cs]; good=[g for g in L if chan(g) in cs]
    P(tag,len(good),len(L),minn,bar,'wrong: %s'%[g for g in L if g not in good])
fams=[g for c in('Ca','Na','K','HCN') for g in present[c]]; ok=[g for g in fams if calls.get(g)==chan(g)]
P('X4',len(ok),len(fams),1,.75,'missed: %s'%sorted((g,calls.get(g)) for g in fams if g not in ok))
for c,(tp,tr) in {'K2P':('X5','X6'),'iGluR':('X7','X8'),'NMDA':('X9','X10'),'FeHyd2':('X11','X12')}.items():
    L=other.get(c,[]); good=[g for g in L if fam(g,c)]
    P(tp,len(good),len(L),2,.9,'wrong: %s'%[g for g in L if g not in good])
    P(tr,sum(g in L for g in present[c]),len(present[c]),2,.75 if c!='K2P' else .7,'missed: %s'%[g for g in present[c] if g not in L])
print('calls by class:',{k:sorted(v) for k,v in other.items()}); print('channel calls:',sorted(calls.items()))
print('\nRESULT',R,'\npassed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable;',sum(r=='ungradeable' for _,r in R),'ungradeable')
