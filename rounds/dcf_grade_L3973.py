"""L3973 grader."""
import re, sys
P = {(g, f): float(p) for g, f, p in re.findall(r'GROUP (\S) FAM (\S+) scored \d+ T_obs [\d.]+ null mean [\d.]+ diff [+-][\d.]+ p_upper [\d.]+ p_lower ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('N2', 'PASS' if P[('A', 'KPORE')] < 0.05 else 'FAIL'), ('N1', 'PASS' if P[('B', 'KPORE')] < 0.05 else 'FAIL')])
