"""L3913 grader. argv: tool output path."""
import re, sys
P = {f: float(u) for f, u in re.findall(r'FAM (\S+) n \d+ T_obs [\d.]+ null mean [\d.]+ sd [\d.]+ p_upper ([\d.]+)', open(sys.argv[1]).read())}; print(P)
print('RESULT', [('D1', 'PASS' if P['KPORE'] < 0.05 else 'FAIL'), ('D2', 'PASS' if P['KCN'] < 0.05 else 'FAIL')])
