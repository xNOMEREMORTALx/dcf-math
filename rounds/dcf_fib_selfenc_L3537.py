"""L3537 frozen: list every n in [1, N] with digit_sum(F(n)) = n (exact big integers)."""
import sys
sys.set_int_max_str_digits(0)
N=int(sys.argv[1]); a,b=0,1; out=[]
for n in range(1,N+1):
    a,b=b,a+b
    if sum(map(int,str(a)))==n: out.append(n)
print('self-encoding n <= %d:'%N, out)
