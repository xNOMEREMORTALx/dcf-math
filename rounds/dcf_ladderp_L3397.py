"""dcf_ladderp_L3397.py - protein FASTA (.gz ok): plain ladder C..C..C...C and Ladder-P C..C..C...CP, both counted OVERLAPPING, per 1000 aa.
Usage: python3 -I dcf_ladderp_L3397.py proteins.fasta[.gz]    Author: Gary NOMEREMORTAL Mason (DCF). Frozen L3397."""
import gzip, re, sys
op = gzip.open if sys.argv[1].endswith('gz') else open
aa = x = y = 0; org = ''
for b in op(sys.argv[1], 'rt').read().split('>')[1:]:
    h, _, s = b.partition('\n'); s = re.sub(r'\s', '', s)
    if not org:
        m = re.search(r'OS=(.*?) OX=', h); org = m.group(1) if m else h[:40]
    aa += len(s); x += len(re.findall(r'(?=C..C..C...C)', s)); y += len(re.findall(r'(?=C..C..C...CP)', s))
print("%s | aa %d | plain_ov %.4f | ladderP %.4f" % (org, aa, 1000.0 * x / aa, 1000.0 * y / aa))
