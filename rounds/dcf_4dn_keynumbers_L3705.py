"""L3705 frozen: DCF key numbers in the 4DN loop files and in the 4D report text, against matched controls.
argv: H1 bedpe, HFFc6 bedpe, report text.
K = 9 37 72 73 89 108 113 137 153 203 216 401 432 541 937 1231 1841 2701.
Statistic for a number n on a list of integers X: rate(n) = fraction of X divisible by n, times n (1.0 = chance for uniform residues).
Controls for key k: every integer n in [ceil(k/2), 2k], n != k, n not in K, with gcd(n,1000) == gcd(k,1000) (same 2/5 content, because
coordinates sit on 1-kb/5-kb grids). Percentile of k = share of controls with rate below rate(k). Significant = percentile >= 99.7 (0.05/18).
Lists: (1) H1 spans s2-s1 (integer anchor-start distance); (2) HFFc6 spans; (3) every integer >= 10 written in the report (commas removed)."""
import sys,re,math
K=[9,37,72,73,89,108,113,137,153,203,216,401,432,541,937,1231,1841,2701]
def spans(p): return [int(l.split('\t')[4])-int(l.split('\t')[1]) for l in open(p)]
def rate(X,n): return sum(x%n==0 for x in X)/len(X)*n
def test(name,X):
    print('##',name,'n =',len(X))
    for k in K:
        ctl=[n for n in range(math.ceil(k/2),2*k+1) if n!=k and n not in K and math.gcd(n,1000)==math.gcd(k,1000)]
        rk=rate(X,k); rc=[rate(X,n) for n in ctl]; pct=100*sum(r<rk for r in rc)/len(rc)
        print('  k=%5d rate %.3f  control median %.3f  controls %4d  percentile %6.2f  %s'%(k,rk,sorted(rc)[len(rc)//2],len(rc),pct,'SIGNIFICANT' if pct>=99.7 else ''),flush=True)
txt=open(sys.argv[3],encoding='utf-8',errors='replace').read()
nums=[int(x.replace(',','')) for x in re.findall(r'(?<![\d.])\d{1,3}(?:,\d{3})+(?![\d.])|(?<![\d.,])\d{2,}(?![\d.,])',txt)]
nums=[x for x in nums if x>=10]
test('H1 spans',spans(sys.argv[1])); test('HFFc6 spans',spans(sys.argv[2])); test('report integers',nums)
