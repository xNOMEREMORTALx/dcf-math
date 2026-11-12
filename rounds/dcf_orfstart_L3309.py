"""dcf_orfstart_L3309.py - start-codon choice for an mRNA's main reading frame. Author: Gary NOMEREMORTAL Mason (DCF). Frozen L3309.
rule A (current tools): longest ATG-to-stop reading frame, starting at its FIRST ATG.
rule K (Kozak -3):      same frame and stop, but scan its in-frame ATGs from the 5' end (first 100 codons) and take the first
                        whose base at -3 is a purine (A or G); if none, keep the first ATG.
Usage as a module: orf_A(seq), orf_K(seq) -> protein strings."""
CODE = {}
_b = 'TCAG'; _aa = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
for i, x in enumerate(_b):
    for j, y in enumerate(_b):
        for k, z in enumerate(_b): CODE[x + y + z] = _aa[16 * i + 4 * j + k]

def _best(s):
    """returns (start_nt, stop_nt) of the longest ATG..stop frame (first ATG after the previous in-frame stop)."""
    best = (0, 0, 0)
    for f in range(3):
        i = f; seg_start = f
        while i + 3 <= len(s):
            c = s[i:i + 3]
            if CODE.get(c) == '*' or i + 6 > len(s):
                end = i if CODE.get(c) == '*' else i + 3
                k = s.find('ATG', seg_start)
                while k != -1 and (k - f) % 3: k = s.find('ATG', k + 1)
                if k != -1 and k < end and end - k > best[0]: best = (end - k, k, end)
                seg_start = i + 3
            i += 3
    return best[1], best[2]

def _tr(s): return ''.join(CODE.get(s[i:i + 3], 'X') for i in range(0, len(s) - 2, 3))

def orf_A(s):
    a, e = _best(s); return _tr(s[a:e])

def orf_K(s, window=100):
    a, e = _best(s)
    for k in range(a, min(e, a + 3 * window), 3):
        if s[k:k + 3] == 'ATG' and k >= 3 and s[k - 3] in 'AG':
            return _tr(s[k:e])
    return _tr(s[a:e])
