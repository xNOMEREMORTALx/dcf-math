"""L3617 frozen: classify the sea hare's glutamate-receptor calls (dcf_nerve v2 'iGluR') by nearest mouse receptor (local aligner).
Classes: NMDA (Grin1, Grin2a-d, Grin3a-b), AMPA (Gria1-4), kainate (Grik1-5), delta (Grid1-2)."""
import gzip,pickle,re,runpy,collections
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v2_L3549.py',run_name='x')
L=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py'); sc=L['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
ref={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
cls=lambda g:'NMDA' if g.startswith('Grin') else 'AMPA' if g.startswith('Gria') else 'kainate' if g.startswith('Grik') else 'delta'
rows=[]
for l in gzip.open('/home/claude/L3613/z/bat.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t')
    if f[1].startswith('Aplysia') and 'iGluR' in N['tags'](f[3]):
        s,r=max((sc(f[3],ref[x]),x) for x in ref); rows.append((f[0],len(f[3]),r,cls(r),s,f[2][:50]))
c=collections.Counter(r[3] for r in rows); nm=[r for r in rows if r[3]=='NMDA']
print('Aplysia iGluR calls:',len(rows),'| nearest class:',dict(c))
for r in sorted(rows,key=lambda x:(x[3],-x[4])): print('  %s %5d aa -> %-7s %-8s score %4d | %s'%r)
print('RESULT',[('G1','PASS' if len(nm)>=2 else 'FAIL'),('G2','PASS' if any(r[2]=='Grin1' for r in nm) else 'FAIL')])
