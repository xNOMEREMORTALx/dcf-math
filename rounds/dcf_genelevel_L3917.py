"""L3917 frozen: are the same pore-forming K+ genes anchored across cell groups? argv: GTF, REF (comma-separated 4DN union files for
the CTCF reference, as L3909), then GROUP:CELL=path entries. GROUP A = ten cell lines (4DN union -> anchors() of L3725; other ENCODE
ChIA-PET -> anchors() of L3825a); B = Hi-C maps, CTCF-anchored loops only (both anchors overlap a reference anchor, all loops read);
N = primary-cell ChIA-PET maps (anchors() of L3825a). Gene table, TSS +-5 kb, hits(), matched candidates (50 per gene, length and
density) exactly as L3909. For each KPORE gene i and group g: freq_g(i) = share of the group's maps with i at an anchor;
resid_g(i) = freq_g(i) - mean over i's 50 candidates of freq_g. Spearman rho between residual vectors; p_upper by 10,000 random
permutations of the second vector (seed 3917)."""
import sys, collections, gzip
import numpy as np
argv = sys.argv; sys.argv = [argv[0], argv[1], 'both', argv[2]]
src = open('/home/claude/dcf-math/rounds/dcf_ctcfsplit_L3909.py').read(); src = src[:src.index('Hs = []')]
g = {'__name__': 'L3917'}; exec(compile(src, 'L3909', 'exec'), g)
hits, anch725, anch825, ov, members, cand, names = g['hits'], g['anch725'], g['anch825'], g['ov'], g['members'], g['cand'], g['names']
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
idx = members['KPORE']; C = cand['KPORE']; R = {}
for grp in sorted(H):
    fr = np.mean(H[grp], axis=0); R[grp] = fr[idx] - fr[C].mean(axis=1)
    print('GROUP %s maps %d KPORE mean freq %.4f matched %.4f mean resid %+.4f' % (grp, len(H[grp]), fr[idx].mean(), fr[C].mean(), R[grp].mean()), flush=True)
rk = lambda v: np.argsort(np.argsort(v, kind='stable'), kind='stable').astype(float)
def rho(a, b):
    from scipy.stats import rankdata
    x, y = rankdata(a), rankdata(b); return np.corrcoef(x, y)[0, 1]
rng = np.random.default_rng(3917)
for a, b in [('A', 'B'), ('A', 'N'), ('B', 'N')]:
    r0 = rho(R[a], R[b]); null = np.array([rho(R[a], rng.permutation(R[b])) for _ in range(10000)])
    print('RHO %s-%s %.4f p_upper %.4f' % (a, b, r0, (1 + (null >= r0).sum()) / 10001), flush=True)
o = np.argsort(-R['A'], kind='stable')
for j in o: print('GENE %-8s resid A %+.3f B %+.3f N %+.3f' % (names[idx[j]], R['A'][j], R['B'][j], R['N'][j]))
