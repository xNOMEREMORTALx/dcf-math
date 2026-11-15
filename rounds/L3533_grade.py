"""L3533 grading of PREREGISTERED_L3529_EK_dating D1-D5 (+ descriptive loops)."""
import gzip,re,collections
exec(open('/home/claude/dcf-math/rounds/dcf_neurochem_L3437.py').read().split("if __name__")[0])
O={};N={};S={}
for l in gzip.open('/home/claude/L3533/z/bil.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t'); O[f[0]]=f[1].split(' (')[0]; N[f[0]]=f[2]; S[f[0]]=f[3]
calls=collections.defaultdict(lambda:collections.defaultdict(list))
for l in open('rounds/L3533_tool.txt'):
    x=l.split()
    if x and x[0]!='proteins:': calls[O[x[1]]][x[0]].append(x[1])
sp=['Lingula anatina','Capitella teleta','Saccoglossus kowalevskii','Strongylocentrotus purpuratus']
size=collections.Counter(O.values()); R=[]
for i,s in enumerate(sp,1):
    r='ungradeable' if size[s]<5000 else ('PASS' if calls[s]['Na'] else 'FAIL'); R.append(('D%d'%i,r))
    print('D%d %-30s proteins %d | Na calls %d | Ca %d | K %d | %s'%(i,s,size[s],len(calls[s]['Na']),len(calls[s]['Ca']),len(calls[s]['K']),r))
letters=collections.defaultdict(list)
for a,p in S.items():
    if len(p)>=1400 and re.search(S4,p):
        for m in re.finditer(r'[AS]T[FY]([A-Z])GW',p): letters[O[a]].append((m.group(1),a,p[m.start()-6:m.end()+6],N[a][:40]))
ok5=all(any(x[0]=='K' for x in letters[s]) for s in sp if size[s]>=5000)
R.append(('D5','PASS' if ok5 else 'FAIL'))
print('\nD5 domain-III letters per species:')
for s in sp:
    print('  %s: %s'%(s,dict(collections.Counter(x[0] for x in letters[s]))))
    for x in letters[s]: print('      %s %s %s | %s'%x)
print('RESULT',R); print('passed',sum(r=='PASS' for _,r in R),'of',sum(r!='ungradeable' for _,r in R),'gradeable')
