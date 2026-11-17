"""L3797 grader, amendment a: identical to dcf_grade_L3797.py except organisms are matched on genus + species (first two words)."""
import re, sys
CRY = {'CRY4(robin)', 'phr6-4(fly)'}
PHR = {'phr-classII(fly)', 'CPD-photolyase(Neurospora)', 'cry-dash(zf)', 'DASH(diatom)'}
ORGS = ['Danaus plexippus', 'Salmo salar', 'Acropora millepora', 'Lottia gigantea']
H = {}
for l in open(sys.argv[1]):
    if l.startswith('ORG\t'):
        x = l.rstrip('\n').split('\t')
        H.setdefault(' '.join(x[1].split()[:2]), []).extend([re.match(r'(.*):(\d+):([A-Z\-]{4}):(.+)$', h).groups() for h in (x[4].split() if len(x) > 4 else [])])
for o in ORGS:
    print(o, 'present' if o in H else 'MISSING')
    for a, s, t, f in H.get(o, []): print('   %-14s %5s %s %s' % (a, s, t, f))
conf = lambda o, fam: [h for h in H.get(o, []) if h[3] in fam and int(h[1]) >= 900]
cry = [h for o in ORGS for h in conf(o, CRY)]; phr = [h for o in ORGS for h in conf(o, PHR) if h[2][3] != '-']
R = []
R.append(('V1', 'ungradeable' if not cry else ('PASS' if all(h[2][3] in 'WYF' for h in cry) else 'FAIL')))
R.append(('V2', 'ungradeable' if not phr else ('PASS' if not any(h[2][3] in 'WYF' for h in phr) else 'FAIL')))
R.append(('V3', 'ungradeable' if 'Danaus plexippus' not in H else ('PASS' if len(conf('Danaus plexippus', CRY)) >= 2 else 'FAIL')))
pres = [o for o in ORGS if o in H]
R.append(('V4', 'ungradeable' if len(pres) < 4 else ('PASS' if all(conf(o, CRY) for o in ORGS) else 'FAIL')))
print('V1 confident CRY/6-4', [(h[0], h[1], h[2]) for h in cry]); print('V2 informative confident photolyase/DASH', phr)
print('RESULT', R)
