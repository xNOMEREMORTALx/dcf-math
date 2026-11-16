"""L3641 frozen blind script. Reads Entry+Sequence only. Per file:
 battery ratio (dcf_battery_v3_L3633); v3 Na calls; Na_partial = 800-1499 aa, >=4 S4 matches, v3 lysine loop, not a v3 Na call;
 4-domain candidates (>=1300 aa with >=3 ring matches or a lysine loop) aligned (local) to mouse Scn*/Cacna1*/Nalcn; NALCN = nearest Nalcn."""
import gzip,pickle,re,runpy,sys
B=runpy.run_path('/home/claude/dcf-math/rounds/dcf_battery_v3_L3633.py',run_name='x'); N=B['N']; S4=re.compile(N['S4']); LYS=re.compile(N['LYS'])
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
ref={g:p for g,p in P['mouse'].items() if re.match(r'^(Scn\d+a|Cacna1[a-z]|Nalcn)$',g)}
for f in sys.argv[1:]:
    print('###',f.split('/')[-1])
    for o,(c,p,n) in B['per_org'](f).items(): print('ratio',o,'proteins',n,'channels',c,'pumps',p,'ratio %.2f'%(c/p) if p else 'inf')
    L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); ie=h.index('Entry'); iq=h.index('Sequence')
    for l in L[1:]:
        x=l.split('\t'); s=x[iq]; ch=N['channel'](s)
        part=800<=len(s)<1500 and len(S4.findall(s))>=4 and LYS.search(s) and ch!='Na'
        cand=len(s)>=1300 and (len(re.findall(N['RING'],s))>=3 or LYS.search(s))
        if ch=='Na' or part or cand:
            v,r=max((sc(s,ref[g]),g) for g in ref)
            print('CH',x[ie],len(s),'Na' if ch=='Na' else 'Na_partial' if part else 'cand','nearest',r,v,flush=True)
