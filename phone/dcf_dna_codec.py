"""DCF DNA codec prototype (L2664).
bytes -> whitening with base-4 period of 1/p (the classical '1/P generator', Blum-Blum-Shub 1986)
      -> base-3 digits -> Goldman-style rotating code (next base != previous base: no homopolymers)
      -> per-strand index + mod-255 'casting-out' checksum (the base-256 analogue of casting out nines).
Self-test measures bits/nt, GC content, max homopolymer, and single-substitution detection."""
import sys, random, hashlib
BASES="ACGT"
def base_period(p,b=4):
    # digits of 1/p in base b over one period
    from sympy import n_order
    T=n_order(b,p); r=1; out=[]
    for _ in range(T): r*=b; out.append(r//p); r%=p
    return out
P_WHITEN=1000003     # prime with ord_1000003(4) large (checked in selftest)
_W=None
def whitening_bytes(n):
    global _W
    if _W is None:
        d=base_period(P_WHITEN)     # base-4 digits
        _W=bytes((d[4*i]<<6)|(d[4*i+1]<<4)|(d[4*i+2]<<2)|d[4*i+3] for i in range(len(d)//4))
    return (_W*(n//len(_W)+1))[:n]
def to_trits(data):
    n=int.from_bytes(b'\x01'+data,'big'); t=[]
    while n: t.append(n%3); n//=3
    return t[::-1]
def from_trits(t):
    n=0
    for x in t: n=n*3+x
    b=n.to_bytes((n.bit_length()+7)//8,'big'); return b[1:]
def rot_encode(trits,prev='A'):
    s=[]
    for x in trits:
        choices=[c for c in BASES if c!=prev]; c=choices[x]; s.append(c); prev=c
    return ''.join(s)
def rot_decode(seq,prev='A'):
    t=[]
    for c in seq:
        choices=[q for q in BASES if q!=prev]; t.append(choices.index(c)); prev=c
    return t
def checksum255(data): return sum(data)%255      # casting out 255s (base-256 'nines')
def encode(data,chunk=24):
    w=whitening_bytes(len(data)); x=bytes(a^b for a,b in zip(data,w))
    strands=[]
    for i in range(0,len(x),chunk):
        block=x[i:i+chunk]; idx=(i//chunk).to_bytes(2,'big')
        payload=idx+block+bytes([checksum255(idx+block)])
        strands.append(rot_encode(to_trits(payload)))
    return strands
def decode(strands,n):
    out={}
    for s in strands:
        try: payload=from_trits(rot_decode(s))
        except Exception: continue
        if len(payload)<3 or checksum255(payload[:-1])!=payload[-1]: continue
        out[int.from_bytes(payload[:2],'big')]=payload[2:-1]
    x=b''.join(out[k] for k in sorted(out)); w=whitening_bytes(len(x))
    return bytes(a^b for a,b in zip(x,w))[:n], len(out)
def maxrun(s):
    m=c=1
    for a,b in zip(s,s[1:]): c=c+1 if a==b else 1; m=max(m,c)
    return m
def selftest():
    from sympy import n_order
    print("ord_%d(4) = %d (whitening period in base-4 digits)"%(P_WHITEN,n_order(4,P_WHITEN)))
    rng=random.Random(1)
    for name,data in (("random",bytes(rng.randrange(256) for _ in range(4096))),("all-zero",bytes(4096)),("text",(b"DIGITAL COSMOS FRAMEWORK "*200)[:4096])):
        st=encode(data); seq=''.join(st)
        back,nb=decode(st,len(data))
        gc=sum(c in 'GC' for c in seq)/len(seq)
        print("%-8s ok=%s strands=%d nt=%d bits/nt=%.3f GC=%.3f max homopolymer=%d"%(name,back==data,len(st),len(seq),8*len(data)/len(seq),gc,max(maxrun(s) for s in st)))
    # error detection: single substitutions
    data=bytes(rng.randrange(256) for _ in range(2400)); st=encode(data); det=0; N=2000
    for _ in range(N):
        i=rng.randrange(len(st)); s=list(st[i]); j=rng.randrange(len(s)); s[j]=rng.choice([c for c in BASES if c!=s[j]])
        bad=st[:]; bad[i]=''.join(s)
        back,nb=decode(bad,len(data))
        det+= (nb==len(st)-1)          # corrupted strand rejected
    print("single substitutions detected (strand rejected): %d/%d"%(det,N))
if __name__=="__main__": selftest()
