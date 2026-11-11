import mpmath
mpmath.mp.dps = 12000
def digs(X): return mpmath.nstr(X, 10000, strip_zeros=False).split('.')[1]
def pos(X,S): return digs(X).find(S)+1
d43=digs(mpmath.mpf(1)/43)
print("1/43 =", "0."+d43[:42])
# period
from sympy import n_order
print("period of 1/43:", n_order(10,43))
p=d43[:21]; print("period digits",p,"sum",sum(map(int,p)))
print("'581' position in 1/43:", pos(mpmath.mpf(1)/43,'581'))
print("'55' position:", pos(mpmath.mpf(1)/43,'55'))
print("5s in first period at:", [i+1 for i,c in enumerate(p) if c=='5'])
print("sum digits 1..8:", sum(map(int,d43[:8])), " digits", d43[:8])
for a in range(1,9):
    for b in range(a,9):
        if sum(map(int,d43[a-1:b]))==17: print("  positions %d-%d sum to 17: %s"%(a,b,d43[a-1:b]))
# 64/11
print("64/11 =", mpmath.nstr(mpmath.mpf(64)/11,12))
# Zn nucleon counts
for A in (64,65,66,67,68,70): print("Zn-%d: p30 n%d e30 total %d"%(A,A-30,30+A))
print("Zn standard atomic weight 65.38 -> 30+35.38+30 = 95.38")
# which n first contains 581 in 1/n (first 10000 digits)
for n in range(2,2000):
    if '581' in digs(mpmath.mpf(1)/n): print("first n with '581' in 1/n:", n, "at", pos(mpmath.mpf(1)/n,'581')); break
first=[n for n in range(2,2000) if '581' in digs(mpmath.mpf(1)/n)][:10]; print("first ten n containing 581:", first)
d17=digs(mpmath.mpf(1)/17); print("1/17 =",d17[:32], "period", n_order(10,17), "11 at", pos(mpmath.mpf(1)/17,'11'), "88 at", pos(mpmath.mpf(1)/17,'88'))
print("midy check 05882352+94117647 =", 5882352+94117647)
both=[n for n in range(2,200) if '11' in digs(mpmath.mpf(1)/n) and '88' in digs(mpmath.mpf(1)/n)][:10]; print("first n with both 11 and 88 in 1/n:", both)
from sympy import isprime
print("first primes with both:", [n for n in both if isprime(n)])
# base rate for a 3-digit string within first 21 digits of a reciprocal: how many n<=100 contain 581 anywhere
print("n<=100 whose 1/n contains 581 (10000 digits):", [n for n in range(2,101) if '581' in digs(mpmath.mpf(1)/n)])
print("supersingular primes (divide Monster order): 2 3 5 7 11 13 17 19 23 29 31 41 47 59 71")
