"""L3979 frozen: L3949 script, seed 3979."""
"""L3949 frozen: L3941 script, seed 3949, adds KPORE (all 79) and nonKv (K2P+Kir+KCa, 39) to the subfamily list."""
"""L3941 frozen: L3937 script with the four pore-forming K+ subfamilies (KPORE split by L3873 rules; KPORE candidates), seed 3941."""
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
SUB = [('KPORE', r'^KCN'), ('Kv', r'^KCN[ABCDFGHQSV]\d'), ('nonKv', r'^(KCNK\d|KCNJ\d|KCNMA1$|KCNN\d|KCNT\d|KCNU\d)'), ('K2P', r'^KCNK\d'), ('Kir', r'^KCNJ\d'), ('KCa', r'^(KCNMA1$|KCNN\d|KCNT\d|KCNU\d)')]
kp = members['KPORE']; S = {}
for f, rx in SUB:
    j = np.array([k for k, i in enumerate(kp) if re.match(rx, names[i])]); S[f] = (kp[j], cand['KPORE'][j])
    print('SUB %s n %d: %s' % (f, len(j), ' '.join(sorted(names[i] for i in kp[j]))), flush=True)
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
rng = np.random.default_rng(3979)
for grp in sorted(H):
    Hm = np.mean(H[grp], axis=0)
    for f, (idx, C) in S.items():
        obs = Hm[idx].mean(); null = np.array([Hm[C[np.arange(len(C)), rng.integers(0, 50, len(C))]].mean() for _ in range(10000)])
        print('GROUP %s FAM %s n %d T_obs %.4f null mean %.4f excess %+.4f p_upper %.4f' % (grp, f, len(idx), obs, null.mean(), obs - null.mean(), (1 + (null >= obs).sum()) / 10001), flush=True)
