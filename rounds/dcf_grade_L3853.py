"""L3853 grader (L1-L4), frozen with the pre-registration."""
import re, sys
rows = [l for l in open(sys.argv[1]) if '| KCN' in l]
D = {f: [float(x) for x in re.findall(r'%s [\d.]+ ctrl [\d.]+ delta ([-+\d.]+)' % f, ''.join(rows))] for f in ('KCN', 'GRIN', 'CACNA1')}
LT = [tuple(map(float, m)) for m in re.findall(r'LONG10 ([\d.]+) NONCH ([\d.]+)', ''.join(rows))]
print('cells', len(rows), D, LT); assert len(rows) == 10
R = [('L1', 'PASS' if sum(d > 0 for d in D['KCN']) >= 7 else 'FAIL'), ('L2', 'PASS' if sum(d < 0 for d in D['CACNA1']) >= 7 else 'FAIL'),
     ('L3', 'PASS' if sum(d > 0 for d in D['GRIN']) >= 7 else 'FAIL'), ('L4', 'PASS' if sum(a < b for a, b in LT) >= 7 else 'FAIL')]
print('RESULT', R)
