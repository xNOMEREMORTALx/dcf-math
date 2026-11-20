"""L3889 grader. argv: N=path P=path L=path (missing -> ungradeable)."""
import re, sys
R = []; have = {}
for arg in sys.argv[1:]:
    k, p = arg.split('=', 1); T = open(p).read()
    have[k] = (T.count('cell '), {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', T)}); print(k, have[k])
g = lambda k, need: k in have and have[k][0] >= need
R += [('N1', 'PASS' if have['N'][1]['KCN'] < 0.05 else 'FAIL') if g('N', 2) else ('N1', 'ungradeable'),
      ('N2', 'PASS' if have['N'][1]['ALL'] < 0.05 else 'FAIL') if g('N', 2) else ('N2', 'ungradeable'),
      ('P1', 'PASS' if have['P'][1]['KCN'] >= 0.05 else 'FAIL') if g('P', 1) else ('P1', 'ungradeable'),
      ('L1', 'PASS' if have['L'][1]['KCN'] < 0.05 else 'FAIL') if g('L', 1) else ('L1', 'ungradeable')]
print('RESULT', R)
