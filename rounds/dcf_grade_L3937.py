"""L3937 grader."""
import re, sys
P = {(g, f): (float(e), float(p)) for g, f, e, p in re.findall(r'GROUP (\S) FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ excess ([+-][\d.]+) p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('S1', 'PASS' if P[('A', 'TETRA4')][1] < 0.05 else 'FAIL'), ('S2', 'PASS' if P[('B', 'TETRA4')][1] < 0.05 else 'FAIL'),
                 ('S3', 'PASS' if P[('A', 'TETRA4')][0] < P[('A', 'KPORE')][0] else 'FAIL')])
