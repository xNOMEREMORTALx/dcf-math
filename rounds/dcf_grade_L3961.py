"""L3961 grader. argv: HIC9=path TCELL=path."""
import re, sys
P = {}
for a in sys.argv[1:]:
    k, p = a.split('=', 1); P[k] = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', open(p).read())}; print(k, P[k])
print('RESULT', [('Z1', 'PASS' if P['HIC9']['KPORE'] < 0.05 else 'FAIL'), ('Z2', 'PASS' if P['TCELL']['KPORE'] < 0.05 else 'FAIL')])
