"""L3857 grader (S1-S4)."""
import re, sys
Z = {f: (float(z), int(n)) for f, z, n in re.findall(r'STOUFFER (\S+) Z ([-+\d.]+) n (\d+)', open(sys.argv[1]).read())}; print(Z)
assert all(Z[f][1] == 10 for f in Z)
print('RESULT', [('S1', 'PASS' if Z['KCN'][0] > 1.645 else 'FAIL'), ('S2', 'PASS' if Z['GRIN'][0] > 1.645 else 'FAIL'),
                 ('S3', 'PASS' if Z['CACNA1'][0] < -1.645 else 'FAIL'), ('S4', 'PASS' if Z['ALL'][0] > 3.09 else 'FAIL')])
