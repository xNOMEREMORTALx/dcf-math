"""L3937 frozen: do non-potassium four-fold (tetrameric) channel genes share the CTCF-anchor excess? argv: GTF, REF (as L3909),
then GROUP:CELL=path. GROUP A = ten cell lines (4DN union -> anchors() of L3725; others anchors() of L3825a); GROUP B = Hi-C maps,
CTCF-anchored loops (both anchors overlap a reference anchor; as L3909). Set TETRA4 (37): TRPC1,3-7, TRPV1-6, TRPM1-8, TRPA1,
MCOLN1-3, PKD2, PKD2L1, PKD2L2, CNGA1-4, CNGB1, CNGB3, CATSPER1-4. Matched candidates: 50 nearest in (z log10 length,
z log10(1 + TSS density)) from the L3909 pool with the TETRA4 genes removed. KPORE is re-run with its L3909 candidates for comparison.
10,000 sets, seed 3937, per group on the mean over the group's maps."""
import sys, collections, gzip, re
import numpy as np
argv = sys.argv; sys.argv = [argv[0], argv[1], 'both', argv[2]]
src = open('/home/claude/dcf-math/rounds/dcf_ctcfsplit_L3909.py').read(); src = src[:src.index('Hs = []')]
g = {'__name__': 'L3937'}; exec(compile(src, 'L3909', 'exec'), g)
hits, anch725, anch825, ov, members, cand, names, pool, zl, zd = [g[k] for k in ('hits', 'anch725', 'anch825', 'ov', 'members', 'cand', 'names', 'pool', 'zl', 'zd')]
T4 = re.compile(r'^(TRPC[134567]|TRPV[1-6]|TRPM[1-8]|TRPA1|MCOLN[1-3]|PKD2|PKD2L[12]|CNGA[1-4]|CNGB[13]|CATSPER[1-4])$')
t4 = np.array([i for i, n in enumerate(names) if T4.match(n)]); print('TETRA4 n %d: %s' % (len(t4), ' '.join(sorted(names[i] for i in t4))), flush=True)
pool4 = np.array([i for i in pool if not T4.match(names[i])])
C4 = np.array([pool4[np.argsort(np.hypot(zl[pool4] - zl[i], zd[pool4] - zd[i]), kind='stable')[:50]] for i in t4])
def hic_both(p):
    A = collections.defaultdict(list)
    for l in gzip.open(p, 'rt'):
        if l.startswith('#'): continue
        f = l.rstrip('\n').split('\t')
        if len(f) < 6 or not f[1].isdigit(): continue
        c1 = f[0] if f[0].startswith('chr') else 'chr' + f[0]; c2 = f[3] if f[3].startswith('chr') else 'chr' + f[3]
        s1, e1, s2, e2 = int(f[1]), int(f[2]), int(f[4]), int(f[5])
        if ov(c1, s1, e1) and ov(c2, s2, e2): A[c1].append((s1, e1)); A[c2].append((s2, e2))
    return A
H = collections.defaultdict(list)
for arg in argv[3:]:
    grp, rest = arg.split(':', 1); cell, p = rest.split('=', 1)
    if grp == 'B': A = hic_both(p)
    elif cell in ('H1', 'HFFc6'): A = anch725(p)
    else: A = anch825(p)[0]; A = {(c if c.startswith('chr') else 'chr' + c): v for c, v in A.items()}
    H[grp].append(hits(A, {}).astype(float)); print('map', grp, cell, flush=True)
rng = np.random.default_rng(3937)
for grp in sorted(H):
    Hm = np.mean(H[grp], axis=0)
    for f, idx, C in (('TETRA4', t4, C4), ('KPORE', members['KPORE'], cand['KPORE'])):
        obs = Hm[idx].mean(); null = np.array([Hm[C[np.arange(len(C)), rng.integers(0, 50, len(C))]].mean() for _ in range(10000)])
        print('GROUP %s FAM %s n %d T_obs %.4f null mean %.4f excess %+.4f p_upper %.4f p_lower %.4f' % (grp, f, len(idx), obs, null.mean(), obs - null.mean(), (1 + (null >= obs).sum()) / 10001, (1 + (null <= obs).sum()) / 10001), flush=True)
for grp in sorted(H):
    Hm = np.mean(H[grp], axis=0)
    for j in np.argsort(-(Hm[t4] - Hm[C4].mean(axis=1)), kind='stable'):
        print('GENE %s %-8s resid %+.3f' % (grp, names[t4[j]], Hm[t4[j]] - Hm[C4[j]].mean()))
