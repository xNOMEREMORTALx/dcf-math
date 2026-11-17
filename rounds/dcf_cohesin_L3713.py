"""L3713 frozen: cohesin core (SMC1, SMC3) per proteome, all organisms seen. Candidates: 900-1600 aa with the SMC signature LSGG[EQ] and a
Walker A G..G.GK[ST]; nearest (local aligner) of mouse Smc1a, Smc1b, Smc2, Smc3, Smc4, Smc5, Smc6 with score >= 1000 assigns the class."""
import gzip,glob,collections,pickle,re,runpy
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
REF={k:P['mouse'][k] for k in ['Smc1a','Smc1b','Smc2','Smc3','Smc4','Smc5','Smc6']}
def cls(items):
    c=collections.Counter()
    for a,s in items:
        if 900<=len(s)<=1600 and re.search('LSGG[EQ]',s) and re.search(r'G..G.GK[ST]',s):
            v,r=max((sc(s,REF[k]),k) for k in REF)
            if v>=1000: c[{'Smc1a':'SMC1','Smc1b':'SMC1','Smc3':'SMC3'}.get(r,'other')]+=1
    return c
sets=[(sp,list(P[sp].items())) for sp in ['mouse','zebrafish','chicken','fly']]
F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz','/home/claude/L3605/z/nn.tsv.gz',
   '/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz','/home/claude/L3661/z/worm.tsv.gz','/home/claude/L3669/z3/h2.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+\
  sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))+sorted(glob.glob('/home/claude/L3677/z/*.gz'))+sorted(glob.glob('/home/claude/L3689/z/*.gz'))+sorted(glob.glob('/home/claude/L3701/z/*.gz'))
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io,ie,iq=h.index('Organism'),h.index('Entry'),h.index('Sequence'); d=collections.defaultdict(list)
    for l in L[1:]: x=l.split('\t'); d[x[io].split(' (')[0]].append((x[ie],x[iq]))
    sets+=list(d.items())
sets.append(('Hofstenia miamia',list(N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').items())))
seen=set()
for o,items in sets:
    if len(items)<5000 or o in seen: continue
    seen.add(o); c=cls(items); print('ORG\t%s\tSMC1\t%d\tSMC3\t%d\tother_SMC\t%d'%(o,c['SMC1'],c['SMC3'],c['other']),flush=True)
