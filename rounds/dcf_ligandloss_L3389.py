"""dcf_ligandloss_L3389.py - iron-ligand loss in DNA-repair glycosylases. For each annotated CDS whose /product matches
endonuclease III (not '... domain-containing') or 'A/G-specific adenine glycosylase' (MutY), report its length, total cysteines and whether
it carries the [4Fe-4S] FCL loop C-x6-C-x2-C-x5-C (from the annotated /translation). Annotation identifies the enzyme; the outcome measured is
cysteine content. Usage: python3 -I dcf_ligandloss_L3389.py genome.gb    Author: Gary NOMEREMORTAL Mason (DCF). Frozen L3389."""
import re, sys
t = open(sys.argv[1]).read().split('\nORIGIN')[0]
rows = []
for feat in re.split(r'\n     CDS             ', t)[1:]:
    ff = feat.replace('\n                     ', ' ')
    pr = re.search(r'/product="([^"]+)"', ff); tr = re.search(r'/translation="([^"]+)"', ff)
    if not pr or not tr: continue
    p = pr.group(1).lower()
    if re.search(r'endonuclease iii(?! domain)', p): enz = 'EndoIII'
    elif 'a/g-specific adenine glycosylase' in p: enz = 'MutY'
    else: continue
    s = tr.group(1).replace(' ', '')
    rows.append((enz, len(s), s.count('C'), bool(re.search(r'C.{6}C..C.{5}C', s))))
for r in rows: print("%s len %d cysteines %d FCL %s" % r)
print("SUMMARY proteins %d with_FCL %d cysteines %s" % (len(rows), sum(r[3] for r in rows), ','.join(str(r[2]) for r in rows)))
