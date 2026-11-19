"""L3873 grader (Q1-Q4)."""
import re, sys
T = open(sys.argv[1]).read()
P = {f: (float(o), float(m), float(u)) for f, o, m, u in re.findall(r'FAM (\S+) n \d+ T_obs ([\d.]+) null mean ([\d.]+) sd [\d.]+ p_upper ([\d.]+)', T)}
print(P); assert T.count('cell ') == 10
R = [('Q1', 'PASS' if P['GLUR'][2] < 0.05 else 'FAIL'), ('Q2', 'PASS' if P['Kv'][2] < 0.05 else 'FAIL'),
     ('Q3', 'PASS' if sum(P[f][0] > P[f][1] for f in ('Kv', 'K2P', 'Kir', 'KCa')) >= 3 else 'FAIL'), ('Q4', 'PASS' if P['Kaux'][0] > P['Kaux'][1] else 'FAIL')]
print('RESULT', R)
