"""L3837 grader (C1, C2), frozen with the pre-registration."""
import re, sys
rows = re.findall(r'^(\S+)\s+AUX ([\d.]+) CA ([\d.]+) OTHER ([\d.]+) \| D_ca ([-\d.]+) null mean [-\d.]+ p_lower ([\d.]+)', open(sys.argv[1]).read(), re.M)
for r in rows: print(r)
assert len(rows) == 3
c1 = all(float(a) < float(o) for _, a, c, o, d, p in rows)
c2 = sum(float(c) < float(o) and float(p) < 0.05 for _, a, c, o, d, p in rows) >= 2
print('RESULT', [('C1', 'PASS' if c1 else 'FAIL'), ('C2', 'PASS' if c2 else 'FAIL')])
