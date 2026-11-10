import sys, random, re
sys.argv=['x',sys.argv[1],'/home/claude/dcf-math/mrna/dcf_ire.py']
exec(open('/home/claude/dcf-math/mrna/dcf_mrna_wide.py').read().split("if __name__")[0])
best={}
for acc,desc,s in records(sys.argv[1]):
    if not acc.startswith('NM_'): continue
    m=re.search(r'\(([A-Za-z0-9\-\.]+)\), ',desc); g=m.group(1) if m else acc
    num=int(re.search(r'NM_(\d+)',acc).group(1))
    if g not in best or num<best[g][0]: best[g]=(num,acc,s)
rng=random.Random(9); real=0; sh=0; hitg=[]
for g,(num,acc,s) in best.items():
    a,b=ire.longest_orf(s); h=[x for x in ire.scan(s) if x<a]; real+=len(h)
    if h: hitg.append(g)
    for _ in range(20):
        t=dishuffle(s[:a],rng)+s[a:]; sh+=sum(x<a for x in ire.scan(t))/20
print("genes %d (one transcript each) | 5' UTR hits real %d vs shuffled %.1f (ratio %.2f)"%(len(best),real,sh,real/max(sh,1e-9)))
print("genes hit:",sorted(hitg))
