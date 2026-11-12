"""L3325 [Enzyme map], development on graded blind_20 genomes: which annotated products carry 3-3-4 ladders in proteins > 200 aa, by tier."""
import sys, re, collections
sys.path.insert(0,'/home/claude/dcf-genefinder'); import dcf_redox as R
tier={'NC_013198':1,'NC_004116':1,'NC_007929':1,'NC_008530':1,'NC_012560':2,'NC_008686':2,'NC_014532':2,'NC_007651':2,
'NC_009495':3,'NC_009012':3,'NC_009718':3,'NC_011898':3,'NC_009515':4,'NC_011296':4,'NC_012438':4,'NC_008554':4}
def fam(prod):
    p=prod.lower()
    for k,ws in [('hydrogenase',['hydrogenase']),('PFOR / 2-oxoacid:Fd oxidoreductase',['pyruvate:ferredoxin','pyruvate ferredoxin','pyruvate synthase','oxoacid:ferredoxin','oxoglutarate','2-oxoacid','indolepyruvate','pyruvate flavodoxin','por ']),
                 ('CODH / acetyl-CoA synthase',['carbon monoxide','co dehydrogenase','acetyl-coa decarbonylase','codh']),('heterodisulfide reductase',['heterodisulfide']),
                 ('formate dehydrogenase',['formate dehydrogenase']),('NADH / complex I-type',['nadh','nuo','complex i']),('Rnf / electron transport complex',['rnf','electron transport complex']),
                 ('radical SAM',['radical sam']),('succinate/fumarate reductase',['succinate dehydrogenase','fumarate reductase']),('sulfite / APS reductase',['sulfite reductase','adenylyl','aps reductase','dsr']),
                 ('glutamate synthase',['glutamate synthase']),('Fe-S ferredoxin-domain protein (other)',['4fe-4s','ferredoxin','iron-sulfur','fe-s'])]:
        if any(w in p for w in ws): return k
    return 'other / hypothetical'
cnt={t:collections.Counter() for t in (1,2,3,4)}; OTHER=collections.Counter()
for a,t in tier.items():
    d='/home/claude/L3273' if a=='NC_008530' else '/home/claude/L3269'
    txt=open(f'{d}/g/{a}.gb').read().split('\nORIGIN')[0]
    stops={}
    for feat in re.split(r'\n     CDS             ',txt)[1:]:
        loc=feat.split('\n')[0]; m=re.findall(r'\d+',loc)
        if not m: continue
        pr=re.search(r'/product="([^"]+)"',feat.replace('\n                     ',' '))
        st=int(m[0]) if 'complement' in loc else int(m[-1])
        stops[(st,'complement' in loc)]=pr.group(1) if pr else 'unnamed'
    seq=R.read_seq(f'{d}/g/{a}.gb')
    for l in open(f'{d}/out/{a}.gff3'):
        f=l.split('\t')
        if len(f)<7 or f[2]!='CDS': continue
        s,e,sd=int(f[3]),int(f[4]),f[6]
        g=seq[s-1:e] if sd=='+' else seq[s-1:e].translate(R.comp)[::-1]
        p=''.join(R.CODE.get(g[i:i+3],'X') for i in range(0,len(g)-3,3))
        c=len(re.findall(r'(?=C..C..C...C)',p))
        if c and len(p)>200:
            prod=stops.get((s,True) if sd=='-' else (e,False),'(no annotated match)')
            cnt[t][fam(prod)]+=c
            if fam(prod).startswith("other") and t>=3: OTHER[prod]+=c
for t in (1,2,3,4):
    tot=sum(cnt[t].values()); print("tier %d: %d ladders in large proteins"%(t,tot))
    for k,v in cnt[t].most_common(8): print("   %-40s %4d (%2.0f%%)"%(k,v,100*v/max(tot,1)))
print("\ntop tier 3-4 other:"); [print("   %3d  %s"%(v,k[:80])) for k,v in OTHER.most_common(15)]
