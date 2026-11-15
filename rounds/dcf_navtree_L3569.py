"""L3569 frozen: NAV1 vs NAV2 by global-alignment identity (rounds/dcf_align_L3569.py), plus a neighbour-joining tree."""
import runpy, re
A = runpy.run_path('/home/claude/dcf-math/rounds/dcf_align_L3569.py'); idt = A['identity']
L = runpy.run_path('/home/claude/dcf-math/rounds/dcf_navfamily2_L3565.py', run_name='lib')   # reuses the loader; its prints go to stdout
S = L['S']
S.update(L['load_tsv']('/home/claude/L3533/z/bil.tsv.gz', {'A0ACM8CKW0', 'A0A7M7N9I2'}))
NAV1 = ['A0A1S3HN89', 'R7TMI4', 'I6NQF8', 'F6QCF9', 'fly_para', 'human_SCN2A']; NAV2 = ['R7TCA7', 'A0A9J7HQP1']
AMB = ['A0ACM8CKW0', 'A0A7M7N9I2']
EARLY = ['A9USM1', 'B3RSS4', 'A7SKR1', 'A0ACF8Y6N4', 'A0ACF8Y996', 'A0ACF8YBX3', 'F6MZB8', 'F6MZB9', 'HMIM006045', 'HMIM019623']
names = NAV1 + NAV2 + AMB + EARLY
I = {}
for x in range(len(names)):
    for y in range(x + 1, len(names)):
        I[(names[x], names[y])] = I[(names[y], names[x])] = idt(S[names[x]], S[names[y]])
print('\n=== L3569 alignment-identity results ===')
c1 = min(max(I[(a, b)] for b in NAV1 if b != a) for a in NAV1); c2 = max(I[(a, b)] for a in NAV1 for b in NAV2)
print('control: min best NAV1-NAV1 %.3f vs max NAV1-NAV2 %.3f -> %s' % (c1, c2, 'informative' if c1 > c2 else 'NOT informative'))
res = {}
for q in AMB + EARLY:
    s1 = max(I[(q, r)] for r in NAV1); s2 = max(I[(q, r)] for r in NAV2); res[q] = 'NAV1' if s1 > s2 else 'NAV2'
    print('  %-12s best NAV1 %.3f  best NAV2 %.3f -> %s' % (q, s1, s2, res[q]))
inf = c1 > c2
R = [('A1', 'ungradeable' if not inf else ('PASS' if all(res[q] == 'NAV2' for q in AMB) else 'FAIL')),
     ('A2', 'ungradeable' if not inf else ('PASS' if all(res[q] == 'NAV2' for q in EARLY) else 'FAIL'))]
# neighbour-joining on distance 1 - identity
import itertools
nodes = {n: n for n in names}; Dm = {(a, b): 1 - I[(a, b)] for a in names for b in names if a != b}
act = list(names); k = 0
while len(act) > 2:
    r = {a: sum(Dm[(a, b)] for b in act if b != a) for a in act}; N = len(act)
    a, b = min(((x, y) for x, y in itertools.combinations(act, 2)), key=lambda p: (N - 2) * Dm[p] - r[p[0]] - r[p[1]])
    k += 1; u = 'n%d' % k; nodes[u] = '(%s,%s)' % (nodes[a], nodes[b])
    for c in act:
        if c not in (a, b): Dm[(u, c)] = Dm[(c, u)] = 0.5 * (Dm[(a, c)] + Dm[(b, c)] - Dm[(a, b)])
    act = [c for c in act if c not in (a, b)] + [u]
print('NJ tree (unrooted, topology only):', '(%s,%s);' % (nodes[act[0]], nodes[act[1]]))
print('RESULT', R)
