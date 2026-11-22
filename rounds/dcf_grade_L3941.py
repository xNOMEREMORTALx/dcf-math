"""L3941 grader."""
import re, sys
P = {(g, f): (float(e), float(p)) for g, f, e, p in re.findall(r'GROUP (\S) FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ excess ([+-][\d.]+) p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('U1', 'PASS' if all(P[('B', f)][0] > 0 for f in ('Kv', 'K2P', 'Kir', 'KCa')) else 'FAIL'),
                 ('U2', 'PASS' if P[('B', 'Kv')][1] < 0.05 else 'FAIL'), ('U3', 'PASS' if P[('B', 'Kir')][1] < 0.05 else 'FAIL')])
