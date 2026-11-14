"""L3441 grading of PREREGISTERED_L3433_zebrafish (+A1) Z1-Z14. Truth by symbol (last parenthesis), case-insensitive."""
import gzip,re
Z=['/home/claude/L3441/z/zebrafish.1.rna.fna.gz','/home/claude/L3441/z/zebrafish.2.rna.fna.gz']
T={'Ca':r'cacna1','Na':r'scn\d+l?a[ab]?$','K':r'kcn[abcdfghqsv]\d','HCN':r'hcn\d','K2P':r'kcnk\d','iGluR':r'gri[akdn]','NMDA':r'grin[12]','FeHyd':r'(th|th2|tph1.*|tph2.*|pah.*)$'}
fam=lambda g,c: bool(re.match('(?i)'+T[c],g))
syms=set(); last={}
for z in Z:
    for line in gzip.open(z,'rt'):
        if line.startswith('>NM_'):
            m=re.findall(r'\(([A-Za-z0-9\-\.:]+)\)',line)
            if m: syms.add(m[-1]); last[line.split()[0][1:]]=m[-1]
def load(f):
    out=[]
    for l in open(f):
        x=l.split()
        if x and x[0] in('Ca','Na','K','HCN','undecided','other','K2P','iGluR','NMDA','FeHyd'): out.append((x[0],last.get(x[1],x[1])))
    return out
chan=lambda g: next((c for c in('Ca','Na','HCN','K') if fam(g,c)),None)
present={c:sorted(g for g in syms if (chan(g)==c if c in('Ca','Na','K','HCN') else fam(g,c))) for c in T}
for c in T: print('present',c,len(present[c]),present[c])
R=[]
def P(tag,good,n,minn,bar):
    r='ungradeable' if n<minn else ('PASS' if good/n>=bar else 'FAIL'); R.append((tag,r)); return r
for ver,f in [('v3','rounds/L3441_v3_tool.txt'),('v4','rounds/L3441_v4_tool.txt')]:
    calls={g:c for c,g in load(f) if c in('Ca','Na','K','HCN','undecided','other')}
    print('\n==',ver,sorted(calls.items()))
    tags=['Z1','Z2','Z3','Z4'] if ver=='v3' else [None,None,'Z7','Z8']
    for cs,ti,minn,bar in [(['Ca'],0,2,.9),(['Na'],1,1,1.0),(['K','HCN'],2,0,.9)]:
        if tags[ti] is None: continue
        L=[g for g,c in calls.items() if c in cs]; good=[g for g in L if chan(g) in (cs if cs!=['K','HCN'] else ['K','HCN'])]
        print(tags[ti],cs,'precision %d/%d'%(len(good),len(L)),P(tags[ti],len(good),len(L),max(minn,1),bar),'wrong:',[g for g in L if g not in good])
    fams=[g for c in('Ca','Na','K','HCN') for g in present[c]]; ok=[g for g in fams if calls.get(g)==chan(g)]
    print(tags[3],'recall %d/%d'%(len(ok),len(fams)),P(tags[3],len(ok),len(fams),1,.75 if ver=='v3' else .80),'missed:',sorted((g,calls.get(g)) for g in fams if g not in ok))
kc=[g for c,g in load('rounds/L3441_k2p_tool.txt')]
print('\nZ5 K2P precision %d/%d'%(sum(fam(g,'K2P') for g in kc),len(kc)),P('Z5',sum(fam(g,'K2P') for g in kc),len(kc),2,.9),kc)
print('Z6 K2P recall %d/%d'%(sum(g in kc for g in present['K2P']),len(present['K2P'])),P('Z6',sum(g in kc for g in present['K2P']),len(present['K2P']),1,.7))
v4=load('rounds/L3441_v4_tool.txt')
for c,(tp,tr) in {'iGluR':('Z9','Z10'),'NMDA':('Z11','Z12'),'FeHyd':('Z13','Z14')}.items():
    L=[g for x,g in v4 if x==c]; good=[g for g in L if fam(g,c)]
    print(tp,c,'precision %d/%d'%(len(good),len(L)),P(tp,len(good),len(L),2,.9),'wrong:',[g for g in L if g not in good])
    print(tr,c,'recall %d/%d'%(sum(g in L for g in present[c]),len(present[c])),P(tr,sum(g in L for g in present[c]),len(present[c]),2 if c=='FeHyd' else 1,.75),'missed:',[g for g in present[c] if g not in L])
print('\nRESULT:',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable;',sum(r=='ungradeable' for _,r in R),'ungradeable')
