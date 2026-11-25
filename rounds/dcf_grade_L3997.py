"""L3997 grader."""
import re, sys
P = {(g, f): float(p) for g, f, p in re.findall(r'GROUP (\S) FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ excess [+-][\d.]+ p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('O1', 'PASS' if P[('A', 'OXPHOS')] >= 0.05 else 'FAIL'), ('O2', 'PASS' if P[('B', 'OXPHOS')] >= 0.05 else 'FAIL')])
