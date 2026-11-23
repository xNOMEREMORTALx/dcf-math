"""L3965 grader."""
import re, sys
P = {(g, f): float(p) for g, f, p in re.findall(r'GROUP (\S) FAM (\S+) scored \d+ T_obs [\d.]+ null mean [\d.]+ diff [+-][\d.]+ p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('L1', 'PASS' if P[('A', 'KPORE')] < 0.05 else 'FAIL'), ('L2', 'PASS' if P[('B', 'KPORE')] < 0.05 else 'FAIL'),
                 ('L3', 'PASS' if P[('A', 'Kaux')] >= 0.05 else 'FAIL')])
