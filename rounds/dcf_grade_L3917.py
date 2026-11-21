"""L3917 grader. argv: tool output."""
import re, sys
t = open(sys.argv[1]).read(); R = {k: (float(r), float(p)) for k, r, p in re.findall(r'RHO (\S+) (\S+) p_upper (\S+)', t)}; print(R)
print('RESULT', [('G1', 'PASS' if R['A-B'][0] > 0 and R['A-B'][1] < 0.05 else 'FAIL'),
                 ('G2', 'PASS' if R['A-N'][0] > 0 and R['A-N'][1] < 0.05 else 'FAIL'),
                 ('G3', 'PASS' if R['A-B'][0] > R['A-N'][0] else 'FAIL')])
