import sys, math, time
from sympy import primerange, n_order, factorint, isprime
fib=[1,2]
while fib[-1]<10**7: fib.append(fib[-1]+fib[-2])
F=set(fib)
# R2: twin-prime products p(p+2), p<10^6, gcd with 10 =1
t=time.time()
sq=[];fb=[];N=0
ps=list(primerange(7,10**6+3))
pset=set(ps)
for p in ps:
    if p+2 in pset:
        N+=1
        L=math.lcm(n_order(10,p),n_order(10,p+2))
        r=math.isqrt(L)
        if r*r==L: sq.append((p,p+2,L))
        if L in F: fb.append((p,p+2,L))
print("R2 twin pairs (7<=p<1e6):",N," square periods:",len(sq)," fibonacci periods:",len(fb))
print(" squares:",sq[:20])
print(" fibonacci:",fb[:20])
print(" time",round(time.time()-t,1))
