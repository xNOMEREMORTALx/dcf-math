"""dcf_campbell_L3321.py - per genome: whole-proteome 3-3-4 ladder /1000 aa, ladders in large proteins (>200 aa) /1000 aa,
and Campbell-style small ferredoxin genes (proteins <= 200 aa with >= 1 ladder) /1000 genes. Gene calls: dcf_genefinder_mobile.py v2.32.
Usage: python3 -I dcf_campbell_L3321.py genome.gb pred.gff3     Author: Gary NOMEREMORTAL Mason (DCF). Frozen L3321."""
import sys, re
sys.path.insert(0, '/home/claude/dcf-genefinder'); import dcf_redox as R
n = aa = lad = small = big = 0
for p in R.proteins(R.read_seq(sys.argv[1]), sys.argv[2]):
    n += 1; aa += len(p); c = len(re.findall(r'(?=C..C..C...C)', p)); lad += c
    if len(p) <= 200:
        small += bool(c)
    else:
        big += c
print("ladder %.4f | large_ladder %.4f | small_fd_genes %.4f | genes %d | aa %d" % (1000*lad/aa, 1000*big/aa, 1000*small/n, n, aa))
