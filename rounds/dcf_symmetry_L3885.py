"""L3885 frozen: channel SYMMETRY ORDER test (L3873a machinery, seed 3885, ten original cells). Groups by pore symmetry:
  TRI (3-fold): ASIC1-5, SCNN1A/B/D/G, P2RX1-7; TETRA (4-fold): pore-forming K+ (Kv, K2P, Kir, KCa as L3873);
  PENTA (5-fold, Cys-loop receptors): CHRN*, GABR*, GLRA*/GLRB, HTR3A-E, ZACN; HEXA (6-fold): GJ* connexins, ORAI1-3.
  The matched pool also excludes every gene in these groups.
L3873 amendment a: identical to dcf_sets_L3873.py except the Kaux rule (the original referred to its own list and recursed; it
crashed before computing any share). L3873 frozen: L3869 gene-resampling test (unchanged machinery, seed 3873) applied to new gene sets:
  GLUR = all ionotropic glutamate receptor genes GRIN1, GRIN2A-D, GRIN3A-B, GRIA1-4, GRIK1-5, GRID1-2 (matched pool also excludes them);
  K+ subfamilies among the L3725 KCN genes: Kv = KCNA/B/C/D/F/G/H/Q/S/V; K2P = KCNK; Kir = KCNJ; KCa = KCNMA1, KCNN, KCNT, KCNU;
  Kaux = the remaining KCN genes (auxiliary subunits such as KCNE, KCNAB, KCNIP, KCNMB).
Original L3869 docstring follows.
L3869 frozen: dependence-aware ten-cell test. Gene-resampling null with length+density matching; all cells scored on the SAME
random gene set, so shared genes and shared CTCF sites are kept. For each member gene, its 50 nearest non-channel genes in (z log length,
z log density) are its candidates; a null set draws one candidate per member (numpy seed 3869), 10,000 sets.
T = mean over the ten cells of the set's anchor share. p_upper = (1 + #null >= obs)/(1 + 10000); p_lower likewise with <=.
Families KCN, GRIN, CACNA1, ALL (139). Code below the docstring reuses L3861 (gene table, length, density).
L3861 frozen: is the family pattern explained by gene length AND local gene density? Based on L3853 (same inputs, hits, families).
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
GLU = re.compile(r'^(GRIN1|GRIN2[A-D]|GRIN3[AB]|GRIA[1-4]|GRIK[1-5]|GRID[12])$')
SYM = {'TRI': re.compile(r'^(ASIC[1-5]|SCNN1[ABDG]|P2RX[1-7])$'), 'PENTA': re.compile(r'^(CHRN[ABDEG]\d*|GABR[ABGDEPQR]\d*|GLR[AB]\d*|HTR3[A-E]|ZACN)$'),
       'HEXA': re.compile(r'^(GJ[ABCD]\d+|ORAI[1-3])$')}
nonch = np.array([not CH.match(n) and not AUX.match(n) and not GLU.match(n) and not any(r.match(n) for r in SYM.values()) for n in names]); pool = np.where(nonch)[0]
KC = lambda n: bool(CH.match(n)) and n.startswith('KCN')
FAM = [('TRI', lambda n: bool(SYM['TRI'].match(n))),
       ('TETRA', lambda n: KC(n) and bool(re.match(r'^(KCN[ABCDFGHQSV]\d|KCNK\d|KCNJ\d|KCNMA1$|KCNN\d|KCNT\d|KCNU\d)', n))),
       ('PENTA', lambda n: bool(SYM['PENTA'].match(n))), ('HEXA', lambda n: bool(SYM['HEXA'].match(n)))]
members = {f: np.array([i for i, n in enumerate(names) if fn(n)]) for f, fn in FAM}
for f, _ in FAM: print('SET %s n %d: %s' % (f, len(members[f]), ' '.join(sorted(names[i] for i in members[f]))), flush=True)
cand = {f: np.array([pool[np.argsort(np.hypot(zl[pool] - zl[i], zd[pool] - zd[i]), kind='stable')[:50]] for i in idx]) for f, idx in members.items()}
Hs = []
for arg in sys.argv[2:]:
    cell, p = arg.split('=', 1)
    A = anch725(p) if cell in ('H1', 'HFFc6') else anch825(p)[0]
    Hs.append(hits(A, {}).astype(float)); print('cell', cell, flush=True)
Hm = np.mean(Hs, axis=0); rng = np.random.default_rng(3885)
for f, _ in FAM:
    obs = Hm[members[f]].mean(); C = cand[f]
    null = np.array([Hm[C[np.arange(len(C)), rng.integers(0, 50, len(C))]].mean() for _ in range(10000)])
    pu = (1 + (null >= obs).sum()) / 10001; pl = (1 + (null <= obs).sum()) / 10001
    print('FAM %s n %d T_obs %.4f null mean %.4f sd %.4f p_upper %.4f p_lower %.4f' % (f, len(C), obs, null.mean(), null.std(), pu, pl), flush=True)
