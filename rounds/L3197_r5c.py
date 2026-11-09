import numpy as np, math, time
from sympy import n_order, isprime, factorint
B=10**8
s=np.ones(B//2,dtype=bool); s[0]=False
for i in range(1,int(B**0.5)//2+1):
    if s[i]: p=2*i+1; s[p*p//2::p]=False
primes=(2*np.nonzero(s)[0]+1)
Ns=[10946,17711,28657,46368,75025]
t=time.time(); cand={N:[] for N in Ns}
for p in primes.tolist():
    if p==5: continue
    for N in Ns:
        if pow(10,N,p)==1:
            pk=p
            while pk<B and pow(10,N,pk)==1:
                cand[N].append((pk,p,n_order(10,pk))); pk*=p
print("scan",round(time.time()-t),"s")
for N in Ns:
    byp={}
    for pk,p,o in cand[N]: byp.setdefault(p,[]).append((pk,o))
    P=sorted(byp); best=[None]
    def go(i,prod,L):
        if L==N and prod>1 and (best[0] is None or prod<best[0]): best[0]=prod
        if i==len(P): return
        go(i+1,prod,L)
        for pk,o in byp[P[i]]:
            if prod*pk < (best[0] or B): go(i+1,prod*pk,math.lcm(L,o))
    go(0,1,1); q=best[0]
    print(N, factorint(N), "min q:", q, (factorint(q) if q else ''), ("prime" if q and isprime(q) else "composite" if q else "none<1e8"),
          "| primes with order dividing N:", [(p,o) for pk,p,o in cand[N] if pk==p])
# cheapest composite cover (exclude single primes)
for N in Ns:
    byp={}
    for pk,p,o in cand[N]: byp.setdefault(p,[]).append((pk,o))
    P=sorted(byp); best=[None,None]
    def go(i,prod,L,parts):
        if L==N and len(parts)>1 and (best[0] is None or prod<best[0]): best[0]=prod; best[1]=parts
        if i==len(P): return
        go(i+1,prod,L,parts)
        for pk,o in byp[P[i]]:
            if prod*pk < (best[0] or B): go(i+1,prod*pk,math.lcm(L,o),parts+[(pk,o)])
    go(0,1,1,[])
    print("cheapest composite",N,best)
