"""L3541 audit 2 of the triangle file: neurotransmitter MWs, repetend digit sums S(1/n), Fibonacci halving, 11/7 vs phi."""
import re
W={'C':12.011,'H':1.008,'N':14.007,'O':15.999}
def mw(f): return sum(W[e]*int(k or 1) for e,k in re.findall(r'([A-Z][a-z]?)(\d*)',f))
print('A. Neurotransmitters and hormones (neutral molecules)')
for n,f,c in [('dopamine','C8H11NO2',153),('acetylcholine (cation)','C7H16NO2',146),('norepinephrine','C8H11NO3',169),('serotonin','C10H12N2O',176),
              ('glutamate (glutamic acid)','C5H9NO4',147),('GABA','C4H9NO2',103),('epinephrine','C9H13NO3',183),('cortisol','C21H30O5',362)]:
    m=mw(f); print('  %-26s %-11s %7.2f claim %d %s'%(n,f,m,c,'OK' if round(m)==c else 'differs'))
def rep(n):
    """digit sum of the repeating block of 1/n (pre-period removed), exact long division; returns (pre-period, period, digit sum)"""
    seen={}; r=1; digits=[]; i=0
    while r and r not in seen:
        seen[r]=i; r*=10; digits.append(r//n); r%=n; i+=1
    if not r: return (len(digits),0,0)
    s=seen[r]; block=digits[s:]; return (s,len(block),sum(block))
print('\nB. Repetend digit sums S(1/n) (exact long division)')
for n,c in [(17,72),(43,90),(89,198),(153,65),(306,73),(372,54),(437,891)]:
    pre,L,S=rep(n); midy=' (Midy: period even and n prime -> S = 9L/2 = %d)'%(9*L//2) if L%2==0 and all(n%k for k in range(2,int(n**.5)+1)) else ''
    print('  1/%-4d pre-period %d, period %4d, S = %4d  claim %4d  %s%s'%(n,pre,L,S,c,'OK' if S==c else 'differs',midy))
print('\nC. Fibonacci halving and ratios')
F=[0,1]
for _ in range(30): F.append(F[-1]+F[-2])
for k in (9,12,15): print('  F(%d)/2 = %s'%(k,F[k]/2))
phi=(1+5**.5)/2; print('  11/7 = %.4f vs phi = %.4f: %.1f%% off (13/8 = %.3f is %.2f%% off; 11/7 is not a Fibonacci ratio)'%(11/7,phi,100*(phi-11/7)/phi,13/8,100*(13/8-phi)/phi))
