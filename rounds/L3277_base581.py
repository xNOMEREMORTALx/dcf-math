import statistics as st
from sympy import n_order
def dec(n, k):  # first k decimal digits of 1/n, exact
    return str(10**k // n).zfill(k)
first={}
for n in range(2, 20001):
    m=n
    while m%2==0: m//=2
    while m%5==0: m//=5
    L = 1 if m==1 else n_order(10,m)
    d = dec(n, min(10000, 40 + L + 3))   # preperiod <= ~15 for n<=20000, plus a full period + overlap
    for i in range(len(d)-2):
        s=d[i:i+3]
        if s not in first: first[s]=n
    if len(first)==1000: break
v=sorted(first.values()); print("strings found", len(first), "max n", v[-1], "median first n", st.median(v))
print("rank of 581 (n=43): %d strings are found at n <= 43 -> percentile %.1f%%"%(sum(x<=43 for x in v), 100*sum(x<=43 for x in v)/1000))
print("strings first found at exactly 43:", sorted(k for k,x in first.items() if x==43))
