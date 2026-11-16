"""L3673 frozen: the "neural kit" call for one proteome (argv[1], UniProt TSV). Reads Entry+Sequence only.
kit present = NR1 >= 1 (iGluR call nearest mouse Grin1, local aligner, L3625 method) OR v3 Na call >= 1 OR Na_partial >= 1 (L3641 rule).
Also prints the battery ratio (v3) for comparison."""
import gzip,pickle,re,runpy,sys
B=runpy.run_path('/home/claude/dcf-math/rounds/dcf_battery_v3_L3633.py',run_name='x'); N=B['N']; S4=re.compile(N['S4']); LYS=re.compile(N['LYS'])
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
igr={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
f=sys.argv[1]
for o,(c,p,n) in B['per_org'](f).items(): print('ratio',o,'proteins',n,'channels',c,'pumps',p,'ratio %.2f'%(c/p) if p else 'inf')
L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); ie,iq=h.index('Entry'),h.index('Sequence'); nr1=na=part=0
for l in L[1:]:
    x=l.split('\t'); s=x[iq]; c=N['channel'](s)
    if c=='Na': na+=1; print('NA',x[ie],len(s),flush=True)
    elif 800<=len(s)<1500 and len(S4.findall(s))>=4 and LYS.search(s): part+=1; print('NA_PARTIAL',x[ie],len(s),flush=True)
    if 'iGluR' in N['tags'](s):
        v,r=max((sc(s,igr[g]),g) for g in igr); nr1+=(r=='Grin1'); print('IGLUR',x[ie],len(s),'nearest',r,v,flush=True)
print('KIT','present' if (nr1 or na or part) else 'absent','NR1',nr1,'Na',na,'Na_partial',part)
