"""L3557 tool run: frozen dcf_nerve_v2_L3549 tags() on each UniProt entry (reads Entry and Sequence only)."""
import gzip,runpy,sys
M=runpy.run_path('/home/claude/dcf-math/rounds/dcf_nerve_v2_L3549.py',run_name='x')
P=M['proteins'](sys.argv[1]); print('proteins:',len(P))
for a,p in sorted(P.items()):
    for t in M['tags'](p): print(t,a)
