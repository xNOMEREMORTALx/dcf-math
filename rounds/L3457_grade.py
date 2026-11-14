"""L3457 grading of PREREGISTERED_L3449_chicken C1-C14 with truth rule v2 (dcf_truth2_L3449)."""
import gzip,re,runpy
TR=runpy.run_path('/home/claude/dcf-math/rounds/dcf_truth2_L3449.py'); classes=TR['classes']; SYM=TR['SYM']
Z='/home/claude/L3457/z/chicken_rna.fna.gz'
genes={}
for l in gzip.open(Z,'rt'):
    if l.startswith(('>NM_','>XM_')):
        m=re.findall(r'\(([A-Za-z0-9\-\.:]+)\)',l); g=m[-1] if m else l.split()[0][1:]
        genes.setdefault(g,l.split(' ',1)[1].strip())
calls={}
for l in open('rounds/L3457_grade.txt'):
    x=l.split()
    if not x or x[0]=='genes:': continue
    calls.setdefault(x[0],[]).append(x[4])
symm=lambda g,c: bool(re.match('(?i)'+SYM[c],g))
R=[]
def P(tag,a,n,minn,bar,extra=''):
    r='ungradeable' if n<minn else ('PASS' if a/n>=bar else 'FAIL'); R.append((tag,r)); print('%-4s %3d/%-3d %-11s %s'%(tag,a,n,r,extra))
def prec(tag,cls,ok,bar=.9,minn=2):
    L=[g for c in cls for g in calls.get(c,[])]; good=[g for g in L if classes(g,genes.get(g,''))&set(ok)]
    # exact class: a call c is correct if c in classes; for K/HCN pooled, K call needs K, HCN call needs HCN
    good=[g for c in cls for g in calls.get(c,[]) if c in classes(g,genes.get(g,''))]
    P(tag,len(good),len(L),minn,bar,'wrong: %s'%[(g,genes.get(g,'')[:60]) for c in cls for g in calls.get(c,[]) if c not in classes(g,genes.get(g,''))])
prec('C1',['Ca'],['Ca']); prec('C2',['Na'],['Na'],1.0,2)
prec('C3',['K','HCN'],['K','HCN'])
chan={g:c for c in('Ca','Na','HCN','K') for g in calls.get(c,[])}
truth=[g for g in genes if any(symm(g,c) for c in('Ca','Na','HCN','K')) and (classes(g,genes[g])&{'Ca','Na','HCN','K'})]
ok=[g for g in truth if chan.get(g) in classes(g,genes[g])]
P('C4',len(ok),len(truth),2,.8,'missed: %s'%sorted(g for g in truth if g not in ok))
for c,(tp,tr,bar,symc) in {'K2P':('C5','C6',.7,['K2P']),'iGluR':('C7','C8',.75,['iGluR']),'NMDA':('C9','C10',.75,['NMDA']),'FeHyd':('C11','C12',.75,['FeHyd'])}.items():
    prec(tp,[c],[c])
    T=[g for g in genes if symm(g,c)]; L=set(calls.get(c,[]))
    P(tr,len([g for g in T if g in L]),len(T),2,bar,'missed: %s'%[g for g in T if g not in L])
prec('C13',['pump_NaK','pump_Ca','pump_Cu'],['pump_NaK','pump_Ca','pump_Cu'])
T=[g for g in genes if re.match(r'(?i)atp(1a|2a|2b|2c|4a|12a|7a|7b)',g)]
L={g:c for c in('pump_NaK','pump_Ca','pump_Cu') for g in calls.get(c,[])}
okp=[g for g in T if L.get(g) in classes(g,genes[g])]
P('C14',len(okp),len(T),2,.75,'missed: %s'%[(g,L.get(g)) for g in T if g not in okp])
print('\nRESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable;',sum(r=='ungradeable' for _,r in R),'ungradeable')
