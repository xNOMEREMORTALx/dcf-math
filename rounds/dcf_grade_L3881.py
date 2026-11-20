"""L3881 grader. argv: PART=path for A and B outputs (either may be missing -> ungradeable)."""
import re, sys
R = []
for arg in sys.argv[1:]:
    part, p = arg.split('=', 1); T = open(p).read(); n = T.count('cell ')
    P = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', T)}; print(part, 'cells', n, P)
    if n < 2: R += [(part + '1', 'ungradeable'), (part + '2', 'ungradeable')]; continue
    if part == 'A': R += [('A1', 'PASS' if P['KCN'] >= 0.05 else 'FAIL'), ('A2', 'PASS' if P['ALL'] >= 0.05 else 'FAIL')]
    else: R += [('B1', 'PASS' if P['KCN'] < 0.05 else 'FAIL'), ('B2', 'PASS' if P['ALL'] < 0.05 else 'FAIL')]
print('RESULT', R)
