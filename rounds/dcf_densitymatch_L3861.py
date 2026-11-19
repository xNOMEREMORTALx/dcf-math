"""L3861 frozen: is the family pattern explained by gene length AND local gene density? Based on L3853 (same inputs, hits, families).
Density = number of protein-coding gene TSSs within +-1 Mb of the gene TSS (itself excluded). Matching: the 20 non-channel genes
nearest in (z-scored log10 length, z-scored log10(1 + density)), Euclidean, ties by table order. Also prints the anchor share of the
lowest-density decile of non-channel genes. Original L3853 docstring follows.
L3853 frozen: is the family pattern at CTCF anchors explained by gene length?
argv: GENCODE v49 GTF, then CELL=path pairs. H1 and HFFc6 paths are 4DN union files (CTCF-ChIAPET-tagged loops, anchors() of L3725);
every other path is an ENCODE loops bedpe (top 28,270 by PET count, anchors() of L3825a).
Gene table, TSS +-5 kb and hits() verbatim from L3725. Gene length = GTF end - start + 1.
Matched control for a family: for each member gene, the 20 non-channel genes (outside the L3725 channel set and outside the calcium
auxiliary set) nearest in log10 length (ties by table order); the pooled list (with repeats) is the control.
Delta(family, cell) = family share - matched-control share. Also prints, per cell, the share of the longest decile of non-channel genes
and the share of all non-channel genes."""
import sys, re, gzip, collections
import numpy as np
src = open('/home/claude/dcf-math/rounds/dcf_channel_perm_L3725.py').read()
g = {'__name__': 'L3853', 'sys': sys}; exec(compile(src.split("isch=np.array")[0], 'L3725', 'exec'), g)
G, hits, CH, anch725 = g['G'], g['hits'], g['CH'], g['anchors']
src2 = open('/home/claude/dcf-math/rounds/dcf_ctcf_neural_L3825a.py').read(); a0 = src2.index('def anchors(p):'); a1 = src2.index('FAM = [')
g2 = {'collections': collections, 'gzip': gzip}; exec(src2[a0:a1], g2); anch825 = g2['anchors']
names, length = [], []
for l in gzip.open(sys.argv[1], 'rt'):
    if l.startswith('#'): continue
    x = l.split('\t')
    if x[2] != 'gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$', x[0]): continue
    names.append(re.search(r'gene_name "([^"]+)"', x[8]).group(1)); length.append(int(x[4]) - int(x[3]) + 1)
assert len(names) == len(G)
loglen = np.log10(np.array(length, float))
byc = collections.defaultdict(list)
for i, q in enumerate(G): byc[q[0]].append(i)
dens = np.zeros(len(G))
for c, idx in byc.items():
    T = np.array([G[i][1] for i in idx]); o = np.sort(T)
    dens[idx] = np.searchsorted(o, T + 1_000_000, side='right') - np.searchsorted(o, T - 1_000_000, side='left') - 1
ld = np.log10(1 + dens); zl = (loglen - loglen.mean()) / loglen.std(); zd = (ld - ld.mean()) / ld.std()
AUX = re.compile(r'^(CACNB[1-4]|CACNA2D[1-4]|CACNG[1-8])$')
nonch = np.array([not CH.match(n) and not AUX.match(n) for n in names]); pool = np.where(nonch)[0]
FAM = [('KCN', r'^KCN'), ('GRIN', r'^GRIN'), ('CACNA1', r'^CACNA1')]
members = {f: [i for i, n in enumerate(names) if re.match(rx, n) and CH.match(n)] for f, rx in FAM}
ctrl = {}
for f, idx in members.items():
    L = []
    for i in idx:
        d = np.hypot(zl[pool] - zl[i], zd[pool] - zd[i]); o = np.argsort(d, kind='stable')[:20]; L.extend(pool[o].tolist())
    ctrl[f] = np.array(L)
    print('FAMILY %s n %d median length %d density %.0f | control median length %d density %.0f' % (f, len(idx), np.median([length[i] for i in idx]), np.median(dens[idx]), np.median([length[i] for i in ctrl[f]]), np.median(dens[ctrl[f]])))
top = pool[ld[pool] <= np.percentile(ld[pool], 10)]
for arg in sys.argv[2:]:
    cell, p = arg.split('=', 1)
    A = anch725(p) if cell in ('H1', 'HFFc6') else anch825(p)[0]
    H = hits(A, {})
    out = ['%s' % cell]
    for f, _ in FAM:
        fs = H[members[f]].mean(); cs = H[ctrl[f]].mean(); out.append('%s %.4f ctrl %.4f delta %+.4f' % (f, fs, cs, fs - cs))
    out.append('SPARSE10 %.4f NONCH %.4f' % (H[top].mean(), H[pool].mean()))
    print(' | '.join(out), flush=True)
