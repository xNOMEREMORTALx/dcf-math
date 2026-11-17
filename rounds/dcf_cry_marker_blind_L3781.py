"""L3781 frozen: the L3777 six-reference scan (work() reused unchanged) on new proteomes given as argv (UniProt TSV)."""
import gzip,sys,runpy,collections
W=runpy.run_path('/home/claude/dcf-math/rounds/dcf_cry_classII_L3777.py',run_name='x')['work']
for f in sys.argv[1:]:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io_,ie,iq=h.index('Organism'),h.index('Entry'),h.index('Sequence'); d=collections.defaultdict(list)
    for l in L[1:]: x=l.split('\t'); d[x[io_].split(' (')[0]].append((x[ie],x[iq]))
    for o,items in d.items():
        if len(items)>=5000: o2,hits=W((o,items)); print('ORG\t%s\thits\t%d\t%s'%(o2,len(hits),' '.join(hits)),flush=True)
