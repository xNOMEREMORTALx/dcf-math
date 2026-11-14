"""L3485 [Audit 2]: recompute the Manuscript 2 tally from committed grade outputs (no hand numbers)."""
import re, ast
F = [('mouse', 'L3429_grade_output.txt'), ('zebrafish curated', 'L3441_grade_output.txt'), ('zebrafish predicted', 'L3445_grade_output.txt'),
     ('chicken', 'L3457_grade_output.txt'), ('fruit fly', 'L3465_grade_output.txt'), ('nematode', 'L3473_grade_output.txt'),
     ('all other animals', 'L3481_grade_output.txt'), ('Na/Ca decision (TrEMBL)', 'L3489_grade_output.txt'), ('before nerves', 'L3501_grade_output.txt'), ('comb jellies', 'L3509_grade_output.txt')]
tp = tg = 0
for name, f in F:
    t = open('rounds/' + f).read()
    m = re.search(r"(?:RESULT|TOTAL):?\s*(\[.*\])", t)
    res = ast.literal_eval(m.group(1))
    res = [r[1] if isinstance(r, tuple) else r for r in res]
    p = res.count('PASS'); g = sum(r != 'ungradeable' for r in res)
    tp += p; tg += g
    print('%-22s %2d / %-2d gradeable  (%d ungradeable)' % (name, p, g, len(res) - g))
print('%-22s %2d / %-2d' % ('TOTAL', tp, tg))
