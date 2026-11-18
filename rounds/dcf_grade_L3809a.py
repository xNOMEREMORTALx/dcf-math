"""L3809 grader, amendment a (adds reference exclusion and P5) - otherwise identical to dcf_grade_L3809.py. Original: L3809 grader (P1-P4), frozen with the pre-registration. argv: tool output, then the two TSV paths as SF18=path SF17=path (for the PANTHER check)."""
import re, sys, gzip
SEEN = {'A0A8W8KH86', 'A0A8W8KKK9', 'A0A8B8EP46', 'A0A8S3V2Y9', 'A0A6I8QP63'}
SEEN |= {'P27526', 'B7FV99', 'A0A2I4SZI9'}  # amendment a: reference accessions (fly/zebrafish references are matched by sequence below)
import runpy as _r; _REFSEQ = set(_r.run_path('/home/claude/dcf-math/rounds/dcf_cry_classII_L3777.py', run_name='x')['refs']().values())
S = {}
for l in open(sys.argv[1]):
    if l.startswith('SET\t'):
        x = l.rstrip('\n').split('\t')
        S[x[1]] = [re.match(r'(.*):(\d+):([A-Z\-]{4}):(.+)$', h).groups() for h in (x[8].split() if len(x) > 8 else [])]
        print(x[1], 'proteins', x[3], 'in window', x[5], 'hits', x[7])
valid = {}
for arg in sys.argv[2:]:
    k, p = arg.split('=', 1); L = gzip.open(p, 'rt').read().splitlines()
    if len(L) < 21: valid[k] = False; print(k, 'void: < 20 proteins'); continue
    h = L[0].split('\t'); ip = [i for i, c in enumerate(h) if 'PANTHER' in c]
    frac = sum(('PTHR11455:' + k) in l.split('\t')[ip[0]] for l in L[1:]) / (len(L) - 1) if ip else 0
    valid[k] = frac >= 0.9; print(k, 'PANTHER column match %.3f' % frac)
    iq = h.index('Sequence'); ie = h.index('Entry')
    for l in L[1:]:
        x = l.split('\t')
        if x[iq].strip() in _REFSEQ: SEEN.add(x[ie]); print('excluded reference entry', x[ie])
def G(k):
    H = [h for h in S.get(k, []) if h[0] not in SEEN]; return H if valid.get(k) and H else None
s18, s17 = G('SF18'), G('SF17')
ar = lambda H: sum(h[2][3] in 'WYF' for h in H)
if s18: print('SF18 graded hits %d: aromatic at TrpD %d; score < 900: %d' % (len(s18), ar(s18), sum(int(h[1]) < 900 for h in s18)))
if s17: print('SF17 graded hits %d: aromatic at TrpD %d; score >= 900: %d' % (len(s17), ar(s17), sum(int(h[1]) >= 900 for h in s17)))
for nm, H in (('SF18', s18), ('SF17', s17)):
    if H:
        from collections import Counter
        print(nm, 'TrpD residues', Counter(h[2][3] for h in H).most_common(), 'best refs', Counter(h[3] for h in H).most_common())
R = []
R.append(('P1', 'ungradeable' if not s18 else ('PASS' if (len(s18) - ar(s18)) >= 0.9 * len(s18) else 'FAIL')))
R.append(('P2', 'ungradeable' if not s17 else ('PASS' if ar(s17) >= 0.9 * len(s17) else 'FAIL')))
R.append(('P3', 'ungradeable' if not s18 else ('PASS' if sum(int(h[1]) < 900 for h in s18) >= 0.8 * len(s18) else 'FAIL')))
R.append(('P4', 'ungradeable' if not s17 else ('PASS' if sum(int(h[1]) >= 900 for h in s17) >= 0.9 * len(s17) else 'FAIL')))
R.append(('P5', 'ungradeable' if not s18 else ('PASS' if sum(h[3] == 'CPD-photolyase(Neurospora)' for h in s18) >= 0.5 * len(s18) else 'FAIL')))
print('RESULT', R)
