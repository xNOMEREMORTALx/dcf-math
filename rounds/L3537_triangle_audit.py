"""L3537 audit of checkable numbers in BATTERY-BIOLOGY-PHYSICS_TRIANGLE.txt (exact integer Fibonacci; standard atomic weights)."""
import math, gzip, re, pickle
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
ds=lambda n: sum(map(int,str(fib(n))))
print("A. Fibonacci digit sums (exact big integers)")
claimed24={24:27,48:54,72:72,96:90,120:126,144:126,168:153,192:180,216:216,240:198,264:252,288:306}
for n,c in claimed24.items(): print('  ds(F(%d)) = %d  claim %d  %s'%(n,ds(n),c,'OK' if ds(n)==c else 'WRONG'))
allmod9=all(ds(24*k)%9==0 for k in range(1,200)); print('  ds(F(24k)) = 0 mod 9 for k=1..199:',allmod9,'| reason: 9 divides F(12)=144, so 9 | F(12k) and the digit sum keeps residue mod 9')
for n,c in {3:2,7:4,31:31,127:121}.items(): print('  ds(F(%d)) = %d  claim %d  %s'%(n,ds(n),c,'OK' if ds(n)==c else 'WRONG'))
se=[n for n in range(1,601) if ds(n)==n]; claim=[1,5,10,31,35,62,72,175,180,216,251,252,360,494,504,540]
print('  self-encoding n<=600:',se,'| claim match:',se==claim)
print('  mod 9 of class B:',{n:n%9 for n in se if n%9})
print("\nB. Molecular weights (average atomic weights, free acid / neutral unless noted)")
W={'C':12.011,'H':1.008,'N':14.007,'O':15.999,'P':30.974}
def mw(f): return sum(W[e]*int(k or 1) for e,k in re.findall(r'([A-Z][a-z]?)(\d*)',f))
mols=[('ATP','C10H16N5O13P3',507),('ADP','C10H15N5O10P2',427),('AMP','C10H14N5O7P',347),('GTP','C10H16N5O14P3',523),('GDP','C10H15N5O11P2',443),
      ('CTP','C9H16N3O14P3',483),('CDP','C9H15N3O11P2',403),('UTP','C9H15N2O15P3',484),('UDP','C9H14N2O12P2',404),('dTTP','C10H17N2O14P3',482),
      ('lactic acid','C3H6O3',90),('citric acid','C6H8O7',192),('glucose','C6H12O6',180),('dopamine','C8H11NO2',153),('acetylcholine (cation)','C7H16NO2',146),
      ('hydroxyl radical','OH',17),('CO2','CO2',44),('water x6','H12O6',108)]
for n,f,c in mols:
    m=mw(f); print('  %-24s %-15s %8.2f  claim %d  %s'%(n,f,m,c,'OK (rounds)' if round(m)==c else 'differs'))
print("\nC. Golden angle vs inverse fine-structure constant")
phi=(1+5**.5)/2; ga=360/phi**2; ai=137.035999177
print('  golden angle = %.4f deg; 1/alpha = %.6f; difference %.3f%%  (a numerical closeness; no physical link is known)'%(ga,ai,100*(ga-ai)/ai))
