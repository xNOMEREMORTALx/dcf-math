"""L3565 frozen: NAV1 vs NAV2 family of the non-bilaterian and acoel E-type sodium-channel homologues (same 4-mer method as L3561)."""
import gzip,re,pickle
def load_tsv(path,ids):
    out={}
    for l in gzip.open(path,'rt'):
        f=l.rstrip('\n').split('\t')
        if f[0] in ids: out[f[0]]=f[-1]
    return out
S={}
S.update(load_tsv('/home/claude/L3533/z/bil.tsv.gz',{'A0A1S3HN89','R7TMI4','R7TCA7'}))
S.update(load_tsv('/home/claude/L3557/z/oc.tsv.gz',{'I6NQF8','F6QCF9','A0A9J7HQP1'}))
S.update(load_tsv('/home/claude/L3501/z/early.tsv.gz',{'A9USM1','B3RSS4','A7SKR1'}))
S.update(load_tsv('/home/claude/L3509/z/cteno.tsv.gz',{'A0ACF8Y6N4','A0ACF8Y996','A0ACF8YBX3','F6MZB8','F6MZB9'}))
txt=gzip.open('/home/claude/L3521/z/hmia.pep.fa.gz','rt').read()
for b in txt.split('>')[1:]:
    h,_,s=b.partition('\n'); g=re.search(r'gene:(\S+)',h)
    if g and g.group(1) in ('HMIM006045','HMIM019623'):
        s=s.replace('\n','').rstrip('*')
        if len(s)>len(S.get(g.group(1),'')): S[g.group(1)]=s
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb')); S['fly_para']=P['fly']['para']; S['human_SCN2A']=P['human']['SCN2A']
K=4; km={a:set(p[i:i+K] for i in range(len(p)-K+1)) for a,p in S.items()}
sim=lambda a,b: len(km[a]&km[b])/min(len(km[a]),len(km[b]))
NAV1=['A0A1S3HN89','R7TMI4','I6NQF8','F6QCF9','fly_para','human_SCN2A']; NAV2=['R7TCA7','A0A9J7HQP1']
Q={'choanoflagellate':['A9USM1'],'placozoan':['B3RSS4'],'sea anemone':['A7SKR1'],'comb jelly':['A0ACF8Y6N4','A0ACF8Y996','A0ACF8YBX3','F6MZB8','F6MZB9'],'acoel':['HMIM006045','HMIM019623']}
print('missing:',[x for v in Q.values() for x in v if x not in S])
allNAV2=True
for grp,ids in Q.items():
    for q in ids:
        s1=max(sim(q,r) for r in NAV1); s2=max(sim(q,r) for r in NAV2); fam='NAV1' if s1>s2 else 'NAV2'; allNAV2&=(fam=='NAV2')
        print('%-16s %-12s best NAV1 %.3f  best NAV2 %.3f  -> %s'%(grp,q,s1,s2,fam))
print('RESULT',[('M1','PASS' if allNAV2 else 'FAIL')])
