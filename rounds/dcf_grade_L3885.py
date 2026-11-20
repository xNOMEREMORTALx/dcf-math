"""L3885 grader (Y1-Y4)."""
import re, sys
T = open(sys.argv[1]).read(); assert T.count('cell ') == 10
P = {f: (float(o), float(m), float(u)) for f, o, m, u in re.findall(r'FAM (\S+) n \d+ T_obs ([\d.]+) null mean ([\d.]+) sd [\d.]+ p_upper ([\d.]+)', T)}; print(P)
D = [P[f][0] - P[f][1] for f in ('TRI', 'TETRA', 'PENTA', 'HEXA')]; print('Delta by order 3,4,5,6:', ['%+.4f' % d for d in D])
mono = all(a < b for a, b in zip(D, D[1:])) or all(a > b for a, b in zip(D, D[1:]))
print('RESULT', [('Y1', 'PASS' if P['PENTA'][2] < 0.05 else 'FAIL'), ('Y2', 'PASS' if P['TRI'][2] < 0.05 else 'FAIL'),
                 ('Y3', 'PASS' if P['HEXA'][2] < 0.05 else 'FAIL'), ('Y4', 'PASS' if mono else 'FAIL')])
