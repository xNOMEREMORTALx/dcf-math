"""L3933 grader."""
import re, sys
P = {(g, f): float(p) for g, f, p in re.findall(r'GROUP (\S) FAM (\S+) T_obs [\d.]+ null mean [\d.]+ p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('Q1', 'PASS' if P[('N', 'KPORE')] < 0.05 else 'FAIL'), ('Q2', 'PASS' if P[('T', 'KPORE')] < 0.05 else 'FAIL'),
                 ('Q3', 'PASS' if P[('A', 'KPORE')] < 0.05 else 'FAIL')])
