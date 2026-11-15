"""L3589 frozen: name sea-anemone (Nematostella) K/K2P/HCN calls (L3509 tool output) by nearest mouse channel, LOCAL alignment score."""
import gzip,pickle,re,runpy,collections
L=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py'); sc=L['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
fam=lambda g: 'K2P' if re.match(r'(?i)kcnk',g) else 'HCN' if re.match(r'(?i)hcn',g) else 'Kv'+g[3].lower()
pat=r'(?i)^(kcn[abcdghqsvk]\d+|hcn\d)'
ref={g:p for g,p in P['mouse'].items() if re.match(pat,g) and len(p)>=200}
S={}
for l in gzip.open('/home/claude/L3501/z/early.tsv.gz','rt').read().splitlines()[1:]:
    f=l.split('\t')
    if f[1].startswith('Nematostella'): S[f[0]]=f[3]
calls=[l.split()[:2] for l in open('/home/claude/dcf-math/rounds/L3501_tool.txt') if l.split() and l.split()[0] in ('K','K2P','HCN') and l.split()[1] in S]
seen=set(); tab=collections.Counter(); rows=[]
for c,a in calls:
    if S[a] in seen: continue
    seen.add(S[a]); b=max(ref,key=lambda r: sc(S[a],ref[r])); tab[(c,fam(b))]+=1; rows.append((c,a,b))
print('distinct sequences:',len(rows))
for k,n in sorted(tab.items(),key=lambda x:-x[1]): print('  tool %-4s nearest %-6s %d'%(k[0],k[1],n))
k2p=[r for r in rows if r[0]=='K2P']; k2p_ok=sum(fam(r[2])=='K2P' for r in k2p)
kv=[r for r in rows if r[0]=='K']; kv14=sum(fam(r[2]) in ('Kva','Kvb','Kvc','Kvd') for r in kv)
print('K2P calls nearest a K2P: %d/%d ; K calls nearest Kv1-Kv4 (a,b,c,d): %d/%d'%(k2p_ok,len(k2p),kv14,len(kv)))
kvf=collections.Counter(fam(r[2]) for r in kv); top=kvf.most_common(1)[0]
print('K-call subfamilies:',dict(kvf),'| largest share %.0f%% (%s)'%(100*top[1]/len(kv),top[0]))
print('RESULT',[('A1','PASS' if sum(1 for f in kvf if f in ('Kva','Kvb','Kvc','Kvd','Kvh'))>=4 else 'FAIL'),('A2','PASS' if top[1]/len(kv)<=0.6 else 'FAIL')])
for r in rows: print('   ',r)
