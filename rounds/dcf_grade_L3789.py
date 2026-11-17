"""L3789 grader for PREREGISTERED_L3789 (G1-G5). Written before the tool output was read."""
import re, sys
ANI = ['Apis mellifera', 'Magallana gigas', 'Xenopus tropicalis']
NON = ['Chlamydomonas reinhardtii', 'Neurospora crassa', 'Phaeodactylum tricornutum']
T = {}
for l in open(sys.argv[1]):
    x = l.rstrip('\n').split('\t')
    if len(x) >= 10 and x[2] == 'hits':
        T[(x[0], x[1].split('(')[0])] = (int(x[3]), int(x[5]), x[7], int(x[8]), x[9])
for o in ANI + NON:
    for k in ['mamB', 'mamE', 'mamK', 'mamP', 'ISCA1']:
        print('%-26s %-6s' % (o, k), T.get((o, k)))
def has(o, k): return (o, k) in T and T[(o, k)][0] >= 1
miss = [(o, k) for o in ANI + NON for k in ['mamB', 'mamE', 'mamK', 'mamP', 'ISCA1'] if (o, k) not in T]
print('missing', miss)
R = []
R.append(('G1', 'ungradeable' if any(o in NON for o, k in miss if k != 'mamP' and k != 'ISCA1') else ('PASS' if all(has(o, k) for o in NON for k in ['mamB', 'mamE', 'mamK']) else 'FAIL')))
R.append(('G2', 'ungradeable' if any(o in ANI for o, k in miss if k != 'mamP' and k != 'ISCA1') else ('PASS' if all(has(o, k) for o in ANI for k in ['mamB', 'mamE', 'mamK']) else 'FAIL')))
R.append(('G3', 'ungradeable' if any(k == 'mamP' for o, k in miss) else ('PASS' if not any(has(o, 'mamP') for o in ANI + NON) else 'FAIL')))
R.append(('G4', 'ungradeable' if any(k == 'ISCA1' for o, k in miss) else ('PASS' if all(has(o, 'ISCA1') for o in ANI + NON) else 'FAIL')))
g5 = []
for o in ANI:
    b = T.get((o, 'mamB'))
    if not b or b[0] < 1 or re.match(r'uncharacterized', b[4], re.I): g5.append('ungradeable'); continue
    g5.append('PASS' if re.search(r'zinc|ZnT|SLC30|cation|metal', b[4], re.I) else 'FAIL')
print('G5 per animal', list(zip(ANI, g5)))
gr = [g for g in g5 if g != 'ungradeable']
R.append(('G5', 'ungradeable' if not gr else ('PASS' if all(g == 'PASS' for g in gr) else 'FAIL')))
print('RESULT', R)
