"""L3473 grading of PREREGISTERED_L3469_worm W1-W12 with truth v4 (UniProt Protein families)."""
import runpy
TR=runpy.run_path('/home/claude/dcf-math/rounds/dcf_truth4_L3469.py'); classes=TR['classes']; rc=TR['recall_class']
F={}; G={}
for l in open('/home/claude/L3473/z/worm.tsv').read().splitlines()[1:]:
    f=l.split('\t')
    if len(f)>=4: F[f[0]]=f[2]; G[f[0]]=f[1]
calls={}
for l in open('rounds/L3473_tool.txt'):
    x=l.split()
    if x and x[0]!='proteins:': calls.setdefault(x[0],[]).append(x[1])
R=[]
def P(tag,a,n,minn,bar,extra=''):
    r='ungradeable' if n<minn else ('PASS' if a/n>=bar-1e-9 else 'FAIL'); R.append((tag,r)); print('%-4s %3d/%-3d %-11s %s'%(tag,a,n,r,extra))
def prec(tag,cls,minn=2,bar=.9):
    L=[(c,a) for c in cls for a in calls.get(c,[])]; good=[(c,a) for c,a in L if c in classes(F.get(a,''))]
    P(tag,len(good),len(L),minn,bar,'wrong: %s'%[(c,G.get(a),F.get(a,'')[:50]) for c,a in L if (c,a) not in good])
def rec(tag,cls,bar,minn=2):
    T=[a for a in F if rc(F[a])&set(cls)]; got=[a for a in T if any(a in calls.get(c,[]) and c in classes(F[a]) for c in cls)]
    P(tag,len(got),len(T),minn,bar,'missed: %s'%[(G[a],F[a][:45]) for a in T if a not in got])
na=calls.get('Na',[]); R.append(('W1','PASS' if not na else 'FAIL')); print('W1   Na calls:',len(na),R[-1][1],na)
prec('W2',['Ca']); prec('W3',['K','HCN']); rec('W4',['K','Ca'],.75)
prec('W5',['K2P']); rec('W6',['K2P'],.5)
prec('W7',['iGluR']); rec('W8',['iGluR'],.75)
prec('W9',['FeHyd']); rec('W10',['FeHyd'],.75)
prec('W11',['pump_NaK','pump_Ca','pump_Cu']); rec('W12',['pump_NaK','pump_Ca','pump_Cu'],.75)
print('\nclass sizes in reference:',{c:sum(1 for a in F if c in classes(F[a])) for c in ['Ca','Na','K','HCN','K2P','iGluR','FeHyd','pump_NaK','pump_Ca','pump_Cu']})
print('RESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable;',sum(r=='ungradeable' for _,r in R),'ungradeable')
