"""dcf_neurochem (L3437) = dcf_neurometal v4 + glutamate receptor and iron hydroxylase finders: label-free sorting of voltage-gated channels by the METAL ION each passes.
Author: Gary NOMEREMORTAL Mason (DCF). Not for medical use.
Input: RefSeq mRNA FASTA (.fna.gz); one transcript per gene (lowest NM_ number), longest ATG ORF.
Step 1 voltage sensor S4 (frozen L3293, passed blind) must be present, OR [v3] the Kv7 sensor R-x-x-Q-x-x-R-x-x-[RH]
       together with the filter [TS]-[VI]-G-Y-G-D and length < 1500 aa (Kv7/KCNQ channels have a 4-charge sensor).
Step 2 shape and pore:
  >= 1500 aa (4 domains): count the calcium ring  [TS]-x-[ED]-x-W  (one E/D per pore loop)
       sodium lysine loop [TS]-[FY]-[KR]-[GA]-W (the K of DEKA) AND ring <= 2 -> Na   [v3: was ring <= 1; Scn4a has an extra
                                                                                    ring match outside the pore, L3429]
       else ring >= 3 -> Ca (calcium channel, EEEE/EEDD ring); otherwise undecided
       == 2  -> undecided
  < 1500 aa: C-I-G-Y-G -> HCN (K/Na pacemaker); else [TSC]-[VITL]-G-[YF]-G (k_filter2) -> K; else other
Gene key = LAST parenthesis in the header [A1: v1 took the first, merging all mouse Kcnh genes under '(eag-related)'].
[v4] weak-sensor route (< 1500 aa, no S4): filter [TS][VI]GYGD (Kv7, Kv6) or S-V-G-F-G-N (EAG/ERG/ELK) AND either
       4 charges at spacing 3 or 5 positions [RKQ] at spacing 3 with 4 of them R/K.  -> then classed as before (HCN/K).
Extra finders (independent of channels):
  iGluR  Y-T-A-N-L-A-A (SYTANLAAF gate of all ionotropic glutamate receptors)
  NMDA   A-S-Y-T-A-N (NMDA receptors GluN1/GluN2: the Mg-blocked, Ca-passing learning receptor)
  FeHyd  C-H-E-[LI]-L-G-H (iron site of the aromatic amino-acid hydroxylases: TH -> dopamine, TPH -> serotonin, PAH)
Mode 'tool': prints accession | aa | S4 | ring | class, NO gene names.  Mode 'grade': adds gene names.
Usage: python3 -I dcf_neurometal_L3425.py tool|grade file1.rna.fna.gz [...]"""
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
S4 = r'(?=[RK]' + H + '{2}[RK]' + H + '{2}[RK]' + H + '{2}[RK]' + H + '{2}[RK])'
RING = r'(?=[TS].[ED].W)'
def classify(p):
    s4 = len(re.findall(S4, p))
    kv7 = len(p) < 1500 and re.search(r'(?=R..Q..R..[RH])', p) and re.search(r'[TS][VI]GYGD', p)
    if not (s4 or kv7) and len(p) < 1500 and re.search(r'[TS][VI]GYGD|SVGFGN', p):   # v4 weak-sensor route
        kv7 = re.search(r'(?=[RK]..[RK]..[RK]..[RK])', p) or any(sum(x in 'RK' for x in m.groups()) == 4
              for m in re.finditer(r'(?=([RKQ])..([RKQ])..([RKQ])..([RKQ])..([RKQ]))', p))
    if not (s4 or kv7): return s4, 0, None
    r = len(re.findall(RING, p))
    if len(p) >= 1500:
        if re.search(r'[TS][FY][KR][GA]W', p) and r <= 2: return s4, r, 'Na'
        return s4, r, 'Ca' if r >= 3 else 'undecided'
    if 'CIGYG' in p: return s4, r, 'HCN'
    if re.search(r'[TSC][VITL]G[YF]G', p): return s4, r, 'K'
    return s4, r, 'other'
if __name__ == '__main__':
    mode = sys.argv[1]; genes = {}
    for path in sys.argv[2:]:
        for blk in gzip.open(path, 'rt').read().split('>')[1:]:
            h, _, s = blk.partition('\n'); acc = h.split()[0]
            if not acc.startswith('NM_'): continue
            m = re.findall(r'\(([A-Za-z0-9\-\.]+)\)', h); g = m[-1] if m else acc
            num = int(re.sub(r'\D', '', acc.split('.')[0]))
            if g not in genes or num < genes[g][0]: genes[g] = (num, acc, s.replace('\n', '').upper())
    print('genes:', len(genes))
    rows = []
    for g, (_, acc, s) in genes.items():
        p = orf(s); s4, r, c = classify(p)
        if c: rows.append((c, acc, len(p), s4, r, g))
        for tag, pat in (('iGluR', 'YTANLAA'), ('NMDA', 'ASYTAN'), ('FeHyd', 'CHE[LI]LGH')):
            if re.search(pat, p): rows.append((tag, acc, len(p), s4, 0, g))
    for c, acc, n, s4, r, g in sorted(rows):
        print('%-9s %-14s %5d aa  S4 x%d  ring %d' % (c, acc, n, s4, r) + ('  ' + g if mode == 'grade' else ''))
