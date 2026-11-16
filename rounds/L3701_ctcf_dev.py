import gzip,pickle,runpy
C=runpy.run_path('/home/claude/dcf-math/rounds/dcf_ctcf_L3701.py'); P=C['_P']
for sp in ['zebrafish','chicken','fly']: print(sp,C['ctcf'](list(P[sp].items())),flush=True)
L=gzip.open('/home/claude/L3661/z/worm.tsv.gz','rt').read().splitlines()[1:]
print('C. elegans (full)',C['ctcf']([(l.split('\t')[0],l.split('\t')[3]) for l in L]),flush=True)
