"""L3825 frozen: channel-gene CTCF-anchor test in a neural cell line (SK-N-SH, ENCODE ENCSR514HBO, CTCF ChIA-PET loops).
argv: GENCODE v49 GTF, one ENCODE loops BEDPE (GRCh38; columns 1-6 = chrA startA endA chrB startB endB; every loop is a CTCF ChIA-PET loop).
Gene table, channel regex, TSS +-5 kb rule and hits() are taken verbatim from rounds/dcf_channel_perm_L3725.py; only anchors() is adapted
(all loops count, no 'CTCF-ChIAPET' tag column). Null: 1,000 per-chromosome common shifts, numpy seed 3825.
Prints pooled D and p, then per-family shares (offset 0)."""
import sys, re, gzip, collections
import numpy as np
src = open('/home/claude/dcf-math/rounds/dcf_channel_perm_L3725.py').read()
g = {'__name__': 'L3825', 'sys': sys}; exec(compile(src.split("isch=np.array")[0], 'L3725', 'exec'), g)
G, hits, Lc, CH = g['G'], g['hits'], g['Lc'], g['CH']
names = []
for l in gzip.open(sys.argv[1], 'rt'):
    if l.startswith('#'): continue
    x = l.split('\t')
    if x[2] != 'gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$', x[0]): continue
    names.append(re.search(r'gene_name "([^"]+)"', x[8]).group(1))
assert len(names) == len(G)
def anchors(p):
    A = collections.defaultdict(list); op = gzip.open if p.endswith('.gz') else open; n = 0
    for l in op(p, 'rt'):
        f = l.rstrip('\n').split('\t')
        if len(f) < 6 or not f[1].isdigit(): continue
        A[f[0]].append((int(f[1]), int(f[2]))); A[f[3]].append((int(f[4]), int(f[5]))); n += 1
    return A, n
FAM = [('KCN', r'^KCN'), ('SCN', r'^SCN'), ('CACNA1', r'^CACNA1'), ('HCN', r'^HCN'), ('NALCN', r'^NALCN$'), ('GRIN', r'^GRIN'), ('ATP1A', r'^ATP1A'), ('ATP2AB', r'^ATP2[AB]')]
fam = np.array([next((f for f, rx in FAM if re.match(rx, n) and CH.match(n)), '') for n in names])
isch = np.array([q[2] for q in G]); rng = np.random.default_rng(3825)
A, n = anchors(sys.argv[2])
for c in A: Lc[c] = max(Lc[c], max(e for _, e in A[c]))
D = lambda H: H[isch].mean() - H[~isch].mean()
H0 = hits(A, {}); d0 = D(H0)
null = np.array([D(hits(A, {c: int(rng.integers(0, Lc[c])) for c in A})) for _ in range(1000)])
pv = (1 + (null >= d0).sum()) / 1001
print('loops %d | genes %d channel %d' % (n, len(G), isch.sum()))
print('SK-N-SH observed D %.4f | null mean %.4f sd %.4f 95th %.4f | p %.4f' % (d0, null.mean(), null.std(), np.percentile(null, 95), pv))
print('OTHER share %.4f n %d' % (H0[~isch].mean(), (~isch).sum()))
for f, _ in FAM: print('FAM %s share %.4f n %d' % (f, H0[fam == f].mean() if (fam == f).any() else float('nan'), (fam == f).sum()))
