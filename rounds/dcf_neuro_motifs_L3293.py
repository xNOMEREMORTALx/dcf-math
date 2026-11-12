"""dcf_neuro_motifs (L3293): label-free nervous-system channel motifs in human mRNA.
One transcript per gene (lowest NM_ number), longest ATG ORF. Motifs:
  K   potassium-channel selectivity filter  T-[VIT]-G-[YF]-G
  S4  voltage-sensor helix: 5 positive residues spaced every 3  [RK]..[RK]..[RK]..[RK]..[RK]
  CL  Cys-loop (neurotransmitter-gated channel, PROSITE PS00236)  C-[LIVMFQ]-x2-[LIVMF]-x2-[FY]-P-[FYW]-D-x3-C
Validation (after counting) by gene symbols: KCN*/HCN*/KCNH* (K), SCN*/CACNA1*/KCN*/HCN* (S4 voltage-gated), CHRN*/GABR*/GLR[AB]*/HTR3*/ZACN (CL).
Usage: python3 -I neuro_motifs.py human.N.rna.fna.gz [...]   Author: Gary NOMEREMORTAL Mason (DCF)."""
import gzip, re, sys
CODE = {}; b = 'TCAG'; aa = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i, x in enumerate(b):
    for j, y in enumerate(b):
        for k, z in enumerate(b): CODE[x + y + z] = aa[16 * i + 4 * j + k]
def orf(s):
    best = ''
    for f in range(3):
        p = ''.join(CODE.get(s[i:i + 3], 'X') for i in range(f, len(s) - 2, 3))
        for seg in p.split('*'):
            k = seg.find('M')
            if k >= 0 and len(seg) - k > len(best): best = seg[k:]
    return best
H = '[AVILMFWYGSTC]'
MOT = {'K': r'[TSC][VIT]G[YF]G', 'S4': r'(?=[RK]'+H+'{2}[RK]'+H+'{2}[RK]'+H+'{2}[RK]'+H+'{2}[RK])', 'CL': r'C.{4,6}[FY]P[FYW]D.{3}C'}
TRUE = {'K': r'^(KCN[ABCDFGHJKNQSTUV]\d|HCN\d)', 'S4': r'^(SCN\d|CACNA1|KCN[ABCDFGHQSV]|HCN|TPCN|CATSPER\d)', 'CL': r'^(CHRN|GABR|GLR[AB]|HTR3|ZACN)'}
genes = {}
for path in sys.argv[1:]:
    for blk in gzip.open(path, 'rt').read().split('>')[1:]:
        h, _, s = blk.partition('\n'); acc = h.split()[0]
        if not acc.startswith('NM_'): continue
        m = re.search(r'\(([A-Za-z0-9\-\.]+)\)', h); g = m.group(1) if m else acc
        num = int(re.sub(r'\D', '', acc.split('.')[0]))
        if g not in genes or num < genes[g][0]: genes[g] = (num, s.replace('\n', '').upper())
print("genes:", len(genes)); HITS = {}
for k, pat in MOT.items():
    hits = set(); fam = set(g for g in genes if re.match(TRUE[k], g))
    for g, (_, s) in genes.items():
        p = orf(s)
        n = len(re.findall(pat, p))
        if n >= 1: hits.add(g)
    tp = hits & fam
    print("%-3s hits %4d | family genes present %3d | recall %3d/%-3d | precision %3d/%-3d | false: %s" %
          (k, len(hits), len(fam), len(tp), len(fam), len(tp), len(hits), ' '.join(sorted(hits - fam)[:15])))
    print("     missed:", ' '.join(sorted(fam - hits)[:20]))
    HITS[k] = hits
both = HITS['K'] & HITS['S4']; vgk = set(g for g in genes if re.match(r'^(KCN[ABCDFGHQSV]\d|HCN\d)', g))
print("K+S4 combined (voltage-gated K pore): hits %d, true %d, precision %d/%d, recall %d/%d | false: %s" % (len(both), len(both & vgk), len(both & vgk), len(both), len(both & vgk), len(vgk), ' '.join(sorted(both - vgk))))
