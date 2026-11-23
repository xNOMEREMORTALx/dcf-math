"""L3981 grader."""
import re, sys
P = {(g, f): float(p) for g, f, p in re.findall(r'GROUP (\S) FAM (\S+) scored \d+ T_obs [\d.]+ null mean [\d.]+ diff [+-][\d.]+ p_upper [\d.]+ p_lower ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('Q1', 'PASS' if P[('A', 'KPORE')] < 0.05 else 'FAIL')])
