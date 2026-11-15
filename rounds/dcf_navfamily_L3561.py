"""L3561 frozen: which sodium-channel family do the sea-urchin and acorn-worm E-type channels belong to?
Similarity = shared amino-acid 4-mers / min(4-mer set sizes) (alignment-free). Reference sets (all from files already graded):
 NAV1 (K-type, bilaterian fast channel): Lingula A0A1S3HN89, Capitella R7TMI4, lancelet I6NQF8, Ciona F6QCF9, fly para, human SCN2A
 NAV2 (E-type within bilaterians, paralog of NAV1): Capitella R7TCA7, lancelet A0A9J7HQP1
 Query: acorn worm A0ACM8CKW0, sea urchin A0A7M7N9I2 (+ A0A7M7SUY6, A0A7M7SV24)."""
import gzip,pickle,sys
def load_tsv(path,ids):
    out={}
    for l in gzip.open(path,'rt'):
        f=l.rstrip('\n').split('\t')
        if f[0] in ids: out[f[0]]=f[-1]
    return out
S={}
S.update(load_tsv('/home/claude/L3533/z/bil.tsv.gz',{'A0A1S3HN89','R7TMI4','R7TCA7','A0ACM8CKW0','A0A7M7N9I2','A0A7M7SUY6','A0A7M7SV24'}))
S.update(load_tsv('/home/claude/L3557/z/oc.tsv.gz',{'I6NQF8','F6QCF9','A0A9J7HQP1'}))
P,D=pickle.load(open('/home/claude/L3469/P6.pkl','rb')); S['fly_para']=P['fly']['para']; S['human_SCN2A']=P['human']['SCN2A']
K=4; km={a:set(p[i:i+K] for i in range(len(p)-K+1)) for a,p in S.items()}
sim=lambda a,b: len(km[a]&km[b])/min(len(km[a]),len(km[b]))
NAV1=['A0A1S3HN89','R7TMI4','I6NQF8','F6QCF9','fly_para','human_SCN2A']; NAV2=['R7TCA7','A0A9J7HQP1']
Q=['A0ACM8CKW0','A0A7M7N9I2','A0A7M7SUY6','A0A7M7SV24']
print('missing:',[x for x in NAV1+NAV2+Q if x not in S])
for q in Q:
    s1=max(sim(q,r) for r in NAV1); s2=max(sim(q,r) for r in NAV2)
    print('%-12s best NAV1 %.3f  best NAV2 %.3f  -> %s'%(q,s1,s2,'NAV1' if s1>s2 else 'NAV2'))
print('control: NAV1 members vs each other (min of best-other):',round(min(max(sim(a,b) for b in NAV1 if b!=a) for a in NAV1),3),
      '| NAV2 vs NAV2:',round(sim(*NAV2),3),'| NAV1 vs NAV2 (max):',round(max(sim(a,b) for a in NAV1 for b in NAV2),3))
