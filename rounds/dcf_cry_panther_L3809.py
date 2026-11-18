"""L3809 frozen: the L3777 six-reference scan (work() unchanged) applied to every protein of a UniProt TSV regardless of organism
(argv: one TSV.gz per PANTHER subfamily; label = file's set name given as name=path). Hit strings acc:score:TETRAD:family as before.
Proteins already seen in L3785/L3805 are excluded by the grader, not here."""
import gzip, sys, runpy
from multiprocessing import Pool
W = runpy.run_path('/home/claude/dcf-math/rounds/dcf_cry_classII_L3777.py', run_name='x')['work']
def chunk(args): return W(args)
if __name__ == '__main__':
    for arg in sys.argv[1:]:
        name, path = arg.split('=', 1)
        L = gzip.open(path, 'rt').read().splitlines(); h = L[0].split('\t'); ie, iq = h.index('Entry'), h.index('Sequence')
        items = [(x[ie], x[iq]) for x in (l.split('\t') for l in L[1:] if l.strip())]
        n400 = sum(400 <= len(s) <= 900 for a, s in items)
        parts = [(name, items[i::2]) for i in range(2)]
        with Pool(2) as p: res = p.map(chunk, parts)
        hits = [x for o, hs in res for x in hs]
        print('SET\t%s\tproteins\t%d\tin_window\t%d\thits\t%d\t%s' % (name, len(items), n400, len(hits), ' '.join(sorted(hits))), flush=True)
