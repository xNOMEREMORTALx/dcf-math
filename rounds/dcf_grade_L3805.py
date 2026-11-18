"""L3805 grader (W1-W5), frozen with the pre-registration before any data exist. argv: concatenated L3781-script output."""
import re, sys
CRY = {'CRY4(robin)', 'phr6-4(fly)'}
ORGS = ['Acropora cervicornis', 'Pocillopora damicornis', 'Mytilus edulis', 'Crassostrea virginica']
H = {}
for l in open(sys.argv[1]):
    if l.startswith('ORG\t'):
        x = l.rstrip('\n').split('\t')
        H.setdefault(' '.join(x[1].split()[:2]), []).extend(re.match(r'(.*):(\d+):([A-Z\-]{4}):(.+)$', h).groups() for h in (x[4].split() if len(x) > 4 else []))
for o in ORGS:
    print(o, 'present' if o in H else 'MISSING (void)')
    for a, s, t, f in H.get(o, []): print('   %-14s %5s %s %s' % (a, s, t, f))
hits = [h for o in ORGS for h in H.get(o, [])]
cc = [h for h in hits if h[3] in CRY and int(h[1]) >= 900]; cw = [h for h in hits if h[3] in CRY and int(h[1]) < 900]
pc = [h for h in hits if h[3] not in CRY and int(h[1]) >= 900 and h[2][3] != '-']
na = lambda L: sum(h[2][3] not in 'WYF' for h in L)
print('confident CRY %d (non-aromatic %d); weak CRY %d (non-aromatic %d); informative confident DASH/photolyase %d' % (len(cc), na(cc), len(cw), na(cw), len(pc)))
R = []
R.append(('W1', 'ungradeable' if not cc else ('PASS' if na(cc) == 0 else 'FAIL')))
R.append(('W2', 'ungradeable' if not cw else ('PASS' if na(cw) >= 1 else 'FAIL')))
R.append(('W3', 'ungradeable' if not cw or not cc else ('PASS' if na(cw) / len(cw) > na(cc) / len(cc) else 'FAIL')))
R.append(('W4', 'ungradeable' if not pc else ('PASS' if not any(h[2][3] in 'WYF' for h in pc) else 'FAIL')))
pres = [o for o in ORGS if o in H]
R.append(('W5', 'ungradeable' if not pres else ('PASS' if all(any(h[3] in CRY and int(h[1]) >= 900 for h in H[o]) for o in pres) else 'FAIL')))
print('voids', [o for o in ORGS if o not in H]); print('RESULT', R)
