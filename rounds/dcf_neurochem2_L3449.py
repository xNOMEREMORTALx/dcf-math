"""dcf_neurochem2 (L3449): nerve chemistry by metal, label-free, on RefSeq mRNA (NM_ AND XM_; per gene the longest ATG ORF).
Runs, unchanged: v4 channel rule + iGluR finder of rounds/dcf_neurochem_L3437.py; K2P rule of rounds/dcf_k2p_L3425.py.
New/corrected: NMDA7 'ASYTANL' (was 'ASYTAN', chance hit in cars2, L3445); FeHyd2 '[CV]HE[LI]LGH' (fish th, L3441);
P-type pumps by metal from rounds/dcf_pump_L3449.py.
Mode 'tool' prints accession | class (no names, no descriptions); 'grade' adds symbol and description.
Usage: python3 -I dcf_neurochem2_L3449.py tool|grade file.rna.fna.gz [...]   Author: Gary NOMEREMORTAL Mason (DCF)."""
import gzip, re, sys, os, runpy
_d = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_d, 'dcf_neurochem_L3437.py')).read().split("if __name__")[0])
pump_class = runpy.run_path(os.path.join(_d, 'dcf_pump_L3449.py'))['pump_class']
def is_k2p(p): return len(p) < 700 and not re.search(S4, p) and len(re.findall(r'T[VIT]G[YFL]G', p)) >= 2
def calls(p):
    out = []
    _, _, c = classify(p)
    if c: out.append(c)
    if is_k2p(p): out.append('K2P')
    for tag, pat in (('iGluR', 'YTANLAA'), ('NMDA', 'ASYTANL'), ('FeHyd', '[CV]HE[LI]LGH')):
        if re.search(pat, p): out.append(tag)
    pc = pump_class(p)
    if pc: out.append('pump_' + pc)
    return out
if __name__ == '__main__':
    mode = sys.argv[1]; best = {}
    for path in sys.argv[2:]:
        for blk in gzip.open(path, 'rt').read().split('>')[1:]:
            h, _, s = blk.partition('\n'); acc = h.split()[0]
            if not acc.startswith(('NM_', 'XM_')): continue
            m = re.findall(r'\(([A-Za-z0-9\-\.:]+)\)', h); g = m[-1] if m else acc
            p = orf(s.replace('\n', '').upper())
            if g not in best or len(p) > len(best[g][1]): best[g] = (acc, p, h)
    print('genes:', len(best))
    rows = []
    for g, (acc, p, h) in best.items():
        for c in calls(p): rows.append((c, acc, len(p), g, h.split(' ', 1)[1][:110] if ' ' in h else ''))
    for c, acc, n, g, d in sorted(rows):
        print('%-10s %-16s %5d aa' % (c, acc, n) + ('  %s  | %s' % (g, d) if mode == 'grade' else ''))
