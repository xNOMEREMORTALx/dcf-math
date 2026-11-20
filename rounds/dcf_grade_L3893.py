"""L3893 grader. argv: M=path H=path C=path (missing -> ungradeable)."""
import re, sys
have = {}
for arg in sys.argv[1:]:
    k, p = arg.split('=', 1); T = open(p).read()
    have[k] = (T.count('cell '), {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', T)}); print(k, have[k])
ok = lambda k: k in have and have[k][0] >= 1
g = lambda k, f: ('PASS' if have[k][1][f] >= 0.05 else 'FAIL') if ok(k) else 'ungradeable'
print('RESULT', [('E1', g('M', 'KCN')), ('E2', g('H', 'KCN')), ('E3', g('C', 'KCN')), ('E4', g('M', 'ALL'))])
