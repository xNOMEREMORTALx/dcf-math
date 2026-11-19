"""L3857 frozen: Stouffer-combined genome-shift test, per gene family, across ten cell types.
argv: GENCODE v49 GTF, then CELL=path pairs (H1/HFFc6: 4DN CTCF-tagged anchors of L3725; others: top 28,270 of L3825a).
Per cell and family f: c_f = share(f) - share(OTHER), OTHER = non-channel, non-calcium-auxiliary protein-coding genes.
Null: 1,000 per-chromosome common shifts (numpy seed 3857, one generator across all cells in argv order); z = (c_obs - mean)/sd.
Stouffer Z_f = sum(z)/sqrt(n cells). Families KCN, GRIN, CACNA1, and ALL (the 139-gene L3725 set)."""
import sys, re, gzip, collections
import numpy as np
src = open('/home/claude/dcf-math/rounds/dcf_channel_perm_L3725.py').read()
g = {'__name__': 'L3857', 'sys': sys}; exec(compile(src.split("isch=np.array")[0], 'L3725', 'exec'), g)
G, hits, CH, anch725, Lc = g['G'], g['hits'], g['CH'], g['anchors'], g['Lc']; Lc0 = dict(Lc)
src2 = open('/home/claude/dcf-math/rounds/dcf_ctcf_neural_L3825a.py').read(); a0 = src2.index('def anchors(p):'); a1 = src2.index('FAM = [')
g2 = {'collections': collections, 'gzip': gzip}; exec(src2[a0:a1], g2); anch825 = g2['anchors']
names = []
for l in gzip.open(sys.argv[1], 'rt'):
    if l.startswith('#'): continue
    x = l.split('\t')
    if x[2] != 'gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$', x[0]): continue
    names.append(re.search(r'gene_name "([^"]+)"', x[8]).group(1))
AUX = re.compile(r'^(CACNB[1-4]|CACNA2D[1-4]|CACNG[1-8])$')
isch = np.array([q[2] for q in G]); other = np.array([not CH.match(n) and not AUX.match(n) for n in names])
F = {'KCN': np.array([bool(re.match('^KCN', n)) and bool(CH.match(n)) for n in names]), 'GRIN': np.array([bool(re.match('^GRIN', n)) and bool(CH.match(n)) for n in names]),
     'CACNA1': np.array([bool(re.match('^CACNA1', n)) and bool(CH.match(n)) for n in names]), 'ALL': isch}
rng = np.random.default_rng(3857); Z = collections.defaultdict(list)
for arg in sys.argv[2:]:
    cell, p = arg.split('=', 1); Lc.clear(); Lc.update(Lc0)
    A = anch725(p) if cell in ('H1', 'HFFc6') else anch825(p)[0]
    for c in A: Lc[c] = max(Lc[c], max(e for _, e in A[c]))
    stat = lambda H: {f: H[m].mean() - H[other].mean() for f, m in F.items()}
    o = stat(hits(A, {})); nulls = collections.defaultdict(list)
    for _ in range(1000):
        s = stat(hits(A, {c: int(rng.integers(0, Lc[c])) for c in A}))
        for f in F: nulls[f].append(s[f])
    row = [cell]
    for f in F:
        n = np.array(nulls[f]); z = (o[f] - n.mean()) / n.std(); Z[f].append(z); row.append('%s c %+.4f z %+.2f' % (f, o[f], z))
    print(' | '.join(row), flush=True)
for f in F: print('STOUFFER %s Z %+.3f n %d' % (f, sum(Z[f]) / np.sqrt(len(Z[f])), len(Z[f])))
