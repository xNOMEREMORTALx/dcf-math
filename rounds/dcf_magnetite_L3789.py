"""L3789 frozen: are the 'universal magnetosome gene homologs' magnetite-specific, or generic protein families?
References (from a UniProt TSV given as argv[1]): MamB, MamE, MamK, MamP of Magnetospirillum gryphiswaldense (the entry whose organism
contains 'MSR-1', else the lowest accession; a gene with no entry is void) and human ISCA1 Q9BUE6 (MagR).
Proteomes (argv[2:]): UniProt TSV.gz. For each reference r and organism o: candidates are proteins of length 0.5-2.0 x len(r);
score = dcf_localalign_L3585 score; floor(r,o) = max score of 300 residue-shuffled candidates (random.Random(3789)) + 1; hit = score >= floor.
Output per (o, r): number of hits, floor, best hit accession, score, protein name."""
import gzip, sys, random, runpy
from multiprocessing import Pool
GENES = ['mamB', 'mamE', 'mamK', 'mamP']
def refs(path):
    L = open(path).read().splitlines(); h = L[0].split('\t')
    ie, io_, ig, iq = h.index('Entry'), h.index('Organism'), h.index('Gene Names'), h.index('Sequence')
    R = {}; rows = [l.split('\t') for l in L[1:] if l.strip()]
    for g in GENES:
        c = sorted([x for x in rows if g in x[ig].split() and 'gryphiswaldense' in x[io_]], key=lambda x: ('MSR-1' not in x[io_], x[ie]))
        if c: R[g] = (c[0][ie], c[0][iq])
    for x in rows:
        if x[ie] == 'Q9BUE6': R['ISCA1'] = (x[ie], x[iq])
    return R
def work(args):
    o, items, R = args; sc = runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']; out = []
    for k, (ra, rs) in R.items():
        n = len(rs); cand = [(a, s, nm) for a, s, nm in items if 0.5 * n <= len(s) <= 2.0 * n]
        rnd = random.Random(3789); fl = 0
        for a, s, nm in rnd.sample(cand, min(300, len(cand))):
            t = list(s); rnd.shuffle(t); fl = max(fl, sc(''.join(t), rs))
        fl += 1; best = (0, '-', '-'); nh = 0
        for a, s, nm in cand:
            v = sc(s, rs)
            if v >= fl: nh += 1
            if v > best[0]: best = (v, a, nm)
        out.append('%s\t%s(%s)\thits\t%d\tfloor\t%d\tbest\t%s\t%d\t%s' % (o, k, ra, nh, fl, best[1], best[0], best[2]))
    return out
if __name__ == '__main__':
    R = refs(sys.argv[1]); print('REFS', {k: (a, len(s)) for k, (a, s) in R.items()}, flush=True); jobs = []
    for f in sys.argv[2:]:
        L = gzip.open(f, 'rt').read().splitlines(); h = L[0].split('\t')
        io_, ie, iq, ip = h.index('Organism'), h.index('Entry'), h.index('Sequence'), h.index('Protein names')
        rows = [l.split('\t') for l in L[1:]]
        jobs.append((rows[0][io_].split(' (')[0], [(x[ie], x[iq], x[ip]) for x in rows], R))
    with Pool(2) as p:
        for out in p.imap_unordered(work, jobs):
            for l in out: print(l, flush=True)
