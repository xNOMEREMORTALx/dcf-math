"""L3949 grader."""
import re, sys
P = {f: (float(e), float(p)) for g, f, e, p in re.findall(r'GROUP (\S) FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ excess ([+-][\d.]+) p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('V1', 'PASS' if P['KPORE'][1] < 0.05 else 'FAIL'), ('V2', 'PASS' if P['nonKv'][0] > P['Kv'][0] else 'FAIL'),
                 ('V3', 'PASS' if P['nonKv'][1] < 0.05 else 'FAIL')])
