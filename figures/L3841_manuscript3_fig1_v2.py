"""Manuscript 3, Figure 1 v2 (L3841): adds SK-N-SH (L3825; null recomputed with seed 3825 and checked against L3825_tool_output.txt). Based on L3821.
Manuscript 3, Figure 1 (L3821). Recomputes the frozen L3725 statistic and null (same code path, numpy seed 3725) and checks
the summary line against rounds/L3725_tool_output.txt before drawing. argv: GENCODE GTF, H1 bedpe, HFFc6 bedpe.
A: share of genes whose TSS (+-5 kb) is at a CTCF-ChIAPET loop anchor, by channel family (offset 0, as L3713/L3725).
B: genome-shift null of D (1,000 shifts) with the observed D, per cell type.
C: what the other end of each channel-anchored loop touches (counts from rounds/L3729_tool_output.txt)."""
import sys, re, runpy, collections
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
src = open('/home/claude/dcf-math/rounds/dcf_channel_perm_L3725.py').read()
head = src.split("isch=np.array")[0]                      # gene table, anchors(), hits() exactly as frozen
g = {'__name__': 'fig', 'sys': sys}; exec(compile(head, 'L3725', 'exec'), g)
G, anchors, hits, Lc, CH = g['G'], g['anchors'], g['hits'], g['Lc'], g['CH']
Lc0 = dict(Lc)  # L3825 started from the gene-table lengths, before any H1/HFFc6 anchors
names = []
for l in __import__('gzip').open(sys.argv[1], 'rt'):
    if l.startswith('#'): continue
    x = l.split('\t')
    if x[2] != 'gene' or 'gene_type "protein_coding"' not in x[8] or not re.match(r'^chr([0-9]+|X)$', x[0]): continue
    names.append(re.search(r'gene_name "([^"]+)"', x[8]).group(1))
assert len(names) == len(G)
isch = np.array([q[2] for q in G]); rng = np.random.default_rng(3725)
FAM = [('K⁺ channels\n(KCN)', r'^KCN'), ('Na⁺ channels\n(SCN)', r'^SCN'), ('Ca²⁺ channels\n(CACNA1)', r'^CACNA1'), ('HCN', r'^HCN'), ('NALCN', r'^NALCN$'),
       ('NMDA\n(GRIN)', r'^GRIN'), ('Na⁺/K⁺ pump\n(ATP1A)', r'^ATP1A'), ('Ca²⁺ pumps\n(ATP2A/B)', r'^ATP2[AB]')]
fam = np.array([next((f for f, rx in FAM if re.match(rx, n) and CH.match(n)), '') for n in names])
out = {}; lines = []
for cell, p in [('H1', sys.argv[2]), ('HFFc6', sys.argv[3])]:
    A = anchors(p)
    for c in A: Lc[c] = max(Lc[c], max(e for _, e in A[c]))
    D = lambda H: H[isch].mean() - H[~isch].mean()
    H0 = hits(A, {}); d0 = D(H0)
    null = np.array([D(hits(A, {c: int(rng.integers(0, Lc[c])) for c in A})) for _ in range(1000)])
    pv = (1 + (null >= d0).sum()) / 1001
    lines.append('%-6s observed D %.4f | null mean %.4f sd %.4f 95th %.4f | p %.4f' % (cell, d0, null.mean(), null.std(), np.percentile(null, 95), pv))
    out[cell] = dict(H0=H0, d0=d0, null=null, p=pv)
frozen = [l.rstrip('\n') for l in open('/home/claude/dcf-math/rounds/L3725_tool_output.txt') if l[:2] in ('H1', 'HF')]
print('\n'.join(lines)); assert lines == frozen, 'recomputed null differs from L3725'
print('identical to L3725_tool_output.txt')
src2 = open('/home/claude/dcf-math/rounds/dcf_ctcf_neural_L3825a.py').read(); a0 = src2.index('def anchors(p):'); a1 = src2.index('FAM = [')
g2 = {'collections': collections, 'gzip': __import__('gzip')}; exec(src2[a0:a1], g2)
A, _ = g2['anchors'](sys.argv[4]); rng2 = np.random.default_rng(3825)
Lc.clear(); Lc.update(Lc0)
for c in A: Lc[c] = max(Lc[c], max(e for _, e in A[c]))
D = lambda H: H[isch].mean() - H[~isch].mean(); H0 = hits(A, {}); d0 = D(H0)
null = np.array([D(hits(A, {c: int(rng2.integers(0, Lc[c])) for c in A})) for _ in range(1000)]); pv = (1 + (null >= d0).sum()) / 1001
l3 = 'SK-N-SH observed D %.4f | null mean %.4f sd %.4f 95th %.4f | p %.4f' % (d0, null.mean(), null.std(), np.percentile(null, 95), pv)
f3 = [l.rstrip('\n') for l in open('/home/claude/dcf-math/rounds/L3825_tool_output.txt') if l.startswith('SK-N-SH')]
print(l3); assert [l3] == f3, 'SK-N-SH null differs from L3825'; print('identical to L3825_tool_output.txt')
out['SK-N-SH'] = dict(H0=H0, d0=d0, null=null, p=pv)
P = {}
for l in open('/home/claude/dcf-math/rounds/L3729_tool_output.txt'):
    m = re.match(r'(\S+) channel-anchored loop ends (\d+): partner channel (\d+) \([\d.]+\), other gene (\d+), none (\d+)', l)
    if m: P[m.group(1)] = tuple(int(m.group(i)) for i in (2, 3, 4, 5))
