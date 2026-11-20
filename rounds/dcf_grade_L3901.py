"""L3901 grader. argv: TRIM=path MICRO=path."""
import re, sys
P = {}
for arg in sys.argv[1:]:
    k, p = arg.split('=', 1)
    P[k] = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', open(p).read())}; print(k, P[k])
print('RESULT', [('R1', 'PASS' if P['TRIM']['KCN'] < 0.05 else 'FAIL'), ('R2', 'PASS' if P['MICRO']['KCN'] < 0.05 else 'FAIL'),
                 ('R3', 'PASS' if P['MICRO']['KPORE'] < 0.05 else 'FAIL')])
