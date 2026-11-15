"""L3633 frozen blind script: battery ratio (v3) per file; every v3 Na call aligned (local) to mouse Scn*/Cacna1*/Nalcn. Reads Entry+Sequence only."""
import gzip,pickle,re,runpy,sys
B=runpy.run_path('/home/claude/dcf-math/rounds/dcf_battery_v3_L3633.py',run_name='x'); N=B['N']
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
ref={g:p for g,p in P['mouse'].items() if re.match(r'^(Scn\d+a|Cacna1[a-z]|Nalcn)$',g)}
for f in sys.argv[1:]:
    print('###',f.split('/')[-1])
    for o,(c,p,n) in B['per_org'](f).items(): print('ratio',o,'proteins',n,'channels',c,'pumps',p,'ratio %.2f'%(c/p) if p else 'inf')
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); ie=h.index('Entry'); iq=h.index('Sequence')
    for l in L[1:]:
        x=l.split('\t'); s=x[iq]
        if N['channel'](s)=='Na':
            v,r=max((sc(s,ref[g]),g) for g in ref); print('NA',x[ie],len(s),'nearest',r,v,flush=True)
