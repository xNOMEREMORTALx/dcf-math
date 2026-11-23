"""L3981 frozen: L3969 script, seed 3981. L3969 frozen: L3965 script, seed 3969, with the per-loop value changed from log10 length to an indicator: 1 if the OTHER anchor
touches any protein-coding TSS +- 5 kb (other than the gene itself), else 0. Gene score = mean over its loops (partner-promoter fraction).
Genes touched by both anchors of one loop are scored once, from anchor 1."""
"""L3965 frozen: are loops anchored at pore-forming K+ genes longer than loops anchored at matched genes?
argv: GTF, REF (setup only, as L3909), then GROUP:CELL=path. Loops per map: 4DN union files (H1, HFFc6) -> loops tagged CTCF-ChIAPET;
ENCODE ChIA-PET -> top 28,270 by column 7 (loops() of L3933); Hi-C (group B) -> all loops. A loop touches gene i if either anchor
overlaps TSS(i) +- 5 kb. Loop length = |midpoint2 - midpoint1| (intrachromosomal only). Per group: gene score = mean log10 length over
all loops touching the gene in the group's maps (NaN if none). Family statistic = mean score over members with a score. Null: each
scored member is replaced by a random scored candidate among its 50 matched candidates (L3909 cand), 10,000 sets, seed 3965."""
import sys, collections, gzip
import numpy as np
argv = sys.argv; sys.argv = [argv[0], argv[1], 'both', argv[2]]
src = open('/home/claude/dcf-math/rounds/dcf_ctcfsplit_L3909.py').read(); src = src[:src.index('Hs = []')]
g = {'__name__': 'L3969'}; exec(compile(src, 'L3909', 'exec'), g)
G, members, cand = g['G'], g['members'], g['cand']
s3 = open('/home/claude/dcf-math/rounds/dcf_ppfilter_L3933.py').read(); a0 = s3.index('def loops(p):'); a1 = s3.index('H = collections.defaultdict(list)')
g3 = {'gzip': gzip}; exec(s3[a0:a1], g3); loops933 = g3['loops']
TS = collections.defaultdict(list)
for i, q in enumerate(G): TS[q[0]].append((q[1], i))
TS = {c: (np.array([t for t, _ in sorted(v)]), np.array([i for _, i in sorted(v)])) for c, v in TS.items()}
def touched(c, s, e):
    if c not in TS: return []
    t, ix = TS[c]; return ix[np.searchsorted(t, s - 5000):np.searchsorted(t, e + 5000, side='right')].tolist()
def read(grp, cell, p):
    if cell in ('H1', 'HFFc6'):
        L = [f for f in (l.rstrip('\n').split('\t') for l in open(p)) if len(f) >= 7 and f[1].isdigit() and 'CTCF-ChIAPET' in f[6].split(',')]
    elif grp == 'B':
        L = [f for f in (l.rstrip('\n').split('\t') for l in gzip.open(p, 'rt') if not l.startswith('#')) if len(f) >= 6 and f[1].isdigit()]
    else: L = loops933(p)
    return L
S = collections.defaultdict(lambda: collections.defaultdict(list))
for arg in argv[3:]:
    grp, rest = arg.split(':', 1); cell, p = rest.split('=', 1); n = 0
    for f in read(grp, cell, p):
        c1 = f[0] if f[0].startswith('chr') else 'chr' + f[0]; c2 = f[3] if f[3].startswith('chr') else 'chr' + f[3]
        if c1 != c2: continue
        s1, e1, s2, e2 = int(f[1]), int(f[2]), int(f[4]), int(f[5]); d = abs((s2 + e2) // 2 - (s1 + e1) // 2)
        if d <= 0: continue
        n += 1; t1, t2 = set(touched(c1, s1, e1)), set(touched(c2, s2, e2))
        for i in t1: S[grp][i].append(float(len(t2 - {i}) > 0))
        for i in t2 - t1: S[grp][i].append(float(len(t1 - {i}) > 0))
    print('map', grp, cell, 'intrachromosomal loops', n, flush=True)
rng = np.random.default_rng(3981)
for grp in sorted(S):
    sc = np.full(len(G), np.nan)
    for i, v in S[grp].items(): sc[i] = np.mean(v)
    for f in ('KPORE', 'KCN', 'ALL', 'Kaux'):
        idx = np.array(members[f]); C = np.array(cand[f]); ok = ~np.isnan(sc[idx]); idx, C = idx[ok], C[ok]
        pools = [c[~np.isnan(sc[c])] for c in C]; keep = [k for k, q in enumerate(pools) if len(q)]
        obs = sc[idx[keep]].mean()
        null = np.array([np.mean([sc[pools[k][rng.integers(0, len(pools[k]))]] for k in keep]) for _ in range(10000)])
        print('GROUP %s FAM %s scored %d T_obs %.4f null mean %.4f diff %+.4f p_upper %.4f p_lower %.4f' % (grp, f, len(keep), obs, null.mean(), obs - null.mean(), (1 + (null >= obs).sum()) / 10001, (1 + (null <= obs).sum()) / 10001), flush=True)
