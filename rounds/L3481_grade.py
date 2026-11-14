"""L3481 grading of PREREGISTERED_L3477_metazoa M1-M14 with truth v4 (UniProt Protein families)."""
import gzip,runpy,re,collections
TR=runpy.run_path('/home/claude/dcf-math/rounds/dcf_truth4_L3469.py'); classes=TR['classes']; rc=TR['recall_class']
F={};G={};O={};L={}
for l in gzip.open('/home/claude/L3481/z/metazoa.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t')
    if len(f)>=6: F[f[0]]=f[4]; G[f[0]]=f[3]; O[f[0]]=f[1]; L[f[0]]=f[2]
calls=collections.defaultdict(list); bycall={}
for l in open('rounds/L3481_tool.txt'):
    x=l.split()
    if x and x[0]!='proteins:': calls[x[0]].append(x[1]); bycall.setdefault(x[1],[]).append(x[0])
R=[]
def P(tag,a,n,minn,bar,extra=''):
    r='ungradeable' if n<minn else ('PASS' if a/n>=bar-1e-9 else 'FAIL'); R.append((tag,r)); print('%-4s %4d/%-4d %-11s %s'%(tag,a,n,r,extra))
def prec(tag,cls,bar=.9):
    Lc=[(c,a) for c in cls for a in calls.get(c,[])]; good=[(c,a) for c,a in Lc if c in classes(F.get(a,''))]
    P(tag,len(good),len(Lc),2,bar,'wrong: %s'%[(c,G.get(a),O.get(a,'')[:25],F.get(a,'')[:45]) for c,a in Lc if (c,a) not in good][:12])
def rec(tag,cls,bar):
    T=[a for a in F if rc(F[a])&set(cls)]; got=[a for a in T if any(a in calls.get(c,[]) and c in classes(F[a]) for c in cls)]
    miss=[(G[a],O[a][:20]) for a in T if a not in got]
    P(tag,len(got),len(T),2,bar,'missed (%d): %s'%(len(miss),miss[:15]))
prec('M1',['Ca']); prec('M2',['Na']); prec('M3',['K','HCN']); rec('M4',['K','Ca','Na'],.75)
prec('M5',['K2P']); rec('M6',['K2P'],.6)
prec('M7',['iGluR']); rec('M8',['iGluR'],.75)
prec('M9',['FeHyd']); rec('M10',['FeHyd'],.75)
prec('M11',['pump_NaK','pump_Ca','pump_Cu']); rec('M12',['pump_NaK','pump_Ca','pump_Cu'],.75)
nem=[a for a in F if 'Nematoda' in L[a]]; nemNa=[a for a in calls.get('Na',[]) if 'Nematoda' in L[a]]
r='ungradeable' if len(nem)<50 else ('PASS' if not nemNa else 'FAIL'); R.append(('M13',r)); print('M13  nematode entries %d, Na calls on them %d: %s'%(len(nem),len(nemNa),r))
NaCa=[a for a in F if classes(F[a])&{'Na','Ca'}]; called=[a for a in NaCa if set(bycall.get(a,[]))&{'Na','Ca'}]
swaps=[(G[a],O[a][:20],bycall[a]) for a in called if ('Na' in classes(F[a]) and 'Ca' in bycall[a]) or ('Ca' in classes(F[a]) and 'Na' in bycall[a])]
r='ungradeable' if len(called)<5 else ('PASS' if not swaps else 'FAIL'); R.append(('M14',r)); print('M14  true Na/Ca channels called %d, swaps %d: %s %s'%(len(called),len(swaps),r,swaps))
print('\nDescriptive: calls by phylum-level lineage term')
ph=collections.Counter()
for c,accs in calls.items():
    for a in accs:
        lin=L[a]; key=next((t for t in ['Chordata','Arthropoda','Mollusca','Annelida','Nematoda','Cnidaria','Platyhelminthes','Echinodermata','Porifera','Placozoa','Ctenophora'] if t in lin),'other')
        ph[(key,c)]+=1
for k in sorted(set(k for k,_ in ph)): print(' ',k,{c:n for (kk,c),n in ph.items() if kk==k})
print('RESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable;',sum(r=='ungradeable' for _,r in R),'ungradeable')
