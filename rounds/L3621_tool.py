"""L3621: run frozen L3609 battery + dcf_nerve v2 tags on the tardigrade file; reads Entry+Sequence only."""
import gzip,runpy,sys,collections
B=runpy.run_path('/home/claude/dcf-math/rounds/dcf_battery_L3609.py',run_name='x'); N=B['N']
p=sys.argv[1]; L=gzip.open(p,'rt').read().splitlines(); h=L[0].split('\t'); ie=h.index('Entry'); iq=h.index('Sequence')
for o,(c,pu,n) in B['per_org'](p).items(): print('ratio',o,'proteins',n,'channels',c,'pumps',pu,'ratio %.2f'%(c/pu) if pu else 'inf')
C=collections.Counter(); calls=[]
for l in L[1:]:
    f=l.split('\t'); t=sorted(N['tags'](f[iq]))
    if t: calls.append((f[ie],len(f[iq]),t)); C.update(t)
print('tag counts',dict(sorted(C.items())))
for a,n,t in calls: print('CALL',a,n,','.join(t))
