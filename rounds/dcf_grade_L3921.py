"""L3921 grader. argv: tool output."""
import re, sys
import numpy as np
t = open(sys.argv[1]).read()
cov = {g: np.median([int(c) for c in re.findall(r'MAP %s \S+ anchors \d+ coverage_bp (\d+)' % g, t)]) for g in 'AN'}; print('median coverage', cov)
P = {(g, f): float(p) for g, f, p in re.findall(r'GROUP (\S) FAM (\S+) T_obs [\d.]+ null mean [\d.]+ p_upper ([\d.]+)', t)}; print(P)
print('RESULT', [('W1', 'PASS' if cov['N'] > cov['A'] else 'FAIL'), ('W2', 'PASS' if P[('N', 'KPORE')] < 0.05 else 'FAIL'),
                 ('W3', 'PASS' if P[('A', 'KPORE')] < 0.05 else 'FAIL')])
