"""dcf_infoiron_L3377.py - per genome: 'information iron' proteins (EndoIII/MutY FCL loop C-x6-C-x2-C-x5-C, count of proteins) and
'energy iron' (3-3-4 ladders) per 1000 predicted genes. Gene calls: dcf_genefinder_mobile.py v2.32.
Usage: python3 -I dcf_infoiron_L3377.py genome.gb pred.gff3    Author: Gary NOMEREMORTAL Mason (DCF). Frozen L3377."""
import sys, re
sys.path.insert(0, '/home/claude/dcf-genefinder'); import dcf_redox as R
n = lad = fcl = 0
for p in R.proteins(R.read_seq(sys.argv[1]), sys.argv[2]):
    n += 1; lad += len(re.findall(r'(?=C..C..C...C)', p)); fcl += bool(re.search(r'C.{6}C..C.{5}C', p))
print("genes %d | FCL_proteins %d | FCL_per_1000_genes %.3f | ladder_per_1000_genes %.3f" % (n, fcl, 1000.0 * fcl / n, 1000.0 * lad / n))
