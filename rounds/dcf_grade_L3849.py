"""L3849 grader (F1-F4), frozen with the pre-registration. argv: CELL=path ... for HEK293, MCF10A, BJ, RWPE1 (missing = void)."""
import re, sys
R = {}
for arg in sys.argv[1:]:
    c, p = arg.split('=', 1); T = open(p).read()
    d = float(re.search(r'observed D ([-\d.]+)', T).group(1)); oth = float(re.search(r'OTHER share ([\d.]+)', T).group(1))
    F = {f: float(s) for f, s in re.findall(r'FAM (\S+) share ([\d.na]+)', T)}; R[c] = (d, oth, F); print(c, R[c])
n = len(R); need = 3 if n >= 3 else None
def g(f):
    if need is None: return 'ungradeable'
    return 'PASS' if sum(f(r) for r in R.values()) >= (3 if n == 4 else 3) else 'FAIL'
res = [('F1', g(lambda r: r[2]['KCN'] > r[1])), ('F2', g(lambda r: r[2]['GRIN'] > r[1])),
       ('F3', g(lambda r: r[2]['CACNA1'] < r[1])), ('F4', g(lambda r: r[0] > 0))]
print('cells graded', n, 'RESULT', res)
