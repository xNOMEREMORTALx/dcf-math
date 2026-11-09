import math, itertools, time
from sympy import primerange, n_order, isprime, divisors
B=2*10**7
Ns=[13,21,34,55,89,144,233,377,610,987]
t=time.time()
cand={N:[] for N in Ns}
for p in primerange(3,B):
    if p==5: continue
    for N in Ns:
        if pow(10,N,p)==1:
            pk=p
            while pk<B and pow(10,N,pk)==1:
                cand[N].append((pk,p,n_order(10,pk))); pk*=p
print("scan",round(time.time()-t,1),"s")
for N in Ns:
    items=cand[N]  # (prime power, prime, order)
    best=None
    # search subsets of distinct primes (choose one power per prime), product < B
    byp={}
    for pk,p,o in items: byp.setdefault(p,[]).append((pk,o))
    P=sorted(byp)
    def rec(i,prod,L,used):
        nonlocal_best=None
    stack=[(0,1,1)]
    res=[]
    def go(i,prod,L):
        global best
        if L==N and prod>1:
            if best is None or prod<best: best=prod
        if i==len(P): return
        go(i+1,prod,L)
        for pk,o in byp[P[i]]:
            if prod*pk < (best or B):
                go(i+1,prod*pk,math.lcm(L,o))
    go(0,1,1)
    primes_full=[pk for pk,p,o in items if o==N and pk==p]
    print(f"F={N}: smallest q (<{B}) with period {N}: {best}; prime? {isprime(best) if best else None}; smallest prime with full period: {min(primes_full) if primes_full else 'none <B'}; candidate prime powers: {len(items)}")
