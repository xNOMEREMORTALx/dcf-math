"""L3793 grader (E1-E4). Written before the L3793 output was read. argv: L3793 output, L3789 output."""
import sys
ALL = ['Apis mellifera', 'Magallana gigas', 'Xenopus tropicalis', 'Chlamydomonas reinhardtii', 'Neurospora crassa', 'Phaeodactylum tricornutum']
def load(f, i):
    T = {}
    for l in open(f):
        x = l.rstrip('\n').split('\t')
        if len(x) > 4 and x[2] == 'hits': T[(x[0], x[1].split('(')[0])] = (int(x[3]), x)
    return T
N, O = load(sys.argv[1], 0), load(sys.argv[2], 0)
for o in ALL:
    for k in ['mamB', 'mamE', 'mamK', 'mamP', 'ISCA1']:
        x = N.get((o, k)); print('%-26s %-6s E-hits %s (L3789 %s)  best %s' % (o, k, x[0] if x else None, O.get((o, k), (None,))[0], '\t'.join(x[1][11:15]) if x else '-'))
miss = [(o, k) for o in ALL for k in ['mamB', 'mamE', 'mamK', 'mamP', 'ISCA1'] if (o, k) not in N]
g = lambda o, k: N[(o, k)][0] >= 1
R = []
R.append(('E1', 'ungradeable' if miss else ('PASS' if not any(g(o, 'mamP') for o in ALL) else 'FAIL')))
R.append(('E2', 'ungradeable' if miss else ('PASS' if all(g(o, k) for o in ALL for k in ['mamB', 'mamE', 'mamK']) else 'FAIL')))
R.append(('E3', 'ungradeable' if miss else ('PASS' if all(g(o, 'ISCA1') for o in ALL if o != 'Neurospora crassa') else 'FAIL')))
R.append(('E4', 'ungradeable' if miss else ('PASS' if all(N[p][0] <= O[p][0] for p in N) else 'FAIL')))
print('missing', miss); print('RESULT', R)
