"""L3785 grader for PREREGISTERED_L3781 (B1-B4). Written before the tool output was read.
Strict reading: a '-' (unaligned) at TrpD in a CRY4/phr6-4 hit counts as NOT aromatic for B1 (fails it);
for B2 a '-' is not aromatic (cannot fail it). Void per organism if < 5,000 proteins (script never emits those)."""
import re, sys
CRY = {'CRY4(robin)', 'phr6-4(fly)'}
PHR = {'phr-classII(fly)', 'CPD-photolyase(Neurospora)', 'cry-dash(zf)', 'DASH(diatom)'}
ORGS = {'Apis mellifera': 'honeybee', 'Magallana gigas': 'oyster', 'Xenopus tropicalis': 'frog'}
H = {}
for l in open(sys.argv[1]):
    if l.startswith('ORG\t'):
        x = l.rstrip('\n').split('\t')
        H[x[1]] = [re.match(r'(.*):(\d+):([A-Z\-]{4}):(.+)$', h).groups() for h in (x[4].split() if len(x) > 4 else [])]
for o in ORGS:
    print('%s (%s): %d hits' % (ORGS[o], o, len(H.get(o, []))))
    for a, s, t, f in H.get(o, []): print('   %-14s %5s %s %s' % (a, s, t, f))
cry = [(o, h) for o in ORGS for h in H.get(o, []) if h[3] in CRY]
phr = [(o, h) for o in ORGS for h in H.get(o, []) if h[3] in PHR]
b1bad = [h for o, h in cry if h[2][3] not in 'WYF']
b2bad = [h for o, h in phr if h[2][3] in 'WYF']
miss = [o for o in ORGS if o not in H]
R = []
R.append(('B1', 'ungradeable' if not cry else ('PASS' if not b1bad else 'FAIL')))
print('B1 CRY/6-4 hits %d; non-aromatic at TrpD %d %s' % (len(cry), len(b1bad), b1bad))
inf = [h for o, h in phr if h[2][3] != '-']
R.append(('B2', 'ungradeable' if not phr else ('PASS' if not b2bad else 'FAIL')))
print('B2 photolyase/DASH hits %d (informative at TrpD %d); aromatic at TrpD %d %s' % (len(phr), len(inf), len(b2bad), b2bad))
R.append(('B3', 'ungradeable' if miss else ('PASS' if all(any(h[3] in CRY for h in H[o]) for o in ORGS) else 'FAIL')))
print('B3 per organism CRY/6-4 counts', {ORGS[o]: sum(h[3] in CRY for h in H.get(o, [])) for o in ORGS}, 'missing', miss)
x = 'Xenopus tropicalis'
R.append(('B4', 'ungradeable' if x not in H else ('PASS' if any(h[3] == 'phr-classII(fly)' for h in H[x]) else 'FAIL')))
print('B4 Xenopus phr-classII hits', [h[0] for h in H.get(x, []) if h[3] == 'phr-classII(fly)'])
print('RESULT', R)
