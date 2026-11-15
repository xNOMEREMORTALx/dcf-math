"""L3537 model (computed BEFORE any digit sum beyond n=600): necessary condition F(n) = n (mod 9) and a normal approximation."""
import math
F=[0,1]
for _ in range(80): F.append((F[-1]+F[-2])%9)
allowed=sorted(r for r in range(72) if F[r%24]==r%9)
print('n mod 72 allowed by digit_sum(F(n)) = n  [needs F(n) = n mod 9; Pisano period mod 9 = 24]:',allowed, '(%d of 72)'%len(allowed))
L=math.log10((1+5**.5)/2)
def p(n):
    if n%72 not in allowed: return 0.0
    d=max(n*L-math.log10(5)/2,1); mu=4.5*d; sd=math.sqrt(8.25*d)
    return 9*math.exp(-0.5*((n-mu)/sd)**2)/(sd*math.sqrt(2*math.pi))
for a,b in [(1,600),(601,1000),(1001,3000),(3001,20000)]:
    print('model expected count in [%d,%d]: %.2f'%(a,b,sum(p(n) for n in range(a,b+1))))
