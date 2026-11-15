"""L3633 frozen (L3609 with dcf_nerve v3): battery ratio = channel calls (Na, Nax, K, Ca, CaT, HCN, K2P) / metal-pump calls (Na/K, Ca, Cu), per organism,
using dcf_nerve v2 (rounds/dcf_nerve_v3_L3633.py). Input: UniProt TSV with Organism column (or a FASTA = one organism)."""
import gzip,runpy,sys,collections
N=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v3_L3633.py',run_name='x')
CH={'Na','Nax','K','Ca','CaT','HCN','K2P'}; PU={'pump_NaK','pump_Ca','pump_Cu'}
def per_org(path,label=None):
    out=collections.defaultdict(lambda:[0,0,0])
    if path.endswith(('.tsv.gz','.tsv')) or not label:
        op=gzip.open if path.endswith('.gz') else open
        L=op(path,'rt').read().splitlines(); h=L[0].split('\t'); io=h.index('Organism'); iq=h.index('Sequence')
        for l in L[1:]:
            f=l.split('\t'); o=f[io].split(' (')[0]; t=set(N['tags'](f[iq])); r=out[o]
            r[0]+=len(t&CH)>0; r[1]+=len(t&PU)>0; r[2]+=1
    else:
        for g,p in N['proteins'](path).items():
            t=set(N['tags'](p)); r=out[label]; r[0]+=len(t&CH)>0; r[1]+=len(t&PU)>0; r[2]+=1
    return out
if __name__=='__main__':
    for a in sys.argv[1:]:
        path,_,label=a.partition('=')
        for o,(c,p,n) in sorted(per_org(path,label or None).items(),key=lambda x:-x[1][2]):
            if n>=5000: print('%-40s proteins %6d channels %4d pumps %3d ratio %s'%(o[:40],n,c,p,'%.2f'%(c/p) if p else 'inf'))
