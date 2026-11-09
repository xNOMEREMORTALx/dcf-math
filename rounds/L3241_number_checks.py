import mpmath, sympy as sp, math
from itertools import permutations
def dr(x): # digital root of the digit string (ignores the decimal point)
    s=sum(int(c) for c in str(x) if c.isdigit()); 
    while s>9: s=sum(int(c) for c in str(s))
    return s
print("== digit reductions")
for x in ["401","41","79","47","131.81","131.8103149","2.300523984 (same angle in radians)","240","248","120","30"]:
    print("  %-38s digit sum -> %d"%(x, dr(x.split()[0])))
print("  share of whole numbers with digital root 5: 1/9 = %.3f"%(1/9))
print("== primes in the path")
for p in [401,79,47,41,5]: print("  %d prime=%s, it is prime #%d"%(p,sp.isprime(p),sp.primepi(p)))
print("  401 + 79 + 47 + 41 + 5 =",401+79+47+41+5, "| 79+47+41 =",79+47+41)
print("== reciprocal periods (order of 10)")
for p in [401,79,47,41,5,163,153,271]:
    print("  1/%d period %s"%(p, sp.n_order(10,p) if math.gcd(p,10)==1 else "terminates"))
print("  41 x 271 = %d (= 11111, five ones)"%(41*271))
print("== 401 in pi (DCF rule: mpmath, 12000 dps, first 10000 decimals)")
mpmath.mp.dps=12000
d=mpmath.nstr(mpmath.pi,10050,strip_zeros=False).split('.')[1][:10000]
for S in ["401","41","163","153","135","351","531","513","79","47"]:
    print("  %-4s first at decimal position %d"%(S,d.find(S)+1))
import random; random.seed(1)
fp=[d.find("%03d"%random.randrange(1000))+1 for _ in range(2000)]
print("  typical first position of a random 3-digit string: median %d"%sorted(fp)[1000])
print("== 163 and the cube")
mpmath.mp.dps=60
r=mpmath.e**(mpmath.pi*mpmath.sqrt(163)); print("  e^(pi*sqrt(163)) =",mpmath.nstr(r,40)); print("  640320^3 + 744   =",640320**3+744,"| difference",mpmath.nstr(640320**3+744-r,6))
print("== phi, sqrt5 and pi")
phi=(1+mpmath.sqrt(5))/2; print("  phi =",mpmath.nstr(phi,20),"| 2cos(pi/5) =",mpmath.nstr(2*mpmath.cos(mpmath.pi/5),20))
print("== the 1-3-5 numbers")
allp=sorted(int(''.join(p)) for p in permutations("135")); print("  all six orderings:",allp,"sum",sum(allp))
five=[153,351,135,531,513]; print("  Gary's five sum to",sum(five),"=",sp.factorint(sum(five)),"(the missing one is 315)")
print("  153 = 1^3+5^3+3^3 =",1+125+27,"| 135 = 1^1+3^2+5^3 =",1+9+125,"| 153 = T17 =",17*18//2,"| 351 = T26 =",26*27//2)
for n in five: print("  ",n,sp.factorint(n))
