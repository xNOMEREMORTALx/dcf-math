"""dcf_neurochem_xm (L3445): run the FROZEN rules of rounds/dcf_neurochem_L3437.py (v4 channels + iGluR/NMDA/FeHyd)
and rounds/dcf_k2p_L3425.py on PREDICTED (XM_) RefSeq transcripts, plus one new finder FeHyd2 = [CV]HE[LI]LGH.
Per gene (last parenthesis in the header): the transcript variant with the LONGEST ATG ORF.
Genes whose symbol also occurs in any NM_ record of the files given with --exclude are skipped (already graded).
Usage: python3 -I dcf_neurochem_xm_L3445.py tool|grade xm_file.fna.gz [--exclude nm_file.fna.gz ...]
Author: Gary NOMEREMORTAL Mason (DCF). Not for medical use."""
import gzip, re, sys, os
_d = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(_d, 'dcf_neurochem_L3437.py')).read().split("if __name__")[0])
K2P_F = r'T[VIT]G[YFL]G'
def is_k2p(p): return len(p) < 700 and not re.search(S4, p) and len(re.findall(K2P_F, p)) >= 2
if __name__ == '__main__':
    a = sys.argv[1:]; mode = a[0]; ex = []
    if '--exclude' in a: i = a.index('--exclude'); ex = a[i + 1:]; a = a[:i]
    skip = set()
    for f in ex:
        for line in gzip.open(f, 'rt'):
            if line.startswith('>NM_'):
                m = re.findall(r'\(([A-Za-z0-9\-\.:]+)\)', line)
                if m: skip.add(m[-1])
    best = {}
    for blk in gzip.open(a[1], 'rt').read().split('>')[1:]:
        h, _, s = blk.partition('\n'); acc = h.split()[0]
        if not acc.startswith('XM_'): continue
        m = re.findall(r'\(([A-Za-z0-9\-\.:]+)\)', h); g = m[-1] if m else acc
        if g in skip: continue
        p = orf(s.replace('\n', '').upper())
        if g not in best or len(p) > len(best[g][1]): best[g] = (acc, p)
    print('genes:', len(best), '| skipped (already in NM_ files):', len(skip))
    rows = []
    for g, (acc, p) in best.items():
        s4, r, c = classify(p)
        if c: rows.append((c, acc, len(p), g))
        if is_k2p(p): rows.append(('K2P', acc, len(p), g))
        for tag, pat in (('iGluR', 'YTANLAA'), ('NMDA', 'ASYTAN'), ('FeHyd', 'CHE[LI]LGH'), ('FeHyd2', '[CV]HE[LI]LGH')):
            if re.search(pat, p): rows.append((tag, acc, len(p), g))
    for c, acc, n, g in sorted(rows):
        print('%-9s %-16s %5d aa' % (c, acc, n) + ('  ' + g if mode == 'grade' else ''))
