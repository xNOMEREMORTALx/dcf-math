"""L3633 development: v2 vs v3dev (sodium loop [TS][FYW][KR][GA]W) on every protein set already seen. Lists every changed call."""
import gzip,pickle,runpy,glob
V2=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v2_L3549.py',run_name='x'); V3=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3dev_L3633.py',run_name='x')
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
sets=[(sp,list(d.items())) for sp,d in P.items()]
for f in ['/home/claude/L3481/z/metazoa.tsv.gz','/home/claude/L3501/z/early.tsv.gz','/home/claude/L3509/z/cteno.tsv.gz','/home/claude/L3533/z/bil.tsv.gz','/home/claude/L3557/z/oc.tsv.gz',
          '/home/claude/L3605/z/nn.tsv.gz','/home/claude/L3613/z/bat.tsv.gz','/home/claude/L3621/z/tard.tsv.gz']+sorted(glob.glob('/home/claude/L3629/z/*.gz')):
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); ie=h.index('Entry'); iq=h.index('Sequence'); io=h.index('Organism')
    sets.append((f.split('/')[-1],[(l.split('\t')[ie]+'|'+l.split('\t')[io].split(' (')[0],l.split('\t')[iq]) for l in L[1:]]))
tot=0;nna=0
for name,items in sets:
    for k,s in items:
        a,b=V2['channel'](s),V3['channel'](s)
        if b=='Na': nna+=1
        if a!=b: tot+=1; print('CHANGED',name,k,len(s),a,'->',b)
print('changed calls',tot,'| total v3 Na calls',nna)
