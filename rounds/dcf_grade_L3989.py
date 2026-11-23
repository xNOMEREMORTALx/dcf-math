"""L3989 grader."""
import re, sys
P = {(g, f): float(p) for g, f, p in re.findall(r'GROUP (\S) FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ excess [+-][\d.]+ p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('H1', 'PASS' if P[('A', 'HEXA')] < 0.05 else 'FAIL'), ('H2', 'PASS' if P[('B', 'HEXA')] < 0.05 else 'FAIL')])
