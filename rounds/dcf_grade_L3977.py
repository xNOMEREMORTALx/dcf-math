"""L3977/L3979 grader. argv: TCELL=path HIC9=path NEW=path."""
import re, sys
P = {}
for a in sys.argv[1:]:
    k, p = a.split('=', 1); t = open(p).read()
    P[k] = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ (?:sd [\d.]+|excess [+-][\d.]+) p_upper ([\d.]+)', t)}; print(k, P[k])
print('RESULT', [('P1', 'PASS' if P['TCELL']['KPORE'] < 0.05 else 'FAIL'), ('P2', 'PASS' if P['HIC9']['KPORE'] < 0.05 else 'FAIL'),
                 ('P3', 'PASS' if P['NEW']['KPORE'] >= 0.05 else 'FAIL')])
