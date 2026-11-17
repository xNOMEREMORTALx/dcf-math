"""dcf_dna_index.py (L3745): find which stored DNA strand a noisy read came from. Pure Python, no numpy.
Exact K-mer cosine index (default K = 6), chosen over hyperdimensional vectors after L3737/L3741 (HD 89.8% vs exact 6-mer 99.8% at 15% substitutions,
development). Robust to substitutions and insertions/deletions because it compares bags of short words, not positions.
Index(strands, K) -> .find(read) -> (strand_index, score). Not for medical use."""
import collections,math
class Index:
    def __init__(self,strands,K=6):
        self.K=K; self.idx=collections.defaultdict(list); self.norm=[]
        for i,s in enumerate(strands):
            c=self._words(s); self.norm.append(math.sqrt(sum(v*v for v in c.values())) or 1.0)
            for w,v in c.items(): self.idx[w].append((i,v))
    def _words(self,s): return collections.Counter(s[j:j+self.K] for j in range(len(s)-self.K+1))
    def find(self,read):
        sc=collections.defaultdict(float)
        for w,v in self._words(read).items():
            for i,u in self.idx.get(w,()): sc[i]+=v*u
        if not sc: return (None,0.0)
        i=max(sc,key=lambda k:sc[k]/self.norm[k]); return (i,sc[i]/self.norm[i])
def mutate(s,sub,dl,r):
    out=[]
    for ch in s:
        if r.random()<dl: continue
        out.append(r.choice([b for b in 'ACGT' if b!=ch]) if r.random()<sub else ch)
        if r.random()<dl: out.append(r.choice('ACGT'))
    return ''.join(out)
def selftest():
    import random,dcf_dna_codec as codec
    r=random.Random(6); S=codec.encode(bytes(r.randrange(256) for _ in range(24*200)))[:200]; ix=Index(S)
    ok=sum(ix.find(mutate(S[t],0.10,0.03,r))[0]==t for t in (r.randrange(len(S)) for _ in range(200)))
    assert ix.find(S[7])[0]==7, 'exact read must find itself'
    assert ok>=190, 'noisy reads: %d/200'%ok
    return ok
if __name__=='__main__': print('dcf_dna_index selftest: %d/200 noisy reads found'%selftest())
