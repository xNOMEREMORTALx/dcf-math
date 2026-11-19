"""L3869 grader (R1-R4)."""
import re, sys
P = {f: (float(u), float(l)) for f, u, l in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+) p_lower ([\d.]+)', open(sys.argv[1]).read())}
print(P); assert len(open(sys.argv[1]).read().split('cell ')) == 11
print('RESULT', [('R1', 'PASS' if P['KCN'][0] < 0.05 else 'FAIL'), ('R2', 'PASS' if P['GRIN'][0] < 0.05 else 'FAIL'),
                 ('R3', 'PASS' if P['CACNA1'][1] < 0.05 else 'FAIL'), ('R4', 'PASS' if P['ALL'][0] < 0.01 else 'FAIL')])
