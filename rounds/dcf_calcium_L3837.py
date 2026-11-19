"""L3837 frozen: are calcium-channel genes (pore + auxiliary subunits) below the genome-wide share at CTCF loop anchors?
argv: GENCODE v49 GTF, H1 union bedpe, HFFc6 union bedpe, SK-N-SH ENCFF775DIU bedpe.gz.
Anchors: H1/HFFc6 = CTCF-ChIAPET-tagged loops (anchors() of L3725); SK-N-SH = top 28,270 loops by PET count (anchors() of L3825a).
Gene table, TSS +-5 kb and hits() verbatim from L3725. Sets: AUX = CACNB1-4, CACNA2D1-4, CACNG1-8 (16); CA = AUX + CACNA1x (26);
OTHER = protein-coding genes outside the L3725 channel set and outside AUX. Null: 1,000 per-chromosome common shifts, seed 3837,
lower tail for D_ca = share(CA) - share(OTHER)."""
import sys, re, gzip, runpy
import numpy as np
src = open('/home/claude/dcf-math/rounds/dcf_channel_perm_L3725.py').read()
g = {'__name__': 'L3837', 'sys': sys}; exec(compile(src.split("isch=np.array")[0], 'L3725', 'exec'), g)
G, hits, Lc, CH, anchors725 = g['G'], g['hits'], g['Lc'], g['CH'], g['anchors']
sys_argv = sys.argv; sys.argv = sys_argv[:2] + [sys_argv[4]]
names = []
for l in gzip.open(sys_argv[1], 'rt'):
    if l.startswith('#'): continue
    x = l.split('\t')
    if x[2] != 'gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$', x[0]): continue
    names.append(re.search(r'gene_name "([^"]+)"', x[8]).group(1))
assert len(names) == len(G)
src2 = open('/home/claude/dcf-math/rounds/dcf_ctcf_neural_L3825a.py').read()
a0 = src2.index('def anchors(p):'); a1 = src2.index('FAM = [')
g2 = {'collections': __import__('collections'), 'gzip': gzip}; exec(src2[a0:a1], g2); anchors825 = g2['anchors']
AUX = re.compile(r'^(CACNB[1-4]|CACNA2D[1-4]|CACNG[1-8])$')
aux = np.array([bool(AUX.match(n)) for n in names]); isch = np.array([q[2] for q in G])
ca = aux | np.array([bool(re.match(r'^CACNA1[A-Z]$', n)) for n in names]); other = ~isch & ~aux
print('AUX %d CA %d OTHER %d' % (aux.sum(), ca.sum(), other.sum()))
rng = np.random.default_rng(3837)
for cell, p, fn in [('H1', sys_argv[2], 'ctcf'), ('HFFc6', sys_argv[3], 'ctcf'), ('SK-N-SH', sys_argv[4], 'top')]:
    A = anchors725(p) if fn == 'ctcf' else anchors825(p)[0]
    for c in A: Lc[c] = max(Lc[c], max(e for _, e in A[c]))
    H0 = hits(A, {}); D = lambda H: H[ca].mean() - H[other].mean(); d0 = D(H0)
    null = np.array([D(hits(A, {c: int(rng.integers(0, Lc[c])) for c in A})) for _ in range(1000)])
    pl = (1 + (null <= d0).sum()) / 1001
    print('%-8s AUX %.4f CA %.4f OTHER %.4f | D_ca %.4f null mean %.4f p_lower %.4f' % (cell, H0[aux].mean(), H0[ca].mean(), H0[other].mean(), d0, null.mean(), pl), flush=True)
