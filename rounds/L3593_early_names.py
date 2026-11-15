"""L3593 descriptive: name K/K2P/HCN calls of choanoflagellate, sponge and placozoan (L3501) by nearest mouse channel (local aligner)."""
import gzip,pickle,re,runpy,collections
L=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py'); sc=L['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
fam=lambda g: 'K2P' if re.match(r'(?i)kcnk',g) else 'HCN' if re.match(r'(?i)hcn',g) else 'Kv'+g[3].lower()
ref={g:p for g,p in P['mouse'].items() if re.match(r'(?i)^(kcn[abcdghqsvk]\d+|hcn\d)',g) and len(p)>=200}
O={};S={}
for l in gzip.open('/home/claude/L3501/z/early.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t'); O[f[0]]=f[1].split(' (')[0]; S[f[0]]=f[3]
for l in open('rounds/L3501_tool.txt'):
    x=l.split()
    if x and x[0] in ('K','K2P','HCN') and not O[x[1]].startswith('Nematostella'):
        sc_=sorted(((sc(S[x[1]],ref[r]),r) for r in ref),reverse=True)[:2]
        print('  %-26s %-4s %s nearest %-7s (%s; score %d, runner-up %s %d)'%(O[x[1]][:26],x[0],x[1],sc_[0][1],fam(sc_[0][1]),sc_[0][0],sc_[1][1],sc_[1][0]))
# mouse symbol-based family counts (mouse files 1-3) for Figure 6
m=collections.Counter(fam(g) for g in P['mouse'] if re.match(r'(?i)^(kcn[abcdghqsv]\d+)$',g))
print('mouse (files 1-3) voltage-gated K genes by symbol family:',dict(m))
