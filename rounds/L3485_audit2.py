"""L3485 [Audit 2]: recompute the Manuscript 2 tally from committed grade outputs (no hand numbers)."""
import re, ast
F = [('mouse', 'L3429_grade_output.txt'), ('zebrafish curated', 'L3441_grade_output.txt'), ('zebrafish predicted', 'L3445_grade_output.txt'),
     ('chicken', 'L3457_grade_output.txt'), ('fruit fly', 'L3465_grade_output.txt'), ('nematode', 'L3473_grade_output.txt'),
     ('all other animals', 'L3481_grade_output.txt'), ('Na/Ca decision (TrEMBL)', 'L3489_grade_output.txt'), ('before nerves', 'L3501_grade_output.txt'), ('comb jellies', 'L3509_grade_output.txt'), ('E->K dating', 'L3533_grade_output.txt'), ('kit + chordate K', 'L3557_grade_output.txt'), ('NAV1/NAV2 family', 'L3561_grade_output.txt'), ('earliest channel family', 'L3565_grade_output.txt'), ('NAV1/NAV2 by alignment', 'L3569_grade_output.txt'), ('naming unnamed genes', 'L3577_grade_output.txt'), ('comb-jelly naming (local)', 'L3585_grade_output.txt'), ('anemone naming', 'L3589_grade_output.txt'), ('battery ratio', 'L3613_grade_output.txt'), ('sea-hare NMDA', 'L3617_grade_output.txt'), ('tardigrade 2', 'L3621_grade_output.txt'), ('NR1 tree', 'L3625_grade_output.txt'), ('moulting Na', 'L3629_grade_output.txt'), ('spiralia v3', 'L3637_grade_output.txt'), ('rotifers', 'L3645_grade_output.txt'), ('NALCN rings', 'L3653_grade_output.txt'), ('CCH1 + worm NALCN', 'L3661_grade_output.txt'), ('placozoan H2', 'L3669_grade_output.txt'), ('neural kit', 'L3677_grade_output.txt'), ('flatworms', 'L3689_grade_output.txt'), ('trematode vs cestode', 'L3701_grade_output.txt'), ('CTCF tree', 'L3701_ctcf_grade_output.txt'), ('DCF numbers in 4DN', 'L3705_grade_output.txt'), ('cohesin control', 'L3713_cohesin_grade_output.txt'), ('channel genes at loops', 'L3717_grade_output.txt'), ('channel loops robustness', 'L3721_grade_output.txt'), ('channel loops permutation', 'L3725_grade_output.txt'), ('channel loop partners', 'L3729_grade_output.txt'), ('selenium and zinc', 'L3733_grade_output.txt'), ('HD DNA retrieval', 'L3737_grade_output.txt'), ('HD tuning', 'L3741_grade_output.txt'), ('6-mer DNA index blind', 'L3745_grade_output.txt'), ('S4 gear teeth', 'L3749_grade_output.txt'), ('cryptochrome tetrad', 'L3753_grade_output.txt'), ('cryptochrome tree', 'L3757_grade_output.txt'), ('cryptochrome full scan', 'L3761_grade_output.txt'), ('cryptochrome outgroups', 'L3769_grade_output.txt')]
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
