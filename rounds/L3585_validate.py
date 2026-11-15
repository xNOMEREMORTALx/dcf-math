"""L3585 validation (development): name zebrafish NAMED K/HCN/K2P channels by nearest mouse channel (local score), truth = zebrafish symbol."""
import pickle,re,runpy,collections
L=runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py'); sc=L['score']
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb'))
fam=lambda g: 'K2P' if re.match(r'(?i)kcnk',g) else 'HCN' if re.match(r'(?i)hcn',g) else g[3].lower()
pat=r'(?i)^(kcn[abcdghqsvk]\d+|hcn\d)'
ref={g:p for g,p in P['mouse'].items() if re.match(pat,g) and len(p)>=200}
qry={g:p for g,p in P['zebrafish'].items() if re.match(pat,g) and len(p)>=200}
import random; random.seed(1); qs=sorted(qry); qs=random.sample(qs,min(40,len(qs)))
ok=0; conf=collections.Counter()
for q in qs:
    b=max(ref,key=lambda r: sc(qry[q],ref[r])); t=fam(q); f=fam(b); ok+=t==f; conf[(t,f)]+=1
    if t!=f: print('  miss',q,'->',b)
print('zebrafish named channels (random 40 of %d): nearest mouse family correct %d/%d'%(len(qry),ok,len(qs)))
