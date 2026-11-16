"""L3701 frozen: CTCF call (dcf_ctcf_L3701) for every organism seen except the development set (zebrafish, chicken, fly, C. elegans)."""
import gzip,glob,collections,runpy
C=runpy.run_path('/home/claude/dcf-math/rounds/dcf_ctcf_L3701.py'); P=C['_P']
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
sets=[('mouse',list(P['mouse'].items()))]
F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz',
   '/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz','/home/claude/L3669/z3/h2.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz'))+\
  sorted(glob.glob('/home/claude/L3637/z/*.gz'))+sorted(glob.glob('/home/claude/L3645/z/*.gz'))+sorted(glob.glob('/home/claude/L3677/z/*.gz'))+\
  sorted(glob.glob('/home/claude/L3689/z/*.gz'))+sorted(glob.glob('/home/claude/L3701/z/*.gz'))
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io,ie,iq=h.index('Organism'),h.index('Entry'),h.index('Sequence'); d=collections.defaultdict(list)
    for l in L[1:]: x=l.split('\t'); d[x[io].split(' (')[0]].append((x[ie],x[iq]))
    sets+=list(d.items())
sets.append(('Hofstenia miamia',list(N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').items())))
seen=set()
for o,items in sets:
    if len(items)<5000 or o in seen: continue
    seen.add(o); r=C['ctcf'](items)
    print('ORG\t%s\tCTCF\t%s\ttop_vs_Ctcf\t%d\tnearest\t%s\t%d\tzf_proteins\t%d\ttop\t%s'%(o,'present' if r[0] else 'absent',r[1],r[2],r[3],r[4],r[5]),flush=True)
