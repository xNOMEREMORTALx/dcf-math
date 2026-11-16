"""L3665 frozen: one proteome (argv[1]). Battery ratio and Na calls (dcf_battery_v3_L3633 / dcf_nerve v3); NALCN hits + rings (frozen L3653 definitions);
iGluR calls -> nearest of the 18 mouse iGluRs by local aligner (L3625 method; NR1 = nearest Grin1). Reads Entry+Sequence only."""
import gzip,re,runpy,sys
B=runpy.run_path('/home/claude/dcf-math/rounds/dcf_battery_v3_L3633.py',run_name='x'); N=B['N']
src=open('/home/claude/dcf-math/rounds/dcf_nalcn_ring_L3653.py').read().split("print('control mouse Nalcn ring:'")[0]; G={}; exec(src,G)
sc=G['sc']; P=G['P']
igr={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(gria\d|grik\d|grid\d|grin\d\w?)$',g)}
f=sys.argv[1]
for o,(c,p,n) in B['per_org'](f).items(): print('ratio',o,'proteins',n,'channels',c,'pumps',p,'ratio %.2f'%(c/p) if p else 'inf')
L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); ie,iq=h.index('Entry'),h.index('Sequence')
for l in L[1:]:
    x=l.split('\t'); s=x[iq]; t=N['tags'](s)
    if 'Na' in t: print('NA',x[ie],len(s),flush=True)
    if 'iGluR' in t:
        v,r=max((sc(s,igr[g]),g) for g in igr); print('IGLUR',x[ie],len(s),'nearest',r,v,flush=True)
    if 1300<=len(s)<=2600 and len(re.findall(r'(?=[TS].[ED].W)',s))>=3:
        v,r=max((sc(s,G['ref'][g]),g) for g in G['ref'])
        if r=='Nalcn' and v>=1000: print('NALCN',x[ie],len(s),v,G['ring'](s),flush=True)
