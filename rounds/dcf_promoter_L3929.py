"""L3929 frozen: are primary-cell CTCF loop anchors more promoter-proximal? argv: GTF, REF (as L3909, setup only), then GROUP:CELL=path
(ChIA-PET; anchors() of L3825a). Per map: fraction of anchors whose midpoint lies within 5 kb of any protein-coding TSS of the L3725 gene
table (G[i][1] = TSS). Prints per-map fractions and group medians; Mann-Whitney U (one-sided, N > A) via scipy."""
import sys, collections
import numpy as np
from scipy.stats import mannwhitneyu
argv = sys.argv; sys.argv = [argv[0], argv[1], 'both', argv[2]]
src = open('/home/claude/dcf-math/rounds/dcf_ctcfsplit_L3909.py').read(); src = src[:src.index('Hs = []')]
g = {'__name__': 'L3929'}; exec(compile(src, 'L3909', 'exec'), g)
G, anch825 = g['G'], g['anch825']
T = collections.defaultdict(list)
for q in G: T[q[0]].append(q[1])
T = {c: np.sort(v) for c, v in T.items()}
F = collections.defaultdict(list)
for arg in argv[3:]:
    grp, rest = arg.split(':', 1); cell, p = rest.split('=', 1)
    A = anch825(p)[0]; A = {(c if c.startswith('chr') else 'chr' + c): v for c, v in A.items()}
    n = k = 0
    for c, v in A.items():
        m = np.array([(s + e) // 2 for s, e in v]); n += len(m)
        if c not in T: continue
        i = np.clip(np.searchsorted(T[c], m), 1, len(T[c]) - 1)
        d = np.minimum(np.abs(T[c][i] - m), np.abs(T[c][i - 1] - m)); k += int((d <= 5000).sum())
    F[grp].append(k / n); print('MAP %s %s anchors %d promoter_fraction %.4f' % (grp, cell, n, k / n), flush=True)
for grp in sorted(F): print('GROUP %s median %.4f' % (grp, np.median(F[grp])))
print('MWU N>A p %.4f' % mannwhitneyu(F['N'], F['A'], alternative='greater').pvalue)
