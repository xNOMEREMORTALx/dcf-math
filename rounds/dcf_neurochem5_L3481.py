"""dcf_neurochem5 (L3481) = v7 (v6 + sodium lysine loop decides first in the 4-domain branch) nerve chemistry by metal, label-free. Input: RefSeq mRNA FASTA (.gz; NM_/XM_, longest ORF per gene)
or a UniProt TSV (.tsv/.tsv.gz with a 'Sequence' column; the tool reads ONLY Entry and Sequence).
Changes from v4/L3449 (developed on human, mouse, zebrafish, chicken, fly; rounds/L3469_dev.txt):
 - 4-domain branch only if >= 1500 aa AND full S4 AND (calcium ring >= 3 or sodium lysine loop); otherwise 1-domain branch
   (fly Shab, 1607 aa, was misfiled);
 - weak-sensor route also accepts the HCN filter C-I-G-Y-G (fly Ih was missed);
 - K2P: < 1100 aa, no S4, >= 2 filters [TS]-[TSV]-[IVT]-G-[YFL]-G (fly leak channels);
 - iron hydroxylase core: [CVI]-H-E-[LI]-[LM]-G-H (fly ple I-H-E-L-L-G-H, Hn C-H-E-L-M-G-H);
 - NMDA finder dropped (not specific outside vertebrates, L3465); iGluR Y-T-A-N-L-A-A kept; pumps as dcf_pump_L3449.
Usage: python3 -I dcf_neurochem3_L3469.py tool|grade file   Author: Gary NOMEREMORTAL Mason (DCF). Not for medical use."""
import gzip, re, sys, os, runpy
_d = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_d, 'dcf_neurochem_L3437.py')).read().split("if __name__")[0])
pump_class = runpy.run_path(os.path.join(_d, 'dcf_pump_L3477.py'))['pump_class']
LYS = r'[TS][FY][KR][GA]W'
def weak(p):
    return bool(re.search(r'(?=[RK]..[RK]..[RK]..[RK])', p)) or any(sum(x in 'RK' for x in m.groups()) == 4
               for m in re.finditer(r'(?=([RKQ])..([RKQ])..([RKQ])..([RKQ])..([RKQ]))', p))
def chan5(p):
    s4 = bool(re.search(S4, p)); r = len(re.findall(RING, p)); lys = bool(re.search(LYS, p))
    kv7 = len(p) < 1500 and re.search(r'(?=R..Q..R..[RH])', p) and re.search(r'[TS][VI]GYGD', p)
    if not (s4 or kv7) and re.search(r'[TS][VI]GYGD|SVGFGN|CIGYG', p): kv7 = weak(p)
    if not (s4 or kv7): return None
    if len(p) >= 1500 and s4 and (r >= 3 or lys):
        if lys: return 'Na'   # v7: rat/horse Scn4a carry extra off-pore ring matches (S-N-D-T-W repeats), L3481
        return 'Ca' if r >= 3 else 'undecided'
    if 'CIGYG' in p: return 'HCN'
    if re.search(r'[TSC][VITL]G[YF]G', p): return 'K'
    return 'other'
def k2p5(p): return len(p) < 1100 and not re.search(S4, p) and len(re.findall(r'[TS][TSV][IVT]G[YFL]G', p)) >= 2
def calls(p):
    out = []; c = chan5(p)
    if c: out.append(c)
    if k2p5(p): out.append('K2P')
    if 'YTANLAA' in p: out.append('iGluR')
    if re.search(r'[CVI]HE[LI][LM]GH', p): out.append('FeHyd')
    pc = pump_class(p)
    if pc: out.append('pump_' + pc)
    return out
def read(path):
    op = gzip.open if path.endswith('.gz') else open
    txt = op(path, 'rt', errors='replace').read()
    if txt.startswith('>'):
        best = {}
        for blk in txt.split('>')[1:]:
            h, _, s = blk.partition('\n'); acc = h.split()[0]
            if not acc.startswith(('NM_', 'XM_')): continue
            m = re.findall(r'\(([A-Za-z0-9\-\.:]+)\)', h); g = m[-1] if m else acc
            p = orf(s.replace('\n', '').upper())
            if g not in best or len(p) > len(best[g][1]): best[g] = (acc, p)
        return [(a, p, g) for g, (a, p) in best.items()]
    lines = txt.splitlines(); hdr = lines[0].split('\t'); ia = hdr.index('Entry'); isq = hdr.index('Sequence')
    return [(f[ia], f[isq], f[ia]) for f in (l.split('\t') for l in lines[1:]) if len(f) > isq]
if __name__ == '__main__':
    mode, path = sys.argv[1], sys.argv[2]; rows = []
    items = read(path); print('proteins:', len(items))
    for acc, p, g in items:
        for c in calls(p): rows.append((c, acc, len(p), g))
    for c, acc, n, g in sorted(rows): print('%-10s %-16s %5d aa' % (c, acc, n) + ('  ' + g if mode == 'grade' else ''))
