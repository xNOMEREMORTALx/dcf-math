"""L3877 grader (T1-T4). argv: tool output."""
import re, sys
T = open(sys.argv[1]).read(); n = T.count('cell ')
P = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', T)}; print('cells', n, P)
if n < 3: print('RESULT', [(k, 'ungradeable') for k in ('T1', 'T2', 'T3', 'T4')]); sys.exit()
print('RESULT', [('T1', 'PASS' if P['KCN'] < 0.05 else 'FAIL'), ('T2', 'PASS' if P['ALL'] < 0.05 else 'FAIL'),
                 ('T3', 'PASS' if P['KPORE'] < 0.05 else 'FAIL'), ('T4', 'PASS' if P['Kaux'] >= 0.05 else 'FAIL')])
