"""L3909 grader. argv: BOTH=path NONE=path (L3909)."""
import re, sys
P = {}
for arg in sys.argv[1:]:
    k, p = arg.split('=', 1)
    P[k] = {f: (float(u), float(lo)) for f, u, lo in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+) p_lower ([\d.]+)', open(p).read())}; print(k, P[k])
print('RESULT', [('C1', 'PASS' if P['BOTH']['KPORE'][0] < 0.05 else 'FAIL'), ('C2', 'PASS' if P['NONE']['KPORE'][0] >= 0.05 else 'FAIL'),
                 ('C3', 'PASS' if P['NONE']['ALL'][1] < 0.05 else 'FAIL')])
