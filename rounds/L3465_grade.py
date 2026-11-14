"""L3465 grading of PREREGISTERED_L3461_fly F1-F14 with truth rule v3 (dcf_truth3_L3461)."""
import gzip,re,runpy
TR=runpy.run_path('/home/claude/dcf-math/rounds/dcf_truth3_L3461.py'); classes=TR['classes']; SYM=TR['SYM']
Z='/home/claude/L3465/z/fly_rna.fna.gz'
genes={}
for l in gzip.open(Z,'rt'):
    if l.startswith(('>NM_','>XM_')):
        m=re.findall(r'\(([A-Za-z0-9\-\.:]+)\)',l); g=m[-1] if m else l.split()[0][1:]
        genes.setdefault(g,l.split(' ',1)[1].strip())
calls={}
for l in open('rounds/L3465_grade.txt'):
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
prec('F1',['Ca'],['Ca']); prec('F2',['Na'],['Na'],1.0,1)
prec('F3',['K','HCN'],['K','HCN'])
chan={g:c for c in('Ca','Na','HCN','K') for g in calls.get(c,[])}
truth=[g for g in genes if any(symm(g,c) for c in('Ca','Na','HCN','K')) and (classes(g,genes[g])&{'Ca','Na','HCN','K'})]
ok=[g for g in truth if chan.get(g) in classes(g,genes[g])]
P('F4',len(ok),len(truth),2,.75,'missed: %s'%sorted(g for g in truth if g not in ok))
for c,(tp,tr,bar,symc) in {'K2P':('F5','F6',.5,['K2P']),'iGluR':('F7','F8',.75,['iGluR']),'NMDA':('F9','F10',1.0,['NMDA']),'FeHyd':('F11','F12',2/3-1e-9,['FeHyd'])}.items():
    prec(tp,[c],[c])
    T=[g for g in genes if symm(g,c)]; L=set(calls.get(c,[]))
    P(tr,len([g for g in T if g in L]),len(T),2,bar,'missed: %s'%[g for g in T if g not in L])
prec('F13',['pump_NaK','pump_Ca','pump_Cu'],['pump_NaK','pump_Ca','pump_Cu'])
T=[g for g in genes if re.match(r'(?i)(atpalpha|serca|pmca|spock|atp7)$',g)]
L={g:c for c in('pump_NaK','pump_Ca','pump_Cu') for g in calls.get(c,[])}
okp=[g for g in T if L.get(g) in classes(g,genes[g])]
P('F14',len(okp),len(T),2,.8-1e-9,'missed: %s'%[(g,L.get(g)) for g in T if g not in okp])
print('\nRESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable;',sum(r=='ungradeable' for _,r in R),'ungradeable')
