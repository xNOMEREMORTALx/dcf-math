"""L3485 [Audit 2]: recompute the Manuscript 2 tally from committed grade outputs (no hand numbers)."""
import re, ast
F = [('mouse', 'L3429_grade_output.txt'), ('zebrafish curated', 'L3441_grade_output.txt'), ('zebrafish predicted', 'L3445_grade_output.txt'),
     ('chicken', 'L3457_grade_output.txt'), ('fruit fly', 'L3465_grade_output.txt'), ('nematode', 'L3473_grade_output.txt'),
     ('all other animals', 'L3481_grade_output.txt'), ('Na/Ca decision (TrEMBL)', 'L3489_grade_output.txt'), ('before nerves', 'L3501_grade_output.txt'), ('comb jellies', 'L3509_grade_output.txt'), ('E->K dating', 'L3533_grade_output.txt'), ('kit + chordate K', 'L3557_grade_output.txt'), ('NAV1/NAV2 family', 'L3561_grade_output.txt'), ('earliest channel family', 'L3565_grade_output.txt'), ('NAV1/NAV2 by alignment', 'L3569_grade_output.txt'), ('naming unnamed genes', 'L3577_grade_output.txt'), ('comb-jelly naming (local)', 'L3585_grade_output.txt'), ('anemone naming', 'L3589_grade_output.txt'), ('battery ratio', 'L3613_grade_output.txt'), ('sea-hare NMDA', 'L3617_grade_output.txt'), ('tardigrade 2', 'L3621_grade_output.txt'), ('NR1 tree', 'L3625_grade_output.txt'), ('moulting Na', 'L3629_grade_output.txt'), ('spiralia v3', 'L3637_grade_output.txt'), ('rotifers', 'L3645_grade_output.txt'), ('NALCN rings', 'L3653_grade_output.txt'), ('CCH1 + worm NALCN', 'L3661_grade_output.txt'), ('placozoan H2', 'L3669_grade_output.txt'), ('neural kit', 'L3677_grade_output.txt'), ('flatworms', 'L3689_grade_output.txt'), ('trematode vs cestode', 'L3701_grade_output.txt')]
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
