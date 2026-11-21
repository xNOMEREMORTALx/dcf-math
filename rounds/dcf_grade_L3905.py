"""L3905 grader. argv: BOTH=path NONE=path."""
import re, sys
P = {}
for arg in sys.argv[1:]:
    k, p = arg.split('=', 1)
    P[k] = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', open(p).read())}; print(k, P[k])
print('RESULT', [('B1', 'PASS' if P['BOTH']['KPORE'] < 0.05 else 'FAIL'), ('B2', 'PASS' if P['NONE']['KPORE'] >= 0.05 else 'FAIL'),
                 ('B3', 'PASS' if P['BOTH']['KCN'] < 0.05 else 'FAIL')])
