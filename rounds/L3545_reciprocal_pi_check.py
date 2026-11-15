"""L3545: verify Gary's reciprocal and pi claims (exact long division; pi via mpmath per the standing rule)."""
import mpmath
def expand(n):
    """digits after the decimal point: pre-period + one period; returns (digits, pre, period)"""
    seen={}; r=1%n; d=[]; i=0
    while r and r not in seen:
        seen[r]=i; r*=10; d.append(r//n); r%=n; i+=1
    if not r: return d,len(d),0
    return d,seen[r],len(d)-seen[r]
def text(n,reps=3):
    d,pre,L=expand(n); return ''.join(map(str,d[:pre]+d[pre:]*reps)),pre,L,d
def first_recip(S,start=2,limit=5000):
    for n in range(start,limit):
        t,pre,L,_=text(n)
        if L and S in t[:pre+L+len(S)-1]: return n
        if not L and S in t: return n
def fives(n):
    t,pre,L,d=text(n,1); return [i+1 for i,c in enumerate(t[:pre+L]) if c=='5']
print('A. Expansions (positions counted after the decimal point; pre-period + one period)')
for n in (26,65,109,59,17,61,58,97,49,69):
    t,pre,L,d=text(n,1); rep=d[pre:]
    print('  1/%-3d pre %d period %3d  repetend sum %4d  5s at %s'%(n,pre,L,sum(rep),fives(n)))
print('\nB. First reciprocal 1/n (smallest n>=2) whose expansion contains the string')
for S,claim in [('153','63 or 65'),('146','109'),('169','59'),('176','17'),('147','61'),('103','58'),('183','49'),('362','69'),('394','109'),('606','61'),('1836','49'),('401','?'),('117','17?'),('82','17?')]:
    print('  %-5s first in 1/%-5s claim %s'%(S,first_recip(S),claim))
n2=first_recip('103',start=59); print('  103 second reciprocal (after 58): 1/%s  claim 97'%n2)
print('\nC. Specific substring claims')
t,pre,L,d=text(109,1); s=t[:pre+L]
print('  1/109: "55" at',[i+1 for i in range(len(s)-1) if s[i:i+2]=='55'],'| "137" at',[i+1 for i in range(len(s)-2) if s[i:i+3]=='137'],'| first reciprocal with two 55s in one period:',next(n for n in range(2,2000) if (lambda q: sum(q[i:i+2]=='55' for i in range(len(q)-1)))(text(n,1)[0][:sum(expand(n)[1:3])])>=2))
t,pre,L,d=text(17,1); s=t[:pre+L]; print('  1/17: "88" at',[i+1 for i in range(len(s)-1) if s[i:i+2]=='88'],'"11" at',[i+1 for i in range(len(s)-1) if s[i:i+2]=='11'])
t,pre,L,d=text(49,1); s=t[:pre+L]; print('  1/49: "77" at',[i+1 for i in range(len(s)-1) if s[i:i+2]=='77'],'| "1836" at',[i+1 for i in range(len(s)-3) if s[i:i+4]=='1836'])
print('\nD. Pi (mpmath, 12000 digits; positions after the decimal point)')
mpmath.mp.dps=12000; P=mpmath.nstr(mpmath.pi,10000,strip_zeros=False).split('.')[1]
occ=lambda S:[i+1 for i in range(len(P)-len(S)+1) if P[i:i+len(S)]==S]
o65=occ('65'); print('  "65" first two occurrences at',o65[:2],'| digits before 2nd:',P[o65[1]-3:o65[1]-1],'| "5665" at',occ('5665')[:2])
print('  "401" first at',occ('401')[:1],'(mpmath check: %d)'%(P.find('401')+1))
print('  digit sum through first "65" (incl. the 3 / excl.):',3+sum(map(int,P[:o65[0]+1])),sum(map(int,P[:o65[0]+1])))
s=sum(int(P[i-1]) for i in range(1,1200) if i%21 in (19,20,0))
print('  sum of digits at positions 19,20,21, 40,41,42, ... up to 1199 (every 21-block):',s)
s2=sum(int(P[i-1]) for i in range(19,1200,20))+sum(int(P[i-1]) for i in range(20,1200,20))
print('  210+211+212+213 =',210+211+212+213,'| 299+299+248 =',299+299+248)
