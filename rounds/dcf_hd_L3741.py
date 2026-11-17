"""L3741: HD index with D and K from argv (else identical to L3737) for DNA-storage strands (method frozen in PREREGISTERED_L3737_hd_retrieval.txt)."""
import os,sys,random
import numpy as np
sys.path.insert(0,'/home/claude/dcf-math/phone'); import dcf_dna_codec as codec
D=int(sys.argv[1]); K=int(sys.argv[2]); rng=np.random.default_rng(3737)
BV={b:rng.choice([-1,1],D).astype(np.int8) for b in 'ACGT'}
ROT={b:[np.roll(BV[b],i) for i in range(K)] for b in 'ACGT'}
def hv(s):
    acc=np.zeros(D,np.int32)
    for i in range(len(s)-K+1):
        v=np.ones(D,np.int8)
        for j,b in enumerate(s[i:i+K]): v=v*ROT[b][j]
        acc+=v
    return np.where(acc>=0,1,-1).astype(np.int8)
def mutate(s,sub,dl,r):
    out=[]
    for ch in s:
        u=r.random()
        if u<dl: continue                                  # deletion
        out.append(r.choice([b for b in 'ACGT' if b!=ch]) if r.random()<sub else ch)
        if r.random()<dl: out.append(r.choice('ACGT'))     # insertion
    return ''.join(out)
if __name__=='__main__':
    random.seed(3737); r=random.Random(3737)
    data=bytes(r.randrange(256) for _ in range(24*1000)); S=codec.encode(data)[:1000]
    M=np.stack([hv(s) for s in S]).astype(np.int32); pre={}
    for i,s in enumerate(S): pre.setdefault(s[:20],[]).append(i)
    print('strands',len(S),'length',len(S[0]),'distinct 20-nt prefixes',len(pre))
    for sub,dl in [(0.05,0),(0.05,0.025),(0.15,0),(0.10,0),(0.10,0.05)]:
        hd=bl=0
        for _ in range(2000):
            t=r.randrange(len(S)); q=mutate(S[t],sub,dl,r)
            hd+=int(np.argmax(M@hv(q).astype(np.int32))==t)
            c=pre.get(q[:20],[]); bl+=int(c==[t])
        print('sub %.3f indel %.3f+%.3f | HD %.4f | prefix baseline %.4f'%(sub,dl,dl,hd/2000,bl/2000),flush=True)
