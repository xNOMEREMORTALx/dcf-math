"""L3597 frozen: K-channel families in non-neural animals (sponges other than Amphimedon; placozoans other than Trichoplax).
Steps: (1) dcf_nerve v2 tags on every protein; (2) every K/HCN/K2P call named by nearest mouse channel with the local aligner;
only matches with local score > 300 count as named (threshold set in L3593)."""
import gzip,pickle,re,runpy,sys,collections
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v2_L3549.py',run_name='x')
L=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py'); sc=L['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
fam=lambda g: 'K2P' if re.match(r'(?i)kcnk',g) else 'HCN' if re.match(r'(?i)hcn',g) else {'a':'Kv1','b':'Kv2','c':'Kv3','d':'Kv4','h':'KCNH','q':'Kv7'}.get(g[3].lower(),'silent')
ref={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(kcn[abcdghqsvk]\d+|hcn\d)',g) and len(p)>=200}
O={};S={}
for l in gzip.open(sys.argv[1],'rt').read().splitlines()[1:]:
    f=l.split('\t'); O[f[0]]=f[1]; S[f[0]]=f[-1]
print('proteins',len(S),'| organisms',len(set(O.values())))
groups=collections.defaultdict(set); na=0
for a,p in S.items():
    t=N['tags'](p)
    if 'Na' in t: na+=1
    if set(t)&{'K','HCN','K2P'}:
        s,r=max((sc(p,ref[r]),r) for r in ref)
        if s>300: groups['all'].add(fam(r)); print('  %-40s %s %s -> %s (%d)'%(O[a][:40],a,t,r,s))
print('named families (score>300):',sorted(groups['all']),'| DEKA Na calls:',na)
print('RESULT',[('B1','PASS' if 'Kv2' in groups['all'] else 'FAIL'),('B2','PASS' if 'KCNH' in groups['all'] else 'FAIL'),('B3','PASS' if na==0 else 'FAIL')])
