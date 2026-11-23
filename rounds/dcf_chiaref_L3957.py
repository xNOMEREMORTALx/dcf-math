"""L3957 frozen: L3933 script with the filter replaced: keep only loops whose two anchors both overlap a reference CTCF anchor
(H1 + HFFc6 CTCF-ChIAPET, ov() of L3909). Seed 3957."""
"""L3933 frozen: does removing promoter-promoter loops restore the K+ excess in primary-cell CTCF ChIA-PET maps?
argv: GTF, REF (as L3909, setup only), then GROUP:CELL=path. Loop selection exactly as anchors() of L3825a (top 28,270 by column 7,
or first 28,270 if column 7 is not numeric). Loops whose two anchor midpoints both lie within 5 kb of a protein-coding TSS
(L3725 gene table) are removed; the rest give anchors. Per group: L3893 resampling (50 candidates, 10,000 sets, seed 3933) on the
mean over the group's maps. Group T = the T-cell maps alone is formed from cells whose name starts with 'T'."""
import sys, collections, gzip
import numpy as np
argv = sys.argv; sys.argv = [argv[0], argv[1], 'both', argv[2]]
src = open('/home/claude/dcf-math/rounds/dcf_ctcfsplit_L3909.py').read(); src = src[:src.index('Hs = []')]
g = {'__name__': 'L3933'}; exec(compile(src, 'L3909', 'exec'), g)
G, hits, members, cand, ov = g['G'], g['hits'], g['members'], g['cand'], g['ov']
TS = collections.defaultdict(list)
for q in G: TS[q[0]].append(q[1])
TS = {c: np.sort(v) for c, v in TS.items()}
def near(c, s, e):
    c = c if c.startswith('chr') else 'chr' + c
    if c not in TS: return False
    m = (s + e) // 2; t = TS[c]; i = min(max(np.searchsorted(t, m), 1), len(t) - 1)
    return min(abs(t[i] - m), abs(t[i - 1] - m)) <= 5000
def loops(p):
    op = gzip.open if p.endswith('.gz') else open; L = []
    for l in op(p, 'rt'):
        f = l.rstrip('\n').split('\t')
        if len(f) < 6 or not f[1].isdigit(): continue
        L.append(f)
    def sc(f):
        try: return float(f[6])
        except (IndexError, ValueError): return None
    if len(L) > 28270:
        if all(sc(f) is not None for f in L): L = [f for _, f in sorted(enumerate(L), key=lambda t: (-sc(t[1]), t[0]))][:28270]
        else: L = L[:28270]
    return L
H = collections.defaultdict(list)
for arg in argv[3:]:
    grp, rest = arg.split(':', 1); cell, p = rest.split('=', 1)
    A = collections.defaultdict(list); L = loops(p); kept = 0
    for f in L:
        s1, e1, s2, e2 = int(f[1]), int(f[2]), int(f[4]), int(f[5])
        c1 = f[0] if f[0].startswith('chr') else 'chr' + f[0]; c2 = f[3] if f[3].startswith('chr') else 'chr' + f[3]
        if not (ov(c1, s1, e1) and ov(c2, s2, e2)): continue
        A[c1].append((s1, e1)); A[c2].append((s2, e2)); kept += 1
    h = hits(A, {}).astype(float); H[grp].append(h)
    if grp == 'N' and cell.startswith('T'): H['T'].append(h)
    print('MAP %s %s loops %d kept %d removed_not_ref_ctcf %.4f' % (grp, cell, len(L), kept, 1 - kept / len(L)), flush=True)
rng = np.random.default_rng(3957)
for grp in sorted(H):
    Hm = np.mean(H[grp], axis=0)
    for f in ('KCN', 'ALL', 'KPORE', 'Kaux'):
        obs = Hm[members[f]].mean(); C = cand[f]
        null = np.array([Hm[C[np.arange(len(C)), rng.integers(0, 50, len(C))]].mean() for _ in range(10000)])
        print('GROUP %s FAM %s T_obs %.4f null mean %.4f p_upper %.4f' % (grp, f, obs, null.mean(), (1 + (null >= obs).sum()) / 10001), flush=True)
