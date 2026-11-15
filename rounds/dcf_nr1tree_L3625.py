"""L3625 frozen: nearest mouse iGluR (local aligner) for every dcf_nerve v2 iGluR call, per complete proteome."""
import gzip,pickle,re,runpy,collections,sys
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v2_L3549.py',run_name='x')
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
ref={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
F=['/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz',
   '/home/claude/L3605/z/nn.tsv.gz','/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz']
org=collections.defaultdict(list)
for f in F:
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); io=h.index('Organism'); ie=h.index('Entry'); iq=h.index('Sequence')
    for l in L[1:]:
        x=l.split('\t'); org[x[io].split(' (')[0]].append((x[ie],x[iq]))
for g,p in N['proteins']('/home/claude/L3521/z/hmia.pep.fa.gz').items(): org['Hofstenia miamia (FASTA)'].append((g,p))
print('mouse refs',len(ref),sorted(ref))
for o,ps in sorted(org.items()):
    if len(ps)<5000: continue
    rows=[]
    for a,s in ps:
        if 'iGluR' in N['tags'](s):
            v,r=max((sc(s,ref[x]),x) for x in ref); rows.append((a,len(s),r,v))
    c=collections.Counter('NMDA' if r.startswith('Grin') else 'AMPA' if r.startswith('Gria') else 'kainate' if r.startswith('Grik') else 'delta' for _,_,r,_ in rows)
    print('ORG %-30s proteins %6d iGluR %3d NR1 %2d classes %s'%(o[:30],len(ps),len(rows),sum(r=='Grin1' for _,_,r,_ in rows),dict(c)),flush=True)
    for a,n,r,v in rows: print('   ',a,n,r,v)
