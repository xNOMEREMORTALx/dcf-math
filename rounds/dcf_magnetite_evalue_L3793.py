"""L3793 frozen: L3789 re-analysed with a size-scaled noise floor (proposed rule 17).
Same references, proteomes, candidate windows and aligner as L3789. For each (reference r, organism o): score 1000 residue-shuffled candidates
(random.Random(3793)); fit a Gumbel by moments (beta = sd*sqrt(6)/pi, mu = mean - 0.5772*beta); E(x) = N_candidates * (1 - exp(-exp(-(x-mu)/beta))).
Hit = E < 0.01. Output per (o, r): hits, N candidates, mu, beta, best accession, best score, best E, best name."""
import gzip, sys, random, runpy, math, statistics
from multiprocessing import Pool
R = runpy.run_path('/home/claude/dcf-math/rounds/dcf_magnetite_L3789.py', run_name='x')['refs']
def work(args):
    o, items, REF = args; sc = runpy.run_path('/home/claude/dcf-math/rounds/dcf_localalign_L3585.py')['score']; out = []
    for k, (ra, rs) in REF.items():
        n = len(rs); cand = [(a, s, nm) for a, s, nm in items if 0.5 * n <= len(s) <= 2.0 * n]; rnd = random.Random(3793); null = []
        for i in range(1000):
            a, s, nm = cand[rnd.randrange(len(cand))]; t = list(s); rnd.shuffle(t); null.append(sc(''.join(t), rs))
        beta = statistics.pstdev(null) * math.sqrt(6) / math.pi; mu = statistics.mean(null) - 0.5772 * beta
        E = lambda x: len(cand) * (-math.expm1(-math.exp(-(x - mu) / beta)))
        nh = 0; best = (0, '-', '-')
        for a, s, nm in cand:
            v = sc(s, rs)
            if E(v) < 0.01: nh += 1
            if v > best[0]: best = (v, a, nm)
        out.append('%s\t%s(%s)\thits\t%d\tN\t%d\tmu\t%.1f\tbeta\t%.2f\tbest\t%s\t%d\t%.3g\t%s' % (o, k, ra, nh, len(cand), mu, beta, best[1], best[0], E(best[0]), best[2]))
    return out
if __name__ == '__main__':
    REF = R(sys.argv[1]); jobs = []
    for f in sys.argv[2:]:
        L = gzip.open(f, 'rt').read().splitlines(); h = L[0].split('\t')
        io_, ie, iq, ip = h.index('Organism'), h.index('Entry'), h.index('Sequence'), h.index('Protein names'); rows = [l.split('\t') for l in L[1:]]
        jobs.append((rows[0][io_].split(' (')[0], [(x[ie], x[iq], x[ip]) for x in rows], REF))
    with Pool(2) as p:
        for out in p.imap_unordered(work, jobs):
            for l in out: print(l, flush=True)
