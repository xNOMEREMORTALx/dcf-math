import sympy as sp, mpmath
mpmath.mp.dps=50
lucky=[p for p in sp.primerange(2,10**4) if all(sp.isprime(n*n+n+p) for n in range(p-1))]
print("lucky numbers of Euler below 10^4:",lucky)
for p in lucky:
    d=4*p-1; v=mpmath.e**(mpmath.pi*mpmath.sqrt(d)); near=mpmath.nint(v)
    print("  p=%2d  d=4p-1=%3d  e^(pi*sqrt(d)) = %s   distance to nearest integer %s"%(p,d,mpmath.nstr(v,25),mpmath.nstr(abs(v-near),3)))
for d,c in [(19,96),(43,960),(67,5280),(163,640320)]:
    print("  d=%d: e^(pi sqrt d) - 744 vs %d^3: diff %s"%(d,c,mpmath.nstr(mpmath.e**(mpmath.pi*mpmath.sqrt(d))-744-c**3,6)))
print("primes made by n^2+n+41 before failing:",sum(1 for n in range(100) if sp.isprime(n*n+n+41) and all(sp.isprime(k*k+k+41) for k in range(n+1))))
