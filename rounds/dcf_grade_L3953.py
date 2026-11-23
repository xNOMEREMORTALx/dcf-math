"""L3953 grader. argv: BOTH=path ALL=path."""
import re, sys
P = {}
for a in sys.argv[1:]:
    k, p = a.split('=', 1); P[k] = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', open(p).read())}; print(k, P[k])
print('RESULT', [('X1', 'PASS' if P['BOTH']['KPORE'] >= 0.05 else 'FAIL'), ('X2', 'PASS' if P['ALL']['KPORE'] >= 0.05 else 'FAIL'),
                 ('X3', 'PASS' if P['BOTH']['ALL'] >= 0.05 else 'FAIL')])
