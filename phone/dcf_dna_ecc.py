"""dcf_dna_ecc v6 (L2784): clusters() indexes every 20-mer (stride 1); unlabelled reads decode at 12% error / 25 reads.
dcf_dna_ecc v5 (L2780): insertion votes counted per read (any insertion), not per exact inserted string.
dcf_dna_ecc v4 (L2772): adds clusters() (unlabelled reads grouped by shared 20-mers), consensus4() (alignment with gap and
insertion votes; handles substitutions, deletions and insertions) and corrupt3(). Recommended decode: clusters -> consensus4 -> decode.
dcf_dna_ecc v3 (L2768): adds consensus2() - deletion-tolerant consensus (reads with <=2 deletions realigned by DP).
dcf_dna_ecc v2 (L2764; was L2665). Changes: K+M<=255 guard (GF(256) block limit; previously crashed), default K=200,M=40
(same density as 20/4 but large blocks average strand loss), and consensus() for base-level majority across reads of one strand.
L2665: outer Reed-Solomon erasure code across strands on top of dcf_dna_codec (inner: rotating code + mod-255 check).
Data is split into groups of K strands; for each group, M parity strands are computed column-wise with RS(K+M, K) over GF(256).
A strand that fails its inner checksum (or is lost) is an erasure; up to M erasures per group are recovered."""
import random, sys
from reedsolo import RSCodec, ReedSolomonError
import zlib
from collections import Counter
CHK=4
def chk(b): return zlib.crc32(b).to_bytes(4,'big')
sys.path.insert(0,'.')
import dcf_dna_codec as C
CH=24
def encode(data,K=200,M=40):
    if K+M>255: raise ValueError('K+M must be <= 255 for RS over GF(256)')
    w=C.whitening_bytes(len(data)); x=bytes(a^b for a,b in zip(data,w))
    x+=bytes((-len(x))%(CH*K))
    chunks=[x[i:i+CH] for i in range(0,len(x),CH)]
    rs=RSCodec(M)
    strands=[]
    for g in range(0,len(chunks),K):
        grp=chunks[g:g+K]
        par=[bytearray(CH) for _ in range(M)]
        for col in range(CH):
            cw=rs.encode(bytes(c[col] for c in grp))[K:]
            for m in range(M): par[m][col]=cw[m]
        for idx,blk in enumerate(grp+[bytes(p) for p in par]):
            sid=((g//K)*(K+M)+idx).to_bytes(2,'big')
            payload=sid+blk+chk(sid+blk)
            strands.append(C.rot_encode(C.to_trits(payload)))
    return strands
def decode(strands,n,K=200,M=40):
    if K+M>255: raise ValueError('K+M must be <= 255 for RS over GF(256)')
    votes={}
    for s in strands:
        try: pl=C.from_trits(C.rot_decode(s))
        except Exception: continue
        if len(pl)!=CH+2+CHK or chk(pl[:-CHK])!=pl[-CHK:]: continue
        votes.setdefault(int.from_bytes(pl[:2],'big'),Counter())[pl[2:-CHK]]+=1
    got={k:v.most_common(1)[0][0] for k,v in votes.items()}
    ngroups=-(-((n+(-n)%(CH*K))//CH)//K)
    rs=RSCodec(M); out=bytearray()
    for g in range(ngroups):
        ids=[g*(K+M)+i for i in range(K+M)]
        er=[i for i,s in enumerate(ids) if s not in got]
        if len(er)>M: return None
        cols=[]
        for col in range(CH):
            cw=bytearray(got[s][col] if s in got else 0 for s in ids)
            try: dec=rs.decode(cw,erase_pos=er)[0] if er else cw[:K]
            except ReedSolomonError: return None
            cols.append(dec)
        for r in range(K): out+=bytes(cols[c][r] for c in range(CH))
    w=C.whitening_bytes(n); return bytes(a^b for a,b in zip(out[:n],w))
def consensus(reads,L):
    """L2764: base-level majority over reads of one strand that kept the expected length L (deletions are discarded)."""
    full=[r for r in reads if len(r)==L]
    if not full: return None
    return ''.join(Counter(col).most_common(1)[0][0] for col in zip(*full))
def best_gapped(read,cons,maxdel=2):
    """insert maxdel-or-fewer gaps into read to best match cons (same length); DP over (pos in cons, gaps used)."""
    L=len(cons); d=L-len(read)
    if d<0 or d>maxdel: return None
    # score[i][g]: best matches aligning cons[:i] with read[:i-g] using g gaps
    NEG=-10**9; S=[[NEG]*(d+1) for _ in range(L+1)]; B=[[0]*(d+1) for _ in range(L+1)]; S[0][0]=0
    for i in range(1,L+1):
        for g in range(d+1):
            j=i-g
            if 1<=j<=len(read) and S[i-1][g]>NEG:
                v=S[i-1][g]+(read[j-1]==cons[i-1])
                if v>S[i][g]: S[i][g]=v; B[i][g]=0
            if g>=1 and S[i-1][g-1]>NEG:
                v=S[i-1][g-1]
                if v>S[i][g]: S[i][g]=v; B[i][g]=1
    out=[]; i,g=L,d
    while i>0:
        if B[i][g]==0: out.append(read[i-g-1]); i-=1
        else: out.append(None); i-=1; g-=1
    return out[::-1]
def consensus2(reads,L,maxdel=2,rounds=2):
    full=[r for r in reads if len(r)==L]
    short=[r for r in reads if L-maxdel<=len(r)<L]
    seed=full or short
    if not seed: return None
    if full: cons=''.join(Counter(c).most_common(1)[0][0] for c in zip(*full))
    else:   # no full read: pad the first short read where needed by aligning to itself (weak); fall back
        return None
    for _ in range(rounds):
        cols=[Counter(c) for c in zip(*full)] if full else [Counter() for _ in range(L)]
        for r in short:
            al=best_gapped(r,cons,maxdel)
            if al is None: continue
            for k,x in enumerate(al):
                if x is not None: cols[k][x]+=1
        cons=''.join(c.most_common(1)[0][0] if c else cons[k] for k,c in enumerate(cols))
    return cons

# ---- L2772 additions ----
from collections import defaultdict
KMER=20
def clusters(reads):
    par=list(range(len(reads)))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    seen={}
    for i,r in enumerate(reads):
        for j in range(0,len(r)-KMER+1,1):                    # every 20-mer: sampled positions miss matches between reads with different indel shifts (L2784)
            k=r[j:j+KMER]
            if k in seen: par[f(i)]=f(seen[k])
            else: seen[k]=i
    g=defaultdict(list)
    for i in range(len(reads)): g[f(i)].append(reads[i])
    return list(g.values())
def corrupt3(s,p_sub,p_del,p_ins,rng):
    t=[]
    for c in s:
        r=rng.random()
        if r<p_ins: t.append(rng.choice('ACGT'))
        r=rng.random()
        if r<p_del: continue
        if r<p_del+p_sub: c=rng.choice([q for q in 'ACGT' if q!=c])
        t.append(c)
    return ''.join(t)
def align_full(read,cons,band=6):
    L,M=len(cons),len(read); S={(0,0):0}; B={}
    for i in range(L+1):
        for j in range(max(0,i-band),min(M,i+band)+1):
            if i==0 and j==0: continue
            best=None; bt=None
            if i>0 and j>0 and (i-1,j-1) in S:
                v=S[(i-1,j-1)]+(1 if read[j-1]==cons[i-1] else -1); best,bt=v,'M'
            if i>0 and (i-1,j) in S:
                v=S[(i-1,j)]-1
                if best is None or v>best: best,bt=v,'D'
            if j>0 and (i,j-1) in S:
                v=S[(i,j-1)]-1
                if best is None or v>best: best,bt=v,'I'
            if bt: S[(i,j)]=best; B[(i,j)]=bt
    if (L,M) not in S: return None
    base=[None]*L; ins=[[] for _ in range(L+1)]; i,j=L,M; pend=[]
    while i>0 or j>0:
        t=B[(i,j)]
        if t=='M': base[i-1]=read[j-1]; i-=1; j-=1
        elif t=='D': base[i-1]='-'; i-=1
        else: ins[i].append(read[j-1]); j-=1
    return base,ins
def consensus4(reads,L,rounds=4,band=6):
    reads=[r for r in reads if abs(len(r)-L)<=band]
    if not reads: return None
    full=[r for r in reads if len(r)==L]
    cons=''.join(Counter(c).most_common(1)[0][0] for c in zip(*full)) if full else min(reads,key=lambda r:abs(len(r)-L))
    for _ in range(rounds):
        n=len(cons); bv=[Counter() for _ in range(n)]; iv=[Counter() for _ in range(n+1)]; used=0
        for r in reads:
            a=align_full(r,cons,band)
            if a is None: continue
            used+=1; base,ins=a
            for k,x in enumerate(base): bv[k][x]+=1
            for k,xs in enumerate(ins): iv[k][''.join(reversed(xs))]+=1
        if not used: return None
        new=[]
        for k in range(n+1):
            nins=sum(v for key,v in iv[k].items() if key)                   # L2780: reads carrying ANY insertion here
            if nins*2>used:
                first=Counter()
                for key,v in iv[k].items():
                    if key: first[key[0]]+=v
                new.append(first.most_common(1)[0][0])                      # insert one base: the most common first inserted base
            if k<n:
                x=bv[k].most_common(1)[0][0] if bv[k] else cons[k]
                if x!='-': new.append(x)
        new=''.join(new)
        if new==cons: break
        cons=new
    return cons if len(cons)==L else None

def corrupt(strands,p_sub,p_del,rng):
    out=[]
    for s in strands:
        t=[]
        for c in s:
            r=rng.random()
            if r<p_del: continue
            if r<p_del+p_sub: c=rng.choice([q for q in 'ACGT' if q!=c])
            t.append(c)
        out.append(''.join(t))
    return out
if __name__=="__main__":
    rng=random.Random(7); data=bytes(rng.randrange(256) for _ in range(9600))
    for K,M in ((20,4),(200,40)):
        st=encode(data,K,M); nt=sum(map(len,st)); dens=8*len(data)/nt
        for rate in (0.0005,0.001,0.002,0.004):
            ok=0; trials=20
            for _ in range(trials):
                bad=corrupt(st,rate*0.7,rate*0.3,rng)
                ok+= decode(bad,len(data),K,M)==data
            print("RS(K=%d,M=%d) density %.3f bits/nt | per-nt error %.2f%%: recovered %d/%d"%(K,M,dens,100*rate,ok,trials))
    st=encode(data); L=len(st[0]); ok=0
    for _ in range(3):
        cons=[x for x in (consensus(corrupt([s]*10,0.007,0.003,rng),L) for s in st) if x]; ok+=decode(cons,len(data))==data
    print("v2 default RS(200,40), 10 reads/strand, 1%% per-base error, base-level consensus: recovered %d/3"%ok)
    ok=0
    for _ in range(3):
        cons=[x for x in (consensus2(corrupt([s]*10,0.021,0.009,rng),L) for s in st) if x]; ok+=decode(cons,len(data))==data
    print("v3 deletion-tolerant consensus, 10 reads/strand, 3%% per-base error: recovered %d/3"%ok)
    pool=[corrupt3(s,0.03,0.01,0.01,rng) for s in st for _ in range(10)]; rng.shuffle(pool)
    cons=[x for x in (consensus4(g,L) for g in clusters(pool) if len(g)>=2) if x]
    print("v4 UNLABELLED shuffled reads, 5%% error incl. insertions, 10 reads/strand: recovered %s"%(decode(cons,len(data))==data))
