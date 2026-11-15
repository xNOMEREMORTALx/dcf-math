"""L3601b frozen: characterise the complement property 10^(L/2) = -1 (mod n) for n < 10000 coprime to 10.
Criterion C: write n = prod p^k; every prime-power factor has ord_{p^k}(10) with the SAME 2-adic valuation v >= 1."""
from sympy import factorint, n_order
def v2(x):
    c=0
    while x%2==0: x//=2; c+=1
    return c
bad=[]; cnt=0
for n in range(3,10000):
    if n%2==0 or n%5==0: continue
    L=n_order(10,n); comp=(L%2==0 and pow(10,L//2,n)==n-1)
    vs={v2(n_order(10,p**k)) for p,k in factorint(n).items()}
    crit=(len(vs)==1 and min(vs)>=1)
    cnt+=comp
    if comp!=crit: bad.append(n)
print('n < 10000 coprime to 10 with the complement property:',cnt,'| mismatches with criterion C:',len(bad),bad[:20])
print('RESULT',[('P4','PASS' if not bad else 'FAIL')])
