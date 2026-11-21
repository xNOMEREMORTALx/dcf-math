"""L3929 grader."""
import re, sys
t = open(sys.argv[1]).read(); m = {g: float(v) for g, v in re.findall(r'GROUP (\S) median ([\d.]+)', t)}; p = float(re.search(r'MWU N>A p ([\d.]+)', t).group(1))
print(m, p); print('RESULT', [('P1', 'PASS' if m['N'] > m['A'] else 'FAIL'), ('P2', 'PASS' if p < 0.05 else 'FAIL')])