INK, MUTED, GRID = '#0b0b0b', '#52514e', '#e4e3df'; C1, C2, C3 = '#2a78d6', '#eb6834', '#1baf7a'   # palette slots 1-3 (dataviz reference)
fig = plt.figure(figsize=(12.5, 7.4), dpi=150); gs = fig.add_gridspec(2, 4, height_ratios=[1.15, 1], hspace=0.55, wspace=0.45)
axA = fig.add_subplot(gs[0, :])
fams = [f for f, _ in FAM]; xs = np.arange(len(fams) + 1); w = 0.27
LAB = {'H1': 'H1 (embryonic stem cells)', 'HFFc6': 'HFFc6 (foreskin fibroblasts)', 'SK-N-SH': 'SK-N-SH (neuroblastoma; blind, L3825)'}
for k, (cell, col) in enumerate([('H1', C1), ('HFFc6', C2), ('SK-N-SH', C3)]):
    H0 = out[cell]['H0']; v = [H0[fam == f].mean() for f in fams] + [H0[~isch].mean()]
    n = [int((fam == f).sum()) for f in fams] + [int((~isch).sum())]
    ax_b = axA.bar(xs + (k - 1) * w, v, w - 0.03, color=col, label=LAB[cell], zorder=2)
    for x, y in zip(xs + (k - 1) * w, v): axA.text(x, y + 0.012, '%.2f' % y, ha='center', va='bottom', fontsize=5.8, color=MUTED, rotation=90)
axA.set_xticks(xs); axA.set_xticklabels(['%s\nn=%d' % (f, int((fam == f).sum())) for f in fams] + ['all other\ngenes\nn=%d' % int((~isch).sum())], fontsize=7.5, color=INK)
axA.set_ylabel('share of genes with TSS at a\nCTCF loop anchor (±5 kb)', fontsize=8.5, color=INK); axA.set_ylim(0, 0.88)
axA.grid(axis='y', color=GRID, lw=0.8, zorder=0); [axA.spines[s].set_visible(False) for s in ('top', 'right')]
axA.legend(frameon=False, fontsize=8, loc='upper left', ncol=3); axA.set_title('A  Share of genes at CTCF loop anchors, by family (139 genes pooled: D = 0.110 H1, 0.057 HFFc6, 0.100 SK-N-SH)', loc='left', fontsize=10, color=INK)
for j, (cell, col) in enumerate([('H1', C1), ('HFFc6', C2), ('SK-N-SH', C3)]):
    ax = fig.add_subplot(gs[1, j]); o = out[cell]
    ax.hist(o['null'], bins=40, color='#b9b8b1', edgecolor='white', lw=0.5, zorder=2)
    ax.axvline(o['d0'], color=col, lw=2, zorder=3); ax.text(o['d0'] - 0.003, ax.get_ylim()[1] * 0.92, 'observed\nD = %.3f\np = %.3f' % (o['d0'], o['p']), color=INK, fontsize=7.5, va='top', ha='right', bbox=dict(facecolor='white', edgecolor='none', pad=1.5))
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.set_xlabel('D = channel share − other-gene share', fontsize=8, color=INK); ax.set_ylabel('genome shifts (of 1,000)', fontsize=8, color=INK)
    ax.grid(axis='y', color=GRID, lw=0.8, zorder=0); [ax.spines[s].set_visible(False) for s in ('top', 'right')]; ax.tick_params(labelsize=7.5)
    ax.set_title('%s  Shifted-anchor null, %s' % ('B' if j == 0 else ' ', cell), loc='left', fontsize=10, color=INK)
axC = fig.add_subplot(gs[1, 3]); cats = ['channel\ngene', 'other\ngene', 'no\ngene']
for k, (cell, col) in enumerate([('H1', C1), ('HFFc6', C2)]):
    t, a, b, c = P[cell]; v = [a / t, b / t, c / t]
    axC.bar(np.arange(3) + (k - 0.5) * w, v, w - 0.04, color=col, label='%s (%d loop ends)' % (cell, t), zorder=2)
    for x, y in zip(np.arange(3) + (k - 0.5) * w, v): axC.text(x, y + 0.015, '%.2f' % y, ha='center', fontsize=7, color=MUTED)
axC.set_xticks(range(3)); axC.set_xticklabels(cats, fontsize=7.5, color=INK); axC.set_ylim(0, 1.35); axC.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0]); axC.set_ylabel('share of loop ends', fontsize=8, color=INK)
axC.grid(axis='y', color=GRID, lw=0.8, zorder=0); [axC.spines[s].set_visible(False) for s in ('top', 'right')]; axC.tick_params(labelsize=7.5)
axC.legend(frameon=False, fontsize=7, loc='upper left'); axC.set_title('C  The other loop end', loc='left', fontsize=10, color=INK)
fig.text(0.01, 0.005, 'Data: 4DN union loop calls (H1, HFFc6; CTCF-ChIAPET-supported); ENCODE CTCF in-situ ChIA-PET SK-N-SH ENCFF775DIU (top 28,270 loops by PET count); GENCODE v49. Statistics frozen in dcf-math L3725, L3825; partner counts L3729 (H1, HFFc6 only).', fontsize=6.3, color=MUTED)
plt.savefig('/home/claude/dcf-math/figures/L3841_manuscript3_fig1_v2.png', bbox_inches='tight')
print('saved')
