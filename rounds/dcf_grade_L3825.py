"""L3825 grader (N1-N4), frozen with the pre-registration."""
import re, sys
T = open(sys.argv[1]).read()
m = re.search(r'observed D ([-\d.]+) .*\| p ([\d.]+)', T); oth = float(re.search(r'OTHER share ([\d.]+)', T).group(1))
F = {f: float(s) for f, s in re.findall(r'FAM (\S+) share ([\d.na]+)', T)}
d, p = float(m.group(1)), float(m.group(2)); print('D', d, 'p', p, 'other', oth, F)
R = [('N1', 'PASS' if d > 0 and p < 0.05 else 'FAIL'), ('N2', 'PASS' if F['KCN'] > oth else 'FAIL'),
     ('N3', 'PASS' if F['GRIN'] > oth else 'FAIL'), ('N4', 'PASS' if F['CACNA1'] < oth else 'FAIL')]
print('RESULT', R)
