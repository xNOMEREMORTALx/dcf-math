"""L3845 grader (M1-M4), frozen with the pre-registration. argv: CELL=path_to_L3825a_output ... (GM12878, K562, HepG2)."""
import re, sys
R = {}
for arg in sys.argv[1:]:
    c, p = arg.split('=', 1); T = open(p).read()
    m = re.search(r'observed D ([-\d.]+) .*\| p ([\d.]+)', T); oth = float(re.search(r'OTHER share ([\d.]+)', T).group(1))
    F = {f: float(s) for f, s in re.findall(r'FAM (\S+) share ([\d.na]+)', T)}
    R[c] = (float(m.group(1)), float(m.group(2)), oth, F); print(c, R[c])
cells = ['GM12878', 'K562', 'HepG2']; ok = all(c in R for c in cells)
g = lambda f: 'ungradeable' if not ok else ('PASS' if all(f(R[c]) for c in cells) else 'FAIL')
res = [('M1', g(lambda r: r[0] > 0 and r[1] < 0.05)), ('M2', g(lambda r: r[3]['KCN'] > r[2])), ('M3', g(lambda r: r[3]['GRIN'] > r[2]))]
have = [c for c in cells if c in R]
res.append(('M4', 'ungradeable' if len(have) < 2 else ('PASS' if sum(R[c][3]['CACNA1'] < R[c][2] for c in have) >= 2 else 'FAIL')))
print('RESULT', res)
