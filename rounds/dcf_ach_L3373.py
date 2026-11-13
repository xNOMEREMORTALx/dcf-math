"""dcf_ach_L3373.py - acetylcholine machinery, label-free, in RefSeq mRNA (one transcript per gene = lowest NM_, longest ATG ORF).
Motifs: Cys-loop C.{4,6}[FY]P[FYWM]D.{3}C (ligand-gated receptors); cholinesterase serine site FGESAG.
Families (gene symbols, case-insensitive, read only to grade): Cys-loop = CHRN*, GABR*, GLRA/GLRB*, HTR3*, ZACN; cholinesterase = ACHE, BCHE.
Usage: python3 -I dcf_ach_L3373.py file1.rna.fna.gz [file2 ...]   Author: Gary NOMEREMORTAL Mason (DCF). Frozen L3373."""
import gzip, re, sys
sys.path.insert(0, '/home/claude/dcf-genefinder'); import dcf_motif_scan as M
genes = {}
for path in sys.argv[1:]:
    for blk in gzip.open(path, 'rt').read().split('>')[1:]:
        h, _, s = blk.partition('\n'); acc = h.split()[0]
        if not acc.startswith('NM_'): continue
        m = re.search(r'\(([A-Za-z0-9\-\.]+)\)', h); g = m.group(1) if m else acc
        num = int(re.sub(r'\D', '', acc.split('.')[0]))
        if g not in genes or num < genes[g][0]: genes[g] = (num, s.replace('\n', '').upper())
P = {g: M.longest_orf(s) for g, (_, s) in genes.items()}
print("genes", len(P))
for name, pat, fam in [('CYSLOOP', r'C.{4,6}[FY]P[FYWM]D.{3}C', r'^(CHRN|GABR|GLR[AB]|HTR3|ZACN)'), ('CHE', r'FGESAG', r'^(ACHE|BCHE)$')]:
    hits = set(g for g, p in P.items() if re.search(pat, p)); F = set(g for g in P if re.match(fam, g, re.I)); tp = hits & F
    print("%s hits %d family %d found %d precision %.3f recall %.3f | hits: %s | missed: %s" % (name, len(hits), len(F), len(tp), len(tp) / max(len(hits), 1), len(tp) / max(len(F), 1), ' '.join(sorted(hits)), ' '.join(sorted(F - hits))))
