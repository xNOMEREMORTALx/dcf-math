"""L3697 frozen (L3685 script with the calibrated NR1 caller): per proteome (argv[1..]): neural kit with the floored NR1 caller (dcf_nr1_L3681) + lysine Na / Na_partial (v3, L3641);
NAV-family count = 4-domain candidates (1300-2600 aa, >= 2 S4 matches, >= 2 ring words [TS]x[EDK]xW or a lysine loop) whose nearest of
mouse Scn2a, Scn8a, Cacna1a, Cacna1c, Cacna1g, Nalcn (local aligner) is an Scn with score >= 1000. Reads Entry+Sequence only."""
import gzip,pickle,re,runpy,sys
C=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nr1_L3693.py'); nr1=C['nr1']
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x'); S4=re.compile(N['S4']); LYS=re.compile(N['LYS'])
sc=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb')); ref={g:P['mouse'][g] for g in ['Scn2a','Scn8a','Cacna1a','Cacna1c','Cacna1g','Nalcn']}
for f in sys.argv[1:]:
    print('###',f.split('/')[-1]); L=gzip.open(f,'rt').read().splitlines(); h=L[0].split('\t'); ie,iq=h.index('Entry'),h.index('Sequence')
    n1=na=part=nav=0
    for l in L[1:]:
        x=l.split('\t'); s=x[iq]; c=N['channel'](s)
        if c=='Na': na+=1; print('NA',x[ie],len(s),flush=True)
        elif 800<=len(s)<1500 and len(S4.findall(s))>=4 and LYS.search(s): part+=1; print('NA_PARTIAL',x[ie],len(s),flush=True)
        ok,r,v=nr1(s)
        if ok: n1+=1; print('NR1',x[ie],len(s),v,flush=True)
        if 1300<=len(s)<=2600 and len(S4.findall(s))>=2 and (len(re.findall(r'(?=[TS].[EDK].W)',s))>=2 or LYS.search(s)):
            v,r=max((sc(s,ref[g]),g) for g in ref)
            if r.startswith('Scn') and v>=1000: nav+=1; print('NAV',x[ie],len(s),r,v,flush=True)
    print('SUMMARY proteins',len(L)-1,'NR1',n1,'Na',na,'Na_partial',part,'NAV_family',nav,'KIT','present' if (n1 or na or part) else 'absent',flush=True)
