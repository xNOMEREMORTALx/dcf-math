"""L3745 frozen blind test of phone/dcf_dna_index.py (K = 6) on fresh strands and reads (seed 3745), same conditions as L3737."""
import sys,random
sys.path.insert(0,'/home/claude/dcf-math/phone'); import dcf_dna_codec as codec, dcf_dna_index as dx
r=random.Random(3745); S=codec.encode(bytes(r.randrange(256) for _ in range(24*1000)))[:1000]; ix=dx.Index(S,6)
for sub,dl in [(0.05,0),(0.05,0.025),(0.15,0),(0.10,0),(0.10,0.05)]:
    ok=sum(ix.find(dx.mutate(S[t],sub,dl,r))[0]==t for t in (r.randrange(len(S)) for _ in range(2000)))
    print('sub %.3f indel %.3f+%.3f | exact 6-mer %.4f'%(sub,dl,dl,ok/2000),flush=True)
