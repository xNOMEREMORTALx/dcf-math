"""L3509 grading of PREREGISTERED_L3505_ctenophore T1-T3 (+ descriptive)."""
import gzip,re,collections
exec(open('/home/claude/dcf-math/rounds/dcf_neurochem_L3437.py').read().split("if __name__")[0])
O={};N={};S={}
for l in gzip.open('/home/claude/L3509/z/cteno.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t'); O[f[0]]=f[1]; N[f[0]]=f[2]; S[f[0]]=f[3]
calls=collections.defaultdict(list)
for l in open('rounds/L3509_tool.txt'):
    x=l.split()
    if x and x[0]!='proteins:': calls[x[0]].append(x[1])
R=[]
R.append(('T1','PASS' if not calls['Na'] else 'FAIL')); print('T1 Na calls:',len(calls['Na']),R[-1][1],calls['Na'])
loops=[]
for a,p in S.items():
    if len(p)>=1400 and re.search(S4,p):
        for m in re.finditer(r'[AS]T[FY]([A-Z])GW',p): loops.append((a,m.group(1),p[m.start()-6:m.end()+6],O[a][:30],N[a][:45]))
print('T2 ATF-x-GW loops in >=1400 aa voltage-sensor proteins:')
for x in loops: print('   ',x)
R.append(('T2','ungradeable' if not loops else ('PASS' if all(x[1]!='K' for x in loops) else 'FAIL')))
R.append(('T3','ungradeable' if len(S)<5000 else ('PASS' if len(calls['K'])>=3 else 'FAIL'))); print('T3 K calls',len(calls['K']))
print('\nDescriptive: counts by class',{c:len(v) for c,v in calls.items()})
for c in ('Ca','undecided','HCN','K2P','iGluR','FeHyd','pump_NaK','pump_Ca','pump_Cu'):
    for a in calls.get(c,[]): print('  %-9s %s %s | %s'%(c,a,O[a][:25],N[a][:55]))
print('RESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable')
