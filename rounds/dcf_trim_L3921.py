"""L3921 frozen: does anchor width explain the primary-cell baseline? argv: GTF, REF (as L3909, only to reuse its setup), W, then
GROUP:CELL=path entries (ChIA-PET maps only; 4DN union -> anchors() of L3725, others anchors() of L3825a). For each map prints the
untrimmed anchor union coverage (bp) and median anchor width; then every anchor is trimmed to its central W bp, and per group the
L3893 resampling (50 candidates, 10,000 sets, seed 3921) is run on the mean over the group's maps."""
import sys, collections
import numpy as np
argv = sys.argv; sys.argv = [argv[0], argv[1], 'both', argv[2]]
src = open('/home/claude/dcf-math/rounds/dcf_ctcfsplit_L3909.py').read(); src = src[:src.index('Hs = []')]
g = {'__name__': 'L3921'}; exec(compile(src, 'L3909', 'exec'), g)
hits, anch725, anch825, members, cand = g['hits'], g['anch725'], g['anch825'], g['members'], g['cand']
W = int(argv[3]); H = collections.defaultdict(list)
for arg in argv[4:]:
    grp, rest = arg.split(':', 1); cell, p = rest.split('=', 1)
    A = anch725(p) if cell in ('H1', 'HFFc6') else anch825(p)[0]
    A = {(c if c.startswith('chr') else 'chr' + c): v for c, v in A.items()}
    cov = 0; wid = []
    for c, v in A.items():
        e0 = -1
        for s, e in sorted(v):
            wid.append(e - s)
            if e <= e0: continue
            cov += e - max(s, e0); e0 = e
    T = {c: [((s + e) // 2 - W // 2, (s + e) // 2 + W // 2) for s, e in v] for c, v in A.items()}
    H[grp].append(hits(T, {}).astype(float))
    print('MAP %s %s anchors %d coverage_bp %d median_width %d' % (grp, cell, len(wid), cov, np.median(wid)), flush=True)
rng = np.random.default_rng(3921)
for grp in sorted(H):
    Hm = np.mean(H[grp], axis=0)
    for f in ('KCN', 'ALL', 'KPORE', 'Kaux'):
        obs = Hm[members[f]].mean(); C = cand[f]
        null = np.array([Hm[C[np.arange(len(C)), rng.integers(0, 50, len(C))]].mean() for _ in range(10000)])
        print('GROUP %s FAM %s T_obs %.4f null mean %.4f p_upper %.4f' % (grp, f, obs, null.mean(), (1 + (null >= obs).sum()) / 10001), flush=True)
