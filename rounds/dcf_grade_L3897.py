"""L3897 grader. argv: HIC=path CHIA=path."""
import re, sys
P = {}
for arg in sys.argv[1:]:
    k, p = arg.split('=', 1)
    P[k] = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', open(p).read())}; print(k, P[k])
print('RESULT', [('A1', 'PASS' if P['CHIA']['KCN'] < 0.05 else 'FAIL'), ('A2', 'PASS' if P['HIC']['KCN'] < 0.05 else 'FAIL'),
                 ('A3', 'PASS' if P['HIC']['ALL'] < 0.05 else 'FAIL')])
