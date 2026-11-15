"""L3601 frozen: generalised Midy for n < 1000 coprime to 10 (repetend of 1/n, period L = ord_n(10))."""
def L(n):
    k,r=1,10%n
    while r!=1: r=r*10%n; k+=1
    return k
def S(n):
    l=L(n); r=1; s=0
    for _ in range(l): r*=10; s+=r//n; r%=n
    return s
rows=[]
for n in range(3,1000):
    if n%2==0 or n%5==0: continue
    l=L(n); s=S(n); comp=(l%2==0 and pow(10,l//2,n)==n-1)
    rows.append((n,l,s,comp,s*2==9*l))
comp=[r for r in rows if r[3]]; half=[r for r in rows if r[4]]
p1=all(r[4] for r in comp)
extra=[r for r in half if not r[3]]
print('n<1000 coprime to 10: %d | with 10^(L/2) = -1 mod n: %d | with S = 9L/2: %d'%(len(rows),len(comp),len(half)))
print('P1 (every complement case has S = 9L/2):',p1)
print('S = 9L/2 WITHOUT the complement property: %d ->'%len(extra),[r[0] for r in extra][:40])
print('composites with the complement property:',[r[0] for r in comp if any(r[0]%p==0 for p in range(2,int(r[0]**.5)+1))][:60])
print('437:',[r for r in rows if r[0]==437])
print('RESULT',[('P1','PASS' if p1 else 'FAIL'),('P2','PASS' if len(extra)<=0.05*len(half) else 'FAIL'),('P3','PASS' if any(r[0]==437 and r[3] for r in rows) else 'FAIL')])
