"""Manuscript 3, Figure 2 (L3865): per-cell genome-shift z for each family contrast (L3857 output) and the length+density-matched
Delta (L3861 output). argv: rounds/L3857_tool_output.txt rounds/L3861_tool_output.txt"""
import re, sys
import numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
T = open(sys.argv[1]).read(); rows = [l for l in T.splitlines() if ' | KCN c ' in l]
cells = [r.split(' | ')[0] for r in rows]
Z = {f: [float(re.search(r'%s c [-+\d.]+ z ([-+\d.]+)' % f, r).group(1)) for r in rows] for f in ('KCN', 'GRIN', 'CACNA1', 'ALL')}
S = {f: float(z) for f, z in re.findall(r'STOUFFER (\S+) Z ([-+\d.]+)', T)}
U = [l for l in open(sys.argv[2]) if '| KCN ' in l]
DL = {f: [float(re.search(r'%s [\d.]+ ctrl [\d.]+ delta ([-+\d.]+)' % f, l).group(1)) for l in U] for f in ('KCN', 'GRIN', 'CACNA1')}
INK, MUTED, GRID = '#0b0b0b', '#52514e', '#e4e3df'; COL = {'KCN': '#2a78d6', 'GRIN': '#eb6834', 'CACNA1': '#1baf7a', 'ALL': '#6b6a64'}
LAB = {'KCN': 'K⁺ channels (96)', 'GRIN': 'NMDA receptors (7)', 'CACNA1': 'Ca²⁺ channel pores (10)', 'ALL': 'all 139 channel/pump genes'}
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 5.2), dpi=150, gridspec_kw=dict(width_ratios=[1.35, 1], wspace=0.32))
y = np.arange(len(cells))[::-1]
for k, f in enumerate(['ALL', 'KCN', 'GRIN', 'CACNA1']):
    a1.scatter(Z[f], y + (k - 1.5) * 0.17, s=34, color=COL[f], edgecolor='white', lw=0.8, zorder=3, label='%s  (combined Z %+.1f)' % (LAB[f], S[f]))
a1.axvline(0, color=MUTED, lw=1); a1.axvspan(-1.645, 1.645, color='#f3f2ee', zorder=0)
a1.set_yticks(y); a1.set_yticklabels(cells, fontsize=8.5, color=INK); a1.set_xlabel('genome-shift z (family share − other-gene share)', fontsize=8.5, color=INK)
a1.grid(axis='x', color=GRID, lw=0.8, zorder=0); [a1.spines[s].set_visible(False) for s in ('top', 'right')]; a1.tick_params(labelsize=8)
a1.legend(frameon=False, fontsize=7.5, loc='lower left', bbox_to_anchor=(0, 1.0), ncol=2)
a1.set_title('A  Ten cell types, each family against the shifted-anchor null (shaded: |z| < 1.645)', loc='left', fontsize=10, color=INK, pad=38)
for k, f in enumerate(['KCN', 'GRIN', 'CACNA1']):
    a2.scatter(DL[f], y + (k - 1) * 0.2, s=34, color=COL[f], edgecolor='white', lw=0.8, zorder=3, label=LAB[f])
a2.axvline(0, color=MUTED, lw=1); a2.set_yticks(y); a2.set_yticklabels(cells, fontsize=8.5, color=INK)
a2.set_xlabel('Δ share vs genes matched for length and local gene density', fontsize=8.5, color=INK)
a2.grid(axis='x', color=GRID, lw=0.8, zorder=0); [a2.spines[s].set_visible(False) for s in ('top', 'right')]; a2.tick_params(labelsize=8)
a2.legend(frameon=False, fontsize=7.5, loc='lower left', bbox_to_anchor=(0, 1.0), ncol=2)
a2.set_title('B  Δ after matching for length and gene density', loc='left', fontsize=10, color=INK, pad=38)
fig.text(0.01, -0.02, 'Combined Z assumes independent cells; cells share genes and many CTCF sites, so it overstates the evidence. Data: dcf-math L3857, L3861.', fontsize=6.8, color=MUTED)
plt.savefig('/home/claude/dcf-math/figures/L3865_tencell_z.png', bbox_inches='tight'); print('saved')
