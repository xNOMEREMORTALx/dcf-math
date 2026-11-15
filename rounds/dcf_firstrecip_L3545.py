"""L3545 frozen: for every 3-digit string 100-999, the smallest n >= 2 whose decimal expansion of 1/n contains it inside one
written period (pre-period + one period, no wrap). Compares the 8 neurotransmitter/hormone MW strings with all 900."""
import statistics
def expand(n):
    seen={}; r=1%n; d=[]; i=0
    while r and r not in seen:
        seen[r]=i; r*=10; d.append(r//n); r%=n; i+=1
    return ''.join(map(str,d))
T={n:expand(n) for n in range(2,20000)}
def first(S):
    for n in range(2,20000):
        if S in T[n]: return n
allv={s:first(str(s)) for s in range(100,1000)}
vals=sorted(v for v in allv.values() if v)
NT={'dopamine':153,'acetylcholine':146,'norepinephrine':169,'serotonin':176,'glutamate':147,'GABA':103,'epinephrine':183,'cortisol':362}
nt={k:allv[v] for k,v in NT.items()}
med=statistics.median(nt.values()); q25=vals[len(vals)//4]
pct=lambda x: 100*sum(v<x for v in vals)/len(vals)
print('first-n for neurotransmitter strings:',nt)
print('median of the 8: %s | 25th percentile of all 900: %s | median of all 900: %s'%(med,q25,statistics.median(vals)))
print('percentile of the 8 medians within all 900: %.1f%%'%pct(med))
print('R1 PASS' if med>=q25 else 'R1 FAIL')
