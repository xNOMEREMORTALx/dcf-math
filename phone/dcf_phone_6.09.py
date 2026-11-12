# DCF PHONE TOOLKIT — Digital Cosmos Framework on Pydroid 3
# Author: Gary NOMEREMORTAL Mason · round L1894 · 2026-10-14 · updated round L2076 · 2026-10-18 · 6.06 round L3277 · 2026-11-10 · 6.07 round L3285 · 2026-11-11 (menu 30 lists only genome files) · 6.08 round L3289 (Theorem D self-test row uses 60-digit mpmath; failed on an ARM phone in float) · 6.09 round L3297 (menus 32 motif scan, 33 exon map)
#
# One file. Press Run in Pydroid 3 and pick from the menu.
# Needs only the Python standard library. mpmath is optional but recommended
# (Pydroid 3: menu -> Pip -> type mpmath -> Install); it is required for the
# project position rule on irrational numbers (pi, e, phi, square roots ...).
#
# What it does
#   1  Reciprocal explorer: preperiod, period, digits, digit sum, positions of a digit, Midy test
#   2  Position rule: "X contains S at position N" -> checked exactly as the project rule says
#   3  Audit a master-list text file (repeat lengths, digit sums, 5-positions, first occurrences)
#   4  Build / verify a local reciprocal database (every row recomputed on retrieval)
#   5  GaryPhone adapter: database rows -> DRC1 descriptors -> G4 coded groups -> receive,
#      verify and recompute (lead L1889)
#   6  Self-test
#   8  Claims inbox: paste an AI answer; every 'S at position N of X' claim is checked
#   9  QR send: a one-code 'ticket' that lets another device verify your table, or any report as QR codes
#  10  QR receive: paste text from any scanner app, or decode QR photos/screenshots (OpenCV)
#  11  Reciprocal cube: exact invariants per 1/n, theorem checks, group-by queries, CSV export
#  12  Compression: size ladder from plain digits to a recipe; Midy-aware archive that restores every digit
#  13  E8 labels: verify the 240 roots, order test on shuffled frames, noise test vs a random code
#  14  Gaussian channel: E8 vs random 240-point codes, your own noise levels, angles and error rates
#  15  Balance explorer: cycles of 1/n, 4.5-ratio balance, surviving characters, Theorem F for n = p*q
#  16  Harmonics: the digit wave of 1/n, DC term (balance) and even harmonics (Midy)
#  17  Quantum period finding: simulation of Shor's algorithm; the period it finds is the period of 1/n
#  18  Fibonacci memory: Pisano periods (60 / 24), half-period mirror, balance (Theorem B), 1/89, Lucas 19/89, Pell 1/79, phi = 2cos(pi/5)
#  19  Fibonacci wheels (60 and 24): quartets {k, P-k, P/2+k, P/2-k}, database table, position sums linked to reciprocals
#  20  Lucas / Pell / Fibonacci wheels (last digits or digital roots), reflection and mirror laws, 60<->24 quartet links
#  21  Fibonacci prime table: rank of apparition alpha(p), Pisano period, period of 1/p; which primes divide F(k)
#  25  DNA view of 1/p: base-4 digits as A C G T; base-4 Midy = Watson-Crick (second half = complement of first half), L2664
#  30  Energy-metal tier of a genome (L3277)   31  Number checks: first 1/n with a string, Monster primes (L3277)
#  26  DNA tools: run the gene finder (dcf_genefinder_mobile.py) on a genome file kept in this folder (L2723-L2808)
#  27  DNA storage: encode a file into DNA strands / decode it back / noise drill (dcf_dna_ecc.py v6, L2665-L2784)
#  28  Theorems L2422-L2848: 2-5 lemma, reduction clock (P3, base-b self-period), casting out 10^q - 1 (D_q),
#      variance as a Dedekind sum, run-length lemma, Note B counts, real-subfield Wieferich test (Theorem R)
# Every result is written to a Markdown + JSON report you can share.

import math, os, sys, re, json, time, hashlib, hmac, struct, sqlite3

VERSION = "DCF-phone-6.09 (L3297)"
try:
    import mpmath
    HAVE_MP = True
except ImportError:
    HAVE_MP = False

# ---------------------------------------------------------------- folders
def out_dir():
    if os.environ.get("DCF_OUT"):
        os.makedirs(os.environ["DCF_OUT"], exist_ok=True); return os.environ["DCF_OUT"]
    for d in ("/storage/emulated/0/Download/DCF", os.path.join(os.path.expanduser("~"), "DCF")):
        try:
            os.makedirs(d, exist_ok=True)
            t = os.path.join(d, ".w"); open(t, "w").close(); os.remove(t)
            return d
        except OSError:
            continue
    return os.getcwd()

OUT = out_dir()
DB_PATH = os.path.join(OUT, "dcf_phone.sqlite")
LOG = []                                   # lines for the session report

def say(*a):
    s = " ".join(str(x) for x in a); print(s); LOG.append(s)

# ---------------------------------------------------------------- exact arithmetic
def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1 if d == 2 else 2
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def lcm(a, b):
    from math import gcd
    return a // gcd(a, b) * b

def mult_order(a, m):
    """order of a modulo m (gcd(a, m) = 1)."""
    if m == 1: return 1
    lam = 1
    for p, e in factor(m).items():                       # Carmichael lambda(m)
        l = 2 ** (e - 2) if (p == 2 and e >= 3) else (p - 1) * p ** (e - 1)
        lam = lcm(lam, l)
    for p in factor(lam):
        while lam % p == 0 and pow(a, lam // p, m) == 1: lam //= p
    return lam

def digits(r, n, k):
    """first k digits after the point of r/n (0 <= r < n), exact long division."""
    out = []
    while k:
        c = min(36, k); q, r = divmod(r * 10 ** c, n)
        out.append(format(q, "0" + str(c) + "d")); k -= c
    return "".join(out)

def recip(n):
    """1/n -> preperiod s, period L (0 = terminating), block = first s+L digits."""
    if n < 2: raise ValueError("n must be >= 2")
    m, a, b = n, 0, 0
    while m % 2 == 0: m //= 2; a += 1
    while m % 5 == 0: m //= 5; b += 1
    s = max(a, b); L = 0 if m == 1 else mult_order(10, m)
    return s, L, digits(1, n, s + L) if s + L else ""

def midy(n):
    s, L, blk = recip(n)
    if L == 0 or L % 2: return None
    per = blk[s:]; h = L // 2
    return all(int(x) + int(y) == 9 for x, y in zip(per[:h], per[h:]))

def sha_digits(n, r, k):
    h = hashlib.sha256(); rem = k
    while rem:
        c = min(36, rem); q, r = divmod(r * 10 ** c, n)
        h.update(format(q, "0" + str(c) + "d").encode()); rem -= c
    return h.digest()

# ---------------------------------------------------------------- position rule
NAMES = {"pi", "e", "phi", "sqrt", "cbrt", "root", "log", "ln", "exp", "zeta", "catalan",
         "euler", "mpf", "power", "sin", "cos", "tan", "atan", "apery"}
RAT = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")
LIMIT = 9000                                     # search the first 9000 digits only

def mp_eval(expr):
    ids = set(re.findall(r"[A-Za-z_]\w*", expr))
    if ids - NAMES: raise ValueError("unknown name(s): " + ", ".join(sorted(ids - NAMES)))
    if re.search(r"__|\[|\]|lambda|import|;|=", expr): raise ValueError("expression not allowed")
    code = re.sub(r"(?<![\w.'])(\d+(?:\.\d+)?)(?![\w.'])", r"mpf('\1')", expr)
    ns = {"__builtins__": {}}
    for k in NAMES - {"ln", "apery"}:
        if hasattr(mpmath, k): ns[k] = getattr(mpmath, k)
    ns["ln"] = mpmath.log; ns["apery"] = mpmath.zeta(3); ns["e"] = mpmath.e
    return eval(code, ns)

def fraction_digits(expr):
    """digits after the point used by the rule, and how they were obtained."""
    m = RAT.match(expr)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        if b == 0: raise ValueError("division by zero")
        exact = digits(a % b, b, LIMIT)
        if HAVE_MP:                                # the project rule, verbatim
            mpmath.mp.dps = 12000
            X = mpmath.mpf(a) / b
            mpd = mpmath.nstr(X, 10000, strip_zeros=False).split(".")[1][:LIMIT]
            if mpd != exact: raise RuntimeError("mpmath and exact division disagree")
            return exact, "exact division + mpmath rule (agree)"
        return exact, "exact division (mpmath not installed)"
    if not HAVE_MP:
        raise RuntimeError("mpmath is needed for irrational numbers: Pydroid 3 menu -> Pip -> mpmath")
    mpmath.mp.dps = 12000                          # X is computed AFTER setting dps
    X = mp_eval(expr)
    return mpmath.nstr(X, 10000, strip_zeros=False).split(".")[1][:LIMIT], "mpmath rule (dps 12000)"

def position(expr, S):
    if not re.fullmatch(r"\d+", S): raise ValueError("substring must be digits")
    d, how = fraction_digits(expr)
    return d.find(S) + 1, how                      # 0 = not found in the first 9000 digits

def check_claim(expr, S, N):
    pos, how = position(expr, S)
    if pos == N: verdict = "VERIFIED"
    elif pos == 0: verdict = "REFUTED: not found in the first %d digits" % LIMIT
    elif pos < N: verdict = "REFUTED: first occurrence is at %d" % pos
    else: verdict = "REFUTED: first occurrence is at %d" % pos
    also = []
    d, _ = fraction_digits(expr)
    if pos != N and N >= 1 and d[N - 1:N - 1 + len(S)] == S:
        verdict = "PARTLY TRUE: S does occur at %d, but its first occurrence is at %d" % (N, pos)
    return dict(X=expr, S=S, claimed=N, first_position=pos, verdict=verdict, method=how,
                convention="A: position 1 = first digit after the decimal point")

# ---------------------------------------------------------------- master-list audit (port of L1885)
ENTRY = re.compile(r"^\s*(?:•\s*)?1/(\d+)\s*=\s*0\.(\d*)(.*)$")

def parse_list(text):
    entries, cur = [], None
    for i, line in enumerate(text.split("\n"), 1):
        m = ENTRY.match(line)
        if m:
            if cur: entries.append(cur)
            cur = dict(n=int(m.group(1)), display=m.group(2), line=i, raw=[line])
        elif cur is not None:
            cur["raw"].append(line)
    if cur: entries.append(cur)
    return entries

def claims_of(e):
    text = " ".join(e["raw"]); out = []
    m = re.search(r"repeats every\s+(\d+)\s*digit", text)
    if m: out.append(("repeat_length", int(m.group(1))))
    m = re.search(r"sums?\s+to\s+(\d+)", text)
    if m: out.append(("digit_sum", int(m.group(1))))
    m = re.search(r"(?:the )?5s?\s+(?:occurs?|is)?\s*at\s+positions?\s+([\d ,and]+)", text)
    if m:
        ps = [int(x) for x in re.findall(r"\d+", m.group(1))]
        if ps: out.append(("five_positions", ps))
    for m in re.finditer(r"first occur[a-z]* of (?:a |the |an )?(\d+)((?: and \d{2,}(?![\d,÷]))*)(\s+in (?:pi|π) at (\d+))?", text, re.I):
        if m.group(3):
            out.append(("pi_position", (m.group(1), int(m.group(4))))); continue
        before = text[max(0, m.start() - 90):m.start()]
        refs = [int(x) for x in re.findall(r"reciprocal of (\d+) is (?:also )?(?:the )?$", before)]
        cn = refs[-1] if refs else e["n"]
        for tg in [m.group(1)] + re.findall(r"\d+", m.group(2) or ""):
            out.append(("first_occurrence", (tg, cn)))
    return out

def first_denominator(target, upto, block_only=False):
    """first k >= 2 whose expansion of 1/k contains target (repeats counted, or one block only)."""
    for k in range(2, upto + 1):
        s, L, blk = recip(k)
        if target in (blk if block_only else digits(1, k, s + max(L, 1) + len(target) + 1)): return k
    return None

def audit_list(text):
    entries = parse_list(text); rows = []
    for e in entries:
        n = e["n"]; s, L, blk = recip(n); D = e["display"]
        disp_ok = digits(1, n, len(D)) == D if D else True
        if not disp_ok: rows.append(dict(n=n, line=e["line"], kind="display", status="MISMATCH",
                                         note="displayed digits differ from exact division"))
        for kind, val in claims_of(e):
            st = "MISMATCH"; note = ""
            if kind == "repeat_length":
                if val == L: st = "OK"
                elif val == s + L: st, note = "OK (counts preperiod)", "period %d, preperiod %d" % (L, s)
                else: note = "true period %d (preperiod %d)" % (L, s)
            elif kind == "digit_sum":
                dd = sum(map(int, D)); per = sum(map(int, blk[s:])) if L else None
                if val in (dd, per, sum(map(int, blk))): st = "OK"
                else: note = "displayed digits sum to %d; one period sums to %s" % (dd, per)
            elif kind == "five_positions":
                act = [i + 1 for i, c in enumerate(D) if c == "5"]
                act2 = [i + 1 for i, c in enumerate(blk) if c == "5"]
                if val in (act, act2): st = "OK"
                elif val and set(val) <= set(act2): st, note = "OK (partial list)", "all 5s: %s" % act2
                else: note = "5s are at %s" % (act or act2)
            elif kind == "first_occurrence":
                tg, cn = val; f = first_denominator(tg, max(cn, n))
                if f == cn: st = "OK"
                elif first_denominator(tg, max(cn, n), True) == cn:
                    st, note = "OK (one displayed block only)", 'counting repeats it first appears in 1/%s' % f
                else: note = '"%s" first appears in 1/%s, not 1/%d' % (tg, f, cn)
            elif kind == "pi_position":
                tg, pos = val
                try:
                    r = check_claim("pi", tg, pos); st = "OK" if r["verdict"] == "VERIFIED" else "MISMATCH"; note = r["verdict"]
                except RuntimeError as ex:
                    st, note = "SKIPPED", str(ex)
            if st == "MISMATCH" and "[L1887 correction" in " ".join(e["raw"]): st = "MISMATCH (already annotated)"
            rows.append(dict(n=n, line=e["line"], kind=kind, claimed=val, status=st, note=note))
    ns = [e["n"] for e in entries]
    summary = dict(entries=len(entries), distinct=len(set(ns)),
                   range=[min(ns), max(ns)] if ns else None,
                   missing_2_to_2000=len(set(range(2, min(max(ns), 2000) + 1)) - set(ns)) if ns else None,
                   duplicates=sorted(k for k in set(ns) if ns.count(k) > 1),
                   claims=sum(1 for r in rows if r["kind"] != "display"),
                   problems=sum(1 for r in rows if r["status"] == "MISMATCH"),
                   annotated=sum(1 for r in rows if r["status"] == "MISMATCH (already annotated)"))
    return summary, rows

# ---------------------------------------------------------------- local database
SCHEMA = """CREATE TABLE IF NOT EXISTS recips(n INTEGER PRIMARY KEY, preperiod INTEGER, period INTEGER,
  digit_sum INTEGER, fives TEXT, midy INTEGER, sha256 TEXT, program TEXT);
CREATE TABLE IF NOT EXISTS checks(id INTEGER PRIMARY KEY, time TEXT, kind TEXT, input TEXT, result TEXT);"""

def row_for(n):
    s, L, blk = recip(n)
    return (n, s, L, sum(map(int, blk)), ",".join(str(i + 1) for i, c in enumerate(blk) if c == "5"),
            {None: None, True: 1, False: 0}[midy(n)], hashlib.sha256(blk.encode()).hexdigest(), VERSION)

def db():
    con = sqlite3.connect(DB_PATH); con.executescript(SCHEMA); return con

def build_db(lo, hi):
    con = db(); t = time.time()
    with con:
        con.executemany("INSERT OR REPLACE INTO recips VALUES(?,?,?,?,?,?,?,?)", (row_for(n) for n in range(lo, hi + 1)))
    con.close(); return hi - lo + 1, time.time() - t

def verify_db():
    con = db(); bad = []; k = 0
    for row in con.execute("SELECT * FROM recips ORDER BY n"):
        k += 1
        if tuple(row[:7]) != row_for(row[0])[:7]: bad.append(row[0])
    con.close(); return k, bad

def log_check(kind, inp, result):
    con = db()
    with con:
        con.execute("INSERT INTO checks(time,kind,input,result) VALUES(?,?,?,?)",
                    (time.strftime("%Y-%m-%d %H:%M:%S"), kind, json.dumps(inp), json.dumps(result)))
    con.close()

# ---------------------------------------------------------------- GaryPhone codec (from phone_plan_driven_benchmark.py)
E, Lg, x = [0] * 510, [0] * 256, 1
for i in range(255):
    E[i], Lg[x] = x, i; x <<= 1
    if x & 256: x ^= 0x11d
for i in range(255, 510): E[i] = E[i - 255]
def gmul(a, b): return 0 if not a or not b else E[Lg[a] + Lg[b]]
def gdiv(a, b):
    if not b: raise ValueError("RS")
    return 0 if not a else E[(Lg[a] - Lg[b]) % 255]
def synd(p):
    out = []
    for i in range(4):
        a = 0
        for b in p: a = gmul(a, E[i]) ^ b
        out.append(a)
    return out
def rs_encode(d):
    if not 1 <= len(d) <= 251: raise ValueError("RS")
    xs = [E[3 - j] for j in range(4)]; y = synd(d + bytes(4))
    A = [[1 if i == 0 else E[(Lg[v] * i) % 255] for v in xs] + [y[i]] for i in range(4)]
    for j in range(4):
        k = next(i for i in range(j, 4) if A[i][j]); A[j], A[k] = A[k], A[j]
        v = A[j][j]; A[j] = [gdiv(a, v) for a in A[j]]
        for i in range(4):
            if i != j:
                v = A[i][j]; A[i] = [a ^ gmul(v, b) for a, b in zip(A[i], A[j])]
    return d + bytes(A[j][-1] for j in range(4))
def rs_decode(p):
    n = len(p)
    if not 5 <= n <= 255: raise ValueError("RS")
    r = bytearray(p); s = synd(r)
    if not any(s): return bytes(r[:-4])
    D = gmul(s[1], s[1]) ^ gmul(s[0], s[2])
    if not D:
        if not s[0]: raise ValueError("RS")
        v = gdiv(s[1], s[0]); loc = [j for j in range(n) if E[n - 1 - j] == v]
        if len(loc) != 1: raise ValueError("RS")
        r[loc[0]] ^= s[0]
    else:
        a = gdiv(gmul(s[2], s[1]) ^ gmul(s[0], s[3]), D); b = gdiv(gmul(s[1], s[3]) ^ gmul(s[2], s[2]), D)
        loc = [j for j in range(n) if gmul(E[n - 1 - j], E[n - 1 - j]) ^ gmul(a, E[n - 1 - j]) ^ b == 0]
        if len(loc) != 2: raise ValueError("RS")
        u, w = [E[n - 1 - j] for j in loc]; v = gdiv(s[1] ^ gmul(s[0], w), u ^ w)
        r[loc[0]] ^= v; r[loc[1]] ^= s[0] ^ v
    if any(synd(r)): raise ValueError("RS")
    return bytes(r[:-4])
def stuff(p):
    out = bytearray([0]); idx = 0; code = 1
    for b in p:
        if not b:
            out[idx] = code; idx = len(out); out.append(0); code = 1
        else:
            out.append(b); code += 1
            if code == 255: out[idx] = code; idx = len(out); out.append(0); code = 1
    out[idx] = code; return bytes(out)
def unstuff(p):
    if not p or 0 in p: raise ValueError("FRAMING")
    out = bytearray(); i = 0
    while i < len(p):
        c = p[i]; i += 1
        if i + c - 1 > len(p): raise ValueError("FRAMING")
        out.extend(p[i:i + c - 1]); i += c - 1
        if c != 255 and i < len(p): out.append(0)
    return bytes(out)
def vi(v):
    out = bytearray()
    while v >= 128: out.append((v & 127) | 128); v >>= 7
    out.append(v); return bytes(out)
def rv(d, pos):
    start = pos; v = 0
    for shift in range(0, 35, 7):
        if pos >= len(d): raise ValueError("LAYOUT")
        b = d[pos]; pos += 1; v |= (b & 127) << shift
        if b < 128:
            if d[start:pos] != vi(v): raise ValueError("LAYOUT")
            return v, pos
    raise ValueError("RESOURCE")
def descriptor(n, r, k):
    if not 2 <= n <= 1000000 or not 0 <= r < n or not 1 <= k <= 20000: raise ValueError("RESOURCE")
    return b"DRC1" + vi(n) + vi(r) + vi(k) + sha_digits(n, r, k)
def check_descriptor(d):
    if d[:4] != b"DRC1": raise ValueError("LAYOUT")
    pos = 4; v = []
    for _ in range(3):
        y, pos = rv(d, pos); v.append(y)
    if len(d) - pos != 32: raise ValueError("LAYOUT")
    n, r, k = v
    if not 2 <= n <= 1000000 or not 0 <= r < n or not 1 <= k <= 20000: raise ValueError("RESOURCE")
    if not hmac.compare_digest(sha_digits(n, r, k), d[pos:]): raise ValueError("DIGEST")
    return n, r, k
def mac(key, prefix, b): return hmac.new(key, prefix + b, hashlib.sha256).digest()

def make_group(key, gid, recs, fault=None):
    """recs: 4 (logical_id, descriptor). Returns the framed wire bytes."""
    bs = [b"G4" + struct.pack(">IBBI", gid, i, 4, lid) + bytes([len(d)]) + d + bytes(42 - len(d))
          for i, (lid, d) in enumerate(recs)]
    rows = [rs_encode(b + mac(key, b"ROW/", b)) for b in bs]
    raw = bytearray(rows[r][c] for c in range(91) for r in range(4))
    if fault == "burst":
        for i in range(37, 45): raw[i] ^= 0x5a                 # 8-byte burst, corrected by RS
    if fault == "heavy":
        for i in range(0, 40): raw[i] ^= 0xa5                  # beyond RS capacity: must be rejected
    return stuff(bytes(raw)) + b"\0"

def receive_group(key, wire):
    if not wire or wire[-1] != 0: raise ValueError("FRAMING")
    raw = unstuff(wire[:-1])
    if len(raw) != 364: raise ValueError("LAYOUT")
    out = []
    for r in range(4):
        p = rs_decode(bytes(raw[r + 4 * c] for c in range(91))); b, tag = p[:-32], p[-32:]
        if not hmac.compare_digest(tag, mac(key, b"ROW/", b)): raise ValueError("MAC")
        gid, slot, count, lid = struct.unpack(">IBBI", b[2:12]); ln = b[12]
        if b[:2] != b"G4" or slot >= 4 or count != 4 or not 1 <= ln <= 42 or any(b[13 + ln:]): raise ValueError("LAYOUT")
        out.append((gid, slot, lid, b[13:13 + ln]))
    if len({o[0] for o in out}) != 1 or {o[1] for o in out} != set(range(4)) or len({o[2] for o in out}) != 4:
        raise ValueError("MEMBERSHIP")
    return out[0][0], [(lid, d, check_descriptor(d)) for _, _, lid, d in sorted(out, key=lambda o: o[1])]

def adapter(lo, hi, inject=True):
    """L1889: reciprocal database rows -> DRC1 descriptors -> G4 groups -> receive -> verify -> recompute."""
    con = db()
    rows = con.execute("SELECT n, preperiod, period FROM recips WHERE n BETWEEN ? AND ? ORDER BY n", (lo, hi)).fetchall()
    con.close()
    if not rows: raise RuntimeError("no database rows in that range: build the database first (menu 4)")
    usable, skipped = [], []
    for n, s, L in rows:
        k = s + L
        if k == 0: skipped.append((n, "terminating: no repeating block")); continue
        d = descriptor(n, 1, k)
        if len(d) > 42: skipped.append((n, "descriptor %d bytes > 42 (G4 row limit)" % len(d))); continue
        usable.append((n, d, s, L))
    pad = len(usable) % 4
    if pad: skipped += [(u[0], "left over (groups need 4 records)") for u in usable[-pad:]]; usable = usable[:len(usable) - pad]
    groups = [usable[i:i + 4] for i in range(0, len(usable), 4)]
    key = os.urandom(32); rx = sqlite3.connect(":memory:")
    rx.executescript("CREATE TABLE received(n INTEGER PRIMARY KEY, r INTEGER, k INTEGER, descriptor BLOB, gid INTEGER);")
    stats = dict(groups=len(groups), records_sent=4 * len(groups), wire_bytes=0, burst_groups=0, burst_corrected=0,
                 heavy_groups=0, heavy_rejected=0, tamper_groups=0, tamper_rejected=0, accepted_groups=0)
    reasons = {}
    for gi, g in enumerate(groups, 1):
        fault = None
        if inject and gi % 5 == 2: fault = "burst"
        if inject and gi % 17 == 9: fault = "heavy"
        recs = [(n, d) for n, d, _, _ in g]
        if inject and gi % 23 == 11:                            # a wrong claim with a stale hash
            n0, d0 = recs[0]; recs[0] = (n0, d0[:-1] + bytes([d0[-1] ^ 1])); fault = "tamper"
        wire = make_group(key, gi, recs, None if fault == "tamper" else fault); stats["wire_bytes"] += len(wire)
        try:
            gid, items = receive_group(key, wire)
            with rx:
                for lid, d, (n, r, k) in items:
                    if lid != n: raise ValueError("ID")
                    rx.execute("INSERT INTO received VALUES(?,?,?,?,?)", (n, r, k, d, gid))
            stats["accepted_groups"] += 1
            if fault == "burst": stats["burst_groups"] += 1; stats["burst_corrected"] += 1
            if fault in ("heavy", "tamper"): raise RuntimeError("a faulty group was accepted: " + fault)
        except ValueError as ex:
            reasons[str(ex)] = reasons.get(str(ex), 0) + 1
            if fault == "heavy": stats["heavy_groups"] += 1; stats["heavy_rejected"] += 1
            elif fault == "tamper": stats["tamper_groups"] += 1; stats["tamper_rejected"] += 1
            else: raise RuntimeError("clean or burst group %d rejected: %s" % (gi, ex))
    # retrieval-and-recompute: every stored descriptor is re-derived from n alone
    semantic_bad, rec = [], 0
    for n, r, k, d in rx.execute("SELECT n, r, k, descriptor FROM received ORDER BY n"):
        rec += 1; s, L, blk = recip(n)
        if r != 1 or k != s + L or d != descriptor(n, 1, s + L): semantic_bad.append(n)
    expect = 4 * (stats["groups"] - stats["heavy_groups"] - stats["tamper_groups"])
    stats.update(records_received=rec, records_expected=expect, recompute_failures=len(semantic_bad),
                 reject_reasons=reasons, skipped=len(skipped),
                 status="ADAPTER PASSED" if rec == expect and not semantic_bad else "ADAPTER FAILED",
                 scope="in-process loopback (no radio or network channel); faults injected on purpose")
    return stats, skipped[:20], semantic_bad

# ---------------------------------------------------------------- self-test
def selftest():
    t = time.time(); res = []
    def ok(name, cond): res.append((name, bool(cond))); say(("PASS  " if cond else "FAIL  ") + name)
    s, L, b = recip(7); ok("1/7: period 6, block 142857, digit sum 27", (s, L, b, sum(map(int, b))) == (0, 6, "142857", 27))
    s, L, b = recip(12); ok("1/12: preperiod 2, period 1, block 083", (s, L, b) == (2, 1, "083"))
    ok("1/97: period 96", recip(97)[1] == 96)
    ok("1/2054: period 78 (the L1887 fragment)", recip(2054)[1] == 78)
    ok("1/17 is Midy; 1/3 has odd period", midy(17) is True and midy(3) is None)
    ok("order of 10 mod 9091 = 10", mult_order(10, 9091) == 10)
    p, _ = position("1/7", "857"); ok('"857" first at position 4 of 1/7', p == 4)
    r = check_claim("1/7", "285", 3); ok("claim check on 1/7 (285 at 3) verified", r["verdict"] == "VERIFIED")
    r = check_claim("1/7", "714", 2); ok("false claim (714 at 2 in 1/7) refuted: first at 6", r["first_position"] == 6 and r["verdict"].startswith("REFUTED"))
    if HAVE_MP:
        p, _ = position("pi", "999999"); ok('pi: "999999" first at 762 (Feynman point)', p == 762)
        p, _ = position("phi", "1231"); ok('phi: "1231" first at 2729', p == 2729)
        p, _ = position("355/113", "9"); ok("355/113 exact division agrees with mpmath", p >= 1)
    else:
        say("SKIP  irrational checks (install mpmath to enable)")
    sample = "• 1/7 =0.142857 (repeats every 6 digits) sums to 27\n• 1/13 =0.076923 (repeats every 6 digits) sums to 28"
    summ, rows = audit_list(sample)
    ok("list audit finds the wrong digit sum of 1/13 (true 27)", summ["problems"] == 1 and rows[-1]["kind"] == "digit_sum")
    txt = ('The sequence 1231 first appears at position 2729 of phi. In 1/7 the string "714" occurs at position 2. '
           'Also, sqrt(17) contains 1231 at position 1.')
    f, u = extract_claims(txt)
    ok("claims inbox extracts 3 claims", [(c["X"], c["S"], c["N"]) for c in f] == [("phi", "1231", 2729), ("1/7", "714", 2), ("sqrt(17)", "1231", 1)])
    global DB_PATH
    keep = DB_PATH; DB_PATH = os.path.join(OUT, "selftest.sqlite")
    try:
        if os.path.exists(DB_PATH): os.remove(DB_PATH)
        build_db(2, 400); k, bad = verify_db(); ok("database 2..400 built and every row recomputed", k == 399 and not bad)
        con = db()
        with con: con.execute("UPDATE recips SET digit_sum = digit_sum + 1 WHERE n = 97")
        con.close(); k, bad = verify_db(); ok("tampered row (n = 97) detected on retrieval", bad == [97])
        build_db(97, 97)
        st, sk, sb = adapter(2, 400)
        ok("adapter: %d groups, bursts corrected, heavy and tampered groups rejected, all records recomputed"
           % st["groups"], st["status"] == "ADAPTER PASSED" and st["burst_corrected"] > 0
           and st["heavy_rejected"] > 0 and st["tamper_rejected"] > 0)
    finally:
        try: os.remove(DB_PATH)
        except OSError: pass
        DB_PATH = keep
    # QR handoff
    import random as _r
    fr = qr_frames(make_ticket(2, 2055), "dcf.range")
    ok("ticket for 1/2..1/2055 fits in %d QR codes (%d chars max)" % (len(fr), max(map(len, fr))), len(fr) == 2)
    got = qr_collect("noise\n" + "\n".join(fr[::-1] + fr[:1]))
    g = list(got.values())[0]
    ok("ticket received out of order with a repeat; table verified by recomputation",
       g.get("complete") and check_ticket(g["payload"])["verdict"].startswith("VERIFIED"))
    bad = json.loads(make_ticket(2, 300)); bad["digest"] = "0" * 64
    ok("ticket with a wrong digest is refuted", check_ticket(json.dumps(bad).encode())["verdict"].startswith("REFUTED"))
    sp = make_ticket(2, 50, "cosmos")
    ok("signed ticket: right password verifies, wrong one is rejected",
       check_ticket(sp, "cosmos")["verdict"].startswith("VERIFIED") and check_ticket(sp, "nope")["verdict"].startswith("REJECTED"))
    blob = os.urandom(5000); fr = qr_frames(blob, "file:test.bin", 300, parity=0); _r.Random(1).shuffle(fr)
    part = qr_collect("\n".join(fr[:-1]))[fr[0][5:13]]
    ok("missing frame detected (%d of %d present)" % (part["have"], part["frames"]), not part.get("complete") and len(part["missing"]) == 1)
    full = qr_collect("\n".join(fr))[fr[0][5:13]]
    ok("5000-byte file reassembled from %d shuffled frames" % len(fr), full.get("complete") and full["payload"] == blob)
    cor = [f if i != 2 or f.split(":")[2] == "0" else f[:-1] + ("A" if f[-1] != "A" else "B") for i, f in enumerate(fr)]
    c2 = qr_collect("\n".join(cor))[fr[0][5:13]]
    ok("a frame altered after scanning is caught by its CRC", not c2.get("complete") and c2["crc_errors"])
    # cube + compression
    keep2 = DB_PATH; DB_PATH = os.path.join(OUT, "selftest_cube.sqlite")
    try:
        cube_build(2, 600); th = cube_theorems(2, 600)
        ok("cube 1/2..1/600: Theorem M and Theorem R hold on every row (%d Midy)" % th["midy"],
           th["M_violations"] == 0 and th["R_violations"] == 0 and th["prime_violations"] == 0)
        ok("ratio 4.5 without Midy: smallest example is 1/21", th["smallest_ratio_4_5_not_midy"][:1] == [21])
        head, rows = cube_query("is_prime,midy", "period>0 AND period%2=0", 2, 600)
        ok("cube query: every even-period prime is Midy", all(r[1] == 1 for r in rows if r[0] == 1))
    finally:
        try: os.remove(DB_PATH)
        except OSError: pass
        DB_PATH = keep2
    try:
        import lzma
        pth = os.path.join(OUT, "selftest.dra"); archive_write(2, 600, pth); r = archive_read(pth); os.remove(pth)
        ok("Midy-aware archive restores every digit of 1/2..1/600", r["sha256_ok"] and r["equals_recomputation"])
    except ImportError:
        say("SKIP  archive test (no lzma module)")
    # L1923: parity frames + claims ticket
    blob = os.urandom(9000); fr = qr_frames(blob, "file:p.bin", 300); n = int(fr[0].split(":")[3]); P = len(fr) - 1 - n
    import random as _r2
    lost = _r2.Random(7).sample(range(1, n + 1), P)
    kept = [f for f in fr if int(f.split(":")[2]) not in lost]
    g = qr_collect("\n".join(kept))[fr[0][5:13]]
    ok("parity: %d data frames + %d parity; %d lost data frames rebuilt" % (n, P, P), g.get("complete") and g["payload"] == blob and sorted(g["rebuilt"]) == sorted(lost))
    kept2 = [f for f in fr if int(f.split(":")[2]) not in _r2.Random(8).sample(range(1, n + 1), P + 1)]
    g2 = qr_collect("\n".join(kept2))[fr[0][5:13]]
    ok("parity: one loss too many is reported as missing, not guessed", not g2.get("complete"))
    cl = [dict(X="1/7", S="285", N=3, verdict="VERIFIED"), dict(X="1/7", S="714", N=2, verdict="VERIFIED")]
    rr = check_claims_ticket(make_claims_ticket(cl))
    ok("claims ticket: receiver re-checks; agrees on the true claim, flags the false one", rr[0]["agrees"] and not rr[1]["agrees"])
    # L1925: E8 labels
    c = e8_check(); ok("E8: 240 distinct roots, 56 neighbours each, 6720 edges", c["roots"] == c["distinct"] == 240 and c["neighbours"] == [56] and c["edges"] == 6720)
    r1 = e8_order_test(make_ticket(221, 401), "dcf.range"); r2 = e8_order_test(make_ticket(100000, 100010), "dcf.range")
    r3 = e8_order_test(os.urandom(6000), "file:x", 11)
    ok("E8 order test: shuffled frames restored, SHA of received payload OK (incl. 6-digit range and a %d-frame file)" % r3["frames"],
       all(r["restored_identical"] and r["sha256_of_received_ok"] for r in (r1, r2, r3)))
    # L1930: Gaussian channel, balance explorer, Theorem F, prime-power Midy
    ang, rows = gaussian_channel([0.15], trials=300, codes=2)
    ok("Gaussian channel: E8 60 deg apart, fewer label errors than random codes at sigma 0.15", abs(ang["e8"] - 60) < 1e-6 and rows[0][1] < min(rows[0][2]))
    b287, b943, b21 = balance_report(287), balance_report(943), balance_report(21)
    ok("balance explorer: 287 has 6 of 8 cycles balanced; 21 universally balanced", b287["balanced_cycles"] == 6 and b287["cycles"] == 8 and b21["universally_balanced"])
    ok("Theorem F: 1/287 balanced (6/41 sums 18 = 1/41), 1/943 not (25/41 sums 27)",
       b287.get("theorem_F", {}).get("agrees") and b943.get("theorem_F", {}).get("agrees") and b287["one_over_n_balanced"] and not b943["one_over_n_balanced"])
    pp = [p ** k for p in (3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41) for k in (1, 2, 3) if p ** k < 30000]
    ok("prime powers with even period are Midy (%d checked)" % len(pp),
       all(pow(10, mult_order(10, x) // 2, x) == x - 1 for x in pp if mult_order(10, x) % 2 == 0))
    # L1933: harmonics, Shor, Fibonacci
    hs = [harmonics(n) for n in (7, 17, 21, 41, 97, 287)]
    ok("harmonics: balanced <=> DC = 0 and Midy <=> even harmonics vanish (7, 17, 21, 41, 97, 287)",
       all(h["balanced"] == (abs(sum(int(c) for c in digits(1, h["n"], h["L"])) * 2 - 9 * h["L"]) == 0) and h["midy"] == h["even_harmonics_zero"] for h in hs))
    s21 = shor_simulation(21)
    ok("Shor simulation: period of 1/21 found (6) and 21 = 3 x 7", s21["period_found"] == 6 and "3 x 7" in s21.get("factor_step", ""))
    ok("Pisano: last digits repeat every 60, digital roots (mod 9) every 24, both with the half-period law",
       fib_memory(10)["pisano"] == 60 and fib_memory(9)["pisano"] == 24 and fib_memory(10)["half_period_negation"] and fib_memory(9)["half_period_negation"])
    # L1937: Fibonacci balance (Theorem B) and recurrence generating functions
    fams = {m: fib_balance(m)["defect"] for m in (5, 25, 125, 10, 50, 6, 30, 12, 60, 300)}
    ok("Theorem B: defect 0 for 5, 25, 125; 2m for 2*5^k and 6*5^k; -4m for 12*5^k (incl. regressions 12, 60, 300)",
       fams[5] == fams[25] == fams[125] == 0 and all(fams[m] == 2 * m for m in (10, 50, 6, 30)) and all(fams[m] == -4 * m for m in (12, 60, 300)))
    ok("alpha(m) = m without a mirror (m = 12, 60, 300) does not give the uniform mean",
       all(fib_balance(m)["alpha"] == m and not fib_balance(m)["mirror"] and fib_balance(m)["defect"] != 0 for m in (12, 60, 300)))
    ok("generating functions: Fibonacci 1/89, Lucas 19/89, Pell 1/79, tribonacci 1/889", all(x[2] for x in recurrence_gf_checks()))
    # L1940: Fibonacci wheels
    r24, v24 = fib_wheel(24); r60, v60 = fib_wheel(60)
    ok("Theorem W holds on both wheels (half-turn negation, reflection by parity)", wheel_theorem_check(24) == 0 and wheel_theorem_check(60) == 0)
    q5 = next(r for r in r24 if r["pos"] == 5)
    ok("wheel 24: quartet of 5 is (5, 7, 17, 19) with digits 5, 4, 4, 5; position sum 48, digit sum 18",
       q5["quartet"] == (5, 7, 17, 19) and [v24[x] for x in q5["quartet"]] == [5, 4, 4, 5] and q5["pos_sum"] == 48 and q5["digit_sum"] == 18)
    ok("wheel 60: 5 sits at every 5th position except multiples of 15 (which are 0); 37 divides F(19) = 4181",
       [k for k in v60 if v60[k] == 5] == [k for k in range(1, 61) if k % 5 == 0 and k % 15] and reciprocal_link(19)["F_s"] % 37 == 0)
    # L1944: Lucas/Pell wheels, wheel links, rank of apparition
    ok("Lucas wheel (last digits) has 12 positions with reflection L(P-k) = -(-1)^(k+1) L(k) and a half-turn mirror; Pell likewise (+ sign)",
       seq_wheel_check("lucas", "last") == (12, True, True) and seq_wheel_check("pell", "last") == (12, True, True) and seq_wheel_check("lucas", "root") == (24, True, True))
    lk = wheel_links()
    ok("wheel links: 60-quartet (1,29,31,59) touches the 24-quartets (1,11,13,23) and (5,7,17,19)", lk[(1, 29, 31, 59)] == [(1, 11, 13, 23), (5, 7, 17, 19)])
    ok("rank of apparition: alpha(37) = 19, alpha(89) = 11, alpha(11) = 10", (fib_rank(37), fib_rank(89), fib_rank(11)) == (19, 11, 10))
    # L1948: recurrence balance, bases, primitive primes
    ok("Lucas never balanced for 3 <= m <= 400; Pell defect = -m at m = 4, 8, ..., 1024; Fibonacci balanced only at 5, 25",
       all(seq_balance("lucas", m)["defect"] != 0 for m in range(3, 401)) and all(seq_balance("pell", 2 ** a)["defect"] == -2 ** a for a in range(2, 11))
       and [m for m in range(3, 101) if seq_balance("fibonacci", m)["defect"] == 0] == [5, 25])
    ok("bases with full quartets on both wheels (3..30): 6, 7, 10, 14, 18, 26, 27; base 12 has neither mirror",
       [x for x in range(3, 31) if base_wheels(x)[1] and base_wheels(x)[3]] == [6, 7, 10, 14, 18, 26, 27] and base_wheels(12) == (24, False, 10, False))
    pp = primitive_primes(19, 2000); pq = primitive_primes(37, 3000)
    ok("primitive primes: F(19) -> 37, 113; F(37) -> 73, 149, 2221; F(12) has none", pp["primitive_found"] == [37, 113] and pp["unexplained_cofactor"] == 1
       and pq["primitive_found"] == [73, 149, 2221] and primitive_primes(12)["primitive_found"] == [] and primitive_primes(12)["unexplained_cofactor"] == 1
       and primitive_primes(89, 2000)["cofactor_is_prime"] and primitive_primes(89, 2000)["unexplained_cofactor"] == 1665088321800481)
    # L1952: Theorem BG
    ok("Theorem BG: balance <=> m in the BG set, and balance <=> uniform distribution (a = 1..12, m = 3..300)",
       all(((ab_orbit(a, m)["defect"] == 0) == bg_set(a, m)) and ((ab_orbit(a, m)["defect"] == 0) == ab_orbit(a, m)["uniform"]) for a in range(1, 13) for m in range(3, 301)))
    # L1956: Theorem BG complete, Theorem BG* (general seeds)
    ok("Theorem BG*: u.d. <=> prediction for seeds 0..4 (a = 1..8, m = 3..150); Lucas seeds (2, a) never balanced when gcd(a, m) = 1; 2F balanced mod 12 (non-primitive seed)",
       all(ab_orbit(a, m, u, w)["uniform"] == ud_predict(a, m, u, w) for a in range(1, 9) for u in range(5) for w in range(5) if (u, w) != (0, 0) for m in range(3, 151))
       and all(ab_orbit(a, m, 2, a)["defect"] != 0 for a in range(1, 9) for m in range(3, 151) if __import__("math").gcd(a, m) == 1)
       and ab_orbit(1, 12, 0, 2)["defect"] == 0 and not ab_orbit(1, 12, 0, 2)["uniform"])
    # L1960: Theorem T* and Prop X
    import random as _r; _r.seed(5); _ok = True
    for _ in range(400):
        a = _r.choice([3, 5, 9, 15, 21, 7, 25]); m = _r.choice([3, 5, 7, 9, 15, 21, 25, 27, 45, 63, 75, 13, 39, 29, 145, 85, 53, 159, 11, 17])
        u, w = _r.randrange(m), _r.randrange(m)
        ans, _w = balance_predict(a, m, u, w)
        if ans is not None and ans != (ab_orbit(a, m, u, w)["defect"] == 0): _ok = False
    ok("Theorem T*: two-value balance s0 + s1 = -1 (mod G) and Prop X agree with direct orbits (400 random cases)", _ok)
    # L1964: audit fixes
    _F = [0, 1]
    for _ in range(300): _F.append(_F[-1] + _F[-2])
    ok("joint wheel: F(k+60) = 71 F(k) mod 90 for 240 terms (external audit, re-checked)", all((_F[k + 60] - 71 * _F[k]) % 90 == 0 for k in range(240)))
    _G = [_F[4 * t] for t in range(4)]
    ok("Lemma N: forward second difference of F(4t) is 5*G(t+1), not 5*G(t) (proof correction L1964)",
       _G[2] - 2 * _G[1] + _G[0] == 5 * _G[1] and _G[2] - 2 * _G[1] + _G[0] != 5 * _G[0])
    # L1968: 2-adic regime and audit regressions
    def _orb(a, m, u, w):
        x, y = u % m, w % m; x0, y0 = x, y; seq = []
        while True:
            seq.append(x); x, y = y, (a * y + x) % m
            if (x, y) == (x0, y0): return seq
    _ok = True
    for a in (2, 6, 10):
        for m in (4, 8, 16, 32):
            for u in range(m):
                for w in range(m):
                    if (u + w) % 2:
                        sq = _orb(a, m, u, w); c = (u if u % 2 else w) % 4
                        _ok &= len(sq) == m and all(sq.count(r) == (1 if r % 2 == 0 else (2 if r % 4 == c else 0)) for r in range(m))
    ok("Theorem 2B (audit): a = 2 mod 4, opposite-parity seeds mod 2^e: evens once, odd class c twice, the other never", _ok)
    ok("Theorem 2C: 4 | a with both seeds odd is never balanced mod 2^e (a = 4..32, e <= 6)",
       not any(2 * sum(_orb(a, 2 ** e, u, w)) == (2 ** e - 1) * len(_orb(a, 2 ** e, u, w)) for a in (4, 8, 12, 16, 32) for e in range(1, 7) for u in range(1, 2 ** e, 2) for w in range(1, 2 ** e, 2)))
    ok("Pell mod 2 is balanced (excluded case, m >= 3 in Theorem B_P); withdrawn Lemma Q closed form fails at F(5)",
       seq_balance("pell", 2)["defect"] == 0 and sum(__import__("math").comb(3, 2 * j) for j in range(3)) == 4 != 5)
    # L1972: Theorems 2D, 2E, T'
    _bad = 0; _cov = 0
    for a in (2, 4, 6, 8, 3, 9, 15, 25):
        for m in (4, 8, 16, 32, 3, 9, 27, 5, 25):
            for u in range(m):
                for w in range(m):
                    ans, _w = balance_predict(a, m, u, w)
                    if ans is not None:
                        _cov += 1; _bad += ans != (ab_orbit(a, m, u, w)["defect"] == 0)
    ok("Theorems 2D/2E/T' and earlier rules agree with direct orbits on every covered case (%d)" % _cov, _bad == 0 and _cov > 3000)
    # L1976: Theorem Q (quadratic regime) and the class-number corollary
    _bad = 0; _cov = 0
    for a in (3, 6, 9, 5, 10, 7):
        for m in (9, 27, 25, 125, 49):
            q = 3 if m % 3 == 0 else (5 if m % 5 == 0 else 7)
            if a % q: continue
            for u in range(0, m, q):
                for w in range(1, m):
                    if w % q == 0: continue
                    ans, why = balance_predict(a, m, u, w)
                    if why.startswith("Theorem Q"):
                        _cov += 1; _bad += ans != (ab_orbit(a, m, u, w)["defect"] == 0)
    _qr = lambda q: {x * x % q for x in range(1, q)}
    ok("Theorem Q: quadratic-regime predictions agree with direct orbits (%d cases); Dirichlet: sum of QR mod 23 = 92 = 23*22/4 - 23*h(-23)/2 with h = 3" % _cov,
       _bad == 0 and _cov > 300 and sum(_qr(23)) == 92)
    # L1980: dimension ladder
    _L = ladder_checks()
    ok("dimension ladder: 120 icosians, 24 Hurwitz units, SL(2,5) = 2I and SL(2,3) = 2T by order statistics, Q^2 mod 5 = order 10, E8 from golden quaternions (240 roots, profile 1/56/126/56/1)",
       _L["600-cell vertices (unit icosians)"] == 120 and _L["24-cell vertices (Hurwitz units) = kissing number of D4"] == 24 and _L["SL(2,5) order statistics = 2I"]
       and _L["SL(2,3) order statistics = 2T"] and _L["Fibonacci Q^2 mod 5 <-> icosian cos 36 deg: order"] == 10 and _L["E8 roots built from golden numbers"] == 240
       and all(p == [1, 56, 126, 56, 1] for p in _L["E8 inner-product profile (-2,-1,0,1,2) per root"]) and _L["class numbers = number of reduced planar lattices"])
    # L1984: regimes = conjugacy types; class-number bridge
    ok("clock types: Q^2 mod 5 has order 10 (a = 1, Fibonacci), 6 (a = 2, Pell), 1 (a = 5); class-number bridge: 1/31 digit sum 54 = 4.5*(15 - 3), 1/71: 126 = 4.5*(35 - 7)",
       [clock_type(a, 5)[0] for a in (1, 2, 5)] == [10, 6, 1] and class_number_bridge(31) == (15, 54, 3, True) and class_number_bridge(71) == (35, 126, 7, True))
    # L1988: partial Legendre sums
    ok("base-b identity sum_j A(floor(jq/b)) = (b - (b/q)) h(-q) for q in {23, 31, 47, 163}, b in {2, 10, 12}",
       all(partial_sum_dictionary(q, b)["holds"] for q in (23, 31, 47, 163) for b in (2, 10, 12)))
    # L1992: Theorem P'' and the digit formula for relative class numbers
    _ok = True
    for q, k in ((5, 3), (7, 2), (11, 2)):
        m = q ** k
        for c in range(0, m, max(1, m // 40)):
            for lam in (1, 2):
                _ok &= __import__('fractions').Fraction(sum((c + lam * u * u) % m for u in range(m)), m) == quad_mean_closed(q, k, c, lam)
    ok("Theorem P'': closed form of the quadratic-half mean at every level; digits of 1/q give h^-: 751 -> 135, 1609 -> 189473 (PARI-checked)",
       _ok and relative_class_number_from_digits(751) == (6, 135) and relative_class_number_from_digits(1609) == (8, 189473))
    # L1996: three-term strands and the Morse principle
    ok("three-term strands: (a, b) = (5, 10), seeds (8, 608, 366) mod 625 has a cubic (non-square) strand; a random strand mod 125 is uniform or squares",
       "other" in strand_types(5, 10, 5, 4, [8, 608, 366])[0] and set(strand_types(5, 5, 5, 3, [1, 2, 3])[0]) <= {"uniform", "squares"})
    # L2000: jet principle and the k-th power dictionary
    _m = 125; _C, _b = 7, 25 * 3
    _A = sorted((_C + _b * x ** 3 + 625 * x ** 4 + 125 * 2 * x ** 5) % _m for x in range(_m)); _B = sorted((_C + _b * w ** 3) % _m for w in range(_m))
    ok("jet principle (a cubic jet mod 125 has exactly the values C + b w^3); dictionary: 1/41 (k=8) and 1/79 (k=6) digit sums = (9/k) x k-th power means",
       _A == _B and kth_power_dictionary(41)[3] and kth_power_dictionary(79)[3] and kth_power_dictionary(53, 2)[3])
    # L2004: quartic class-number recurrence
    _mean, _pred, _B4, _hm = quartic_recurrence_demo(13)
    ok("Theorem Q4: order-4 recurrence mod 13^5 has mean exactly 4 + 13^4 [6 + 2 Re(conj chi4(1/6) B1(chi4))]; |B1(chi4)|^2/2 = 1 = h^- of the quartic field",
       abs(float(_mean) - _pred) < 1e-6 and round(_hm) == 1)
    # L2008: Theorem Q_k
    _r6 = qk_recurrence_demo(7, 6); _r3 = qk_recurrence_demo(7, 3)
    ok("Theorem Q_k: order-6 recurrence mod 7^7 mean exact, sees sextic h^- = 1; order-3 recurrence mean exact, sees no class number",
       abs(float(_r6[0]) - _r6[1]) < 1e-6 and _r6[2] == 1 and abs(float(_r3[0]) - _r3[1]) < 1e-6 and _r3[2] is None)
    # L2012: Theorem L (isolating L-values)
    ok("Theorem L: 4 scaled orbits of the order-4 recurrence mod 13^5 isolate B1(chi4) = -1 - i, B1(chi2) = 0, B1(chi4^3) = -1 + i",
       all(abs(Bi - Bd) < 1e-6 for _, Bi, Bd in isolate_L_values(13, 4)))
    # L2016: Theorems L+ and R (L(1,chi) and h*R from orbits)
    import math as _m
    _rows, _hR = orbit_L1_values(13, 2)
    ok("Theorem R: shifted-centre orbits mod 13^3 rebuild the quadratic character and give h*R = log((3+sqrt13)/2) for Q(sqrt13)",
       _rows[0][2] and abs(_hR - _m.log((3 + _m.sqrt(13)) / 2)) < 1e-8)
    _rows, _hR = orbit_L1_values(7, 3)
    _u = [2 * _m.cos(2 * _m.pi * a / 7) for a in (1, 2, 3)]
    _R = abs(_m.log(abs(_u[0])) * _m.log(abs(_u[2])) - _m.log(abs(_u[1])) ** 2)
    ok("Theorem R: orbits mod 7^4 give h*R = %.6f for the cyclic cubic field of conductor 7 (units 2cos(2 pi a/7))" % _R,
       all(r[2] for r in _rows) and abs(_hR - _R) < 1e-8)
    _rows, _ = orbit_L1_values(7, 6)
    ok("Theorem L+: odd chi mod 7 of order 2: L(1,chi) = pi/sqrt7 (h(-7) = 1) from orbits mod 7^7",
       abs(_rows[2][3] - _m.pi / _m.sqrt(7)) < 1e-8)
    # L2020: Theorem H2 (two recurrences, one class number)
    _hR, _t, _u, _R, _h = two_recurrence_class_number(229)
    ok("Theorem H2: Q(sqrt229): orbit h*R = 8.137396, DCF recurrence a = 15 (15^2 + 4 = 229) growth log R = 2.712465, so h = 3",
       _t == 15 and _u == 1 and abs(_h - 3) < 1e-6)
    ok("pell_minus_one_trace: 61 -> a = 39 (39^2 + 4 = 25 x 61), 257 -> a = 32 (u = 2)",
       pell_minus_one_trace(61) == (39, 5) and pell_minus_one_trace(257) == (32, 2))
    # L2024: Theorem BG- (minus-sign recurrences)
    _ok = all((lambda r, p: r[2] == p[0] and r[1] == p[1])(minus_orbit(A, M), bgminus_predict(A, M)) for A in range(0, 21) for M in range(2, 121))
    ok("Theorem BG-: x(n+1) = a x(n) - x(n-1), seeds (0, 1): u.d. and balance match the prediction for a <= 20, m <= 120; 'six' exception a = 3, m = 30 balanced, not u.d.",
       _ok and minus_orbit(3, 30)[1:] == (True, False))
    import random as _rnd; _rnd.seed(7)
    _cs = [(A, M, _rnd.randrange(M), _rnd.randrange(M)) for A, M in ((_rnd.randrange(30), _rnd.randrange(2, 150)) for _ in range(300))]
    ok("Theorem BG- (any seeds): u.d. prediction matches 300 random orbits (degeneracy 2 s1 - a s0 at odd p, s0 + s1 odd at 2)",
       all(minus_orbit(*c)[2] == bgminus_predict(*c)[0] for c in _cs))
    # L2028: Theorem H2- (q = 3 mod 4) and the Pell / chi_{-4} law
    ok("Pell mod 2^e (e = 2..10): each residue hit 1 + chi_-4(r) times; balance miss = -1/2 = B1(chi_-4) (Q(i), h = 1)",
       all(pell_chi4_law(e) == (True, __import__("fractions").Fraction(-1, 2)) for e in range(2, 11)))
    _r3, _r79 = class_number_3mod4(3), class_number_3mod4(79)
    ok("Theorem H2-: Q(sqrt3): unit 2+sqrt3 from x(n+1) = 4x(n) - x(n-1), h = 1; Q(sqrt79): characters mod 316 rebuilt exactly, a = 160 (160^2 - 4 = 4 x 79 x 9^2), h = 3",
       _r3[5] and _r3[1] == 4 and abs(_r3[4] - 1) < 1e-9 and _r79[5] and (_r79[1], _r79[2]) == (160, 9) and abs(_r79[4] - 3) < 1e-9)
    # L2032: every quadratic field (Theorem H2*) and the chi_-8 reader
    ok("Lemma P8: x(n+1) = 4x(n) - x(n-1) from (1,1) mod 2^e (e = 3..10) hits r exactly 1 + chi_-8(r) times (odd r), evens never",
       all(chim8_reader_law(e) for e in range(3, 11)))
    ok("Lemma P8': x(n+1) = 3x(n) + 3x(n-1) - x(n-2) from (1,1,7) mod 2^e (e = 3..10) hits r exactly 1 + chi_8(r) times (odd r)",
       all(chi8_reader_law(e) for e in range(3, 11)))
    _H = {D: class_number_quadratic(D) for D in (-420, -23, -8, 5, 8, 12, 136, 316)}
    ok("Theorem H2*: h(-420) = 8, h(-23) = 3, h(-8) = 1; Q(sqrt5), Q(sqrt2), Q(sqrt3) have units from Fibonacci (t=1), Pell (t=2), 4x-x (t=4); h(136) = 2, h(316) = 3",
       [round(_H[D][0]) for D in (-420, -23, -8, 5, 8, 12, 136, 316)] == [8, 3, 1, 1, 1, 1, 2, 3]
       and all(abs(_H[D][0] - round(_H[D][0])) < 1e-9 for D in _H) and [_H[D][1][0] for D in (5, 8, 12)] == [1, 2, 4])
    # L2036: cyclic cubic fields (Theorem C3)
    _lb, _g = cubic_classes(13, brute=True); _ls, _ = cubic_classes(13)
    ok("Lemma C1: cube classes mod 13 from the order-3 orbit mod 13^4: full period (2197 steps) = 13-term shortcut = index_g mod 3",
       _lb == _ls and all(pow(s_, 4, 13) == pow(_g, 4 * _lb[s_], 13) for s_ in range(1, 13)))
    _c7, _c163 = cubic_class_number(7), cubic_class_number(163)
    ok("Theorem C3: conductor 7: h = 1, unit x^3 + x^2 - 2x - 1; conductor 163: h = 4 (root extraction depth), unit x^3 - 11x^2 - 14x - 1, R = 6.4437",
       _c7[:3] == (1, -1, -2) and _c163[:3] == (4, 11, -14) and abs(_c163[3] - 6.4437348822) < 1e-6 and abs(_c163[4] - 4 * _c163[3]) < 1e-6)
    # L2040: rigorous cubic certificates (Theorem C3*) and real cyclic quartic fields
    _lq, _gq, _okq = quartic_classes(41)
    ok("Lemma C1 (k = 4): quartic classes mod 41 from four order-4 orbits mod 41^5 = index_g mod 4", _okq)
    if HAVE_MP:
        _cc = cubic_certificate(163)
        ok("Theorem C3*: h = 4 for conductor 163 certified (periods, exact unit norm, v = +-eps^beta, no deeper root)", _cc["certified"] and _cc["h"] == 4 and _cc["unit_poly"] == (1, -11, -14, -1))
        _cc7 = cubic_certificate(7)
        ok("Theorem C3*: h = 1 for conductor 7 certified (Lemma D replaced by a finite enumeration)", _cc7["certified"] and _cc7["h"] == 1)
        _q4 = quartic_class_number(257, 5)
        ok("real cyclic quartic, conductor 257: saturation finds the cube root, h = 3", abs(_q4[0] - 3) < 1e-9 and None not in _q4[3])
    # L2044: rigorous quartic certificates (Theorem Q4R*)
    if HAVE_MP:
        _c17, _c257 = quartic_certificate(17), quartic_certificate(257)
        ok("Theorem Q4R*: conductor 17 certified h = 1; conductor 257 certified h = 3 = |det X| (every prime l up to the regulator bound)",
           _c17["certified"] and _c17["h"] == 1 and _c257["certified"] and _c257["h"] == 3)
    # L2048: one certifier for degrees 3, 4, 6 (Theorem H_n*)
    _l6, _ok6 = cyclic_classes(37, 6)
    ok("Lemma C1_n (n = 6): sextic classes mod 37 from six order-6 orbits mod 37^7 = index_g mod 6", _ok6)
    if HAVE_MP:
        _s13, _s37 = cyclic_certificate(13, 6), cyclic_certificate(37, 6)
        ok("Theorem H_n*: real cyclic sextic fields of conductor 13 and 37 certified, h = 1 (try 229 -> 3 from the menu)", _s13["certified"] and _s13["h"] == 1 and _s37["certified"] and _s37["h"] == 1)
    # L2052: imaginary cyclic quartic and sextic fields (Theorem I_n)
    _i4, _i6 = imaginary_cyclic_class_number(389, 4), imaginary_cyclic_class_number(379, 6)
    ok("Theorem I_n: h-(quartic, conductor 389) = 41 = N(5 - 4i); h-(sextic, conductor 379) = 117 = h(Q(sqrt -379)) x 39, 39 = N(-5 - 2 zeta6) (exact integers)",
       _i4["h_minus"] == 41 and _i6["h_minus"] == 117)
    if HAVE_MP:
        ok("Theorem I_n: h+ certified (Q(sqrt 389): 1; cubic field of conductor 379: 1), so h = 41 and 117", _i4["certified_plus"] and _i4["h"] == 41 and _i6["certified_plus"] and _i6["h"] == 117)
    # L2056: relative class numbers as norms (Theorem N_n)
    _r8, _r12 = relative_class_number(233, 8), relative_class_number(157, 12)
    ok("Theorem N_n: octic conductor 233: h- = N(gamma) = 1433, gamma in Z[zeta8]; degree 12, conductor 157: h- = 65 = 5 (quartic subfield) x N(gamma) = 13",
       _r8["h_minus"] == 1433 and _r12["h_minus"] == 65 and _r12["sub"] == 5)
    ok("Theorem N_n agrees with Theorem I_n: quartic 389 -> 41, sextic 379 -> 117",
       relative_class_number(389, 4)["h_minus"] == 41 and relative_class_number(379, 6)["h_minus"] == 117)
    _r10 = relative_class_number(271, 10)
    ok("Theorem N (any even n): degree 10, conductor 271: h- = 341 = h(Q(sqrt -271)) 11 x N(x/2) 31 (Lemma N2: 2 | x)", _r10["h_minus"] == 341 and _r10["factors"] == [(2, 11), (10, 31)])
    # L2064: norm-factor statistics
    _cnt, _rows = norm_factor_statistics(6, 3000, primes=(7,))
    ok("L2064: Eisenstein factor N(x_6/2), q < 3000 (%d fields): 7 divides it with frequency %.2f, Cohen-Lenstra-Martinet predicts %.2f" % (_cnt, _rows[0][1], _rows[0][2]),
       _cnt > 50 and abs(_rows[0][1] - _rows[0][2]) < 0.15)
    # L2068: Law P (2-part link between the sextic Eisenstein factor and the real cubic subfield)
    if HAVE_MP:
        _p163, _p31 = two_part_link(163), two_part_link(31)
        ok("Law P: q = 163: F = 4 and h(K3) = 4 (both even); q = 31: F = 1 and h(K3) = 1 (both odd)",
           (_p163["F"], _p163["h3"], _p163["agree"]) == (4, 4, True) and (_p31["F"] % 2, _p31["h3"] % 2, _p31["agree"]) == (1, 1, True))
    # L2072: harmonic links
    _hl = harmonic_links(10)
    ok("L2072 harmonic links: sum F_k/2^(k+1) = 1, sum F_k/10^(k+1) = 1/89, clock law at 89 (period 44 = Pisano 44), F_p = (p/5) mod p, 60/24 from 2, 3, 5 (+ L-values with mpmath)",
       all(v for _, v in _hl))
    # L2076: necklace ladder and spiral law
    _nl = {b_: n_ for b_, n_, _ in necklace_ladder(12)}
    _p1, _p2, _p0 = two_adic_pattern(491, 14), two_adic_pattern(239, 14), two_adic_pattern(31, 6)
    ok("L2080 Law P* pattern: q = 491 (n = 14) both primes above 2 divide x/2 (h+ = 8, narrow 64); q = 239 exactly one (h+ = 1, narrow 8); q = 31 (n = 6) none", (_p1["k"], _p1["g"], _p1["f"], _p2["k"], _p0["k"]) == (2, 2, 3, 1, 0))
    _h14, _h6 = two_adic_heuristic(14), two_adic_heuristic(6)
    ok("L2084 Law S: n = 14 has 2 non-self-conjugate primes of degree 3 (naive 0.2614, observed 383/1499); n = 6 one self-conjugate prime of degree 2", (_h14["f"], _h14["g"], _h14["self_conjugate"], round(_h14["naive"], 4), _h6["self_conjugate"], _h6["f"]) == (3, 2, False, 0.2614, True, 2))
    _h14b = two_adic_heuristic(14)
    ok("L2088 BVV pair law for n = 14: P(exactly one prime | not both) = 2/9 (observed 2687/11997 = 0.224); n = 6 self-dual: narrow = wide", abs(_h14b["bvv_one_given_not_both"] - 2 / 9) < 1e-12 and two_adic_heuristic(6)["narrow_equals_wide"])
    _c30, _c42 = component_pattern(1951, 30), component_pattern(1051, 42)
    ok("L2092 component pattern: n = 30, q = 1951 only the cubic piece (m = 6); n = 42, q = 1051 only the order-21 piece (m = 42)", [_c30[m][0] for m in (6, 10, 30)] == [1, 0, 0] and [_c42[m][0] for m in (6, 14, 42)] == [0, 0, 1] and _c42[42][2] == 6)
    _fc = [cubic_parity_fast(qq)[0] for qq in (31, 163, 547, 607, 1087)]
    ok("L2096 fast cubic parity (L-function route) agrees with Theorem N: q = 31 odd, 163, 547, 607 even, 1087 odd", _fc == [False, True, True, True, False] and all(two_part_link(qq)["F_even"] == f_ for qq, f_ in zip((31, 163, 547, 607, 1087), _fc)))
    _ok = True
    for _n, _q in ((10, 191), (14, 491), (14, 239)):
        _g = int(primitive_root(_q)) if 'primitive_root' in globals() else next(t for t in range(2, _q) if all(pow(t, (_q - 1) // p, _q) != 1 for p in factor(_q - 1)))
        _c = [0] * _n; _t = 1
        for _j in range(_q - 1): _c[_j % _n] += _t; _t = _t * _g % _q
        _ok = _ok and fast_minus_coordinates(_q, _n)[0] == [v // _q for v in _cyc_reduce(_c, _n)]
    ok("L2100 O(sqrt q) minus-part coordinates equal the exact 1/q label sums (n = 10, q = 191; n = 14, q = 491, 239)", _ok)
    _U = [theorem_U(qq, ll) for qq, ll in ((163, 3), (31, 3), (547, 3), (3931, 5), (191, 5), (491, 7), (239, 7), (419, 11))]
    ok("L2104 Theorem U holds (l = 3, 5, 7, 11) and gives h(cubic) even for q = 163, 547, odd for 31; quintic q = 3931 even, 191 odd", all(u["identity_holds"] for u in _U) and [u["h_plus_even_if_2_primitive"] for u in _U[:5]] == [True, False, True, True, False])
    _pc = [parity_certificate(qq, ll) for qq, ll in ((491, 7), (239, 7), (4019, 7), (163, 3), (31, 3))]
    ok("L2108/L2124 parity certificates: l = 7, q = 491 narrow and wide even, 239 narrow even but wide odd, 4019 odd; cubic 163 even, 31 odd", [(p_["narrow_even"], p_["wide_even"]) for p_ in _pc] == [(True, True), (True, False), (False, False), (True, True), (False, False)])
    _tb = [two_rank_bound(qq, 3) for qq in (163, 31)]
    ok("L2112 Theorem M bounds: cubic q = 163 has v2(F) = 2 so 2-rank <= 2 (actual 2); q = 31 odd so rank 0", (_tb[0]["v2F"], _tb[0]["rank_lower_bound"], _tb[1]["v2F"]) == (2, 2, 0))
    _m18 = minus_two_part(163, 18)
    ok("L2116 minus 2-part: degree-18 field of conductor 163 has v2(h-) = 2 (from the sextic factor), matching narrow 2-rank 2 of the nonic subfield", _m18["v2_minus"] == 2)
    _dp = [dual_pair_parity(qq, 7) for qq in (491, 239, 4019)]
    ok("L2120 dual-pair parity, l = 7: q = 491 both primes divide (h+ = 8, proved even); 239 one prime; 4019 none", [d_["wide_even_proved"] for d_ in _dp] == [True, False, False] and len(_dp[1]["divides"]) == 1 and _dp[0]["pairs"] == [(0, 1)])
    _w31 = dual_pair_parity(311, 31)
    ok("L2124 Theorem W, l = 31, q = 311: two primes divide but they are not conjugate, so h+ is odd (PARI: h+ = 1)", _w31["divides"] == [3, 5] and not _w31["h_plus_even"])
    _pa = [parity_any_degree(qq, 9)["h_plus_even"] for qq in (163, 3727, 19, 127)]
    ok("L2128 Theorem W composite form, degree 9: q = 163, 3727 even (from the cubic piece), q = 19, 127 odd (PARI agrees)", _pa == [True, True, False, False])
    _cs = [certificate_strength(qq, ll) for qq, ll in ((491, 7), (239, 7), (163, 3))]
    ok("L2132/L2140 certificate strength: l = 7, q = 491 even, 239 odd, cubic 163 even -- all Greither-free since L2140", [(c_["h_plus_even"], c_["greither_free"]) for c_ in _cs] == [(True, True), (False, True), (True, True)])
    _sv = [septic_valuations(qq)["v"] for qq in (491, 239, 17431, 4019)]; assert septic_valuations(491)["certificate"].startswith("h+ even")
    ok("L2136 septic valuations of B/2 at the two primes above 2: 491 (1,1), 239 (0,2), 17431 (1,2), 4019 (0,0); 3(v1+v2) = v2(F)", _sv == [(1, 1), (0, 2), (1, 2), (0, 0)])
    _tab = [(qq, ll, dual_pair_parity(qq, ll)["h_plus_even"]) for qq, ll in ((223, 3), (607, 3), (211, 7), (967, 7), (191, 5), (3931, 5))]
    ok("L2140 manuscript appendix rows reproduced: h+ parity (PARI h+ = 1, 4, 1, 1, 11, 256) from the 1/q labels alone", [e for _, _, e in _tab] == [False, True, False, False, False, True])
    _pr = parity_report(491, 7)
    ok("L2144 parity report for q = 491, l = 7: sign vector 1111111, narrow even, h+ even", _pr[1].endswith("1111111") and _pr[3].endswith("True (Theorem M / Law P*)") and _pr[4].startswith("class number h(K+) even: True"))
    _cc = citation_checklist()
    ok("L2148/L2152 citation checklist: 5 items, BVV verbatim, Greither confirmed from scans (Theorem R subcase only)", len(_cc) == 5 and _cc[-1][2] == "confirmed verbatim" and "not W" in _cc[3][1] and _cc[3][2].startswith("confirmed"))
    ok("L2152 Greither Cor. 4.15 statement recorded (p = 2 included, large circular units C_1F)", "p = 2 included" in greither_cor_4_15() and "C_1F" in greither_cor_4_15())
    _st = fibonacci_staircase(10, 44)
    ok("L2156 Fibonacci staircase with carries reproduces the 44-digit period of 1/89; digital roots agree only at 20 places", "".join(map(str, _st["digits"])) == "01123595505617977528089887640449438202247191" and len(_st["agree"]) == 20)
    _ms = [metallic_stairs(a_, 10, 120) for a_ in (1, 2, 3)]
    ok("L2160 reverse stairs: sum F_k 10^(k-1) = -1/109 (10-adic), last 46 digits 8073394495412844036697247706422018348623853211 (= 1/109 period positions 63-108); Pell -> -1/119, a=3 -> -1/129",
       [m_["m_reverse"] for m_ in _ms] == [109, 119, 129] and all(m_["reverse_is_repetend_backwards"] for m_ in _ms)
       and "".join(map(str, _ms[0]["reverse_digits_units_first"][:46]))[::-1] == "8073394495412844036697247706422018348623853211"
       and [m_["m_forward"] for m_ in _ms] == [89, 79, 69] and [m_["period_reverse"] for m_ in _ms] == [108, 48, 21])
    _r89, _r109 = rung_period(10, -1), rung_period(10, 1)
    _qr = all((lambda d: (not d["prime"]) or d["p"] == 5 or (d["b_qr"] == (b_ % 4 != 3) and d["lemma_ok"]))(rung_period(b_, -1)) for b_ in range(3, 260))
    ok("L2164 rungs: 1/89 period 44 = Pisano(89), 10 = 2 mod 4 so never full; 1/109 period 108 = Pisano(109) in base 10 and 11, 11 = 1/10 is a Fibonacci primitive root of 109; QR theorem b QR <=> b != 3 mod 4 and Pisano lemma for b < 260",
       (_r89["period"], _r89["pisano"], _r89["full"]) == (44, 44, False) and (_r109["period"], _r109["pisano"], _r109["fpr"]) == (108, 108, True)
       and rung_period(11, -1)["period"] == 108 and pow(10, -1, 109) == 11 and _qr)
    def _isp(n):
        if n < 2: return False
        i = 2
        while i * i <= n:
            if n % i == 0: return False
            i += 1
        return True
    _lg = _ml = True; _pell_full = 0
    for a_ in range(1, 9):
        for b_ in range(a_ + 2, 400):
            q_ = b_ * b_ - a_ * b_ - 1
            if q_ == 5 or not _isp(q_): continue
            leg = 1 if pow(b_, (q_ - 1) // 2, q_) == 1 else -1
            if residue_minus_one(b_, q_) != leg: _lg = False
            if metallic_mod4_law(a_, b_) != (leg == -1): _ml = False
    _C = rung_constant(100000)
    ok("L2168 Lemma G (p = -1 mod b) and Theorem Q* (metallic mod-4 law, Pell never full) for a <= 8, b < 400; 1/79 has odd period 13; Euler constant C = 0.7179",
       _lg and _ml and rung_period(10, -1)["p"] == 89 and pow(10, 13, 79) == 1 and 0.7170 < _C < 0.7190)
    _pc = 0; _sv = bytearray([1]) * 9698; _sv[0:2] = b"\x00\x00"
    for i_ in range(2, 99):
        if _sv[i_]: _sv[i_ * i_::i_] = bytearray(len(_sv[i_ * i_::i_]))
    _pc = sum(_sv)
    _s2 = stride_stair(2)
    _a, _b2, _n = 0, 1, 0
    while True:
        _a, _b2 = _b2, (_a + _b2) % 9701; _n += 1
        if (_a, _b2) == (0, 1): break
    ok("L2172 9701: D(2701) = 9697 (prime #1197), D(2702) = 9701 = 89*109 = stride-2 stair 1/9701, period 1188 = Pisano(9701); partner 10301; 47525^2 - 24*9701^2 = 1; m = 3 gives 995999",
       digits_used(2701) == 9697 and digits_used(2702) == 9701 and _sv[9697] and _pc == 1197 and _s2["N"] == 9701 and _s2["period"] == 1188
       and _n == 1188 and _s2["alt_N"] == 10301 and 47525 ** 2 - 24 * 9701 ** 2 == 1 and stride_stair(3)["N"] == 995999 and stride_stair(3)["F_m"] == 2)
    def _isp2(n):
        if n < 2: return False
        i = 2
        while i * i <= n:
            if n % i == 0: return False
            i += 1
        return True
    _q_ok = all(metallic_mod4_law(a_, b_) == (pow(b_, (q_ - 1) // 2, q_) == q_ - 1)
                for a_ in range(1, 13) for b_ in range(a_ + 1, 300) for q_ in [b_ * b_ - a_ * b_ - 1] if q_ > 2 and (a_ * a_ + 4) % q_ and _isp2(q_))
    ok("L2176 Theorem 1.1 closed form on all metallic rungs a <= 12, b < 300; Psi_d: 89, 109, 11191, 10301, 112347191, 9211",
       _q_ok and [fib_cyclotomic(d_) for d_ in range(1, 7)] == [89, 109, 11191, 10301, 112347191, 9211])
    ok("L2180 metallic constants with the Lucas-power correction: M(4) = 3, M(11) = 5, M(29) = 7, M(36) = 3; C_1 = 0.718, C_3 = 0.972, C_4 = 0.589, C_11 = 0.435",
       [metallic_power_index(x_) for x_ in (1, 3, 4, 11, 29, 36)] == [1, 1, 3, 5, 7, 3]
       and abs(metallic_constant(1) - 0.7179) < 0.001 and abs(metallic_constant(3) - 0.9719) < 0.001
       and abs(metallic_constant(4) - 0.5892) < 0.001 and abs(metallic_constant(11) - 0.4353) < 0.001 and metallic_constant(2) == 0.0)
    ok("L2184 golden index law: P(index = 3, 5, 7) = 0.0598, 0.0766, 0.0299 (data 0.0617, 0.0758, 0.0294); 1/89 has index 2",
       [round(golden_index_law(l_), 4) for l_ in (3, 5, 7)] == [0.0598, 0.0766, 0.0299] and 88 // rung_period(10, -1)["period"] == 2)
    ok("L2188 metallic index law: a = 1 reproduces 0.0598/0.0766; a = 4: P(i = 3) = 0.2946; a = 11: P(i = 5) = 0.4179; a = 3: 3, 5, 7 never divide",
       [round(metallic_index_law(1, l_), 4) for l_ in (3, 5)] == [0.0598, 0.0766] and abs(metallic_index_law(4, 3) - 0.2946) < 0.001
       and abs(metallic_index_law(11, 5) - 0.4179) < 0.001 and all(metallic_index_law(3, l_) == 0.0 for l_ in (3, 5, 7)))
    _na = novelty_audit()
    ok("L2192/L2200 novelty audit: 11 zbMATH documents all read; Aigner 1975 overlaps only the p = 1 mod 4 golden case",
       len(_na) == 11 and sum(1 for r_ in _na if r_[1].startswith("read")) == 11 and _na[0][2].startswith("partial"))
    _ac = arxiv_checklist()
    ok("L2196/L2200 arXiv checklist: 7 items, 1 open (endorsement)", len(_ac) == 7 and sum(1 for _, st_ in _ac if st_.startswith("OPEN")) == 1)
    _acs = [aigner_cubic(b_) for b_ in range(4, 400) if _isp2(b_ * b_ - b_ - 1) and (b_ * b_ - b_ - 2) % 3 == 0]
    ok("L2200 Aigner's cubic criterion for the base: b cube mod p <=> p = x^2 + 135 y^2 (golden rungs, b < 400)", len(_acs) > 10 and all(c_ == f_ for c_, f_ in _acs))
    _mc = [metallic_cubic_check(a_, 8000) for a_ in (1, 2, 3, 5)]
    ok("L2204 metallic Aigner: beta_a is a cube mod every prime x^2 + 27 d y^2 (a = 1, 2, 3, 5; p < 8000)", all(k_ == n_ and n_ > 0 for k_, n_ in _mc))
    _ch = [metallic_chain(b_, g_) for b_, g_ in ((1, 10), (2, 6), (3, 5))]
    ok("L2208 metallic chains: N = 144, 239, 469; strong-bond frequency -> beta/(beta+1); hydrogen Halpha/Hbeta = 27/20 (rational); Z = 79 is gold",
       [c_["N"] for c_ in _ch] == [144, 239, 469] and abs(metallic_chain(2, 10)["nu"] - (1 + 2 ** 0.5) / (2 + 2 ** 0.5)) < 1e-6
       and str(hydrogen_line_ratio(2, 4, 2, 3)) == "27/20" and periodic_table_rungs()[79].startswith("Au"))
    _m8 = e8_masses(); _ph = (1 + 5 ** 0.5) / 2
    ok("L2212 E8: four golden pairs m2/m1 = m6/m3 = m7/m4 = m8/m5 = phi; E8 rung 93139201 has ord(10) = 363825; golden rung 89 = (x^2-x-1)(10)",
       all(abs(_m8[i] / _m8[j] - _ph) < 1e-12 for i, j in ((1, 0), (5, 2), (6, 3), (7, 4))) and e8_rung() == 93139201
       and pow(10, 363825, 93139201) == 1 and all(pow(10, 363825 // q_, 93139201) != 1 for q_ in (3, 5, 7, 11)) and 10*10 - 10 - 1 == 89)
    _gp = all(chi_base_pm1(b_, q_, -1) == (1 if pow(b_, (q_ - 1) // 2, q_) == 1 else -1)
              for b_ in range(3, 200) for q_ in [b_ ** 3 + 2 * b_ - 1] if _isp2(q_))
    ok("L2216 general principle (p = f(b), f(0) = +-1) on f = x^3 + 2x - 1; cosine rungs psi_10(10) = 89, psi_5(10) = 109, psi_9(10) = 971, psi_12(10) = 97",
       _gp and [cosine_rung(n_) for n_ in (10, 5, 9, 12)] == [89, 109, 971, 97])
    ok("L2220 psi_n exact (psi_10 = x^2 - x - 1, psi_7 = x^3 + x^2 - 2x - 1); cosine families: n = 10 -> b = 3 mod 4, n = 5 -> b = 2 mod 4, n = 14, 23, 24 never full",
       psi_poly(10) == [-1, -1, 1] and psi_poly(7) == [-1, -2, 1, 1] and cosine_full_period_classes(10) == [3, 7, 11, 15]
       and cosine_full_period_classes(5) == [2, 6, 10, 14] and all(cosine_full_period_classes(n_) == [] for n_ in (14, 23, 24)))
    _bf = lambda n_, b_: sum(len(_tobase(k_, b_)) for k_ in range(1, n_ + 1))
    ok("L2224 DSO: closed form = brute force (n < 3000, bases 2, 3, 10, 16); D(10) = 11, D(49) = 89, D(44) = 79, D(108) = 216, D(157) - D(78) = 216, D(2701) = 9697; inverse",
       all(dso(n_, b_) == _bf(n_, b_) for b_ in (2, 3, 10, 16) for n_ in list(range(1, 300)) + [999, 1000, 1001, 2999])
       and [dso(x_) for x_ in (10, 49, 44, 108, 2701)] == [11, 89, 79, 216, 9697] and dso(157) - dso(78) == 216
       and dso_inverse(9701) == 2702 and dso_inverse(12) is None and digits_used(2701) == dso(2701))
    ok("L2224 mod-24 law (proved by finite check over q mod 48): prime-n cosine families never have full period iff q = +-1 mod 24",
       all((cosine_full_period_classes(q_) == []) == (q_ % 24 in (1, 23)) for q_ in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 73, 97)))
    _al, _bl = dso_prime_lengths(24)
    ok("L2228 DSO log form exact (round(.) = D for n < 5000 and 10^6 + 7); D never prime for 3-, 6-, 9-, 22-digit n; D(n) for 3-digit n divisible by 3",
       all(round(dso_log_form(n_)) == dso(n_) for n_ in list(range(1, 5000)) + [10 ** 6 + 7]) and _bl == [3, 6, 9, 12, 15, 18, 21, 22, 24]
       and all(dso(n_) % 3 == 0 for n_ in range(100, 1000)))
    _st = dso_stair(3, 1200)
    ok("L2232 DSO stair: 3-digit blocks equal D(n) for n = 1..367, D(369) = 999; n = 2q cosine families never full iff q = +-1 mod 8",
       all(int(_st[3 * n_:3 * n_ + 3]) == dso(n_) for n_ in range(1, 368)) and dso(369) == 999
       and all((cosine_full_period_classes(2 * q_) == []) == (q_ % 8 in (1, 7)) for q_ in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59)))
    ok("L2236 cosine-family law (proved for q^k, 2q^k; conjectured otherwise) agrees with the exact class table for all admissible 5 <= n <= 200, n != 6",
       all(bool(cosine_full_period_classes(n_)) == cosine_family_law(n_) for n_ in range(5, 201) if n_ != 6 and psi_poly(n_)[0] in (1, -1)))
    ok("L2240 3q^k law: 15, 21, 51, 75 possible; 33, 39, 69 blocked; 27, 54 possible; totative parity even for 35, 77, 1001",
       [cosine_family_law(n_) for n_ in (15, 21, 51, 75, 33, 39, 69, 27, 54)] == [True] * 4 + [False] * 3 + [True] * 2
       and all(x_ % 2 == 0 for n_ in (35, 77, 1001) for x_ in totative_parity(n_)))
    ok("L2244 transfer lemma: (-1)^mu(a) = a^(phi/2) for N <= 120, a in {2, 3}; = +1 for non-cyclic N (35, 77, 91, 143)",
       all(len({*transfer_sign(a_, N_)}) == 1 for N_ in range(3, 121) for a_ in (2, 3) if N_ % a_)
       and all(transfer_sign(a_, N_) == (1, 1) for N_ in (35, 77, 91, 143) for a_ in (2, 3)))
    _lc = legendre_code(131)
    _ac = [sum(_lc[i] * _lc[(i + t_) % 131] for i in range(131)) for t_ in range(1, 131)]
    _st, _od = pr_interleave(list(range(108)), 109, 11)
    ok("L2248 Welch-Costas from rung prime 109 (g = 11) is Costas; Legendre code of 131 has autocorrelation -1 off-peak; interleaver round-trips; rung generators start (41, 7), (109, 11)",
       is_costas(costas_welch(109, 11)) and set(_ac) == {-1} and pr_deinterleave(_st, _od) == list(range(108)) and rung_generators(60)[:2] == [(41, 7), (109, 11)])
    _ts = coded_strobe_times()
    ok("L2256 coded strobe: 108 sample times, one per frame, sub-frame slots form a permutation of 0..107",
       len(_ts) == 108 and sorted(round((t_ * 60 - int(t_ * 60 + 1e-9)) * 108) for t_ in _ts) == list(range(108)))
    _vals = [1, 2, 3, 4, 89, 109, 9701, 2701]
    _fl = fibonacci_lattice(11)
    ok("L2260 Fibonacci code round-trips (no internal '11'); Fibonacci lattice F_11 = 89 points with generator 55; golden strobe has 300 off-grid times",
       fib_code_decode(fib_code_encode(_vals)) == _vals and all("11" not in fib_code_encode([v_])[:-1] for v_ in _vals)
       and len(_fl) == 89 and _fl[1] == (1 / 89, 55 / 89) and len(golden_strobe_times()) == 300)
    ok("L2264 Korobov: rung multiplier b = 40 for p = 1559 is catastrophic in 3D (P2 > 1, dual vector (1,1,-1)) while a typical multiplier is < 0.05",
       rung_korobov_warning(1559, 40) and korobov_P2(1559, [1, 40, 1600 % 1559]) > 1 and korobov_P2(1559, [1, 300, 300 * 300 % 1559]) < 0.05)
    _ho = hybrid_interleave()
    ok("L2268 hybrid interleave: permutation of 4080, groups of 16 hold distinct codewords, inverse works", sorted(_ho) == list(range(4080)) and all(len({x // 255 for x in _ho[16*i:16*i+16]}) == 16 for i in range(255)) and hybrid_deinterleave([_ho[k] for k in range(4080)], _ho) == list(range(4080)))
    _tk, _fc = coded_strobe_grid()
    ok("L2268 strobe grid: 700 distinct ticks of a 42 kHz clock, one per frame", len(set(_tk)) == 700 and _fc == 42000.0 and all(_tk[n_] // 700 == n_ for n_ in range(700)))
    _a1 = interleave_audit(helical_interleave(5, 25, 1), 5, 25, 5); _a2 = interleave_audit(helical_interleave(4, 17, 1), 4, 17, 4)
    _a3 = interleave_audit(helical_interleave(10, 40, 1), 10, 40, 10); _a4 = interleave_audit(helical_interleave(4, 16, 2), 4, 16, 4)
    ok("L2272 helical audit: m=t=5,n=25 optimal (25, []); n=mt+1 fails at d=m^2=16; m=t=10,n=40 fails at d=4 (not a prime power); even step u=2 fails", _a1 == (25, []) and 16 in _a2[1] and _a3[1][:1] == [4] and _a4[1] != [] and helical_optimal_predict(16, 255, 16) and not helical_optimal_predict(10, 40, 10))
    _tm = digit_sum_rotation(2, 16); _O2 = helical_interleave(2, 255, rot=_tm); _O4 = helical_interleave(4, 255, rot=digit_sum_rotation(4, 16))
    _f36 = [int(c) for c in "012012120120201201"]
    ok("L2276 perfect layouts: Thue-Morse depth-2 and digit-sum depth-4 RS(255,223) audits perfect; (3,6) balanced; (6,6) obstruction g=4", "".join(map(str, _tm)) == "0110100110010110" and interleave_audit(_O2, 2, 255, 16) == (32, []) and interleave_audit(_O4, 4, 255, 16) == (64, []) and interleave_balanced(_f36, 3, 6) and interleave_obstruction(6, 6) == [4] and interleave_obstruction(16, 16) == [])
    _b36 = balanced_layout(3, 6); _b510 = balanced_layout(5, 10)
    _L3 = layout_from_period([int(c) for c in RS255_PERFECT_PERIODS[3]], 3, 255)
    ok("L2280 construction balanced for (3,6),(5,10); depth-3 RS(255,223) period perfect at n = 255 (burst 48, no unforced periods)", interleave_balanced(_b36, 3, 6) and interleave_balanced(_b510, 5, 10) and interleave_audit(_L3, 3, 255, 16) == (48, []))
    _st = staircase_layout(8, 16)
    ok("L2284 staircase: (k + floor(k/t)) mod m balanced for (8,16),(3,6),(9,18); RS(255,223) depth 8 audit (128, []); RS(255,239) impossible (n > t^2)", interleave_balanced(_st, 8, 16) and interleave_balanced(staircase_layout(3, 6), 3, 6) and interleave_balanced(staircase_layout(9, 18), 9, 18) and interleave_audit(layout_from_period(_st, 8, 255), 8, 255, 16) == (128, []) and perfect_interleave_status(4, 8, 255).startswith("impossible") and staircase_layout(4, 4) == [((k % 4) + k // 4) % 4 for k in range(16)])
    ok("L2288 averaging obstruction: (2,7,28),(2,7,42),(5,16,80) impossible; (3,16,255),(2,8,48),(5,4,12) not flagged", all(averaging_obstruction(*c_) for c_ in ((2, 7, 28), (2, 7, 42), (5, 16, 80))) and not any(averaging_obstruction(*c_) for c_ in ((3, 16, 255), (2, 8, 48), (5, 4, 12))))
    ok("L2292 sharpened averaging: (2,9,43) now flagged; (3,16,255) still not; condition C' true for (16,16),(11,8), false for (8,5),(2,5)", averaging_obstruction(2, 9, 43) is not None and averaging_obstruction(3, 16, 255) is None and interleave_condition_C(16, 16) and interleave_condition_C(11, 8) and not interleave_condition_C(8, 5) and not interleave_condition_C(2, 5))
    ok("L2296 coprime construction k + (k mod t): (7,5) and (11,3) perfect at n = 11..25 / 7..9 (direct audit)", all(interleave_audit(layout_from_period(coprime_period_layout(7, 5, n_), 7, n_), 7, n_, 5) == (35, []) for n_ in range(11, 26)) and all(interleave_audit(layout_from_period(coprime_period_layout(11, 3, n_), 11, n_), 11, n_, 3) == (33, []) for n_ in range(7, 10)))
    _ts = transposed_staircase(9, 3); _ts2 = transposed_staircase(27, 9)
    ok("L2300 transposed staircase: (9,3),(25,5),(27,9) balanced; (27,9) audited perfect at n = 19, 40, 81; (9,3) at n = 7..9", interleave_balanced(_ts, 9, 3) and interleave_balanced(transposed_staircase(25, 5), 25, 5) and interleave_balanced(_ts2, 27, 9) and all(interleave_audit(layout_from_period(_ts2, 27, n_), 27, n_, 9) == (243, []) for n_ in (19, 40, 81)) and all(interleave_audit(layout_from_period(_ts, 9, n_), 9, n_, 3) == (27, []) for n_ in (7, 8, 9)) and perfect_interleave_status(27, 9, 50).startswith("perfect"))
    _ad = additive_layout((3, 6, 5, 2, 0, 4, 1), (0, 1, 4, 2), 7, 4, 13)
    ok("L2304 additive colouring (7,4), rho=1: balanced; perfect at n = 9 and 13 (direct audit)", interleave_balanced(_ad, 7, 4) and all(interleave_audit(layout_from_period(_ad, 7, n_), 7, n_, 4) == (28, []) for n_ in (9, 13)))
    _dr = double_rotation_layout(5, 4, 9); _dr3 = double_rotation_layout(5, 4, 11)
    ok("L2308 double rotation (5,4): rho=1 and rho=3 layouts perfect at n = 9, 13 and 11, 15 (direct audit)", all(interleave_audit(layout_from_period(_dr, 5, n_), 5, n_, 4) == (20, []) for n_ in (9, 13)) and all(interleave_audit(layout_from_period(_dr3, 5, n_), 5, n_, 4) == (20, []) for n_ in (11, 15)))
    _ro = reflection_order_layout(11, 6, 13)
    ok("L2312 reflection-ordering layout (11,6), rho=1: perfect at n = 13, 19, 25, 31 (direct audit)", all(interleave_audit(layout_from_period(_ro, 11, n_), 11, n_, 6) == (66, []) for n_ in (13, 19, 25, 31)))
    _hp = half_period_layout(11, 8)
    ok("L2324 C' witness: (10,5)->(20,4) and averaging confirms; (6,6)->(24,4); half-period (11,8) perfect at n = 20, 28 (direct audit)", condition_C_witness(10, 5) == (20, 4) and averaging_obstruction(10, 5, 20) is not None and condition_C_witness(6, 6) == (24, 4) and condition_C_witness(16, 16) is None and all(interleave_audit(layout_from_period(_hp, 11, n_), 11, n_, 8) == (88, []) for n_ in (20, 28)))
    ok("L2328 even t, even rho: coprime_period_layout (13,10) and (11,8) perfect at n = 24, 26 / 18, 20, 22 (direct audit)", all(interleave_audit(layout_from_period(coprime_period_layout(13, 10, n_), 13, n_), 13, n_, 10) == (130, []) for n_ in (24, 26)) and all(interleave_audit(layout_from_period(coprime_period_layout(11, 8, n_), 11, n_), 11, n_, 8) == (88, []) for n_ in (18, 20, 22)))
    _bs = block_shift_layout(7, 6, (5, 3, 2, 0, 6, 4), 0)
    ok("L2332 block shift (7,6) odd rho=3: criterion true, balanced, perfect at n = 15, 21, 27, 33 (direct audit)", block_shift_window_ok(7, 6, (5, 3, 2, 0, 6, 4), 0, 3) and interleave_balanced(_bs, 7, 6) and all(interleave_audit(layout_from_period(_bs, 7, n_), 7, n_, 6) == (42, []) for n_ in (15, 21, 27, 33)))
    _fa = fibonacci_anyon_data()
    ok("L2336 Fibonacci anyons: F^2 = I, Yang-Baxter, d^2 = d + 1, fusion dims 1,1,2,3,5,...; 150 Hz voice at 60 fps folds 40 harmonics onto 2 aliases", _fa["F2_identity"] and _fa["yang_baxter"] and _fa["golden_dimension"] and _fa["fusion_dims"][:6] == [1, 1, 2, 3, 5, 8] and harmonic_aliases(150.0) == 2 and harmonic_aliases(147.3) == 40)
    _e3, _d3 = tl_chain_energy(3); _bh = braid_gate_search([[2**-0.5, 2**-0.5], [2**-0.5, -2**-0.5]], 5)
    ok("L2340 golden chain exact energy: -(sqrt5-1) per TL bond, sqrt5-3 = -2/phi^2 per projector; log2(phi) bits/anyon; Hadamard by 3-braid within 0.085", abs(_e3 + (5**0.5 - 1)) < 1e-6 and abs(_e3/_d3 - (5**0.5 - 3)) < 1e-6 and abs(anyon_storage_bits(1000) - 0.69308) < 1e-4 and abs(_bh[0] - 0.0842) < 1e-3)
    ok("L2344 anyon-chain energy closed form = Bethe integral for N = 3..12; golden N = 5 gives -(sqrt5-1), per projector sqrt5-3 = -2/phi^2", all(abs(anyon_chain_energy_closed(N_) - tl_chain_energy(N_ - 2)[0]) < 1e-6 for N_ in range(3, 13)) and abs(anyon_chain_energy_closed(5) + 5**0.5 - 1) < 1e-12 and abs(anyon_chain_energy_closed(5)/(2*math.cos(math.pi/5)) - (5**0.5 - 3)) < 1e-12)
    ok("L2348 Girstmair: alternating digit sum of the period of 1/p = -11 h(-p) for p = 7, 19, 23, 47, 59, 167 (base 10); tangent class sums for p = 7..43", all(girstmair_digits(p_)[0] == girstmair_digits(p_)[1] for p_ in (7, 19, 23, 47, 59, 167)) and girstmair_digits(23) == (-33, -33) and all(abs(tangent_class_sum(p_)[0] - tangent_class_sum(p_)[1]) < 1e-8 for p_ in (7, 11, 19, 23, 31, 43)))
    ok("L2352 decimal digits -> relative class number h^-(Q(zeta_p)): p = 23, 29, 31, 37, 47, 59, 89 give 3, 8, 9, 37, 695, 41241, 13379363737 (OEIS A000927)", [decimal_hminus(p_) for p_ in (23, 29, 31, 37, 47, 59, 89)] == [3, 8, 9, 37, 695, 41241, 13379363737])
    ok("L2356 irregular primes from decimal periods: 37 -> [32], 59 -> [44], 157 -> [62, 110], 31 -> [] (Kummer, B_k)", irregular_indices_decimal(37) == [32] and irregular_indices_decimal(59) == [44] and irregular_indices_decimal(157) == [62, 110] and irregular_indices_decimal(31) == [])
    _Ls = decimal_L_spectrum(47)
    ok("L2360 L-value spectrum from 1/47's digits: quadratic line |L| = pi h(-47)/sqrt47 = 5pi/sqrt47; range 0.4866..2.2912", abs(_Ls[23] - 5*math.pi/math.sqrt(47)) < 1e-9 and abs(min(_Ls.values()) - 0.486606) < 1e-5 and abs(max(_Ls.values()) - 2.29124) < 1e-5)
    ok("L2364 irregular spectral lines have p-adic valuation exactly 1: (37,32), (59,44), (157,62), (157,110); regular line (37,2) valuation 0", [irregular_line_valuation(p_, k_) for p_, k_ in ((37, 32), (59, 44), (157, 62), (157, 110))] == [1, 1, 1, 1] and irregular_line_valuation(37, 2) == 0)
    _bsa = [4, 11, 7, 9, 12, 3, 5, 2, 8, 10, 0, 1]
    ok("L2364 block shift (13,12) odd rho=5 from exact search: criterion, balance and direct audit at n = 29, 41", block_shift_window_ok(13, 12, _bsa, 0, 5) and interleave_balanced(block_shift_layout(13, 12, _bsa, 0), 13, 12) and all(interleave_audit(layout_from_period(block_shift_layout(13, 12, _bsa, 0), 13, n_), 13, n_, 12) == (156, []) for n_ in (29, 41)))
    _wa = odd_rho_walk_layout(17, 16, 7)
    ok("L2368 walk lemma: odd_rho_walk_layout (17,16), rho=7 satisfies the window criterion, is balanced, and is perfect at n = 39 (direct audit)", _wa is not None and block_shift_window_ok(17, 16, _wa, 0, 7) and interleave_balanced(block_shift_layout(17, 16, _wa, 0), 17, 16) and interleave_audit(layout_from_period(block_shift_layout(17, 16, _wa, 0), 17, 39), 17, 39, 16) == (272, []))
    _X_ = oddrho_half_solution(10); _a_ = oddrho_lift(11, 10, _X_)
    ok("L2372 Theorem H: explicit s = t/2 solution (t = 10) is an integer certificate in [0, t] and lifts to a balanced window at (11, 10, rho = 5)", oddrho_integer_ok(10, 5, _X_) and max(_X_) <= 10 and block_shift_window_ok(11, 10, _a_, 0, 5))
    _ok_ = all(oddrho_integer_ok(t_, s_, oddrho_certificate(t_, s_)[0]) for t_ in range(6, 87, 2) for s_ in range(1, t_, 2))
    ok("L2372 certificates: I(t,s) solved for every even t in [6,86] and every odd s (embedded + mirror + Theorem H)", _ok_)
    _a2_ = odd_rho_layout_any_m(59, 58, 31); _a3_ = odd_rho_layout_any_m(1009, 40, 17)
    ok("L2372 lift lemma: no-search layouts at (59,58,31) and (1009,40,17) satisfy the window criterion and are balanced", _a2_ is not None and block_shift_window_ok(59, 58, _a2_, 0, 31) and interleave_balanced(block_shift_layout(59, 58, _a2_, 0), 59, 58) and _a3_ is not None and block_shift_window_ok(1009, 40, _a3_, 0, 17))
    _a4_ = odd_rho_layout_any_m(79, 74, 33)
    ok("L2378 certificate extension: no-search layout at (79,74,33) satisfies the window criterion and is balanced", _a4_ is not None and block_shift_window_ok(79, 74, _a4_, 0, 33) and interleave_balanced(block_shift_layout(79, 74, _a4_, 0), 79, 74))
    _e_ = anyon_chain_energy_closed
    ok("L2389 L2344 special cases: N=3 -> XXZ Delta=-1/2 energy -3/4 per site; N=4 -> critical Ising -4/pi (Pfeuty); N=5 -> golden -2/phi; N=6 -> 3-state Potts -4/3 - 2 sqrt3/pi (Z3 centre of SU(3), Svetitsky-Yaffe)", abs(_e_(3) + 0.25 + 0.75) < 1e-12 and abs(2*math.sqrt(2)*_e_(4) + 2 + 4/math.pi) < 1e-12 and abs(_e_(5) + 2/((1+5**0.5)/2)) < 1e-12 and abs(2*math.sqrt(3)*_e_(6) + 2 + 4/3 + 2*math.sqrt(3)/math.pi) < 1e-12)
    _ok1_ = all(abs(anyon_energy_units(N_) - anyon_chain_energy_closed(N_)) < 1e-9 for N_ in range(3, 40, 2))
    import cmath as _cm
    _c7_ = anyon_energy_zw(7); _v7_ = sum(c_*_cm.exp(2j*math.pi*k_/7) for k_, c_ in enumerate(_c7_)).real
    ok("L2393 cyclotomic-unit form: e(N) = zeta^-1 sum (-1)^j (w-1)/(w^j-1) for odd N <= 39; e(7) is an exact Z[w] vector; e(7) from the digits 142857 of 1/7", _ok1_ and abs(_v7_ - anyon_chain_energy_closed(7)) < 1e-12 and abs(anyon_energy_from_digits(7, 10) - anyon_chain_energy_closed(7)) < 1e-9 and abs(anyon_energy_from_digits(5, 2) + 2/((1+5**0.5)/2)) < 1e-9)
    _two_ = lambda p_: all(((v_ - anyon_energy_zw(p_)[p_-1]) % 2 == 0) for v_ in anyon_energy_zw(p_)[:p_-1])
    ok("L2393 Theorem 3: 2 | e(p) in Z[w] iff p = 1 mod 4 (all primes 5 <= p <= 113)", all(_two_(p_) == (p_ % 4 == 1) for p_ in range(5, 114) if all(p_ % d_ for d_ in range(2, int(p_**0.5)+1))))
    _dn_ = all(abs(anyon_energy_denominator(N_)*anyon_energy_norm_float(N_) - round(anyon_energy_denominator(N_)*anyon_energy_norm_float(N_))) < 1e-3 for N_ in (9, 15, 21, 25, 27))
    ok("L2399 Theorem D: denominators of N(e(N)) = 3, 45, 189, 25, 81 for N = 9, 15, 21, 25, 27 (Glaisher/Fermat-quotient law); Wieferich 1093, 3511 detected", _dn_ and [anyon_energy_denominator(n_) for n_ in (9, 15, 21, 25, 27)] == [3, 45, 189, 25, 81] and anyon_energy_denominator(3*1093) == 3**546 and anyon_energy_denominator(3*1097) == 3**548*1097 and anyon_energy_denominator(3*3511) % 3511 != 0)
    ok("L2405 Theorem W: e(N) integral iff N prime or all prime factors Wieferich (3*1093 no, 1093*3511 and 1093^2 yes); Theorem E even-N unit formula N = 4..30", (not anyon_energy_is_integral(3*1093)) and anyon_energy_is_integral(1093*3511) and anyon_energy_is_integral(1093**2) and anyon_energy_is_integral(13) and not anyon_energy_is_integral(21) and all(abs(anyon_energy_even_units(n_) - anyon_chain_energy_closed(n_) - 2*math.sin(math.pi/n_)/math.pi) < 1e-9 for n_ in range(4, 31, 2)))
    _pr_ = [p_ for p_ in range(5, 200) if all(p_ % d_ for d_ in range(2, int(p_**0.5) + 1))]
    ok("L2411 Theorem T/T': Tr(e(p)) == -q_p(2), e(p) == 2 q_p(2) mod (1-zeta) for p < 200; N(e(p)) == (2q/p) mod p (p = 7, 11, 13); 1093 | Tr(e(1093))", all((anyon_energy_trace(p_) + fermat_quotient(p_)) % p_ == 0 and (anyon_energy_mod_lambda(p_) - 2*fermat_quotient(p_)) % p_ == 0 for p_ in _pr_) and all(round(anyon_energy_norm_float(p_)) % p_ == pow(2*fermat_quotient(p_), (p_ - 1)//2, p_) for p_ in (7, 11, 13)) and anyon_energy_trace(1093) % 1093 == 0)
    ok("L2411 twisted coefficients: c(zeta_3) vanishes at 11 (base-3 Wieferich) not 13; c(zeta_6) always; c(zeta_4) at 1093", twisted_coefficient_vanishes(3, 11) and not twisted_coefficient_vanishes(3, 13) and twisted_coefficient_vanishes(6, 101) and twisted_coefficient_vanishes(4, 1093) and not twisted_coefficient_vanishes(4, 1097))
    ok("L2417 Theorem L: mu-adic digits of e(p) are a_n + b_n q_p(2) with universal Bernoulli-Euler coefficients (p = 41, 43, 101, n <= 4); golden twist c(zeta_10) never vanishes for p < 200 (no Wall-Sun-Sun prime)", all(anyon_energy_mu_digits(p_, 4) == anyon_energy_mu_predicted(p_, 4) for p_ in (41, 43, 101)) and not any(twisted_coefficient_vanishes(10, p_) for p_ in (7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199)))
    ok("L2436 trace formula: Tr e(7) = -18 and Tr e(p) == -2 q_p(2) mod p for p < 200", anyon_trace_lehmer(7)[0] == -18 and all((anyon_trace_lehmer(p)[0] + 2*fermat_quotient(p)) % p == 0 for p in range(5, 200) if all(p % d for d in range(2, p))))
    ok("L2448 Lehmer mod-4 rule: N(p) == 2 (p == 1 mod 4), 0 (p == 3 mod 4), p < 400", all(lehmer_count(p) % 4 == (2 if p % 4 == 1 else 0) for p in range(5, 400) if all(p % d for d in range(2, p))))
    ok("L2442 even-m correction: 10 antipodal (Fibonacci), 35 not, no multiple of 4", lucas_antipodal(10) and not lucas_antipodal(35) and not any(lucas_antipodal(m) for m in range(4, 200, 4)))
    ok("L2448 Theorem 8 matches brute force, m in 3..150, Fibonacci and Pell", all(lucas_antipodal(m, P, -1) == lucas_antipodal_predicted(m, P, -1) for P in (1, 2) for m in range(3, 151)))
    ok("L2430 wheel group orders: m=10 -> 8, m=9 -> 4, m=11 -> 2", (wheel_group_order(10), wheel_group_order(9), wheel_group_order(11)) == (8, 4, 2))
    ok("L2422 step-10 ladder 1/(99-10n), n = -2..5 (truncation error < 1e-100)", all(abs(float(step10_ladder(n)[0] - step10_ladder(n)[1])) < 1e-100 for n in range(-2, 6)))
    ok("L2478 Theorem B': bulk energy closed form = Bethe integral (N <= 12, a <= 5), = e(5) at a=1, Razumov-Stroganov -1 at N=3", all(abs(bulk_energy_closed(a, N) - bulk_energy_integral(math.pi*a/N)) < 1e-6 for N in range(3, 13) for a in range(1, min(N, 6)) if math.gcd(a, N) == 1) and abs(bulk_energy_closed(1, 5) - (1 - math.sqrt(5))) < 1e-12 and abs(bulk_energy_closed(1, 3) + 1) < 1e-12)
    ok("L2076 necklace ladder: N(10) = 89, N(11) = 109 (signed base 10), N(b+1) - N(b) = 2b; golden spiral rate 0.306349 = slowest", _nl[10] == 89 and _nl[11] == 109 and all(_nl[b_ + 1] - _nl[b_] == 2 * b_ for b_ in range(2, 12)) and abs(spiral_rate(5, 1, 1) - 0.306348962530) < 1e-9)
    # ---- L2522-L2578 results (added in 5.84) ----
    from fractions import Fraction as _Fr
    def _dsum(num, n):                      # digit sum of one period of num/n (n coprime to 10 not required)
        r = num % n; seen = {}; ds = []; i = 0
        while r not in seen:
            seen[r] = i; d, r = divmod(10 * r, n); ds.append(d); i += 1
        return sum(ds[seen[r]:]), ds[seen[r]:]
    ok("L2532: digit sums 1/201=144, 1/163=360, 1/203=360 (class-number identities)",
       (_dsum(1, 201)[0], _dsum(1, 163)[0], _dsum(1, 203)[0]) == (144, 360, 360))
    a_ = (_dsum(1, 173)[0] - _Fr(9 * 43, 2)) / _Fr(9, 2); b_ = (_dsum(1, 865)[0] - _Fr(9 * 43, 2)) / _Fr(9, 2)
    ok("L2536: index-4 recipe p=173: S(1/173)=207, S(1/865)=198 -> h^-=(a^2+b^2)/2=5", (a_ * a_ + b_ * b_) / 2 == 5)
    d7 = _dsum(1, 7)[1]; d51 = _dsum(1, 51)[1]
    ok("L2542 v1.1: sum (-1)^j d_j over 1/7 = 11 = 11 h(-7) (first digit negative)", sum((-1) ** (j + 1) * d7[j] for j in range(6)) == 11)
    ok("L2546 erratum: 1/51 has 4|T but alternating sum -11 (needs 10^(T/2)=-1)", len(d51) == 16 and sum((-1) ** j * d51[j] for j in range(16)) == -11 and pow(10, 8, 51) != 50)
    d19 = _dsum(1, 19)[1]; T19 = len(d19)
    ok("L2542: full-reptend variance 1/19 = 33/4 - 24/18 = 83/12", _Fr(sum(x * x for x in d19), T19) - _Fr(sum(d19), T19) ** 2 == _Fr(83, 12))
    def _bal(a, m):
        seen = set(); c = 0
        for x in range(m):
            for y in range(m):
                if (x, y) in seen: continue
                S = P = 0; u, w = x, y
                while (u, w) not in seen:
                    seen.add((u, w)); S += u; P += 1; u, w = w, (a * w + u) % m
                c += (2 * S == (m - 1) * P)
        return c
    ok("L2553/L2557: balanced orbits a=4 mod 32 -> 4, a=8 mod 128 -> 20 ((4^f-4)/3); odd a=1 mod 64 -> 0",
       (_bal(4, 32), _bal(8, 128), _bal(1, 64)) == (4, 20, 0))
    ok("L2557 window formula: a=16 mod 256 -> (2^7+2^0)/3 = 43", _bal(16, 256) == 43)
    def _fib_anti_bal(m):
        a, b, sq = 0, 1, []
        while True:
            sq.append(a); a, b = b, (a + b) % m
            if (a, b) == (0, 1): break
        T = len(sq)
        anti = T % 2 == 0 and all((sq[i] + sq[(i + T // 2) % T]) % m == 0 for i in range(T))
        return anti and 2 * sum(sq) == (m - 1) * T
    ok("L2546/L2553: Fibonacci balanced antipodal moduli <= 700 are 5, 25, 125, 625",
       [m for m in range(3, 701) if _fib_anti_bal(m)] == [5, 25, 125, 625])
    if HAVE_MP:
        import mpmath as _mp
        def _eB(a, N):
            g = _mp.pi * a / N; s1 = s2 = 0
            for k in range(1, N):
                if not ((2 * a * k) % N == 0 and ((2 * a * k) // N) % 2 == 1): s1 += k * _mp.tan(g * k)
            for j in range(1, 2 * a, 2):
                if (N * j) % (2 * a): s2 += j * _mp.cot(_mp.pi * N * j / (2 * a))
            return 2 * _mp.sin(g) / N * s1 - N * _mp.sin(g) / a ** 2 * s2 - (2 * _mp.sin(g) / (_mp.pi * a) if N % 2 == 0 else 0)
        ok("Paper 2 Theorem B': e(pi/5) = 1-sqrt5 and e(pi/4) = -sqrt2/2 - sqrt2/pi",
           abs(_eB(1, 5) - (1 - _mp.sqrt(5))) < 1e-12 and abs(_eB(1, 4) + _mp.sqrt(2) / 2 + _mp.sqrt(2) / _mp.pi) < 1e-12)
        def _bn(n):
            B = _mp.bernoulli(2 * n); return 2 ** (2 * n) * (2 ** (2 * n) - 1) * B * abs(B) / (2 * n * _mp.factorial(2 * n))
        ok("Note R: Bernoulli perturbative coefficients b_1..b_3 = 1/12, -1/360, 1/1890",
           all(abs(_bn(n) - v) < 1e-25 for n, v in ((1, _mp.mpf(1) / 12), (2, -_mp.mpf(1) / 360), (3, _mp.mpf(1) / 1890))))
    pw = 58601; M2 = pw * pw; g_ = next(g for g in range(2, pw) if all(pow(g, (pw - 1) // q, pw) != 1 for q in (2, 5, 293)))
    w_ = pow(g_, (pw - 1) // 8, pw)
    for _ in range(4): w_ = pow(w_, pw, M2)
    ells = []
    for jj in (1, 3):
        Nj = (2 - pow(w_, jj, M2) - pow(w_, 8 - jj, M2)) % M2; dd = (Nj - pow(Nj, pw, M2)) % M2
        ells.append((dd // pw) * pow(pow(Nj, pw, pw), -1, pw) % pw)
    ok("Paper 3 norm constraint k=8, p=58601: l_1+l_3 = -q_p(2), with l_3 = 0 (the hit)",
       (sum(ells) + (pow(2, pw - 1, M2) - 1) // pw) % pw == 0 and ells[1] == 0)
    # L2808: DNA strand
    ok("1/5 in base 4 = AT repeating; halves pair A-T (base-4 Midy)", dna_recip(5) == "AT" and dna_midy(5) is True)
    ok("1/7 in base 4 has odd period 3 (no halves)", len(dna_recip(7)) == 3 and dna_midy(7) is None)
    ok("every base-4 Midy prime below 300: second half is the Watson-Crick complement of the first half",
       all(dna_midy(q) for q in range(3, 300, 2) if all(q % d for d in range(2, int(q ** 0.5) + 1))
           and mult_order(4, q) % 2 == 0 and pow(4, mult_order(4, q) // 2, q) == q - 1))
    ok("L2664: 277 of 668 odd primes below 5000 are base-4 Midy (Watson-Crick paired)", dna_midy_count(5000) == (277, 668))
    # L2852: theorems proved L2422-L2848 not previously in the toolkit
    ok("L2422 (+L2852 correction): rev(n) = 2n - 1 below 10^5 exactly 1 (trivial), 37, 397, 3997, 39997; 37*73 = 2701 = T_73", rev_triangular(10 ** 5) == [1, 37, 397, 3997, 39997] and 37 * 73 == 73 * 74 // 2 == 2701)
    ok("L2436 b(k): least n containing every k-digit string: b(1) = 17, b(2) = 109", (all_strings_least_n(1), all_strings_least_n(2)) == (17, 109))
    ok("L2505 Theorem R (k=8): 47 is a real-subfield Wieferich hit, 31 and 23 are not",
       True in real_subfield_wieferich(47, 8) and True not in real_subfield_wieferich(31, 8) and True not in real_subfield_wieferich(23, 8))
    ok("L2515: the hardest m-digit string needs n = 10^m + 1 (m = 1: 11, m = 2: 101)", (least_n_all_strings(1, 200), least_n_all_strings(2, 400)) == (11, 101))
    ok("L2522 2-5 lemma: 1/(2^a 5^b m) depends only on b - a mod d(m), m = 7, 21, 13, 41", all(thm_25_lemma(m, 3, 3) for m in (7, 21, 13, 41)))
    ok("L2553-L2595 Note B counts: a = 8 (f=3), e = 2..7 -> 2, 4, 4, 6, 11, 20 (regimes e<=f, f<e<=2f, e=2f+1)",
       [bal_count(8, e) for e in range(2, 8)] == [2, 4, 4, 6, 11, 20])
    ok("L2609 variance = Dedekind-sum form (exact) for full-reptend p = 7, 17, 19, 23, 29, 47, 59, 61", all(f == d for f, d in (variance_dedekind(p) for p in (7, 17, 19, 23, 29, 47, 59, 61))))
    ok("L2641/L2645 casting out 10^q - 1 (Theorem D, D_q): every applicable prime < 600, q = 2, 3, 4",
       all(casting_out(p, q) in (True, None) for q in (2, 3, 4) for p in range(7, 600) if all(p % d for d in range(2, int(p ** 0.5) + 1))))
    ok("L2656/L2660 Theorem P3: reduction-clock period = T*3^min(2,max(0,a-t)) for every n < 1500 coprime to 10",
       all(clock_period(n)[0] == theorem_P3(n) for n in range(3, 1500) if n % 2 and n % 5))
    ok("L2660 self-period: clock period = n only for 3^k in base 10 (n < 1500); base-b rule holds b = 7, 12, 13, 16 (n < 300)",
       [n for n in range(3, 1500) if n % 2 and n % 5 and clock_period(n)[0] == n] == [3, 9, 27, 81, 243, 729]
       and all((clock_period(n, b)[0] == n) == self_period_rule(n, b) for b in (7, 12, 13, 16) for n in range(2, 300) if _gcd(n, b) == 1))
    ok("L2833 run-length lemma (b^k < n for 0/b-1 runs; b^k <= max(d,b-1-d) n otherwise): every a/n, n < 400, bases 4 and 10",
       all(run_bound_ok(n, b) for b in (4, 10) for n in range(3, 400) if _gcd(n, b) == 1))
    selftest_L3297(ok)   # L3297: hedgehog motif on IHH; exon mapper on a synthetic minus-strand gene
    selftest_L3277(ok)   # L3277: 4 rows (581 -> 43, 11+88 -> 17, supersingular primes, Euler lucky)
    selftest_L2853(ok)   # L2853: 18 rows (reduction R_b/E_b/C1/C3_b, clock F1/F2/H, dark frequencies, Girstmair, legacy Prop 6.1, Thms 9/10/12, Lemma U, T'', 1/841)
    n_ok = sum(c for _, c in res)
    say("SELF-TEST %s: %d/%d passed in %.1f s (mpmath %s)" % ("PASSED" if n_ok == len(res) else "FAILED",
        n_ok, len(res), time.time() - t, "yes" if HAVE_MP else "no"))
    return n_ok == len(res)

# ---------------------------------------------------------------- report
def save_report(title, data):
    stamp = time.strftime("%Y%m%d_%H%M%S")
    base = os.path.join(OUT, "dcf_%s_%s" % (re.sub(r"\W+", "_", title.lower()).strip("_"), stamp))
    with open(base + ".json", "w", encoding="utf-8") as f: json.dump(data, f, indent=1, default=str)
    with open(base + ".md", "w", encoding="utf-8") as f:
        f.write("# %s\n\n**Author:** Gary NOMEREMORTAL Mason · %s · %s\n\n" % (title, VERSION, time.strftime("%Y-%m-%d %H:%M")))
        f.write("Convention A: position 1 is the first digit after the decimal point.\n\n```\n")
        f.write("\n".join(LOG[-200:]) + "\n```\n")
    say("Report saved:", base + ".md"); say("Data saved:  ", base + ".json")

# ---------------------------------------------------------------- claims inbox (lead L1896)
XPAT = [(r"(?:sqrt|√)\s*\(?\s*(\d+)\s*\)?", lambda m: "sqrt(%s)" % m.group(1)),
        (r"\b1\s*/\s*(\d+)\b", lambda m: "1/%s" % m.group(1)),
        (r"reciprocal of (\d+)", lambda m: "1/%s" % m.group(1)),
        (r"\b(?:pi|π)\b", lambda m: "pi"),
        (r"\b(?:phi|φ)\b|golden ratio", lambda m: "phi"),
        (r"zeta\s*\(\s*3\s*\)|ap[eé]ry", lambda m: "zeta(3)"),
        (r"\b(?:ln|log)\s*\(?\s*2\b", lambda m: "log(2)"),
        (r"euler'?s number|\be\b(?! ?=)", lambda m: "e")]

def extract_claims(text):
    """find 'S at position N of X' style claims, one per sentence; anything unclear is listed for a manual check."""
    found, unclear = [], []
    for sent in re.split(r"(?<=[.!?])\s+|\n+|;\s*|,\s*and\s+", text):
        if not re.search(r"position|digit\s*(?:#|no\.?|number)\s*\d|\bplace\s+\d", sent, re.I): continue
        mN = re.search(r"(?:position|digit|place)\s*(?:#|no\.?|number)?\s*(\d[\d,]*)", sent, re.I)
        N = int(mN.group(1).replace(",", "")) if mN else None
        mS = (re.search(r"[\"“”'‘’](\d+)[\"“”'‘’]", sent) or
              re.search(r"first\s+(\d+)\s+(?:is\s+|occurs\s+|appears\s+)?at\s+position", sent, re.I) or
              re.search(r"(?:sequence|string|digits|substring|pattern|block|number)\s+[\"“]?(\d{2,})", sent, re.I))
        S = mS.group(1) if mS else None
        if S is None:
            cands = [d for d in re.findall(r"(?<![\d.,/])(\d{3,})(?![\d.,])", sent) if not mN or d != mN.group(1).replace(",", "")]
            S = cands[0] if len(cands) == 1 else None
        X = None
        for pat, f in XPAT:
            m = re.search(pat, sent, re.I)
            if m: X = f(m); break
        if X and S and N: found.append(dict(X=X, S=S, N=N, sentence=sent.strip()[:200]))
        else: unclear.append(dict(sentence=sent.strip()[:200], X=X, S=S, N=N))
    return found, unclear

def menu_inbox():
    say("Paste the AI text below. Finish with a line containing only END.")
    lines = []
    while True:
        try: l = input()
        except EOFError: break
        if l.strip() == "END": break
        lines.append(l)
    found, unclear = extract_claims("\n".join(lines)); results = []
    say("position claims found: %d; sentences needing a manual check: %d" % (len(found), len(unclear)))
    for c in found:
        try:
            r = check_claim(c["X"], c["S"], c["N"])
        except Exception as ex:
            r = dict(verdict="NOT CHECKED: %s" % ex, first_position=None)
        say("  %s contains %s at %d? -> %s" % (c["X"], c["S"], c["N"], r["verdict"]))
        results.append(dict(c, **{k: r.get(k) for k in ("verdict", "first_position")}))
        log_check("inbox", c, r)
    for u in unclear: say("  MANUAL CHECK:", u["sentence"])
    ok = sum(1 for r in results if r["verdict"] == "VERIFIED")
    say("verified %d of %d extracted claims" % (ok, len(results)))
    save_report("Claims inbox", dict(claims=results, manual=unclear))

# ---------------------------------------------------------------- QR handoff (L1902)
# Frames use only characters from the QR "alphanumeric" set (A-Z, 0-9, ':'), so codes stay small.
#   header  DCF1:<id>:0:<N>:<SHA-256 of payload>:<kind, base32>
#   data    DCF1:<id>:<i>:<N>:<CRC-32 of chunk>:<chunk of base32(zlib(payload))>
# Frames can be scanned in any order, repeated or mixed with other text; nothing is accepted
# until every frame is present, each CRC matches and the SHA-256 of the whole payload matches.
import base64, zlib, glob
QR_FRAME = 400                                     # characters of data per QR code (smaller = easier to scan)
FRAME_RE = re.compile(r"DCF1:([0-9A-F]{8}):(\d+):(\d+):([0-9A-F]{8}|[0-9A-F]{64}):([A-Z2-7]*)")
INBOX = os.path.join(OUT, "qr_inbox.txt")

def b32(b): return base64.b32encode(b).decode().rstrip("=")
def unb32(s): return base64.b32decode(s + "=" * (-len(s) % 8))

def _cauchy(k, m):
    return [[gdiv(1, (k + i) ^ j) for j in range(k)] for i in range(m)]

def _gf_solve(A, Y):
    """Gauss-Jordan over GF(256): A k x k, Y k byte-rows -> k byte-rows."""
    k = len(A); A = [r[:] for r in A]; Y = [bytearray(y) for y in Y]
    for c in range(k):
        p = next(r for r in range(c, k) if A[r][c]); A[c], A[p] = A[p], A[c]; Y[c], Y[p] = Y[p], Y[c]
        iv = gdiv(1, A[c][c]); A[c] = [gmul(iv, v) for v in A[c]]; Y[c] = bytearray(gmul(iv, v) for v in Y[c])
        for r in range(k):
            if r != c and A[r][c]:
                f = A[r][c]; A[r] = [a ^ gmul(f, b) for a, b in zip(A[r], A[c])]
                Y[r] = bytearray(a ^ gmul(f, b) for a, b in zip(Y[r], Y[c]))
    return [bytes(y) for y in Y]

def qr_frames(payload, kind, size=QR_FRAME, parity=None):
    """header + data frames, plus Reed-Solomon parity frames: any `parity` lost data frames can be rebuilt."""
    sha = hashlib.sha256(payload).hexdigest().upper(); cid = sha[:8]
    body = b32(zlib.compress(payload, 9))
    parts = [body[i:i + size] for i in range(0, len(body), size)] or [""]
    n = len(parts)
    frames = ["DCF1:%s:0:%d:%s:%s" % (cid, n, sha, b32(kind.encode()))]
    for i, p in enumerate(parts, 1):
        frames.append("DCF1:%s:%d:%d:%08X:%s" % (cid, i, n, zlib.crc32(p.encode()), p))
    P = (0 if n == 1 else max(1, n // 8)) if parity is None else parity
    if P:
        w = max(len(x) for x in parts); D = [x.encode().ljust(w, b"\0") for x in parts]; C = _cauchy(n, P)
        for i in range(P):
            par = bytearray(w)
            for j in range(n):
                c = C[i][j]
                if c:
                    for t in range(w): par[t] ^= gmul(c, D[j][t])
            data = b32(struct.pack(">IB", len(body), P) + bytes(par))
            frames.append("DCF1:%s:%d:%d:%08X:%s" % (cid, n + 1 + i, n, zlib.crc32(data.encode()), data))
    return frames

def qr_collect(text):
    """all DCF1 frames found in any text -> {id: status}; complete ones carry kind + payload.
    Missing data frames are rebuilt from parity frames when enough are present."""
    got = {}
    for cid, i, n, chk, data in FRAME_RE.findall(text.upper()):
        i, n = int(i), int(n); g = got.setdefault(cid, dict(n=n, frames={}, bad=set()))
        if n != g["n"]: g["bad"].add("N"); continue
        if i > 0 and "%08X" % zlib.crc32(data.encode()) != chk: g["bad"].add(i); continue
        g["frames"][i] = (chk, data)
    out = {}
    for cid, g in got.items():
        n = g["n"]; fr = g["frames"]
        par = {i: fr[i][1] for i in fr if i > n}
        missing = [i for i in range(n + 1) if i not in fr]
        st = dict(frames=n + 1, parity_frames=len(par), have=len([i for i in fr if i <= n]), missing=list(missing),
                  crc_errors=sorted(x for x in g["bad"] if x != "N"), rebuilt=[])
        lost = [i for i in missing if i > 0]
        if 0 not in missing and lost and len(par) >= len(lost):
            try:
                raws = {i: unb32(v) for i, v in par.items()}
                blen, P = struct.unpack(">IB", next(iter(raws.values()))[:5]); w = len(next(iter(raws.values()))) - 5
                C = _cauchy(n, P); rows, Y = [], []
                for j in range(1, n + 1):
                    if j in fr: rows.append([1 if t == j - 1 else 0 for t in range(n)]); Y.append(fr[j][1].encode().ljust(w, b"\0"))
                for i in sorted(raws):
                    if len(rows) == n: break
                    rows.append(C[i - n - 1]); Y.append(raws[i][5:])
                D = _gf_solve(rows, Y)
                for j in lost:
                    ln = min(w, blen - (j - 1) * w); txt = D[j - 1][:ln].decode()
                    fr[j] = ("%08X" % zlib.crc32(txt.encode()), txt); st["rebuilt"].append(j)
                missing = [0] if 0 in missing else []; st["missing"] = missing
            except Exception as ex:
                st["error"] = "parity rebuild failed: %s" % ex
        if not missing:
            sha, kind = fr[0]
            payload = zlib.decompress(unb32("".join(fr[i][1] for i in range(1, n + 1))))
            if hashlib.sha256(payload).hexdigest().upper() != sha or sha[:8] != cid:
                st["error"] = "SHA-256 mismatch: payload rejected"
            else:
                st.update(complete=True, kind=unb32(kind).decode(), payload=payload)
        out[cid] = st
    return out

def rows_digest(lo, hi):
    """SHA-256 over the canonical recomputed rows 1/lo .. 1/hi (independent of any database)."""
    h = hashlib.sha256()
    for n in range(lo, hi + 1): h.update(("%d,%d,%d,%d,%s,%s,%s\n" % row_for(n)[:7]).encode())
    return h.hexdigest()

def make_ticket(lo, hi, password=None):
    t = dict(t="dcf.range", lo=lo, hi=hi, rows=hi - lo + 1, digest=rows_digest(lo, hi),
             program=VERSION, made=time.strftime("%Y-%m-%d %H:%M"))
    if password:
        salt = os.urandom(16); key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 200000, dklen=32)
        t["salt"] = salt.hex(); t["hmac"] = hmac.new(key, json.dumps(t, sort_keys=True).encode(), hashlib.sha256).hexdigest()
    return json.dumps(t, sort_keys=True, separators=(",", ":")).encode()

def check_ticket(payload, password=None):
    t = json.loads(payload)
    if t.get("t") != "dcf.range": raise ValueError("not a range ticket")
    if "hmac" in t:
        if not password: return dict(verdict="NEEDS PASSWORD (ticket is signed)")
        body = {k: v for k, v in t.items() if k != "hmac"}
        key = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(t["salt"]), 200000, dklen=32)
        if not hmac.compare_digest(t["hmac"], hmac.new(key, json.dumps(body, sort_keys=True).encode(), hashlib.sha256).hexdigest()):
            return dict(verdict="REJECTED: signature does not match (wrong password or altered ticket)")
    mine = rows_digest(t["lo"], t["hi"])
    v = "VERIFIED: 1/%d .. 1/%d (%d rows) recomputed here are identical to the sender's table" % (t["lo"], t["hi"], t["rows"]) \
        if mine == t["digest"] else "REFUTED: the sender's table for 1/%d .. 1/%d differs from exact recomputation" % (t["lo"], t["hi"])
    return dict(verdict=v, signed="hmac" in t, sender_program=t.get("program"), made=t.get("made"))

def make_claims_ticket(claims):
    """claims: list of dicts X, S, N (and the sender's verdict); the receiver re-checks every one itself."""
    return json.dumps(dict(t="dcf.claims", claims=claims, program=VERSION, made=time.strftime("%Y-%m-%d %H:%M")),
                      sort_keys=True, separators=(",", ":")).encode()

def check_claims_ticket(payload):
    t = json.loads(payload)
    if t.get("t") != "dcf.claims": raise ValueError("not a claims ticket")
    res = []
    for c in t["claims"]:
        try:
            r = check_claim(c["X"], c["S"], int(c["N"])); v = r["verdict"]; fp = r["first_position"]
        except Exception as ex:
            v, fp = "NOT CHECKED: %s" % ex, None
        res.append(dict(c, receiver_verdict=v, receiver_first=fp,
                        agrees=(c.get("verdict") is None or (c.get("verdict", "")[:8] == v[:8]))))
    return res

def recent_claims(k=10):
    con = db(); rows = con.execute("SELECT input, result FROM checks WHERE kind IN ('position', 'inbox') ORDER BY id DESC LIMIT ?", (k,)).fetchall(); con.close()
    out = []
    for inp, res in rows:
        i, r = json.loads(inp), json.loads(res)
        if i.get("N") in (None, ""): continue
        out.append(dict(X=i["X"], S=i["S"], N=int(i["N"]), verdict=r.get("verdict")))
    return out[::-1]

def render_frames(frames, tag):
    """PNG per frame if the qrcode package is installed, plus a text file of all frames."""
    folder = os.path.join(OUT, "qr_" + tag); os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "frames.txt"), "w") as f: f.write("\n".join(frames) + "\n")
    try:
        import qrcode
    except ImportError:
        return folder, 0
    for i, fr in enumerate(frames):
        q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=8, border=4)
        q.add_data(fr, optimize=0); q.make(fit=True)
        q.make_image().save(os.path.join(folder, "qr_%03d.png" % i))
    return folder, len(frames)

def decode_images(paths):
    """read QR codes from photos/screenshots: OpenCV if installed, else pyzbar; returns the decoded texts."""
    texts = []
    try:
        import cv2
        dets = [cv2.QRCodeDetector()]
        if hasattr(cv2, "QRCodeDetectorAruco"): dets.insert(0, cv2.QRCodeDetectorAruco())
        for p in paths:
            img = cv2.imread(p)
            if img is None: continue
            found = set()
            for det in dets:                       # try several detectors; keep every distinct code read
                try:
                    ok_, vals, _, _ = det.detectAndDecodeMulti(img)
                    if ok_: found.update(v for v in vals if v)
                except cv2.error:
                    pass
                v = det.detectAndDecode(img)[0]
                if v: found.add(v)
            texts += sorted(found)
        return texts, "opencv"
    except ImportError:
        pass
    try:
        from pyzbar.pyzbar import decode
        from PIL import Image
        for p in paths: texts += [d.data.decode() for d in decode(Image.open(p))]
        return texts, "pyzbar"
    except ImportError:
        raise RuntimeError("no QR image decoder: install opencv-python (Pydroid 3 Pip) or scan with the camera app and paste")

def menu_qr_send():
    say("a  ticket: one QR that lets another device verify your reciprocal table 1/lo .. 1/hi")
    say("b  file:   send any saved report (.json/.md/.txt) as a set of QR codes")
    say("c  claims: your recent position checks as QR codes; the receiver re-checks each claim itself")
    c = ask("a, b or c", "a").lower()
    if c == "a":
        lo = int(ask("from n", 2)); hi = int(ask("to n", 2055)); pw = ask("password to sign it (blank = unsigned)", "")
        frames = qr_frames(make_ticket(lo, hi, pw or None), "dcf.range")
        tag = "ticket_%d_%d" % (lo, hi)
    elif c == "c":
        k = int(ask("how many recent position checks", 10)); claims = recent_claims(k)
        if not claims: say("no position checks with a claimed N yet: use option 2 or 8 first"); return
        for x in claims: say("  %s contains %s at %d (your verdict: %s)" % (x["X"], x["S"], x["N"], x["verdict"]))
        frames = qr_frames(make_claims_ticket(claims), "dcf.claims"); tag = "claims_" + frames[0][5:13]
    else:
        path = ask("file to send", "")
        frames = qr_frames(open(path, "rb").read(), "file:" + os.path.basename(path)); tag = "file_" + frames[0][5:13]
    folder, png = render_frames(frames, tag)
    say("%d QR codes (1 header + %d data) -> %s" % (len(frames), len(frames) - 1, folder))
    say("PNG images written: %d%s" % (png, "" if png else " (install the qrcode package to get images; frames.txt has the text)"))
    if len(frames) > 40: say("WARNING: %d codes is a lot to scan; prefer a ticket, or share the file directly" % len(frames))

def menu_qr_receive():
    say("Paste scanned text (any order, repeats are fine), and/or give an image folder. Finish with END.")
    lines = []
    while True:
        try: l = input()
        except EOFError: break
        if l.strip() == "END": break
        lines.append(l)
    folder = ask("folder of QR photos/screenshots to decode (blank = none)", "")
    if folder:
        paths = sorted(glob.glob(os.path.join(folder, "*.png")) + glob.glob(os.path.join(folder, "*.jpg")) + glob.glob(os.path.join(folder, "*.jpeg")))
        texts, how = decode_images(paths); lines += texts; say("decoded %d codes from %d images (%s)" % (len(texts), len(paths), how))
    with open(INBOX, "a") as f: f.write("\n".join(lines) + "\n")        # partial scans are kept between runs
    done_path = os.path.join(OUT, "qr_done.txt")
    done = set(open(done_path).read().split()) if os.path.exists(done_path) else set()
    for cid, st in qr_collect(open(INBOX).read()).items():
        if cid in done: continue
        if not st.get("complete"):
            say("transfer %s: %d/%d frames (+%d parity), missing %s%s" % (cid, st["have"], st["frames"], st["parity_frames"], st["missing"][:20],
                ("; " + st["error"]) if "error" in st else ""))
            continue
        say("transfer %s complete: %s, %d bytes, SHA-256 verified" % (cid, st["kind"], len(st["payload"])))
        if st.get("rebuilt"): say("  frames rebuilt from parity: %s" % st["rebuilt"])
        if st["kind"] == "dcf.claims":
            for r in check_claims_ticket(st["payload"]):
                say("  %s contains %s at %d? receiver: %s%s" % (r["X"], r["S"], r["N"], r["receiver_verdict"],
                    "" if r["agrees"] else "   <-- DISAGREES with sender (%s)" % r.get("verdict")))
            log_check("qr_claims", dict(id=cid), dict(n=len(json.loads(st["payload"])["claims"])))
        elif st["kind"] == "dcf.range":
            pw = ""
            if b'"hmac"' in st["payload"]: pw = ask("ticket is signed; password", "")
            r = check_ticket(st["payload"], pw or None); say("  " + r["verdict"]); log_check("qr_ticket", dict(id=cid), r)
        else:
            name = st["kind"].split(":", 1)[-1]; dest = os.path.join(OUT, "received_" + cid + "_" + os.path.basename(name))
            with open(dest, "wb") as f: f.write(st["payload"])
            say("  saved:", dest); log_check("qr_file", dict(id=cid), dict(saved=dest))
        with open(done_path, "a") as f: f.write(cid + "\n")

# ---------------------------------------------------------------- reciprocal cube + math-aware compression (L1911)
# Each reciprocal 1/n is a point with exact coordinates. Every coordinate is an invariant
# with a theorem behind it, so the cube's patterns can be checked, not just observed.
#
# Theorem M (Midy criterion). Let the repeating part of 1/n be c/m (m = n without 2s and 5s,
#   period L even, h = L/2). Its period halves sum to 99...9  <=>  m divides c*(10^h + 1).
#   For n coprime to 10 (c = 1): Midy <=> 10^h = -1 (mod n).
# Theorem R (the 4.5 ratio). If the period has the Midy property, digit sum = 4.5 * L exactly
#   (base b: (b-1)/2 * L; 5.5 in base 12). For a prime p (not 2, 5): ratio = 4.5 <=> L even.
#   The converse fails for composite n (smallest example 1/21 = 0.(047619): sum 27 = 4.5*6, not Midy).
CUBE_COLS = ["n", "m", "pre", "period", "idx", "is_prime", "full_reptend", "midy", "midy_pred",
             "digit_sum", "ratio_is_4_5", "omega"]
CUBE_SCHEMA = ("CREATE TABLE IF NOT EXISTS cube(n INTEGER PRIMARY KEY, m INTEGER, pre INTEGER, period INTEGER, "
               "idx INTEGER, is_prime INTEGER, full_reptend INTEGER, midy INTEGER, midy_pred INTEGER, "
               "digit_sum INTEGER, ratio_is_4_5 INTEGER, omega INTEGER, program TEXT)")

def phi(m):
    r = m
    for p in factor(m): r = r // p * (p - 1)
    return r

def cube_row(n):
    s, L, blk = recip(n)
    m = n
    while m % 2 == 0: m //= 2
    while m % 5 == 0: m //= 5
    f = factor(n); prime = int(len(f) == 1 and list(f.values())[0] == 1)
    if L == 0:
        return (n, m, s, 0, None, prime, 0, None, None, 0, None, len(f))
    P = blk[s:]; c = int(P) * m // (10 ** L - 1)                 # repeating part = c/m
    ds = sum(map(int, P)); idx = phi(m) // L
    mid = int(L % 2 == 0 and all(int(x) + int(y) == 9 for x, y in zip(P[:L // 2], P[L // 2:])))
    pred = int(L % 2 == 0 and (c * (pow(10, L // 2, m) + 1)) % m == 0)
    return (n, m, s, L, idx, prime, int(prime and m == n and idx == 1), mid, pred, ds, int(2 * ds == 9 * L), len(f))

def cube_build(lo, hi):
    con = db(); con.execute(CUBE_SCHEMA)
    with con:
        con.executemany("INSERT OR REPLACE INTO cube VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (cube_row(n) + (VERSION,) for n in range(lo, hi + 1)))
    k = con.execute("SELECT COUNT(*) FROM cube WHERE n BETWEEN ? AND ?", (lo, hi)).fetchone()[0]
    con.close(); return k

def cube_theorems(lo, hi):
    """check Theorems M and R on every row; returns a dict of counts (all violations must be 0)."""
    con = db(); q = lambda sql: con.execute(sql + " AND n BETWEEN ? AND ?", (lo, hi)).fetchone()[0]
    r = dict(rows=q("SELECT COUNT(*) FROM cube WHERE 1"),
             periodic=q("SELECT COUNT(*) FROM cube WHERE period > 0"),
             midy=q("SELECT COUNT(*) FROM cube WHERE midy = 1"),
             M_violations=q("SELECT COUNT(*) FROM cube WHERE period > 0 AND midy != midy_pred"),
             R_violations=q("SELECT COUNT(*) FROM cube WHERE midy = 1 AND ratio_is_4_5 = 0"),
             prime_violations=q("SELECT COUNT(*) FROM cube WHERE is_prime = 1 AND period > 0 AND ratio_is_4_5 != (period % 2 = 0)"),
             ratio_4_5_not_midy=q("SELECT COUNT(*) FROM cube WHERE ratio_is_4_5 = 1 AND midy = 0"),
             prime_power_violations=q("SELECT COUNT(*) FROM cube WHERE omega = 1 AND n = m AND period > 0 AND period % 2 = 0 AND midy = 0"))
    r["smallest_ratio_4_5_not_midy"] = [x[0] for x in con.execute(
        "SELECT n FROM cube WHERE ratio_is_4_5 = 1 AND midy = 0 AND n BETWEEN ? AND ? ORDER BY n LIMIT 8", (lo, hi))]
    con.close(); return r

def cube_query(by, where="", lo=2, hi=2055, csv_path=None):
    """GROUP BY up to 3 cube columns, with an optional simple filter like 'is_prime=1 AND period%2=0'."""
    cols = [c.strip() for c in by.split(",") if c.strip()]
    if not cols or len(cols) > 3 or set(cols) - set(CUBE_COLS): raise ValueError("choose 1-3 of: " + ", ".join(CUBE_COLS))
    if where and not re.fullmatch(r"[\w\s=<>!%().,+*-]+", where): raise ValueError("filter not allowed")
    if where and set(re.findall(r"[A-Za-z_]\w*", where)) - set(CUBE_COLS) - {"AND", "OR", "NOT", "and", "or", "not", "IN", "in"}:
        raise ValueError("filter may only use cube columns")
    sql = ("SELECT %s, COUNT(*), ROUND(AVG(period),2), SUM(midy) FROM cube WHERE n BETWEEN ? AND ? %s GROUP BY %s ORDER BY %s"
           % (", ".join(cols), ("AND (%s)" % where) if where else "", ", ".join(cols), ", ".join(cols)))
    con = db(); rows = con.execute(sql, (lo, hi)).fetchall(); con.close()
    head = cols + ["count", "mean_period", "midy_count"]
    if csv_path:
        import csv
        with open(csv_path, "w", newline="") as f: w = csv.writer(f); w.writerow(head); w.writerows(rows)
    return head, rows

# -------- compression
def table_blocks(lo, hi):
    return [(n,) + recip(n) for n in range(lo, hi + 1)]

def archive_write(lo, hi, path):
    """explicit archive: index (s, L, halved) as varints + digits, Midy periods stored as their first half
    only (the second half is the 9s complement), all lzma-compressed; SHA-256 of the full digits in the header."""
    import lzma
    idx, dig, full = bytearray(), [], hashlib.sha256()
    for n, s, L, blk in table_blocks(lo, hi):
        full.update(blk.encode() + b"\n"); P = blk[s:]
        halved = L % 2 == 0 and L > 0 and all(int(x) + int(y) == 9 for x, y in zip(P[:L // 2], P[L // 2:]))
        idx += vi(s) + vi(L) + bytes([halved]); dig.append(blk[:s] + (P[:L // 2] if halved else P))
    body = lzma.compress(bytes(idx) + b"|" + "".join(dig).encode(), preset=9 | lzma.PRESET_EXTREME)
    head = json.dumps(dict(t="dcf.archive", lo=lo, hi=hi, sha256=full.hexdigest(), program=VERSION)).encode()
    with open(path, "wb") as f: f.write(head + b"\n" + body)
    return len(head) + 1 + len(body)

def archive_read(path, recompute=True):
    import lzma
    raw = open(path, "rb").read(); head, body = raw.split(b"\n", 1); h = json.loads(head)
    data = lzma.decompress(body); idx, dig = data.split(b"|", 1); dig = dig.decode()
    pos = 0; dpos = 0; full = hashlib.sha256(); blocks = []
    for n in range(h["lo"], h["hi"] + 1):
        s, pos = rv(idx, pos); L, pos = rv(idx, pos); halved = idx[pos]; pos += 1
        pre = dig[dpos:dpos + s]; dpos += s
        if halved:
            a = dig[dpos:dpos + L // 2]; dpos += L // 2; P = a + "".join(str(9 - int(x)) for x in a)
        else:
            P = dig[dpos:dpos + L]; dpos += L
        blocks.append(pre + P); full.update((pre + P).encode() + b"\n")
    ok = full.hexdigest() == h["sha256"]
    exact = all(recip(n)[2] == b for n, b in zip(range(h["lo"], h["hi"] + 1), blocks)) if recompute else None
    return dict(rows=len(blocks), sha256_ok=ok, equals_recomputation=exact)

def compression_ladder(lo, hi):
    import zlib, bz2, math
    raw = "".join(b for _, _, _, b in table_blocks(lo, hi)).encode(); D = len(raw)
    out = [("plain digits (1 byte per digit)", D)]
    out.append(("zlib level 9", len(zlib.compress(raw, 9))))
    out.append(("bz2 level 9", len(bz2.compress(raw, 9))))
    out.append(("packed digits, limit for random digits (log2 10 = 3.32 bits)", math.ceil(D * math.log2(10) / 8)))
    try:
        import lzma
        out.append(("lzma extreme", len(lzma.compress(raw, preset=9 | lzma.PRESET_EXTREME))))
        tmp = os.path.join(OUT, ".ladder.dra"); out.append(("Midy halving + lzma (explicit archive)", archive_write(lo, hi, tmp))); os.remove(tmp)
    except ImportError:
        pass
    out.append(("recipe ticket (receiver recomputes)", len(make_ticket(lo, hi))))
    return D, [(name, size, 8.0 * size / D) for name, size in out]

def menu_cube():
    lo = int(ask("from n", 2)); hi = int(ask("to n", 2055))
    k = cube_build(lo, hi); say("cube: %d rows (1/%d .. 1/%d)" % (k, lo, hi))
    t = cube_theorems(lo, hi)
    say("Theorem M (Midy criterion) violations: %d   Theorem R (Midy => digit sum = 4.5 L) violations: %d   primes: ratio 4.5 <=> even period, violations: %d"
        % (t["M_violations"], t["R_violations"], t["prime_violations"]))
    say("prime powers p^k (p not 2, 5) with even period that are not Midy: %d (theorem: always 0, because the unit group mod p^k is cyclic)" % t["prime_power_violations"])
    say("Midy rows %d of %d periodic; ratio exactly 4.5 without Midy: %d (smallest %s)"
        % (t["midy"], t["periodic"], t["ratio_4_5_not_midy"], t["smallest_ratio_4_5_not_midy"]))
    say("columns: " + ", ".join(CUBE_COLS))
    by = ask("group by (1-3 columns, comma separated)", "is_prime,midy"); wh = ask("filter (blank = none), e.g. period>0 AND period%2=0", "")
    path = os.path.join(OUT, "cube_%s.csv" % re.sub(r"\W+", "_", by))
    head, rows = cube_query(by, wh, lo, hi, path)
    say("  ".join(head))
    for r in rows[:60]: say("  ".join(str(x) for x in r))
    say("CSV:", path); log_check("cube", dict(by=by, where=wh, lo=lo, hi=hi), dict(theorems=t, cells=len(rows)))

def menu_compress():
    lo = int(ask("from n", 2)); hi = int(ask("to n", 2055))
    D, ladder = compression_ladder(lo, hi)
    say("table 1/%d .. 1/%d: %d digits (preperiod + one period each)" % (lo, hi, D))
    for name, size, bits in ladder: say("  %-62s %9d bytes  %6.3f bits/digit" % (name, size, bits))
    path = os.path.join(OUT, "reciprocals_%d_%d.dra" % (lo, hi)); size = archive_write(lo, hi, path)
    r = archive_read(path); say("archive written: %s (%d bytes); read back: SHA-256 %s, equals recomputation: %s"
                                % (path, size, "OK" if r["sha256_ok"] else "FAILED", r["equals_recomputation"]))

# ---------------------------------------------------------------- E8 labels (L1925)
# The 240 roots of E8 used as frame labels. Honest scope: a label is an ADDRESS (it restores order,
# like a frame number). Its geometric extra is noise tolerance: E8 roots are 60 degrees apart, so a
# label blurred by analog noise snaps back to the right root more often than with a random 240-point code.
def e8_roots():
    import itertools
    R = []
    for i, j in itertools.combinations(range(8), 2):
        for a, b in itertools.product((-2, 2), repeat=2):
            v = [0] * 8; v[i] = a; v[j] = b; R.append(tuple(v))
    for v in itertools.product((-1, 1), repeat=8):
        if sum(x < 0 for x in v) % 2 == 0: R.append(tuple(v))
    return R                                        # doubled coordinates, squared length 8

def e8_check():
    R = e8_roots(); ip = lambda a, b: sum(x * y for x, y in zip(a, b))
    deg = [sum(1 for b in R if ip(a, b) == 4) for a in R]
    return dict(roots=len(R), distinct=len(set(R)), norms=sorted({ip(a, a) for a in R}),
                neighbours=sorted(set(deg)), edges=sum(deg) // 2)

def e8_nearest(R, y):
    return max(range(len(R)), key=lambda i: sum(a * b for a, b in zip(R[i], y)))

def e8_order_test(payload, kind, seed=11):
    """frames labelled by E8 roots, shuffled, restored by label, reassembled; SHA-256 checked on what was RECEIVED."""
    import random
    R = e8_roots(); fr = qr_frames(payload, kind, parity=0)
    if len(fr) > 240: raise ValueError("more than 240 frames: E8 has only 240 labels")
    labelled = [(R[i], f.split(":", 5)[5]) for i, f in enumerate(fr)]        # label + frame body only (number removed)
    random.Random(seed).shuffle(labelled)
    restored = sorted(labelled, key=lambda t: e8_nearest(R, t[0]))
    head = restored[0][1]; body = "".join(t[1] for t in restored[1:])
    got = zlib.decompress(unb32(body))
    sha_ok = hashlib.sha256(got).hexdigest().upper() == fr[0].split(":")[4]
    return dict(frames=len(fr), restored_identical=(got == payload), sha256_of_received_ok=sha_ok)

def e8_noise_test(sigmas=(0.15, 0.25, 0.35), trials=500, seed=9):
    """symbol error rate: E8 labels vs a random 240-point code on the same 8-D sphere, same Gaussian noise."""
    import random, math
    norm = lambda v: [x / math.sqrt(sum(t * t for t in v)) for x in v]
    E = [norm(r) for r in e8_roots()]
    rg = random.Random(1); Rnd = [norm([rg.gauss(0, 1) for _ in range(8)]) for _ in range(240)]
    out = []
    for s in sigmas:
        row = [s]
        for C in (E, Rnd):
            g = random.Random(seed); e = 0
            for _ in range(trials):
                k = g.randrange(240); y = [x + g.gauss(0, s) for x in C[k]]
                e += e8_nearest(C, y) != k
            row.append(e / trials)
        out.append(tuple(row))
    return out

def menu_e8():
    c = e8_check()
    say("E8: %d roots (%d distinct), squared length %s, %d neighbours each, %d edges" % (c["roots"], c["distinct"], c["norms"], c["neighbours"][0], c["edges"]))
    lo = int(ask("ticket from n", 221)); hi = int(ask("to n", 401))
    r = e8_order_test(make_ticket(lo, hi), "dcf.range")
    say("order test (%d frames, shuffled, restored by E8 label): identical %s, SHA-256 of received payload %s"
        % (r["frames"], r["restored_identical"], "OK" if r["sha256_of_received_ok"] else "FAILED"))
    if ask("run the noise test? (about a minute on a phone) y/n", "n").lower().startswith("y"):
        for s, e8e, rnd in e8_noise_test():
            say("  noise sigma %.2f: E8 label errors %.1f%%   random 240-point code %.1f%%" % (s, 100 * e8e, 100 * rnd))
        say("E8 helps only when labels pass through an analog, noisy channel; QR codes are digital and already error-corrected.")
    log_check("e8", dict(lo=lo, hi=hi), r)

# ---------------------------------------------------------------- Gaussian channel + spherical code (L1930)
def min_angle(C):
    import math, itertools
    best = max(sum(a * b for a, b in zip(u, v)) for u, v in itertools.combinations(C, 2))
    return math.degrees(math.acos(min(1.0, best)))

def gaussian_channel(sigmas, trials=500, seed=9, codes=3):
    """E8 vs several random 240-point codes on the 8-D unit sphere; Gaussian noise added to every coordinate."""
    import random, math
    norm = lambda v: [x / math.sqrt(sum(t * t for t in v)) for x in v]
    E = [norm(r) for r in e8_roots()]
    rand = []
    for c in range(codes):
        rg = random.Random(c + 1); rand.append([norm([rg.gauss(0, 1) for _ in range(8)]) for _ in range(240)])
    def err(C, s):
        g = random.Random(seed); e = 0
        for _ in range(trials):
            k = g.randrange(240); y = [x + g.gauss(0, s) for x in C[k]]
            e += e8_nearest(C, y) != k
        return e / trials
    angles = dict(e8=min_angle(E), random=[min_angle(C) for C in rand])
    rows = [(s, err(E, s), [err(C, s) for C in rand]) for s in sigmas]
    return angles, rows

def menu_gauss():
    say("Gaussian channel: each 8-D label gets independent Gaussian noise of size sigma per coordinate;")
    say("the receiver picks the nearest of the 240 labels. E8 roots vs random 240-point codes.")
    sig = ask("sigmas (comma separated)", "0.05,0.10,0.15,0.20,0.25,0.35")
    sigmas = [float(x) for x in sig.split(",") if x.strip()]; trials = int(ask("trials per value (500 is about a minute)", 500))
    ang, rows = gaussian_channel(sigmas, trials)
    say("smallest angle between labels: E8 %.1f deg; random codes %s deg" % (ang["e8"], ", ".join("%.1f" % a for a in ang["random"])))
    say("sigma   E8 errors   random codes (each)          relative reduction vs mean random")
    for s, e, rs in rows:
        mr = sum(rs) / len(rs)
        say("%5.2f   %6.1f%%     %-28s %s" % (s, 100 * e, " ".join("%5.1f%%" % (100 * x) for x in rs),
                                             ("%.0f%%" % (100 * (mr - e) / mr)) if mr > 0 else "-"))
    say("Reading: E8's 60-degree spacing cuts label errors most at low noise. It matters for analog channels")
    say("(tones, light levels, raw signal amplitudes), not for QR codes, which deliver exact bytes.")
    log_check("gauss", dict(sigmas=sigmas, trials=trials), dict(angles=ang, rows=rows))

# ---------------------------------------------------------------- balance explorer + Theorem F (L1927, L1930)
def cycles_mod(n):
    """cycles of x -> 10x on the units mod n: list of (start, remainder sum, length)."""
    from math import gcd
    seen = bytearray(n); out = []
    for a in range(1, n):
        if seen[a] or gcd(a, n) != 1: continue
        s = 0; L = 0; x = a
        while not seen[x]:
            seen[x] = 1; s += x; L += 1; x = x * 10 % n
        out.append((a, s, L))
    return out

def digit_sum_cycle(a, p):
    s, L, r = 0, mult_order(10, p), a % p
    for _ in range(L): s += (10 * r) // p; r = (10 * r) % p
    return s

def surviving_conductors(p, q, cap=600):
    """n = p*q (distinct primes, coprime to 10): conductors of odd characters trivial on <10> with c_chi != 0.
    Pure Python; returns None if there are more than `cap` characters to test."""
    import cmath, math
    def plog(m):
        g = next(g for g in range(2, m) if all(pow(g, (m - 1) // f, m) != 1 for f in factor(m - 1)))
        lg = [0] * m; x = 1
        for e in range(m - 1): lg[x] = e; x = x * g % m
        return lg
    lp, lq = plog(p), plog(q); n = p * q
    la, lb = lp[10 % p], lq[10 % q]
    pairs = [(a, b) for a in range(p - 1) for b in range(q - 1)
             if (a * la * (q - 1) + b * lb * (p - 1)) % ((p - 1) * (q - 1)) == 0 and (a + b) % 2 == 1]
    if len(pairs) > cap: return None
    rs = [r for r in range(1, n) if r % p and r % q]
    conds = set()
    for a, b in pairs:
        c = sum(cmath.exp(2j * math.pi * (a * lp[r % p] / (p - 1) + b * lq[r % q] / (q - 1))) * r for r in rs)
        if abs(c) > 1e-6 * n: conds.add((p if a else 1) * (q if b else 1))
    return conds

def balance_report(n):
    f = factor(n)
    if n < 3 or any(p in (2, 5) for p in f): raise ValueError("n must be coprime to 10 and > 2")
    cyc = cycles_mod(n); L = cyc[0][2]
    bal = [a for a, s, l in cyc if 2 * s == n * l]
    one = next(2 * s == n * l for a, s, l in cyc if a == 1)
    r = dict(n=n, factors=f, period=L, cycles=len(cyc), balanced_cycles=len(bal), one_over_n_balanced=one,
             universally_balanced=len(bal) == len(cyc), midy=(L % 2 == 0 and pow(10, L // 2, n) == n - 1))
    if len(f) == 2 and all(e == 1 for e in f.values()):
        p, q = sorted(f)
        sc = surviving_conductors(p, q)
        r["surviving_conductors"] = sorted(sc) if sc is not None else "too many characters to test"
        for P, Q in ((p, q), (q, p)):
            if sc is not None and sc and sc <= {P}:
                d1 = digit_sum_cycle(1, P); dq = digit_sum_cycle(pow(Q, -1, P), P)
                r["theorem_F"] = dict(p=P, digit_sum_1_over_p=d1, q_inverse=pow(Q, -1, P), digit_sum_qinv_over_p=dq,
                                      predicts_balanced=(d1 == dq), agrees=((d1 == dq) == one))
    return r

def menu_balance():
    n = int(ask("denominator n (coprime to 10)", 287)); r = balance_report(n)
    say("1/%d: period %d; %d cycles of remainders, %d balanced (digit sum exactly 4.5 x period)" % (n, r["period"], r["cycles"], r["balanced_cycles"]))
    say("1/%d itself balanced: %s;  every fraction a/%d balanced (universal balance): %s;  Midy: %s"
        % (n, r["one_over_n_balanced"], n, r["universally_balanced"], r["midy"]))
    if "surviving_conductors" in r: say("odd characters with nonzero c_chi have conductors: %s" % r["surviving_conductors"])
    if "theorem_F" in r:
        t = r["theorem_F"]
        say("Theorem F applies (only conductor %d survives): digit sum of 1/%d = %d, of %d/%d = %d -> predicts %s; actual %s %s"
            % (t["p"], t["p"], t["digit_sum_1_over_p"], t["q_inverse"], t["p"], t["digit_sum_qinv_over_p"],
               "balanced" if t["predicts_balanced"] else "not balanced", "balanced" if r["one_over_n_balanced"] else "not balanced",
               "(agrees)" if t["agrees"] else "(DISAGREES - please report)"))
    log_check("balance", dict(n=n), r)

# ---------------------------------------------------------------- harmonics, quantum period finding, Fibonacci memory (L1933)
def harmonics(n, maxL=800):
    """DFT of the centred digits x_j = d_j - 4.5 of 1/n (n coprime to 10). Balanced <=> DC = 0; Midy <=> every even harmonic = 0."""
    import cmath, math
    if n < 3 or n % 2 == 0 or n % 5 == 0: raise ValueError("n must be odd, not divisible by 5, and > 2")
    L = mult_order(10, n)
    if L > maxL: raise ValueError("period %d is longer than %d (too slow on a phone)" % (L, maxL))
    x = [d - 4.5 for d in map(int, digits(1, n, L))]
    X = [sum(x[j] * cmath.exp(-2j * math.pi * j * k / L) for j in range(L)) for k in range(L)]
    P = [abs(z) ** 2 for z in X]; tot = sum(P) or 1.0
    even = sum(P[k] for k in range(0, L, 2)); odd = tot - even
    return dict(n=n, L=L, dc=abs(X[0]), balanced=abs(X[0]) < 1e-6, even_energy=even / tot, odd_energy=odd / tot,
                midy=(L % 2 == 0 and pow(10, L // 2, n) == n - 1), even_harmonics_zero=(even / tot < 1e-12),
                top=sorted(range(1, L), key=lambda k: -P[k])[:5])

def _fft(a):
    import cmath
    n = len(a); a = list(a); j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit: j ^= bit; bit >>= 1
        j |= bit
        if i < j: a[i], a[j] = a[j], a[i]
    size = 2
    while size <= n:
        w = cmath.exp(-2j * cmath.pi / size)
        for s in range(0, n, size):
            wk = 1
            for k in range(size // 2):
                u = a[s + k]; v = a[s + k + size // 2] * wk
                a[s + k] = u + v; a[s + k + size // 2] = u - v; wk *= w
        size <<= 1
    return a

def shor_simulation(n, base=10, shots=8, seed=1):
    """Classical simulation of the quantum period-finding step of Shor's algorithm for small n,
    followed by the classical factoring step. Finds L = ord_n(base) = the period of the reciprocal 1/n."""
    import random
    from math import gcd
    from fractions import Fraction
    if not 3 <= n <= 255 or gcd(n, base) != 1: raise ValueError("use 3 <= n <= 255 with gcd(n, base) = 1")
    q = (n * n - 1).bit_length(); Q = 1 << q                       # Q >= n^2
    rg = random.Random(seed); x0 = rg.randrange(Q); v = pow(base, x0, n)
    reg = [1.0 if pow(base, x, n) == v else 0.0 for x in range(Q)]   # first register after measuring f(x) = v
    amp = _fft(reg); prob = [abs(z) ** 2 for z in amp]; s = sum(prob); prob = [p / s for p in prob]
    cands = []
    for _ in range(shots):
        y = rg.choices(range(Q), weights=prob)[0]
        r = Fraction(y, Q).limit_denominator(n).denominator          # continued fractions
        cands.append((y, r))
    from math import lcm
    L = 1
    for _, r in cands:
        if r: L = lcm(L, r)
    true_L = mult_order(base, n)
    out = dict(n=n, qubits=q, Q=Q, measured_value=v, samples=cands, period_found=L if pow(base, L, n) == 1 else None, true_period=true_L)
    if out["period_found"] and out["period_found"] % 2 == 0:
        h = pow(base, out["period_found"] // 2, n)
        if h == n - 1: out["factor_step"] = "fails: base^(L/2) = -1 mod n, i.e. 1/n is Midy"
        else:
            f = gcd(h - 1, n); out["factor_step"] = "factor found: %d = %d x %d" % (n, f, n // f) if 1 < f < n else "no factor (n prime or prime power)"
    elif out["period_found"]:
        out["factor_step"] = "fails: the period is odd"
    peak = Q / true_L
    out["mass_on_peaks"] = sum(prob[y] for y in range(Q) if abs(y / peak - round(y / peak)) * peak <= 1.0)
    return out

def pisano(m):
    a, b, k = 0, 1, 0
    while True:
        a, b = b, (a + b) % m; k += 1
        if (a, b) == (0, 1): return k

def fib_memory(m):
    """Fibonacci mod m: period (Pisano), and whether the second half is the negative of the first (a Midy law for Fibonacci)."""
    p = pisano(m); F = [0, 1]
    for _ in range(2 * p + 2): F.append((F[-1] + F[-2]) % m)
    half = p % 2 == 0 and all((F[k + p // 2] + F[k]) % m == 0 for k in range(p))
    return dict(m=m, pisano=p, half_period_negation=half, first=F[:min(p, 60)])

def fib_balance(m):
    """residue sum S over one Pisano period, mean vs (m-1)/2, defect D = 2S - (m-1)P, rank alpha, mirror,
    and the Theorem B family of m (equal mean <=> m = 5^k)."""
    a, b, P, S, z, alpha = 0, 1 % m, 0, 0, 0, None
    while True:
        S += a; z += (a == 0)
        if a == 0 and P > 0 and alpha is None: alpha = P
        a, b = b, (a + b) % m; P += 1
        if (a, b) == (0, 1 % m): break
    k, d = 0, m
    while d % 5 == 0: d //= 5; k += 1
    fam = {1: "5^k", 2: "2*5^k", 6: "6*5^k", 12: "12*5^k"}.get(d)
    return dict(m=m, period=P, sum=S, zeros=z, alpha=alpha, mean=S / P, uniform_mean=(m - 1) / 2,
                defect=2 * S - (m - 1) * P, mirror=fib_memory(m)["half_period_negation"],
                family=fam if (fam and (k >= 1 or d in (6, 12))) else None)

def recurrence_gf_checks():
    from fractions import Fraction
    def gsum(init, rule, N=400):
        v = list(init); s = Fraction(0)
        for k in range(N):
            s += Fraction(v[0], 10 ** (k + 1)); v = v[1:] + [rule(v)]
        return s
    rows = [("Fibonacci (0,1)", [0, 1], sum, Fraction(1, 89)), ("Lucas (2,1)", [2, 1], sum, Fraction(19, 89)),
            ("Pell (0,1)", [0, 1], lambda v: v[0] + 2 * v[1], Fraction(1, 79)), ("Tribonacci (0,0,1)", [0, 0, 1], sum, Fraction(1, 889))]
    return [(name, str(t), abs(gsum(i, r) - t) < Fraction(1, 10 ** 200)) for name, i, r, t in rows]

def menu_harmonics():
    n = int(ask("denominator n (odd, not a multiple of 5)", 17)); h = harmonics(n)
    say("1/%d: period %d. DC (zero-frequency) term %.3g -> %s" % (n, h["L"], h["dc"], "balanced: digit average exactly 4.5" if h["balanced"] else "not balanced"))
    say("energy in even harmonics %.4f, odd harmonics %.4f; Midy %s; even harmonics all zero %s"
        % (h["even_energy"], h["odd_energy"], h["midy"], h["even_harmonics_zero"]))
    say("strongest harmonics k: %s" % h["top"])
    say("Theorems: balanced <=> DC = 0;  Midy <=> every even harmonic vanishes (half-period antisymmetry).")
    log_check("harmonics", dict(n=n), h)

def menu_shor():
    say("Shor's algorithm finds the period of base^x mod n -- for base 10 that is the period of 1/n.")
    say("This is a classical SIMULATION of the quantum step (no quantum hardware), practical for n <= 255.")
    n = int(ask("n", 21)); r = shor_simulation(n)
    say("register: %d qubits (Q = %d); measured 10^x mod n = %d; probability on the ideal peaks %.3f" % (r["qubits"], r["Q"], r["measured_value"], r["mass_on_peaks"]))
    say("samples (y, continued-fraction denominator): %s" % r["samples"])
    say("period found %s (true period of 1/%d: %d)" % (r["period_found"], n, r["true_period"]))
    if "factor_step" in r: say("factoring step: " + r["factor_step"])
    log_check("shor", dict(n=n), {k: v for k, v in r.items() if k != "samples"})

def menu_fib():
    m = int(ask("modulus m (10 = last digits, 9 = digital roots)", 10)); f = fib_memory(m)
    say("Fibonacci mod %d repeats every %d steps (Pisano period)" % (m, f["pisano"]))
    say("second half = negative of the first half (a Midy law, F(n + P/2) = -F(n) mod m): %s" % f["half_period_negation"])
    say("first terms: %s" % f["first"])
    F = [0, 1]
    for _ in range(300): F.append(F[-1] + F[-2])
    from fractions import Fraction
    err = abs(sum(Fraction(F[k], 10 ** (k + 1)) for k in range(300)) - Fraction(1, 89))
    import math
    say("1/89 = sum of F(k)/10^(k+1): error after 300 terms < 1e-%d" % (len(str(err.denominator)) - len(str(err.numerator)) - 1))
    say("phi = 2 cos(pi/5): %.15f vs %.15f" % ((1 + 5 ** 0.5) / 2, 2 * math.cos(math.pi / 5)))
    fb = fib_balance(m)
    say("balance: residue sum %d over %d steps, mean %.4f vs uniform mean %.1f, defect D = %d; rank alpha = %s; zeros per cycle %d"
        % (fb["sum"], fb["period"], fb["mean"], fb["uniform_mean"], fb["defect"], fb["alpha"], fb["zeros"]))
    say("Theorem B: the mean equals (m-1)/2 exactly when m is a power of 5. %s"
        % ("m = %s is in a candidate family (5^k, 2*5^k, 6*5^k, 12*5^k), with defect D = %d" % (fb["family"], fb["defect"]) if fb["family"] else "m is not in any candidate family, so its mean cannot equal (m-1)/2"))
    for name, t, okk in recurrence_gf_checks():
        say("  sum of %s terms / 10^(k+1) = %s: %s" % (name, t, "exact" if okk else "MISMATCH"))
    log_check("fibonacci", dict(m=m), dict(pisano=f["pisano"], half=f["half_period_negation"]))

# ---------------------------------------------------------------- Fibonacci wheels (L1940)
# Wheel of 60: position k (1..60) shows F(k) mod 10 (last digit).
# Wheel of 24: position k (1..24) shows the digital root of F(k) (1..9).
# Theorem W: with P the wheel size and h = P/2,
#   (a) half-turn:  F(k+h) = -F(k) (mod m)    -> nonzero digits sum to 10 (wheel 60; zero pairs show 0+0) / 9 (wheel 24; 9 pairs with 9 -> 18)
#   (b) reflection: F(P-k) = (-1)^(k+1) F(k)  -> odd k: equal digits; even k: complementary digits
# so every position lies in a "quartet" {k, P-k, h+k, h-k} (the orbit of a Klein four-group),
# whose positions always sum to 2P (120 or 48) and whose digits sum to 20 (or 18).
def fib_wheel(P):
    if P not in (24, 60): raise ValueError("wheels are 24 (digital roots) and 60 (last digits)")
    F = [0, 1]
    for _ in range(P + 2): F.append(F[-1] + F[-2])
    val = {k: (F[k] % 10 if P == 60 else 1 + (F[k] - 1) % 9) for k in range(1, P + 1)}
    wrap = lambda x: (x - 1) % P + 1
    rows = []
    for k in range(1, P + 1):
        q = tuple(sorted({wrap(k), wrap(P - k), wrap(P // 2 + k), wrap(P // 2 - k)}))
        rows.append(dict(pos=k, fib=F[k], value=val[k], reflect=wrap(P - k), half=wrap(k + P // 2), cross=wrap(P // 2 - k),
                         quartet=q, pos_sum=sum(q), digit_sum=sum(val[x] for x in q)))
    return rows, val

def wheel_theorem_check(P):
    rows, val = fib_wheel(P); comp = 10 if P == 60 else 9; bad = 0
    for r in rows:
        k, a = r["pos"], r["value"]; b, c = val[r["reflect"]], val[r["half"]]
        okr = (a == b) if k % 2 else ((a + b) % comp == 0)
        bad += not (okr and (a + c) % comp == 0)
    return bad

def wheel_db(P):
    rows, _ = fib_wheel(P); con = db()
    with con:
        con.execute("CREATE TABLE IF NOT EXISTS fib_wheel(wheel INTEGER, pos INTEGER, fib TEXT, value INTEGER, reflect INTEGER, half INTEGER, cross INTEGER, quartet TEXT, quartet_pos_sum INTEGER, quartet_digit_sum INTEGER, PRIMARY KEY(wheel, pos))")
        con.executemany("INSERT OR REPLACE INTO fib_wheel VALUES(?,?,?,?,?,?,?,?,?,?)",
                        [(P, r["pos"], str(r["fib"]), r["value"], r["reflect"], r["half"], r["cross"], " ".join(map(str, r["quartet"])), r["pos_sum"], r["digit_sum"]) for r in rows])
    con.close(); return len(rows)

def reciprocal_link(s):
    """what the reciprocal side says about a position sum s (and about the Fibonacci number F(s))."""
    out = dict(s=s, mod60=s % 60, mod24=s % 24, factors=factor(s) if s > 1 else {})
    if s >= 2:
        pre, L, blk = recip(s); per = blk[pre:]
        out.update(preperiod=pre, period=L, midy=midy(s), period_digit_sum=sum(map(int, per)) if L else 0,
                   ratio_4_5=(L > 0 and 2 * sum(map(int, per)) == 9 * L))
    a, b = 0, 1
    for _ in range(s): a, b = b, a + b
    out["F_s"] = a; out["F_s_small_prime_factors"] = {p: e for p, e in factor_small(a).items()} if a > 1 else {}
    return out

def factor_small(n, bound=10000):
    f, d = {}, 2
    while d <= bound and d * d <= n:
        while n % d == 0: f[d] = f.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: f[n if n < bound * bound else "cofactor>%d" % (bound * bound)] = 1
    return f

def menu_wheels():
    P = int(ask("wheel (60 = last digits, 24 = digital roots)", 24))
    rows, val = fib_wheel(P); n = wheel_db(P)
    say("Wheel of %d (stored in database table fib_wheel, %d rows). Theorem W violations: %d" % (P, n, wheel_theorem_check(P)))
    seen = set()
    for r in rows:
        if r["quartet"] in seen: continue
        seen.add(r["quartet"])
        say("  quartet %-18s digits %-14s position sum %3d  digit sum %2d" % (r["quartet"], [val[x] for x in r["quartet"]], r["pos_sum"], r["digit_sum"]))
    say("Every full quartet has position sum %d and digit sum %d: these follow from Theorem W, for every quartet alike." % (2 * P, 20 if P == 60 else 18))
    pos = ask("positions to combine (comma separated, e.g. 5,7,17,19)", "5,7,17,19")
    ps = [int(x) for x in pos.split(",") if x.strip()]
    s = sum(ps)
    say("positions %s: digits %s, position sum %d, digit sum %d" % (ps, [val[((x - 1) % P) + 1] for x in ps], s, sum(val[((x - 1) % P) + 1] for x in ps)))
    rl = reciprocal_link(s)
    say("reciprocal link for %d: factors %s; 1/%d has preperiod %s, period %s, Midy %s, period digit sum %s, 4.5 ratio %s"
        % (s, rl["factors"], s, rl.get("preperiod"), rl.get("period"), rl.get("midy"), rl.get("period_digit_sum"), rl.get("ratio_4_5")))
    say("F(%d) = %d, small prime factors %s" % (s, rl["F_s"], rl["F_s_small_prime_factors"]))
    say("Base rate: about 40-50% of all sums of 2-4 positions on the 24-wheel are multiples of 11 or 12, or next to a square;")
    say("so a single 'connector' sum is not evidence by itself. The structural facts are the quartets (Theorem W).")
    log_check("wheels", dict(P=P, positions=ps), {k: (str(v) if k.startswith("F_s") else v) for k, v in rl.items()})

# ---------------------------------------------------------------- more wheels, wheel links, Fibonacci prime table (L1944)
SEQS = {"fibonacci": ((0, 1), 1, +1), "lucas": ((2, 1), 1, -1), "pell": ((0, 1), 2, +1)}   # seed, a in x(n+1) = a x(n) + x(n-1), reflection type

def seq_wheel(name, kind):
    """kind: 'last' (mod 10) or 'root' (digital roots, mod 9). Returns period P, values 1..P, terms.
    Reflection law: x(P-k) = s (-1)^(k+1) x(k), with s = +1 (Fibonacci, Pell) or -1 (Lucas)."""
    seed, a, s = SEQS[name]; m = 10 if kind == "last" else 9
    x = list(seed)
    while True:
        x.append(a * x[-1] + x[-2])
        if len(x) > 3 and x[-2] % m == seed[0] % m and x[-1] % m == seed[1] % m: break
    P = len(x) - 2
    val = {k: (x[k] % 10 if m == 10 else (1 + (x[k] - 1) % 9 if x[k] > 0 else 0)) for k in range(1, P + 1)}
    return P, val, x, s

def seq_wheel_check(name, kind):
    P, val, x, s = seq_wheel(name, kind); m = 10 if kind == "last" else 9
    refl = all((x[P - k] - s * (-1) ** (k + 1) * x[k]) % m == 0 for k in range(1, P))
    half = P % 2 == 0 and all((x[k + P // 2] + x[k]) % m == 0 for k in range(1, P // 2 + 1))
    return P, refl, half

def wheel_links():
    """which 24-wheel quartets each 60-wheel quartet touches (positions k = 1..120 read mod 60 and mod 24)."""
    w = lambda k, P: (k - 1) % P + 1
    q = lambda k, P: tuple(sorted({w(k, P), w(P - k, P), w(P // 2 + k, P), w(P // 2 - k, P)}))
    inc = {}
    for k in range(1, 121): inc.setdefault(q(k, 60), set()).add(q(k, 24))
    return {a: sorted(b) for a, b in sorted(inc.items())}

def fib_rank(p):
    a, b, k = 0, 1 % p, 0
    while True:
        a, b = b, (a + b) % p; k += 1
        if a == 0: return k

def fib_prime_table(limit=1000):
    rows = []
    for p in range(3, limit + 1):
        if any(p % d == 0 for d in range(2, int(p ** 0.5) + 1)): continue
        rows.append((p, fib_rank(p), pisano(p), mult_order(10, p) if p != 5 else 0))
    con = db()
    with con:
        con.execute("CREATE TABLE IF NOT EXISTS fib_rank(p INTEGER PRIMARY KEY, rank_alpha INTEGER, pisano INTEGER, period_1_over_p INTEGER)")
        con.executemany("INSERT OR REPLACE INTO fib_rank VALUES(?,?,?,?)", rows)
    con.close(); return rows

def menu_wheels2():
    say("sequences: fibonacci, lucas, pell;  wheels: last (last digits) or root (digital roots)")
    name = ask("sequence", "lucas").lower(); kind = ask("wheel", "last").lower()
    P, val, x, s = seq_wheel(name, kind); P2, refl, half = seq_wheel_check(name, kind)
    say("%s %s-wheel: %d positions; reflection law x(P-k) = %s(-1)^(k+1) x(k): %s; half-turn mirror: %s"
        % (name, kind, P, "+" if s > 0 else "-", refl, half))
    say("values: %s" % [val[k] for k in range(1, P + 1)])
    if name == "fibonacci":
        say("joint wheel F mod 90 (period 120): exact twist F(k+60) = 71*F(k) mod 90  (71 = 1 mod 10, -1 mod 9, 71^2 = 1 mod 90)")
        say("links between the Fibonacci 60-wheel and 24-wheel quartets, read on the common 120-clock (positions k = 1..120);")
        say("each 60-quartet meets the listed 24-quartets, contributing two positions to each:")
        for a, b in wheel_links().items(): say("  %-18s -> %s" % (a, b))

def menu_fibprimes():
    lim = int(ask("primes up to", 1000)); rows = fib_prime_table(lim)
    say("stored %d primes in table fib_rank: p, rank alpha(p) (p divides F(k) exactly when alpha(p) divides k), Pisano period, period of 1/p" % len(rows))
    k = int(ask("which primes divide F(k)? k =", 19))
    hits = [p for p, al, pi_, L in rows if k % al == 0]
    say("primes up to %d dividing F(%d): %s" % (lim, k, hits))
    for p, al, pi_, L in rows[:25]: say("  p=%4d  alpha=%4d  pisano=%5d  period of 1/p=%4d" % (p, al, pi_, L))
    pp = primitive_primes(k, max(lim, 100000))
    say("primitive primes of F(%d) (first appearance at k = %d; each is 2, 3, 5 or = +-1 mod k): %s" % (k, k, pp["primitive_found"]))
    if pp["unexplained_cofactor"] > 1:
        say("  remaining primitive cofactor %d (%s)" % (pp["unexplained_cofactor"], "prime (Miller-Rabin, deterministic below 3.3e24)" if pp["cofactor_is_prime"] else "not resolved by this search"))
    say("Carmichael (1913): every F(k) with k not in {1, 2, 6, 12} has a primitive prime factor (checked here for k <= 150).")

# ---------------------------------------------------------------- recurrence balance, other bases, primitive primes (L1948)
def seq_balance(name, m):
    """orbit of the sequence mod m: period P, residue sum S, defect D = 2S - (m-1)P (D = 0 means mean (m-1)/2).
    Theorems (L1948): Fibonacci balanced <=> m = 5^k (Theorem B); Lucas never (B_L); Pell never, D = -m at m = 2^a (B_P)."""
    seed, a, _ = SEQS[name]; x0, y0 = seed[0] % m, seed[1] % m; x, y, P, S = x0, y0, 0, 0
    while True:
        S += x; P += 1; x, y = y, (a * y + x) % m
        if (x, y) == (x0, y0): break
    return dict(m=m, period=P, sum=S, defect=2 * S - (m - 1) * P)

def base_wheels(b):
    """base b: last-digit wheel = F mod b, digit-root wheel = F mod (b-1). Returns sizes and half-turn mirrors.
    Full quartets on both wheels need both mirrors (base 10 yes; base 12 neither)."""
    out = []
    for m in (b, b - 1):
        if m < 3: out += [pisano(m) if m > 1 else 1, None]; continue
        f = fib_memory(m); out += [f["pisano"], f["half_period_negation"]]
    return tuple(out)

def is_prime_mr(n):
    """deterministic Miller-Rabin for n < 3.3e24 (bases = first 12 primes)."""
    if n < 2: return False
    ps = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
    for p in ps:
        if n % p == 0: return n == p
    d, r = n - 1, 0
    while d % 2 == 0: d //= 2; r += 1
    for a in ps:
        x = pow(a, d, n)
        if x in (1, n - 1): continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1: break
        else: return False
    return True

def primitive_primes(k, limit=100000):
    """primes p <= limit with alpha(p) = k (first appearance in F(k)). Uses p = 2, 3, 5 or p = +-1 (mod k)."""
    a, b = 0, 1
    for _ in range(k): a, b = b, a + b
    Fk = a; found = []
    cands = [p for p in (2, 3, 5) if p <= limit] + sorted({c for j in range(1, limit // max(k, 1) + 2) for c in (j * k - 1, j * k + 1) if 5 < c <= limit})
    for p in cands:
        if Fk % p == 0 and all(p % d for d in range(2, int(p ** 0.5) + 1)) and fib_rank(p) == k: found.append(p)
    rest = Fk
    for j in range(1, k):
        if k % j == 0:
            g = 1; a2, b2 = 0, 1
            for _ in range(j): a2, b2 = b2, a2 + b2
            for p in factor_small(a2, 2000):
                if isinstance(p, int):
                    while rest % p == 0: rest //= p
    for p in found:
        while rest % p == 0: rest //= p
    return dict(k=k, F=Fk, primitive_found=found, unexplained_cofactor=rest,
                cofactor_is_prime=rest > 1 and (rest < limit * limit or (rest < 3 * 10 ** 24 and is_prime_mr(rest))))

def ab_orbit(a, m, s0=0, s1=1):
    """x(n+1) = a x(n) + x(n-1), seeds s0, s1, mod m: period, residue sum, defect, uniform distribution?"""
    x0, y0 = s0 % m, s1 % m; x, y, P, S = x0, y0, 0, 0; cnt = [0] * m
    while True:
        S += x; cnt[x] += 1; P += 1; x, y = y, (a * y + x) % m
        if (x, y) == (x0, y0): break
    return dict(a=a, m=m, period=P, sum=S, defect=2 * S - (m - 1) * P, uniform=len(set(cnt)) == 1)

def bg_set(a, m):
    """Theorem BG (L1952): balanced <=> m = d * prod p^k, p odd primes dividing a^2 + 4, d = 1 (a odd) or d in {1, 2} (a even)."""
    D, r = a * a + 4, m
    if a % 2 == 0 and r % 2 == 0: r //= 2
    p = 3
    while p * p <= D or p <= D:
        if D % p == 0:
            while r % p == 0: r //= p
            while D % p == 0: D //= p
        p += 2
        if p > D: break
    return r == 1 and m >= 3

def ud_predict(a, m, s0=0, s1=1):
    """Theorem BG* (L1956): u.d. mod m <=> m = d * prod p^k (odd p | a^2+4) with 2*s0 + a*s1 != 0 mod each such p,
    d = 1, or d = 2 when a is even and s0 + s1 is odd.  (Sufficiency proved; necessity proved when gcd(a, m) = 1.)"""
    D, r = a * a + 4, m
    if a % 2 == 0 and r % 2 == 0:
        if (s0 + s1) % 2 == 0: return False
        r //= 2
    p = 3
    while p <= D:
        if D % p == 0:
            if r % p == 0 and (2 * s0 + a * s1) % p == 0: return False
            while r % p == 0: r //= p
            while D % p == 0: D //= p
        p += 2
    return r == 1 and m >= 3

def balance_predict(a, m, s0, s1):
    """Proved balance predictions (L1960).  Returns (answer, reason); answer None = outside the proved range.
    Prop X: a prime p >= 5 of m dividing neither a nor a^2+4 -> never balanced.
    Theorem T*: m odd, every prime of m divides a or a^2+4, seed a unit at the primes of a and non-degenerate at the
    primes of a^2+4 -> balanced <=> s0 + s1 = -1 (mod G), G = prod q^min(v_q(a), v_q(m)) over primes q of m dividing a."""
    D = a * a + 4; fs = factor_small(m, 100000); ps = [p for p in fs if isinstance(p, int)]
    if any(p >= 5 and a % p and D % p for p in ps): return False, "Prop X: prime outside a(a^2+4)"
    if m & (m - 1) == 0 and a % 2 == 0 and m >= 4:          # pure power of 2 dividing-a regime (L1968)
        e = m.bit_length() - 1; f = (a & -a).bit_length() - 1
        if s0 % 2 == 0 and s1 % 2 == 0: return None, "both seeds even (non-primitive)"
        if e <= f: return (s0 % m + s1 % m == m - 1), "Prop 2A: pure alternation, balanced <=> s0 + s1 = m - 1"
        if s0 % 2 and s1 % 2:
            return (False, "Theorem 2C: 4 | a, both seeds odd") if f >= 2 else (False, "Theorem 2D: a = 2 mod 4, both seeds odd (period divides m/2)")
        if f == 1: return False, "Theorem 2B: a = 2 mod 4, opposite parity, mean m/2 - 1 or m/2"
        se, so = (s0, s1) if s0 % 2 == 0 else (s1, s0)
        sig = ((se % m) & -(se % m)).bit_length() - 1 if se % m else e
        if sig == f - 1: return None, "open: even seed has v2 = f - 1 (quadratic tie, lead L1973)"
        h = min(e, f + min(sig, f))
        pred = (se % 2 ** f) + (so % 2 ** h) == 2 ** (f - 1) + 2 ** (h - 1) - 1
        if sig <= f - 2: return pred, "Theorem 2E: s_even mod 2^f + s_odd mod 2^h = 2^(f-1) + 2^(h-1) - 1, h = %d" % h
        return None, "verified formula (not yet proved) predicts %s: v2(even seed) >= f, h = %d" % (pred, h)
    if len(ps) == 1 and ps[0] % 2 and a % ps[0] == 0:          # m = q^e, q odd, q | a (L1972: Theorem T')
        q = ps[0]; e = fs[q]; f, t = 0, a
        while t % q == 0: t //= q; f += 1
        if (s0 % q == 0) != (s1 % q == 0) and e > f:
            se, so = (s0, s1) if s0 % q == 0 else (s1, s0)
            sig, t = 0, se % m
            if t == 0: sig = e
            else:
                while t % q == 0: t //= q; sig += 1
            if sig < f:
                h = min(e, f + sig)
                return (se % q ** f) + (so % q ** h) == (q ** f + q ** h) // 2 - 1, "Theorem T': one seed divisible by q, h = %d" % h
            # Theorem Q (L1976): the half starting at the unit seed takes the values C + lam*u^2 (u mod q^e)
            if s0 % q == 0: S0, S1 = s0 % m, s1 % m
            else: S0, S1 = (s1 - a * s0) % m, s0 % m
            inv2 = pow(2, -1, m); af = a // q ** f
            r = (S0 // q ** f) * pow(af, -1, m) % m
            beta = (1 + 2 * (r * pow(S1, -1, m) % m)) * inv2 % m; lam = a * a * S1 * inv2 % m
            C = (S1 - lam * beta * beta) % m
            tq = sum((C + lam * u * u) % m for u in range(m))       # m * mean of the quadratic half
            return 2 * tq + m * (m - q ** f) == 2 * m * (m - 1), "Theorem Q: quadratic half = C + lam*u^2, C = %d, lam = %d" % (C, lam)
    if m % 2 == 0 or any(a % p and D % p for p in ps): return None, "outside the proved range (prime 2 or 3)"
    G = 1
    for p in ps:
        if a % p == 0:
            if s0 % p == 0 or s1 % p == 0: return None, "seed not a unit at %d (non-unit regime, lead L1961)" % p
            f, t = 0, a
            while t % p == 0: t //= p; f += 1
            G *= p ** min(f, fs[p])
        elif (2 * s0 + a * s1) % p == 0: return False, "degenerate at %d (Theorem BG*)" % p
    return (s0 + s1 + 1) % G == 0, "Theorem T*: G = %d" % G

def strand_types(a, b, q, e, seeds):
    """L1996: y(n+1) = a y(n) + b y(n-1) + y(n-2) mod q^e with q | a, b.  Classify each of the three strands y(3t+i):
    'uniform' (on a class mod q^g), 'squares' (exactly C + lam*w^2), or 'other' (degenerate, e.g. cubic)."""
    from collections import Counter
    m = q ** e; x = tuple(v % m for v in seeds); x0 = x; seq = []
    while True:
        seq.append(x[0]); x = (x[1], x[2], (a * x[2] + b * x[1] + x[0]) % m)
        if x == x0: break
    s3 = seq * (3 if len(seq) % 3 else 1); out = []
    for i in range(3):
        t = s3[i::3]; c = Counter(t); tot = len(t)
        if len(set(c.values())) == 1 and len(c) in [q ** k for k in range(e + 1)]: out.append("uniform"); continue
        kind = "other"
        for C in c:
            for j in range(1, e):
                for lu in range(1, q):
                    H = Counter((C + q ** j * lu * w * w) % m for w in range(m))
                    if all(c.get(k, 0) * m == H.get(k, 0) * tot for k in set(c) | set(H)): kind = "squares"; break
                if kind == "squares": break
            if kind == "squares": break
        out.append(kind)
    mean_ok = 2 * sum(seq) == (m - 1) * len(seq)
    return out, mean_ok

def kth_power_dictionary(q, a=1):
    """L2000 Corollary M2: if ord_q(10) = (q-1)/k then digit sum of a/q = (9/k) * mean of lr(a*u^k mod q)."""
    from fractions import Fraction as F
    L = mult_order(10, q); k = (q - 1) // L
    r, D = a % q, 0
    for _ in range(L): D += 10 * r // q; r = 10 * r % q
    mean = F(sum((a * pow(u, k, q)) % q for u in range(q)), q)
    return k, D, mean, F(D) == F(9, k) * mean

def quartic_recurrence_demo(q=13, e=5):
    """L2004 Theorem Q4: order-4 recurrence with roots (1+q)^(+-1), (1+q)^(+-i); its mean mod q^5 is
    4 + q^4 [(q-1)/2 + 2 Re(conj chi4(1/6) B1(chi4))], and |B1(chi4)|^2/2 = h^-(quartic field) for q = 5 mod 8."""
    import cmath
    from fractions import Fraction as F
    m, per = q ** e, q ** (e - 1)
    r = next(x for x in range(2, q) if x * x % q == q - 1); M = q
    while M < per: M *= q; r = (r - (r * r + 1) * pow(2 * r, -1, M)) % M
    mu = 1 + q; roots = [pow(mu, s % per, m) for s in (1, -1, r, -r)]
    xs, S = [1, 1, 1, 1], 0
    for _ in range(per):
        S += sum(xs) % m; xs = [x * rr % m for x, rr in zip(xs, roots)]
    g = next(x for x in range(2, q) if mult_order(x, q) == q - 1); ind, x = {}, 1
    for k in range(q - 1): ind[x] = k; x = x * g % q
    chi4 = lambda z: cmath.exp(2j * cmath.pi * ind[z % q] / 4)
    B4 = sum(chi4(y) * y for y in range(1, q)) / q
    pred = 4 + q ** 4 * ((q - 1) / 2 + 2 * (chi4(pow(6, -1, q)).conjugate() * B4).real)
    return F(S, per), pred, B4, abs(B4) ** 2 / 2

def qk_recurrence_demo(q=7, k=6):
    """L2008 Theorem Q_k: order-k recurrence with roots (1+q)^zeta (zeta = k-th roots of unity in Z_q).
    Mean mod q^(k+1) = k + q^k [(q-1)/2 + sum_{chi^k=1, chi!=1} conj chi(1/(k-1)!) B1(chi)];
    h^-(degree-k field) = 2 prod over odd chi of (-B1/2).  Returns (mean, predicted, h^- or None)."""
    import cmath, math
    from fractions import Fraction as F
    e = k + 1; m, per = q ** e, q ** (e - 1)
    g = next(x for x in range(2, q) if mult_order(x, q) == q - 1)
    zeta = pow(pow(g, (q - 1) // k, q), q ** (e - 1), per)
    roots = [pow(1 + q, pow(zeta, j, per), m) for j in range(k)]
    xs, S = [1] * k, 0
    for _ in range(per):
        S += sum(xs) % m; xs = [x * r % m for x, r in zip(xs, roots)]
    ind, x = {}, 1
    for i in range(q - 1): ind[x] = i; x = x * g % q
    lam = pow(math.factorial(k - 1) % q, -1, q); pred = (q - 1) / 2; prod = 1; odd = 0
    for j in range(1, k):
        t = (q - 1) * j // k
        chi = lambda z, t=t: cmath.exp(2j * cmath.pi * t * ind[z % q] / (q - 1))
        B = sum(chi(y) * y for y in range(1, q)) / q
        pred += (chi(lam).conjugate() * B).real
        if chi(q - 1).real < 0: prod *= -B / 2; odd += 1
    w = 2 * q if k == q - 1 else 2          # roots of unity in K: w = 2q when K = Q(zeta_q)
    return F(S, per), k + q ** k * pred, (round((w * prod).real, 6) if odd else None)

def isolate_L_values(q=13, k=4):
    """L2012 Theorem L: run Theorem Q_k's recurrence from k scaled seeds s; the balance misses invert to every B1(chi), chi^k = 1.
    Returns [(j, isolated B1, direct B1)] for chi = omega^((q-1) j / k)."""
    import cmath, math
    from fractions import Fraction as F
    e = k + 1; m, per = q ** e, q ** (e - 1)
    g = next(x for x in range(2, q) if mult_order(x, q) == q - 1)
    z = pow(pow(g, (q - 1) // k, q), q ** (e - 1), per)
    roots = [pow(1 + q, pow(z, j, per), m) for j in range(k)]
    lam0 = pow(math.factorial(k - 1) % q, -1, q)
    reps = [pow(g, i, q) for i in range(k)]; miss = {}
    for sc in reps:
        xs, S = [1] * k, 0
        for _ in range(per):
            S += (sum(xs) * sc) % m; xs = [x * r % m for x, r in zip(xs, roots)]
        miss[sc] = (F(S, per) - sc * k) / q ** k - F(q - 1, 2)
    ind, x = {}, 1
    for i in range(q - 1): ind[x] = i; x = x * g % q
    out = []
    for j in range(1, k):
        chi = lambda y, t=(q - 1) * j // k: cmath.exp(2j * cmath.pi * t * ind[y % q] / (q - 1))
        Biso = sum(chi(sc * lam0) * float(miss[sc]) for sc in reps) / k
        Bdir = sum(chi(y) * y for y in range(1, q)) / q
        out.append((j, Biso, Bdir))
    return out

def orbit_L1_values(q=7, k=3):
    """L2016 Theorems L+ and R: k scaled orbits x q centre offsets d = q^k c of Theorem Q_k's recurrence.
    The misses give V(c) = B1(chi) - chi(-1) A_chi(c); differences rebuild chi itself; then
    odd chi:  L(1,chi) = pi i tau(chi) conj(B1(chi)) / q
    even chi: L(1,chi) = -(tau(chi)/q) sum_a conj(chi(a)) log|1 - zeta_q^a|.
    Returns (rows [(j, parity, chi_rebuilt_ok, L1)], h*R of the degree-k field if totally real else None)."""
    import cmath, math
    from fractions import Fraction as F
    e = k + 1; m, per = q ** e, q ** (e - 1)
    g = next(x for x in range(2, q) if mult_order(x, q) == q - 1)
    z = pow(pow(g, (q - 1) // k, q), q ** (e - 1), per)
    roots = [pow(1 + q, pow(z, j, per), m) for j in range(k)]
    lam0 = pow(math.factorial(k - 1) % q, -1, q)
    reps = [pow(g, i, q) for i in range(k)]
    orbit = []; xs = [1] * k
    for _ in range(per):
        orbit.append(sum(xs) % m); xs = [x * r % m for x, r in zip(xs, roots)]
    ind, x = {}, 1
    for i in range(q - 1): ind[x] = i; x = x * g % q
    miss = {}
    for c in range(q):
        d = q ** k * c
        for sc in reps:
            S = sum((f * sc + d) % m for f in orbit)
            miss[(c, sc)] = (F(S, per) - sc * k - d) / q ** k - F(q - 1, 2)
    rows, prod, allreal = [], 1, True
    for j in range(1, k):
        chi = lambda y, t=(q - 1) * j // k: cmath.exp(2j * cmath.pi * t * ind[y % q] / (q - 1))
        par = round(chi(q - 1).real)
        V = [sum(chi(sc * lam0) * float(miss[(c, sc)]) for sc in reps) / k for c in range(q)]
        A = [(V[0] - V[c]) * par for c in range(q)]
        rec = [A[c] - A[c - 1] for c in range(1, q)]
        okc = all(abs(rec[c - 1] - chi(c)) < 1e-6 for c in range(1, q))
        tau = sum(chi(y) * cmath.exp(2j * cmath.pi * y / q) for y in range(1, q))
        if par < 0:
            L1 = math.pi * 1j * tau * V[0].conjugate() / q; allreal = False
        else:
            L1 = -(tau / q) * sum(rec[a - 1].conjugate() * math.log(abs(1 - cmath.exp(2j * cmath.pi * a / q))) for a in range(1, q))
        rows.append((j, "odd" if par < 0 else "even", okc, L1)); prod *= L1
    hR = prod.real * math.sqrt(q ** (k - 1)) / 2 ** (k - 1) if allreal else None
    return rows, hR

def pell_minus_one_trace(q):
    """Smallest t > 0 with t^2 + 4 = q u^2 (q prime, q = 1 mod 4), i.e. the fundamental unit (t + u sqrt q)/2,
    = the growth ratio of the DCF recurrence x(n+1) = t x(n) + x(n-1). Continued fraction of sqrt q, then an exact
    test for a half-integral cube root."""
    import math
    a0 = math.isqrt(q); m, d, a = 0, 1, a0; p0, p1, q0, q1 = 1, a0, 0, 1
    while p1 * p1 - q * q1 * q1 != -1:
        m = d * a - m; d = (q - m * m) // d; a = (a0 + m) // d
        p0, p1 = p1, a * p1 + p0; q0, q1 = q1, a * q1 + q0
    x, y = p1, q1; t, u = 2 * x, 2 * y
    lo, hi = 1, 2 * x + 2                       # integer search for t with (t^3 + 3 t u^2 q) = 8x
    while lo < hi:
        mid = (lo + hi) // 2
        if mid ** 3 + 3 * mid * (mid * mid + 4) < 8 * x: lo = mid + 1
        else: hi = mid
    n = lo * lo + 4
    if n % q == 0 and math.isqrt(n // q) ** 2 * q == n:
        uu = math.isqrt(n // q)
        if lo ** 3 + 3 * lo * uu * uu * q == 8 * x and 3 * lo * lo * uu + uu ** 3 * q == 8 * y: t, u = lo, uu
    return t, u

def two_recurrence_class_number(q=229):
    """L2020 Theorem H2: class number of Q(sqrt q), q prime = 1 mod 4, from two recurrences.
    (1) Order-2 recurrence of Theorem Q_k (roots (1+q)^(+-1) mod q^3), 2 scaled orbits x q shifted centres -> chi, L(1,chi), h*R.
    (2) DCF recurrence x(n+1) = t x(n) + x(n-1) with t^2 + 4 = q u^2: its growth ratio is the fundamental unit, R = log of it.
    Returns (h*R, t, u, R, h)."""
    import math, bisect
    from fractions import Fraction as F
    m, per = q ** 3, q * q
    g = next(x for x in range(2, q) if mult_order(x, q) == q - 1)
    r1 = (1 + q) % m; r2 = pow(1 + q, per - 1, m)       # Teichmuller -1 mod q^2 is q^2 - 1
    orbit = []; x, y = 1, 1
    for _ in range(per): orbit.append((x + y) % m); x = x * r1 % m; y = y * r2 % m
    leg = lambda v: 0 if v % q == 0 else (1 if pow(v, (q - 1) // 2, q) == 1 else -1)
    sums = {}
    for sc in (1, g):
        rs = sorted(o * sc % m for o in orbit); tot = sum(rs)
        for c in range(q):
            d = q * q * c; over = per - bisect.bisect_left(rs, m - d)
            sums[(c, sc)] = tot + per * d - m * over
    V = []
    for c in range(q):
        ms = [(F(sums[(c, sc)], per) - 2 * sc - q * q * c) / (q * q) - F(q - 1, 2) for sc in (1, g)]
        V.append((ms[0] + leg(g) * ms[1]) / 2)
    chi = [(V[0] - V[c]) - (V[0] - V[c - 1]) for c in range(1, q)]
    assert all(chi[c - 1] == leg(c) for c in range(1, q))
    L1 = -sum(int(chi[a - 1]) * math.log(abs(2 * math.sin(math.pi * a / q))) for a in range(1, q)) / math.sqrt(q)
    hR = math.sqrt(q) * L1 / 2
    t, u = pell_minus_one_trace(q)
    R = math.log((t + math.sqrt(t * t + 4)) / 2)
    return hR, t, u, R, hR / R

def minus_orbit(a, m, s0=0, s1=1):
    """Orbit of the minus-sign (Chebyshev) recurrence x(n+1) = a x(n) - x(n-1) mod m: (period, balanced, uniform)."""
    x, y = s0 % m, s1 % m; st = (x, y); S = 0; n = 0; cnt = [0] * m
    while True:
        S += x; cnt[x] += 1; n += 1; x, y = y, (a * y - x) % m
        if (x, y) == st: break
    return n, 2 * S == n * (m - 1), min(cnt) * m == n and max(cnt) * m == n

def bgminus_predict(a, m, s0=0, s1=1):
    """L2024 Theorem BG-: uniform distribution of x(n+1) = a x(n) - x(n-1) mod m (any seeds), and balance for seeds (0, 1).
    u.d. <=> every prime p | m divides a^2 - 4, with the seed test 2 s1 - a s0 != 0 mod p (odd p), s0 + s1 odd (p = 2),
    and: 4 | m needs a = 2 mod 4;  9 | m needs a != +-1 mod 9.
    Balance (seeds 0, 1) <=> u.d., or the 'six' exception: a = 3 mod 6 and m = 6 m' with m' = 1 or u.d. and gcd(m', 6) = 1.
    Returns (ud_prediction, balance_prediction)."""
    def ud(mm):
        if mm == 1: return True
        for p, e in factorint_small(mm).items():
            if (a * a - 4) % p: return False
            if p == 2 and ((s0 + s1) % 2 == 0 or (e >= 2 and a % 4 == 0)): return False
            if p != 2 and (2 * s1 - a * s0) % p == 0: return False
            if p == 3 and e >= 2 and a % 9 in (1, 8): return False
        return True
    u = ud(m)
    six = (s0 % m, s1 % m) == (0, 1 % m) and a % 6 == 3 and m % 6 == 0 and math.gcd(m // 6, 6) == 1 and ud(m // 6)
    return u, u or six

def factorint_small(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0: f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f

def pell_chi4_law(e):
    """L2028: Pell numbers mod 2^e (e >= 2) hit each residue r exactly 1 + chi_{-4}(r) times per period 2^e,
    so their balance miss is B1(chi_{-4}) = -1/2 = -h(Q(i)) * 2 / w (w = 4). Returns (law holds, miss)."""
    from fractions import Fraction as F
    m = 2 ** e; x, y, seq = 0, 1, []
    while True:
        seq.append(x); x, y = y, (2 * y + x) % m
        if (x, y) == (0, 1): break
    chi = lambda r: 0 if r % 2 == 0 else (1 if r % 4 == 1 else -1)
    law = len(seq) == m and all(seq.count(r) == 1 + chi(r) for r in range(m))
    return law, F(sum(seq), len(seq)) - F(m - 1, 2)

def pell_plus_one(q):
    """smallest x^2 - q y^2 = 1 (continued fraction of sqrt q); for prime q = 3 mod 4 this is the fundamental unit
    x + y sqrt q, the growth ratio of the minus-family recurrence x(n+1) = 2x x(n) - x(n-1)."""
    a0 = math.isqrt(q); m, d, a = 0, 1, a0; p0, p1, q0, q1 = 1, a0, 0, 1
    while p1 * p1 - q * q1 * q1 != 1:
        m = d * a - m; d = (q - m * m) // d; a = (a0 + m) // d
        p0, p1 = p1, a * p1 + p0; q0, q1 = q1, a * q1 + q0
    return p1, q1

def class_number_3mod4(q=79):
    """L2028 Theorem H2-: class number of Q(sqrt q), q prime = 3 mod 4, from three recurrences.
    (1) Pell mod 4 (period 4: values 0,1,2,1 -> counts 1 + chi_{-4}) and (2) the order-2 orbit (1+q)^n + (1+q)^-n mod q^3
    (period q^2; top digit = n^2 mod q -> counts q(1 + chi_q)), read jointly as one residue Y(n) mod 4q over 4q^2 steps.
    Shifted-centre balance sums S(c) = sum lr(Y + c) give every residue count, hence chi_{-4}, chi_q and chi_{4q}
    = (4q/.), the even character of Q(sqrt q); h*R = -(1/2) sum chi_{4q}(a) log|2 sin(pi a/4q)|.
    (3) Minus recurrence x(n+1) = a x(n) - x(n-1), a = 2x with a^2 - 4 = 4 q u^2: growth ratio = unit, R = log.
    Returns (h*R, a, u, R, h, characters rebuilt exactly)."""
    M, N, per, m = 4 * q, 4 * q * q, q * q, q ** 3
    pell = [0, 1, 2, 1]; r2 = pow(1 + q, per - 1, m); x = y = 1; top = []
    for _ in range(per): top.append((((x + y) - 2) % m) // per); x = x * (1 + q) % m; y = y * r2 % m
    i4, iq = pow(q, -1, 4), pow(4, -1, q); cnt = [0] * M
    for n in range(N): cnt[(pell[n % 4] * q * i4 + top[n % per] * 4 * iq) % M] += 1
    S = [sum(v * k for v, k in enumerate(cnt))]                       # balance sums at every centre
    for c in range(1, M): S.append(S[-1] + N - M * cnt[M - c])
    k = [0] * M
    for c in range(1, M): k[M - c] = (S[c - 1] + N - S[c]) // M      # counts read back from the sums alone
    k[0] = N - sum(k[1:])
    m4 = [sum(k[v] for v in range(r, M, 4)) for r in range(4)]; mq = [sum(k[v] for v in range(s, M, q)) for s in range(q)]
    c4 = [t // per - 1 for t in m4]; cq = [t // (4 * q) - 1 for t in mq]
    c4q = [k[v] // q - 1 - c4[v % 4] - cq[v % q] for v in range(M)]
    jac = lambda v: 0 if v % 2 == 0 or v % q == 0 else (1 if pow(v % q, (q - 1) // 2, q) == 1 else -1) * (1 if (v % 4 == 1 or q % 4 == 1) else -1)
    exact = all(c4q[v] == jac(v) for v in range(M))                  # (4q/v) = (q/v) = (v/q)(-1)^((v-1)/2) for q = 3 mod 4
    hR = -0.5 * sum(c4q[v] * math.log(abs(2 * math.sin(math.pi * v / M))) for v in range(1, M))
    X, U = pell_plus_one(q); a = 2 * X; R = math.log(X + U * math.sqrt(q))
    return hR, a, U, R, hR / R, exact

def chim8_reader_law(e):
    """L2032 Lemma P8: x(n+1) = 4 x(n) - x(n-1) from seeds (1, 1) (the unit recurrence of Q(sqrt3)) mod 2^e, e >= 3,
    has period 2^(e-1) and hits each residue r exactly 1 + chi_{-8}(r) times when r is odd, never when r is even."""
    m = 2 ** e; x, y, seq = 1, 1, []
    while True:
        seq.append(x); x, y = y, (4 * y - x) % m
        if (x, y) == (1, 1): break
    chi = lambda r: 1 if r % 8 in (1, 3) else -1
    return len(seq) == m // 2 and all(seq.count(r) == (0 if r % 2 == 0 else 1 + chi(r)) for r in range(m))

def chi8_reader_law(e):
    """L2032 Lemma P8': x(n+1) = 3 x(n) + 3 x(n-1) - x(n-2) from seeds (1, 1, 7) (characteristic polynomial
    (z + 1)(z^2 - 4z + 1): the Q(sqrt3) unit recurrence twisted by (-1)^n) mod 2^e, e >= 3, has period 2^(e-1) and hits
    each odd residue r exactly 1 + chi_8(r) times, evens never."""
    m = 2 ** e; x, y, z, seq = 1, 1, 7 % m, []
    while True:
        seq.append(x); x, y, z = y, z, (3 * z + 3 * y - x) % m
        if (x, y, z) == (1, 1, 7 % m): break
    chi = lambda r: 1 if r % 8 in (1, 7) else -1
    return len(seq) == m // 2 and all(seq.count(r) == (0 if r % 2 == 0 else 1 + chi(r)) for r in range(m))

def _counts_from_sums(orbit, m):
    N = len(orbit); cnt = [0] * m
    for v in orbit: cnt[v] += 1
    S = [sum(v * k for v, k in enumerate(cnt))]                      # balance sums at every centre
    for c in range(1, m): S.append(S[-1] + N - m * cnt[m - c])
    k = [0] * m
    for c in range(1, m): k[m - c] = (S[c - 1] + N - S[c]) // m      # counts read back from the sums alone
    k[0] = N - sum(k[1:]); return k, N

def legendre_reader(p):
    """L2032: the Legendre symbol (./p) rebuilt from the balance sums of the top digit of (1+p)^n + (1+p)^-n mod p^3."""
    m, per = p ** 3, p * p; r2 = pow(1 + p, per - 1, m); x = y = 1; top = []
    for _ in range(per): top.append((((x + y) - 2) % m) // per); x = x * (1 + p) % m; y = y * r2 % m
    k, N = _counts_from_sums(top, p)
    return [0] + [k[s] // p - 1 for s in range(1, p)]

def quadratic_unit(D):
    """smallest (t, u, norm) with t^2 - D u^2 = 4 norm, norm = +-1: the fundamental unit (t + u sqrt D)/2 of Q(sqrt D),
    and the growth ratio of x(n+1) = t x(n) - norm x(n-1) (plus family for norm -1, minus family for norm +1)."""
    s = D % 2; P, Q = s, 2; r = math.isqrt(D); p0, p1, q0, q1 = 0, 1, 1, 0
    while True:
        a = (P + r) // Q; p0, p1, q0, q1 = p1, a * p1 + p0, q1, a * q1 + q0
        t, u = 2 * p1 - s * q1, q1
        if t > 0 and t * t - D * u * u in (4, -4): return t, u, (t * t - D * u * u) // 4
        P = a * Q - P; Q = (D - P * P) // Q

def class_number_quadratic(D):
    """L2032 Theorem H2*: class number of Q(sqrt D), any fundamental discriminant D (either sign), from recurrence orbits:
    chi_D = chi_{D2} * prod (./p);  (./p) from the order-2 orbit, chi_{-4} from Pell, chi_{-8} from 4x - x, chi_8 = chi_{-4} chi_{-8}.
    D > 0: h = h*R / log(unit), the unit from x(n+1) = t x(n) -+ x(n-1).  D < 0: h = -(w/2) B1(chi_D).
    Returns (h, extra): extra = (t, u, norm, R) for D > 0, B1 for D < 0."""
    m = 64; k, N = _counts_from_sums(ab_orbit_list(2, 1, 0, 1, m), m); cm4 = [k[r] * m // N - 1 for r in range(m)]
    k, N = _counts_from_sums(ab_orbit_list(4, -1, 1, 1, m), m); cm8 = [0 if r % 2 == 0 else k[r] * m // (2 * N) - 1 for r in range(m)]
    a = abs(D); odd = sorted(p for p in factor(a) if p != 2); L = {p: legendre_reader(p) for p in odd}
    D2 = D // math.prod(p if p % 4 == 1 else -p for p in odd)
    x3, o3 = [1, 1, 7], []
    while True:
        o3.append(x3[0]); x3 = [x3[1], x3[2], (3 * x3[2] + 3 * x3[1] - x3[0]) % m]
        if x3 == [1, 1, 7]: break
    k, N = _counts_from_sums(o3, m); cp8 = [0 if r % 2 == 0 else k[r] * m // (2 * N) - 1 for r in range(m)]
    assert all(cp8[r] == cm4[r] * cm8[r] for r in range(m))          # direct chi_8 reader = product of the other two
    two = {1: lambda y: 1, -4: lambda y: cm4[y % m], -8: lambda y: cm8[y % m], 8: lambda y: cp8[y % m]}[D2]
    chi = lambda y: two(y) * math.prod(L[p][y % p] for p in odd)
    if D > 0:
        hR = -0.5 * sum(chi(j) * math.log(abs(2 * math.sin(math.pi * j / a))) for j in range(1, a))
        t, u, nrm = quadratic_unit(D); R = math.log((t + u * math.sqrt(D)) / 2)
        return hR / R, (t, u, nrm, R)
    B1 = sum(chi(j) * j for j in range(1, a)) / a
    return -{-3: 6, -4: 4}.get(D, 2) * B1 / 2, B1

def ab_orbit_list(a, b, s0, s1, m):
    x, y, out = s0 % m, s1 % m, []
    while True:
        out.append(x); x, y = y, (a * y + b * x) % m
        if (x, y) == (s0 % m, s1 % m): return out

def cubic_classes(q, brute=False):
    """L2036 Lemma C1: cube classes mod q (q prime = 1 mod 3) from the order-3 orbit f(t) = sum_j (1+q)^(zeta^j t) mod q^4
    (zeta a Teichmuller cube root of unity mod q^3).  Top digit (f - 3)/q^3 = t^3/2 mod q.  Two orbits (scale 1 and scale g)
    are read through their balance sums; returns (labels, g): labels[s] = index_g(s) mod 3, labels[0] = None.
    brute=True runs the full period q^3; otherwise the q terms t = 0..q-1, each counted q^2 times (Lemma C1)."""
    m, q3 = q ** 4, q ** 3
    g = next(x for x in range(2, q) if all(pow(x, (q - 1) // f, q) != 1 for f in factor(q - 1)))
    z = pow(pow(g, (q - 1) // 3, q), q3, q3); r = [pow(1 + q, pow(z, j, q3), m) for j in range(3)]
    def top_counts(sc):
        x = [1, 1, 1]; steps = q3 if brute else q; mult = 1 if brute else q * q; cnt = [0] * q
        for _ in range(steps):
            cnt[(((x[0] + x[1] + x[2]) * sc - 3 * sc) % m) // q3] += mult; x = [a * b % m for a, b in zip(x, r)]
        N = steps * mult; S = [sum(v * c for v, c in enumerate(cnt))]          # balance sums at every centre
        for c in range(1, q): S.append(S[-1] + N - q * cnt[q - c])
        k = [0] * q
        for c in range(1, q): k[q - c] = (S[c - 1] + N - S[c]) // q           # counts read back from the sums
        k[0] = N - sum(k[1:]); return k
    k1, k2 = top_counts(1), top_counts(g)
    base = 0 if k1[1] else (1 if k2[1] else 2)
    lab = [None] + [((0 if k1[s] else (1 if k2[s] else 2)) - base) % 3 for s in range(1, q)]
    return lab, g

def cubic_class_number(q, brute=False):
    """L2036 Theorem C3: class number of the cyclic cubic field of prime conductor q by root extraction.
    v = prod over half-cosets of 2 sin(pi a/q) (cyclotomic units from the cube classes), [E : C] = h, E/+-1 = Z[zeta3] eps.
    h = largest N(pi), pi Eisenstein, such that v^(1/pi) has an integral characteristic polynomial x^3 - T x^2 + S x - 1;
    that polynomial is the fundamental-unit recurrence y(n+1) = T y(n) - S y(n-1) + y(n-2).  Needs mpmath for large q.
    Returns (h, T, S, R, hR)."""
    lab, g = cubic_classes(q, brute)
    if HAVE_MP:
        mp = mpmath; mp.mp.dps = 120; lg = lambda a: mp.log(abs(2 * mp.sin(mp.pi * a / q))); ex = mp.exp; tol = mp.mpf(10) ** -40
        rnd = lambda v: int(mp.nint(v))
    else:
        lg = lambda a: math.log(abs(2 * math.sin(math.pi * a / q))); ex = math.exp; tol = 1e-6; rnd = lambda v: int(round(v))
    D = [0, 0, 0]
    for a in range(1, (q - 1) // 2 + 1): D[lab[a]] = D[lab[a]] + lg(a)
    L = [D[1] - D[0], D[2] - D[1], D[0] - D[2]]; hR = float(sum(x * x for x in L) / 2)
    cap = hR / (math.log(q * q / 4) ** 2 / 16)                       # Cusick: R >= log^2(D/4)/16
    cands = sorted({(a * a - a * b + b * b, a, b) for a in range(-60, 61) for b in range(-60, 61) if 0 < a * a - a * b + b * b <= cap + 1e-9}, reverse=True)
    for n, a, b in cands:
        M = [((a - b) * L[i] - b * L[(i + 1) % 3]) / n for i in range(3)]
        if max(abs(float(x)) for x in M) > (600 if HAVE_MP else 30): continue
        E = [ex(x) for x in M]
        for sg in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)):
            e = [sg[i] * E[i] for i in range(3)]; T = e[0] + e[1] + e[2]; S = e[0] * e[1] + e[1] * e[2] + e[2] * e[0]
            if abs(T - rnd(T)) < tol and abs(S - rnd(S)) < tol:
                R = float(sum(x * x for x in M) / 2)
                return n, rnd(T), rnd(S), R, hR
    return None

def cubic_certificate(q):
    """L2040 Theorem C3*: rigorous certificate for the cubic class number (needs mpmath; interval arithmetic).
    (1) the period polynomial from interval Gauss periods (integers) = Gauss's formula; (2) eps = sum c_k eta_k with integer c,
    N(eps) = +-1 exactly; (3) v = +-eps^beta (log vectors agree, quotient = +-1 by Lemma S); (4) eps is no proper root:
    every Eisenstein prime pi with N(pi) <= R(eps)/R_low fails, R_low = log^2(q/8)/12 (Lemma D; q = 7 by enumeration).
    Returns dict(h, unit_poly, certified, parts)."""
    if not HAVE_MP: return None
    iv, mp = mpmath.iv, mpmath.mp; iv.dps = mp.dps = 160
    lab, g = cubic_classes(q)
    eta = [iv.mpf(0)] * 3; D = [iv.mpf(0)] * 3
    for a in range(1, (q - 1) // 2 + 1):
        x = iv.pi * a / q; eta[lab[a]] += 2 * iv.cos(2 * x); D[lab[a]] += iv.log(2 * iv.sin(x))
    def the_int(I):
        lo, hi = int(mpmath.ceil(I.a)), int(mpmath.floor(I.b)); return lo if lo == hi else None
    has_int = lambda I: int(mpmath.floor(I.b)) >= int(mpmath.ceil(I.a))
    gI = [eta[0] + eta[1] + eta[2], eta[0] * eta[1] + eta[1] * eta[2] + eta[2] * eta[0], eta[0] * eta[1] * eta[2]]
    gp = [1, -the_int(gI[0]), the_int(gI[1]), -the_int(gI[2])]
    M_ = next(M for M in range(1, q) if 4 * q - 27 * M * M >= 0 and math.isqrt(4 * q - 27 * M * M) ** 2 == 4 * q - 27 * M * M)
    Lg = math.isqrt(4 * q - 27 * M_ * M_); Lg = Lg if Lg % 3 == 1 else -Lg
    ok_g = gp == [1, 1, -(q - 1) // 3, -(q * (Lg + 3) - 1) // 27]
    Lv = [D[1] - D[0], D[2] - D[1], D[0] - D[2]]; Lm = [mp.mpf(x.mid) for x in Lv]
    SG = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))
    hR = float(sum(x * x for x in Lm) / 2); cap0 = hR / (math.log(q * q / 4) ** 2 / 16) if q > 8 else 1
    found = None
    for n, a, b in sorted({(a * a - a * b + b * b, a, b) for a in range(-60, 61) for b in range(-60, 61) if 0 < a * a - a * b + b * b <= max(cap0, 1) + 1e-9}, reverse=True):
        M = [((a - b) * Lm[i] - b * Lm[(i + 1) % 3]) / n for i in range(3)]
        if max(abs(x) for x in M) > 600: continue
        E = [mp.exp(x) for x in M]
        for sg in SG:
            e = [sg[i] * E[i] for i in range(3)]; T = sum(e); S_ = e[0] * e[1] + e[1] * e[2] + e[2] * e[0]
            if abs(T - mp.nint(T)) < mp.mpf(10) ** -30 and abs(S_ - mp.nint(S_)) < mp.mpf(10) ** -30: found = (n, a, b, [sg[i] * E[i] for i in range(3)]); break
        if found: break
    n, a, b, eps = found
    em = [mp.mpf(x.mid) for x in eta]
    c = mp.lu_solve(mp.matrix([[em[(k + j) % 3] for k in range(3)] for j in range(3)]), mp.matrix(eps)); ci = [int(mp.nint(c[i])) for i in range(3)]
    eI = [sum(ci[k] * eta[(k + j) % 3] for k in range(3)) for j in range(3)]
    nrm = the_int(eI[0] * eI[1] * eI[2]); T_, S2 = the_int(eI[0] + eI[1] + eI[2]), the_int(eI[0] * eI[1] + eI[1] * eI[2] + eI[2] * eI[0])
    ok_unit = nrm in (1, -1) and T_ is not None and S2 is not None
    l = [iv.log(abs(z)) for z in eI]
    delta = max(max(abs(float(d.a)), abs(float(d.b))) for d in [Lv[j] - (a * l[j] + b * l[(j + 1) % 3]) for j in range(3)])
    ok_rel = delta < 1e-50
    R_hi = float(((l[0] ** 2 + l[1] ** 2 + l[2] ** 2) / 2).b)
    if q > 8:
        cap = R_hi / (math.log(q / 8) ** 2 / 12); prs = [(3, 1, -1)] if cap >= 3 else []
        for p_ in range(2, int(cap) + 1):
            if all(p_ % d for d in range(2, int(p_ ** 0.5) + 1)):
                if p_ % 3 == 1:
                    a2, b2 = next((x, y) for x in range(1, p_) for y in range(-x, x + 1) if x * x - x * y + y * y == p_)
                    prs += [(p_, a2, b2), (p_, a2, a2 - b2)]
                elif p_ % 3 == 2 and p_ * p_ <= cap: prs.append((p_ * p_, p_, 0))
        ok_fund = True
        for N_, pa, pb in prs:
            M = [((pa - pb) * l[i] - pb * l[(i + 1) % 3]) / N_ for i in range(3)]; E = [iv.exp(x) for x in M]
            for sg in SG:
                e = [sg[i] * E[i] for i in range(3)]
                if has_int(e[0] + e[1] + e[2]) and has_int(e[0] * e[1] + e[1] * e[2] + e[2] * e[0]): ok_fund = False
    else:
        m = math.sqrt(4 * (R_hi / 3) / 3); ok_fund = True; mp.dps = 40
        for t in range(-int(3 * math.exp(m)) - 1, int(3 * math.exp(m)) + 2):
            for s_ in range(-int(3 * math.exp(2 * m)) - 1, int(3 * math.exp(2 * m)) + 2):
                if (1 - t + s_ - 1) == 0 or (-1 - t - s_ - 1) == 0: continue
                rts = mpmath.polyroots([1, -t, s_, -1], maxsteps=200, extraprec=100)
                if all(abs(mp.im(z)) < 1e-20 and abs(mp.log(abs(mp.re(z)))) <= m + 1e-12 for z in rts): ok_fund = False
    parts = dict(period_poly=ok_g, unit=ok_unit, relation=ok_rel, fundamental=ok_fund)
    return dict(h=n, unit_poly=(1, -T_, S2, -nrm), certified=all(parts.values()), parts=parts)

def quartic_classes(q):
    """L2040 Lemma C1 (k = 4): quartic classes mod q (q prime = 1 mod 8) from four scaled order-4 orbits mod q^5;
    top digit = t^4/6 mod q, counts read back from balance sums.  Returns (labels, g, all labels = index_g mod 4)."""
    m, q4 = q ** 5, q ** 4
    g = next(x for x in range(2, q) if all(pow(x, (q - 1) // f, q) != 1 for f in factor(q - 1)))
    z = pow(pow(g, (q - 1) // 4, q), q4, q4); r = [pow(1 + q, pow(z, j, q4), m) for j in range(4)]
    sup = []
    for c in range(4):
        sc = pow(g, c, q); x = [1, 1, 1, 1]; cnt = [0] * q
        for _ in range(q): cnt[((sum(x) * sc - 4 * sc) % m) // q4] += q ** 3; x = [a * b % m for a, b in zip(x, r)]
        N = q ** 4; S = [sum(v * k for v, k in enumerate(cnt))]
        for cc in range(1, q): S.append(S[-1] + N - q * cnt[q - cc])
        k = [0] * q
        for cc in range(1, q): k[q - cc] = (S[cc - 1] + N - S[cc]) // q
        sup.append({s for s in range(1, q) if k[s] > 0})
    base = next(c for c in range(4) if 1 in sup[c])
    lab = [None] + [(next(c for c in range(4) if s in sup[c]) - base) % 4 for s in range(1, q)]
    return lab, g, all(pow(s, (q - 1) // 4, q) == pow(g, lab[s] * (q - 1) // 4, q) for s in range(1, q))

def quartic_class_number(q, lmax=13):
    """L2040 Theorem Q4R [V]: class number of the real cyclic quartic field of prime conductor q = 1 mod 8 by saturating the
    cyclotomic units <v, sv, s^2 v> at every prime l <= lmax (needs mpmath).  Returns (h, R_E, R_C, unit polynomials)."""
    if not HAVE_MP: return None
    import itertools
    mp = mpmath.mp; mp.dps = 200; lab, g, _ = quartic_classes(q)
    D = [mp.mpf(0)] * 4
    for a in range(1, (q - 1) // 2 + 1): D[lab[a]] += mp.log(2 * mp.sin(mp.pi * a / q))
    L = [D[(j + 1) % 4] - D[j] for j in range(4)]; B = [[L[(j + i) % 4] for j in range(4)] for i in range(3)]
    reg = lambda B: abs(mp.det(mp.matrix([[B[r][j] for j in range(3)] for r in range(3)])))
    SG = [s for s in itertools.product((1, -1), repeat=4) if s[0] == 1]
    eta = [mp.mpf(0)] * 4
    for a in range(1, (q - 1) // 2 + 1): eta[lab[a]] += 2 * mp.cos(2 * mp.pi * a / q)
    VI = mp.inverse(mp.matrix([[eta[(k + j) % 4] for k in range(4)] for j in range(4)]))   # normal integral basis
    def unitpoly(y):
        """a unit OF K: integer coordinates in the Gauss-period basis (an integral char. polynomial alone is not enough)"""
        E = [mp.exp(t) for t in y]
        for sg in SG:
            e = [sg[i] * E[i] for i in range(4)]
            cc = VI * mp.matrix(e)
            if not all(abs(cc[i] - mp.nint(cc[i])) < mp.mpf(10) ** -30 for i in range(4)): continue
            cs = [sum(e), sum(e[i] * e[j] for i, j in itertools.combinations(range(4), 2)),
                  sum(e[i] * e[j] * e[k] for i, j, k in itertools.combinations(range(4), 3)), e[0] * e[1] * e[2] * e[3]]
            if all(abs(c - mp.nint(c)) < mp.mpf(10) ** -30 for c in cs): return [1] + [int((-1) ** (i + 1) * mp.nint(cs[i])) for i in range(4)]
        return None
    RC = reg(B)
    for l in [p for p in range(2, lmax + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]:
        again = True
        while again:
            again = False
            for x in itertools.product(range(l), repeat=3):
                if not any(x) or x[next(i for i in range(3) if x[i])] != 1: continue
                y = [sum(x[r] * B[r][j] for r in range(3)) / l for j in range(4)]
                if max(abs(t) for t in y) > 90: continue
                if unitpoly(y): B[next(i for i in range(3) if x[i])] = y; again = True; break
    RE = reg(B)
    return float(RC / RE), float(RE), float(RC), [unitpoly(b) for b in B]

def quartic_certificate(q, lmax_sat=13, budget=60000):
    """L2044 Theorem Q4R*: rigorous certificate for the class number of the real cyclic quartic field of prime conductor
    q = 1 mod 8 (needs mpmath).  (1) unit basis W from saturation, each unit with integer period coordinates and norm +-1
    (intervals); (2) C inside W with relation matrix X (Lemma S4), [W : C] = |det X|; (3) E = W: for every prime
    l <= R_W / R_low, R_low = (2/3) m0^3 (Lemma D4 + box enumeration), the l-th power residue characters at primes above
    p = 1 mod q l map W/W^l injectively.  Returns dict(h, certified, parts, cap)."""
    if not HAVE_MP: return None
    import itertools
    mp, iv = mpmath.mp, mpmath.iv; mp.dps = iv.dps = 200
    lab, g, okl = quartic_classes(q)
    eta = [iv.mpf(0)] * 4; D = [iv.mpf(0)] * 4
    for a in range(1, (q - 1) // 2 + 1):
        x = iv.pi * a / q; eta[lab[a]] += 2 * iv.cos(2 * x); D[lab[a]] += iv.log(2 * iv.sin(x))
    em = [mp.mpf(x.mid) for x in eta]; VI = mp.inverse(mp.matrix([[em[(k + j) % 4] for k in range(4)] for j in range(4)]))
    the_int = lambda I: (lambda lo, hi: lo if lo == hi else None)(int(mpmath.ceil(I.a)), int(mpmath.floor(I.b)))
    SG = [t for t in itertools.product((1, -1), repeat=4) if t[0] == 1]
    def coords(y):
        E = [mp.exp(t) for t in y]
        for sg in SG:
            c = VI * mp.matrix([sg[i] * E[i] for i in range(4)])
            if all(abs(c[i] - mp.nint(c[i])) < mp.mpf(10) ** -30 for i in range(4)): return [int(mp.nint(c[i])) for i in range(4)]
        return None
    Lm = [mp.mpf((D[(j + 1) % 4] - D[j]).mid) for j in range(4)]
    B = [[Lm[(j + i) % 4] for j in range(4)] for i in range(3)]
    reg = lambda B: abs(mp.det(mp.matrix([[B[r][j] for j in range(3)] for r in range(3)])))
    for l in [p_ for p_ in range(2, lmax_sat + 1) if is_prime_mr(p_)]:
        again = True
        while again:
            again = False
            for x in itertools.product(range(l), repeat=3):
                if not any(x) or x[next(i for i in range(3) if x[i])] != 1: continue
                y = [sum(x[r] * B[r][j] for r in range(3)) / l for j in range(4)]
                if max(abs(t) for t in y) <= 90 and coords(y): B[next(i for i in range(3) if x[i])] = y; again = True; break
    cs = [coords(b) for b in B]
    if None in cs: return dict(h=None, certified=False, parts=dict(units=False))
    wI = [[sum(c[k] * eta[(k + j) % 4] for k in range(4)) for j in range(4)] for c in cs]
    ok_unit = all(the_int(w[0] * w[1] * w[2] * w[3]) in (1, -1) for w in wI)
    lw = [[iv.log(abs(z)) for z in w] for w in wI]
    Bm = mp.matrix([[mp.mpf(lw[r][j].mid) for j in range(3)] for r in range(3)]); Bi = mp.inverse(Bm)
    Lv = [D[(j + 1) % 4] - D[j] for j in range(4)]; X = []; delta = 0
    for i in range(3):
        xv = mp.matrix([[mp.mpf(Lv[(j + i) % 4].mid) for j in range(3)]]) * Bi; X.append([int(mp.nint(xv[0, r])) for r in range(3)])
        for j in range(4):
            d = Lv[(j + i) % 4] - sum(X[i][r] * lw[r][j] for r in range(3)); delta = max(delta, abs(float(d.a)), abs(float(d.b)))
    detX = abs(X[0][0] * (X[1][1] * X[2][2] - X[1][2] * X[2][1]) - X[0][1] * (X[1][0] * X[2][2] - X[1][2] * X[2][0]) + X[0][2] * (X[1][0] * X[2][1] - X[1][1] * X[2][0]))
    # lambda_1 lower bound: Lemma D4, improved by a box enumeration of small units
    m0 = 3 / 8 * math.log(q / 16); rows_ = [float(sum(abs(VI[k, j]) for j in range(4))) for k in range(4)]; m = m0
    while math.prod(2 * int(r_ * math.exp(m + 0.05)) + 1 for r_ in rows_) <= budget: m += 0.05
    if m > m0:
        bnd = [int(r_ * math.exp(m)) for r_ in rows_]; fl = [float(x) for x in em]; best = None
        for c in itertools.product(*[range(-b_, b_ + 1) for b_ in bnd]):
            if c in ((1, 1, 1, 1), (-1, -1, -1, -1)) or not any(c): continue
            w = [sum(c[k] * fl[(k + j) % 4] for k in range(4)) for j in range(4)]
            if any(abs(x) < math.exp(-m) * (1 - 1e-9) or abs(x) > math.exp(m) * (1 + 1e-9) for x in w): continue
            if abs(abs(w[0] * w[1] * w[2] * w[3]) - 1) > 1e-6: continue
            sup = max(abs(math.log(abs(x))) for x in w); best = sup if best is None else min(best, sup)
        m0 = best if best is not None else m
    cap = float(reg(B)) * (1 + 1e-20) / ((2 / 3) * m0 ** 3)
    def rank_mod(rows, l):
        A = [list(r) for r in rows]; rk = 0
        for col in range(len(A[0])):
            piv = next((i for i in range(rk, len(A)) if A[i][col] % l), None)
            if piv is None: continue
            A[rk], A[piv] = A[piv], A[rk]; inv = pow(A[rk][col], -1, l); A[rk] = [v * inv % l for v in A[rk]]
            for i in range(len(A)):
                if i != rk and A[i][col] % l: f = A[i][col]; A[i] = [(a_ - f * b_) % l for a_, b_ in zip(A[i], A[rk])]
            rk += 1
        return rk
    ok_sat = True
    for l in [p_ for p_ in range(2, int(cap) + 1) if is_prime_mr(p_)]:
        us = ([[1, 1, 1, 1]] + cs) if l == 2 else cs; rows = []; k = 1
        while rank_mod(rows, l) < len(us) if rows else True:
            p_ = 1 + k * q * l; k += 1
            if not is_prime_mr(p_): continue
            x_ = 2
            while pow(x_, (p_ - 1) // q, p_) == 1: x_ += 1
            r_ = pow(x_, (p_ - 1) // q, p_); rho = [0] * 4; ra = 1
            for a in range(1, q): ra = ra * r_ % p_; rho[lab[a]] = (rho[lab[a]] + ra) % p_
            z_ = 2
            while pow(z_, (p_ - 1) // l, p_) == 1: z_ += 1
            zl = pow(z_, (p_ - 1) // l, p_); ms = math.isqrt(l) + 1; baby = {}; t_ = 1
            for j in range(ms): baby.setdefault(t_, j); t_ = t_ * zl % p_
            gi = pow(zl, l - ms, p_)
            def dlog(y):
                for i in range(ms + 1):
                    if y in baby: return (i * ms + baby[y]) % l
                    y = y * gi % p_
            for sh in range(4):
                rows.append([dlog(pow(sum(c[kk] * rho[(kk + sh) % 4] for kk in range(4)) % p_, (p_ - 1) // l, p_)) for c in us])
            if k > 400: ok_sat = False; break
    parts = dict(labels=okl, units=ok_unit, relation=delta < 1e-50, saturated=ok_sat)
    return dict(h=detX, certified=all(parts.values()), parts=parts, cap=cap, X=X)

def cyclic_classes(q, n):
    """L2048 Lemma C1_n: classes mod n-th powers (n | q - 1) from n scaled order-n orbits mod q^(n+1);
    top digit = t^n/(n-1)! mod q, counts read back from balance sums.  Returns (labels, all correct)."""
    m, qn = q ** (n + 1), q ** n
    g = next(x for x in range(2, q) if all(pow(x, (q - 1) // f, q) != 1 for f in factor(q - 1)))
    z = pow(pow(g, (q - 1) // n, q), qn, qn); r = [pow(1 + q, pow(z, j, qn), m) for j in range(n)]; sup = []
    for c in range(n):
        sc = pow(g, c, q); x = [1] * n; cnt = [0] * q
        for _ in range(q): cnt[((sum(x) * sc - n * sc) % m) // qn] += q ** (n - 1); x = [a * b % m for a, b in zip(x, r)]
        N = q ** n; S = [sum(v * k for v, k in enumerate(cnt))]
        for cc in range(1, q): S.append(S[-1] + N - q * cnt[q - cc])
        k = [0] * q
        for cc in range(1, q): k[q - cc] = (S[cc - 1] + N - S[cc]) // q
        sup.append({s_ for s_ in range(1, q) if k[s_] > 0})
    base = next(c for c in range(n) if 1 in sup[c])
    lab = [None] + [(next(c for c in range(n) if s_ in sup[c]) - base) % n for s_ in range(1, q)]
    return lab, all(pow(s_, (q - 1) // n, q) == pow(g, lab[s_] * (q - 1) // n, q) for s_ in range(1, q))

def cyclic_certificate(q, n, budget=40000):
    """L2048 Theorem H_n*: certified class number of the real cyclic field of degree n (n = 3, 4, 6; (q-1)/n even) of prime
    conductor q (needs mpmath).  Saturation and certificate by l-th power residue characters; lambda_1 from Lemma D_n and a
    box enumeration with rigorous float error bounds; R_low = P_r m0^r (Minkowski II).  Returns dict(h, certified, parts, cap)."""
    if not HAVE_MP: return None
    import itertools
    from fractions import Fraction
    mp, iv = mpmath.mp, mpmath.iv; mp.dps = iv.dps = 200; r = n - 1
    lab, okl = cyclic_classes(q, n)
    eta = [iv.mpf(0)] * n; D = [iv.mpf(0)] * n
    for a in range(1, (q - 1) // 2 + 1):
        x = iv.pi * a / q; eta[lab[a]] += 2 * iv.cos(2 * x); D[lab[a]] += iv.log(2 * iv.sin(x))
    em = [mp.mpf(x.mid) for x in eta]; VI = mp.inverse(mp.matrix([[em[(k + j) % n] for k in range(n)] for j in range(n)]))
    SG = [t for t in itertools.product((1, -1), repeat=n) if t[0] == 1]
    def coords(y):
        E = [mp.exp(t) for t in y]
        for sg in SG:
            c = VI * mp.matrix([sg[i] * E[i] for i in range(n)])
            if all(abs(c[i] - mp.nint(c[i])) < mp.mpf(10) ** -30 for i in range(n)): return [int(mp.nint(c[i])) for i in range(n)]
    def emb(c): return [sum((c[k] * eta[(k + j) % n] for k in range(1, n)), c[0] * eta[j]) for j in range(n)]
    Lv = [D[(j + 1) % n] - D[j] for j in range(n)]; Lm = [mp.mpf(x.mid) for x in Lv]
    B = [[Lm[(j + i) % n] for j in range(n)] for i in range(r)]; C = [coords(b) for b in B]
    reg = lambda B: abs(mp.det(mp.matrix([[B[i][j] for j in range(r)] for i in range(r)])))
    # lambda_1: Lemma D_d for every divisor d > 1 of n, then a rigorous box enumeration
    def mgen(d):
        w = [d - i for i in range(1, d + 1)]; h_ = d // 2; W = sum(w[:h_]) - sum(w[d - h_:])
        return ((d - 1) * math.log(q) - d * (d - 1) / 2 * math.log(4)) / (2 * W)
    mD = min(mgen(d) for d in range(2, n + 1) if n % d == 0)
    rows_ = [float(sum(abs(VI[k, j]) for j in range(n))) * (1 + 1e-12) for k in range(n)]; m = max(mD, 0.0); m0 = mD
    if math.prod(2 * int(x * math.exp(m + 0.05)) + 1 for x in rows_) <= budget:
        while math.prod(2 * int(x * math.exp(m + 0.05)) + 1 for x in rows_) <= budget: m += 0.05
        bnd = [int(x * math.exp(m)) for x in rows_]; ef = [float(x) for x in em]; best = None
        for c in itertools.product(*[range(-b, b + 1) for b in bnd]):
            if not any(c) or c in (tuple([1] * n), tuple([-1] * n)): continue
            err = 1e-13 * (sum(abs(c[k] * ef[k]) for k in range(n)) + 1)
            w = [sum(c[k] * ef[(k + j) % n] for k in range(n)) for j in range(n)]
            if any(abs(x) + err < math.exp(-m) or abs(x) - err > math.exp(m) for x in w): continue
            e = emb(list(c)); N = e[0]
            for z in e[1:]: N = N * z
            if not any(int(mpmath.floor(N.b)) >= t and int(mpmath.ceil(N.a)) <= t for t in (1, -1)): continue
            sl = max(float(abs(iv.log(abs(z))).a) for z in e); best = sl if best is None else min(best, sl)
        m0 = max(mD, m if best is None else min(m, best))
    PR = {1: 1.0, 2: 0.75, 3: 2 / 3, 5: 0.55}[r]; Rlow = PR * m0 ** r
    def kernel(rows, nc, l):
        A = [list(x) for x in rows]; piv = []; rk = 0
        for col in range(nc):
            pr = next((i for i in range(rk, len(A)) if A[i][col] % l), None)
            if pr is None: continue
            A[rk], A[pr] = A[pr], A[rk]; inv = pow(A[rk][col], -1, l); A[rk] = [v * inv % l for v in A[rk]]
            for i in range(len(A)):
                if i != rk and A[i][col] % l: f = A[i][col]; A[i] = [(a_ - f * b_) % l for a_, b_ in zip(A[i], A[rk])]
            piv.append(col); rk += 1
        out = []
        for fc in [c for c in range(nc) if c not in piv]:
            x = [0] * nc; x[fc] = 1
            for i, pc in enumerate(piv): x[pc] = (-A[i][fc]) % l
            out.append(x)
        return out
    def chars(us, l, npr):
        rows = []; k = 1; got = 0
        while got < npr:
            p_ = 1 + k * q * l; k += 1
            if not is_prime_mr(p_): continue
            got += 1; x_ = 2
            while pow(x_, (p_ - 1) // q, p_) == 1: x_ += 1
            r_ = pow(x_, (p_ - 1) // q, p_); rho = [0] * n; ra = 1
            for a in range(1, q): ra = ra * r_ % p_; rho[lab[a]] = (rho[lab[a]] + ra) % p_
            z_ = 2
            while pow(z_, (p_ - 1) // l, p_) == 1: z_ += 1
            zl = pow(z_, (p_ - 1) // l, p_); ms = math.isqrt(l) + 1; baby = {}; t_ = 1
            for j in range(ms): baby.setdefault(t_, j); t_ = t_ * zl % p_
            gi = pow(zl, l - ms, p_)
            def dlog(y):
                for i in range(ms + 1):
                    if y in baby: return (i * ms + baby[y]) % l
                    y = y * gi % p_
            for sh in range(n):
                rows.append([dlog(pow(sum(c[kk] * rho[(kk + sh) % n] for kk in range(n)) % p_, (p_ - 1) // l, p_)) for c in us])
        return rows
    nextp = lambda l: next(x for x in itertools.count(l + 1) if is_prime_mr(x))
    l = 2
    while l <= float(reg(B)) / Rlow:
        us = lambda: ([[1] * n] + C) if l == 2 else C
        K = kernel(chars(us(), l, 2), len(us()), l); tries = 0
        while K and tries < 6:
            found = False
            for x in K:
                xs = x[1:] if l == 2 else x
                if not any(v % l for v in xs): continue
                i0 = next(i for i in range(r) if xs[i] % l); inv = pow(xs[i0], -1, l); xs = [v * inv % l for v in xs]
                y = [sum(xs[i] * B[i][j] for i in range(r)) / l for j in range(n)]; c = coords(y)
                if c is not None: B[i0] = y; C[i0] = c; found = True; break
            if not found: tries += 1
            K = kernel(chars(us(), l, 2 + 2 * tries), len(us()), l)
        if K: return dict(h=None, certified=False, parts=dict(saturated=False))
        l = nextp(l)
    ok_u = True; LW = []
    for c in C:
        e = emb(c); N = e[0]
        for z in e[1:]: N = N * z
        ok_u &= int(mpmath.ceil(N.a)) == int(mpmath.floor(N.b)) and abs(int(mpmath.ceil(N.a))) == 1; LW.append([iv.log(abs(z)) for z in e])
    Bi = mp.inverse(mp.matrix([[mp.mpf(LW[i][j].mid) for j in range(r)] for i in range(r)])); X = []; delta = 0
    for i in range(r):
        xv = mp.matrix([[mp.mpf(Lv[(j + i) % n].mid) for j in range(r)]]) * Bi; X.append([int(mp.nint(xv[0, k])) for k in range(r)])
        for j in range(n):
            d = Lv[(j + i) % n] - sum(X[i][k] * LW[k][j] for k in range(r)); delta = max(delta, abs(float(d.a)), abs(float(d.b)))
    Mx = [[Fraction(v) for v in row] for row in X]; detX = Fraction(1)
    for i in range(r):
        pv = next((k for k in range(i, r) if Mx[k][i] != 0), None)
        if pv is None: detX = Fraction(0); break
        if pv != i: Mx[i], Mx[pv] = Mx[pv], Mx[i]; detX = -detX
        detX *= Mx[i][i]
        for k in range(i + 1, r):
            f = Mx[k][i] / Mx[i][i]; Mx[k] = [a_ - f * b_ for a_, b_ in zip(Mx[k], Mx[i])]
    cap = float(reg(B)) * (1 + 1e-12) / Rlow; ok_s = True; l = 2
    while l <= cap:
        us = ([[1] * n] + C) if l == 2 else C; npr = 3
        while kernel(chars(us, l, npr), len(us), l) and npr < 24: npr += 3
        if npr >= 24: ok_s = False; break
        l = nextp(l)
    parts = dict(labels=okl, units=ok_u, relation=delta < 1e-50, saturated=ok_s)
    return dict(h=abs(int(detX)), certified=all(parts.values()), parts=parts, cap=cap, m0=m0)

def imaginary_cyclic_class_number(q, n):
    """L2052 Theorem I_n: class number h = h+ . h- of the imaginary cyclic field of degree n = 4 or 6 and prime conductor q
    ((q - 1)/n odd).  h- exactly from the orbit labels: c_k = sum_{lab(a) = k} a,
      n = 4: h- = w |S1|^2/(4 q^2), |S1|^2 = (c0 - c2)^2 + (c1 - c3)^2 (w = 2; 10 for q = 5);
      n = 6: h- = -w S3 |S1|^2/(8 q^3), S3 = sum (-1)^k c_k = -q h(Q(sqrt -q)), |S1|^2 an Eisenstein norm (w = 2; 14 for q = 7).
    h+ certified by cyclic_certificate on the real subfield (degree n/2; needs mpmath; q = 5, 7 have h+ = 1 directly).
    Returns dict(h_minus, h_plus, h, certified_plus)."""
    from fractions import Fraction
    lab, ok = cyclic_classes(q, n); c = [0] * n
    for a in range(1, q): c[lab[a]] += a
    if n == 4:
        w = 10 if q == 5 else 2; hm = Fraction(w * ((c[0] - c[2]) ** 2 + (c[1] - c[3]) ** 2), 4 * q * q)
    else:
        w = 14 if q == 7 else 2; S3 = sum((-1) ** k * c[k] for k in range(6))
        P = [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)]
        A = sum(c[k] * P[k][0] for k in range(6)); B = sum(c[k] * P[k][1] for k in range(6))
        hm = Fraction(-w * S3 * (A * A + A * B + B * B), 8 * q ** 3)
    if q in (5, 7): hp, cert = 1, True                                 # Q(sqrt5), Q(zeta7)+ : h+ = 1 (small fields)
    elif HAVE_MP:
        r = cyclic_certificate(q, n // 2); hp, cert = r["h"], r["certified"]
    else: hp, cert = None, False
    return dict(h_minus=hm, h_plus=hp, h=(hm * hp if hp else None), certified_plus=cert, labels_ok=ok)

_PHI_CACHE = {}

def _phi(m):
    """cyclotomic polynomial Phi_m as an integer list, x^0 first (exact division of x^m - 1)"""
    if m in _PHI_CACHE: return _PHI_CACHE[m]
    num = [-1] + [0] * (m - 1) + [1]
    for d in range(1, m):
        if m % d == 0:
            den = _phi(d); out = [0] * (len(num) - len(den) + 1); r = list(num)
            for i in range(len(out) - 1, -1, -1):
                out[i] = r[i + len(den) - 1]
                for k in range(len(den)): r[i + k] -= out[i] * den[k]
            num = out
    _PHI_CACHE[m] = num; return num

def _cyc_reduce(a, m):
    ph = _phi(m); d = len(ph) - 1; a = list(a) + [0] * max(0, d - len(a))
    for i in range(len(a) - 1, d - 1, -1):
        c = a[i]
        if c:
            for k in range(d + 1): a[i - d + k] -= c * ph[k]
    return a[:d]

def _cyc_mul(a, b, m):
    out = [0] * (len(a) + len(b) - 1)
    for i, x_ in enumerate(a):
        if x_:
            for j, y in enumerate(b): out[i + j] += x_ * y
    return _cyc_reduce(out, m)

def _cyc_conj(a, m, u):
    out = [0] * m
    for i, x_ in enumerate(a): out[(i * u) % m] += x_
    return _cyc_reduce(out, m)

def _cyc_norm(a, m):
    prod = [1]
    for u in range(1, m):
        if math.gcd(u, m) == 1: prod = _cyc_mul(prod, _cyc_conj(a, m, u), m)
    assert all(v == 0 for v in prod[1:]); return prod[0]

def _cyc_divide(a, d, m):
    """a / d in Z[zeta_m] (exact) or None"""
    num = list(a)
    for u in range(2, m):
        if math.gcd(u, m) == 1: num = _cyc_mul(num, _cyc_conj(d, m, u), m)
    Nd = _cyc_norm(d, m)
    return [v // Nd for v in num] if all(v % Nd == 0 for v in num) else None

def relative_class_number(q, n):
    """L2060 Theorem N (every even n): relative class number of the imaginary cyclic field K of degree n = 2^v n' and prime
    conductor q > n + 1 ((q - 1)/n odd), as a product of norms.  x_m = (1/q) sum_a chi_m(a) a for chi_m of exact order m
    (m | n, n/m odd), with chi_m(a) = zeta_m^lab(a) from the orbit labels.
      h-(K) = h-(K_{2^v}) prod_{m' | n', m' > 1} N(x_m / 2);  h-(K_{2^v}) = h(Q(sqrt -q)) (v = 1) or N(x / (1 - zeta)^(2^(v-1)-1)).
    Returns dict(h_minus, factors = [(m, factor)], sub = h-(K_{2^v}), labels_ok)."""
    lab, ok = cyclic_classes(q, n); c = [0] * n
    for a in range(1, q): c[lab[a]] += a
    v = (n & -n).bit_length() - 1; no = n >> v; factors = []
    for mo in [d for d in range(1, no + 1) if no % d == 0]:
        m = (1 << v) * mo; co = [0] * m
        for k in range(n): co[k % m] += c[k]
        X = _cyc_reduce(co, m); assert all(t % q == 0 for t in X), "q does not divide S_m"
        X = [t // q for t in X]
        if mo == 1:
            if v == 1: f = -X[0]
            else:
                d = [1]
                for _ in range((1 << (v - 1)) - 1): d = _cyc_mul(d, [1, -1], m)
                G = _cyc_divide(X, d, m); assert G is not None, "2-power division failed"; f = _cyc_norm(G, m)
        else:
            assert all(t % 2 == 0 for t in X), "Lemma N2 failed"; f = _cyc_norm([t // 2 for t in X], m)
        factors.append((m, f))
    return dict(h_minus=math.prod(f for _, f in factors), factors=factors, sub=factors[0][1], labels_ok=ok)

def norm_factor_statistics(n, qmax, primes=(3, 5, 7, 11, 13)):
    """L2064: divisibility statistics of the top norm factor of Theorem N (n = 4: h-; n = 6, 10: N(x_n/2)) over all primes
    q < qmax with (q - 1)/n odd, against Cohen-Lenstra-Martinet: P(l | F) = 1 - prod_{L | l} prod_k (1 - N(L)^-k).
    Labels from a primitive-root index table (equal to the orbit labels by Lemma C1_n).  Returns (count, [(l, observed, predicted)])."""
    vals = []
    for q in range(n + 3, qmax):
        if not is_prime_mr(q) or (q - 1) % n or ((q - 1) // n) % 2 == 0: continue
        fs = factor(q - 1); g = next(x for x in range(2, q) if all(pow(x, (q - 1) // f, q) != 1 for f in fs))
        lab = [None] * q; t = 1
        for k in range(q - 1): lab[t] = k % n; t = t * g % q
        c = [0] * n
        for a in range(1, q): c[lab[a]] += a
        X = [v // q for v in _cyc_reduce(c, n)]
        G = _cyc_divide(X, [1, 1], 4) if n == 4 else [v // 2 for v in X]
        vals.append(_cyc_norm(G, n))
    out = []
    for l in primes:
        if n % l == 0: continue
        f = next(k for k in range(1, n + 1) if pow(l, k, n) == 1); g_ = sum(1 for u in range(1, n) if math.gcd(u, n) == 1) // f
        eta = 1.0
        for k in range(1, 100): eta *= 1 - float(l) ** (-f * k)
        out.append((l, sum(1 for v in vals if v % l == 0) / max(1, len(vals)), 1 - eta ** g_))
    return len(vals), out

def two_part_link(q):
    """L2068 Law P (verified): for the imaginary cyclic sextic field of prime conductor q = 7 mod 12, the Eisenstein factor
    F = N(x_6/2) of Theorem N is even exactly when the class number h(K3) of the real cubic subfield is even
    (2 is inert in Z[zeta3], so F even <=> 4 | x_6;  h(K3) even <=> the cyclotomic unit v is +- a square).
    Needs mpmath for the cubic certificate.  Returns dict(F, h3, F_even, h3_even, agree)."""
    r = relative_class_number(q, 6); F = r["factors"][-1][1]
    if not HAVE_MP: return dict(F=F, h3=None, F_even=F % 2 == 0, h3_even=None, agree=None)
    h3 = cubic_certificate(q)["h"]
    return dict(F=F, h3=h3, F_even=F % 2 == 0, h3_even=h3 % 2 == 0, agree=(F % 2 == 0) == (h3 % 2 == 0))

def harmonic_links(b=10, pmax=400):
    """L2072: exact links between 1/n, Fibonacci, the 60/24 clocks, phi, pi and log spirals (all checked, exact where possible).
    Returns a list of (statement, verified)."""
    from fractions import Fraction
    out = []; F = [0, 1]
    for _ in range(1200): F.append(F[-1] + F[-2])                      # (phi/2)^1200 ~ 1e-110: tail far below the tolerance
    def pis(m):
        x, y, k = 0, 1, 0
        while True:
            x, y = y, (x + y) % m; k += 1
            if (x, y) == (0, 1): return k
    def order(a, m):
        k, t = 1, a % m
        while t != 1: t = t * a % m; k += 1
        return k
    out.append(("sum F_k/2^(k+1) = 1 exactly (b = 2 case of 1/(b^2-b-1))", abs(sum(Fraction(F[k], 2 ** (k + 1)) for k in range(1200)) - 1) < Fraction(1, 10 ** 80)))
    out.append(("sum F_k/%d^(k+1) = 1/%d" % (b, b * b - b - 1), abs(sum(Fraction(F[k], b ** (k + 1)) for k in range(300)) - Fraction(1, b * b - b - 1)) < Fraction(1, 10 ** 200)))
    n = b * b - b - 1; T = order(b, n) if math.gcd(n, 5 * b) == 1 else None
    if T: out.append(("clock law for n = %d: base-%d period T = %d, Pisano period = %d (= T if T even, 2T if odd)" % (n, b, T, pis(n)), pis(n) == (T if T % 2 == 0 else 2 * T)))
    chi5 = lambda a: [0, 1, -1, -1, 1][a % 5]
    out.append(("Fibonacci reads chi_5: F_p = (p/5) mod p for primes 7 <= p < %d" % pmax,
                all(F[p] % p == (1 if chi5(p) == 1 else p - 1) for p in range(7, min(pmax, 290)) if is_prime_mr(p))))
    out.append(("60 = lcm(pi(2) = 3, pi(5) = 20); 24 = pi(9) = 3 pi(3) = 3 x 8", (pis(2), pis(5), pis(10), pis(3), pis(9)) == (3, 20, 60, 8, 24)))
    if HAVE_MP:
        mp = mpmath.mp; mp.dps = 40; phi = (1 + mp.sqrt(5)) / 2
        L4 = mpmath.nsum(lambda k: (-1) ** k / (2 * k + 1), [0, mpmath.inf])
        L5 = -sum(chi5(a) * mpmath.digamma(mp.mpf(a) / 5) for a in range(1, 5)) / 5
        out.append(("L(1, chi_-4) = pi/4 and L(1, chi_5) = 2 log(phi)/sqrt5", abs(L4 - mp.pi / 4) < 1e-30 and abs(L5 - 2 * mp.log(phi) / mp.sqrt(5)) < 1e-30))
        out.append(("golden spiral growth per radian 2 log(phi)/pi = sqrt5 L(1,chi_5) / (4 L(1,chi_-4)) = %s" % mpmath.nstr(2 * mp.log(phi) / mp.pi, 12),
                    abs(2 * mp.log(phi) / mp.pi - mp.sqrt(5) * L5 / (4 * L4)) < 1e-30))
    return out

def necklace_ladder(bmax=20, a=1):
    """L2076: the Fibonacci-necklace ladder for x(n+1) = a x(n) + x(n-1): N(b) = b^2 - a b - 1 = Norm(b - eps).
    sum x_k / b^(k+1) = 1/N(b);  for a = 1 the signed necklace of base b is the direct necklace of base b + 1
    (N(b+1) - N(b) = 2b), so 89 (base 10) and 109 (base 11) are neighbouring rungs.  Returns [(b, N(b), factors)]."""
    return [(b, b * b - a * b - 1, factor(b * b - a * b - 1) if b * b - a * b - 1 > 1 else []) for b in range(2, bmax + 1)]

def spiral_rate(D, t, u):
    """L2076 spiral law: the logarithmic spiral growing by the fundamental unit (t + u sqrt D)/2 every quarter turn has rate
    2 log(eps)/pi = sqrt(D) L(1, chi_D) / (4 h L(1, chi_-4)) (classical class number formula).  Returns the rate per radian."""
    return 2 * math.log((t + u * math.sqrt(D)) / 2) / math.pi

def _gf2_mod(a, b):
    db = b.bit_length() - 1
    while a and a.bit_length() - 1 >= db: a ^= b << (a.bit_length() - 1 - db)
    return a

def _gf2_gcd(a, b):
    while b: a, b = b, _gf2_mod(a, b)
    return a

def two_adic_pattern(q, n):
    """L2080 Law P* (verified, n = 2l with l an odd prime): for the imaginary cyclic field K of degree n and prime conductor q
    ((q - 1)/n odd), let x = (1/q) sum_a chi(a) a (chi of order n, from the index labels) and k = the number of primes above 2 in
    Z[zeta_n] dividing x/2.  F = N(x/2) is even iff k > 0; observed: the NARROW class number of the real subfield K+ is even iff
    k > 0, with 2-rank f*k (f = order of 2 mod l; L2084: the exact valuation v2 = f*k fails at q = 29611, n = 14), and the wide h+ is even iff k = g (all primes above 2).
    Pure Python (GF(2) polynomial gcd).  Returns dict(k, g, f, F_even, narrow_even_pred, wide_even_pred)."""
    fs = factor(q - 1); gr = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    lab = [None] * q; t = 1
    for j in range(q - 1): lab[t] = j % n; t = t * gr % q
    c = [0] * n
    for a in range(1, q): c[lab[a]] += a
    X = _cyc_reduce(c, n); assert all(v % q == 0 for v in X); X = [v // q for v in X]
    assert all(v % 2 == 0 for v in X), "Lemma N2 failed"
    y = sum(((v // 2) & 1) << i for i, v in enumerate(X)); ph = sum((v & 1) << i for i, v in enumerate(_phi(n)))
    f = next(k for k in range(1, n + 1) if pow(2, k, n // 2 if n % 4 == 2 else n) == 1)
    deg = (_gf2_gcd(ph, y).bit_length() - 1) if y else len(_phi(n)) - 1
    k = deg // f; g = (len(_phi(n)) - 1) // f
    return dict(k=k, g=g, f=f, F_even=k > 0, narrow_even_pred=k > 0, wide_even_pred=k == g)

def two_adic_heuristic(n):
    """L2084 Law S (observed): for n = 2l (l an odd prime), how often some prime above 2 divides x/2 (k > 0), i.e. how often the
    narrow class number of the real degree-l subfield is even.  2 has g primes of degree f = ord_l(2) above it; they are
    self-conjugate exactly when -1 is a power of 2 mod l.  Not self-conjugate: the naive Cohen-Lenstra-Martinet value
    1 - prod_i (1 - 2^-fi)^g fits (n = 14, 46, 62).  Self-conjugate: strongly suppressed (n = 6, 10, 18, 34); a tentative fit is
    1 - prod_i (1 + Q^-(2i+1))^-g with Q = 2^(f/2) (L2096 revision: the L2084 form 1 - prod (1 - Q^-(2i+1)) is rejected
    at f = 2 by 22 000 cubic fields up to 1e11, z = -7.3; the two agree to 2% for f >= 4).  Returns dict(f, g, self_conjugate, naive, tentative)."""
    l = n // 2; f = next(k for k in range(1, l) if pow(2, k, l) == 1); g = (l - 1) // f
    sc = any(pow(2, k, l) == l - 1 for k in range(f))
    e1 = e2 = 1.0; Q = 2.0 ** (f / 2)
    for i in range(1, 200): e1 *= 1 - 2.0 ** (-f * i); e2 /= 1 + Q ** (-(2 * i + 1))   # L2096: revised Law S (variant B)
    e3 = 1.0
    for i in range(2, 200): e3 *= 1 - 2.0 ** (-f * i)
    m = g // 2 if not sc else 0                                          # number of dual pairs (chi, chi*)
    return dict(f=f, g=g, self_conjugate=sc, naive=1 - e1 ** g, tentative=(1 - e2 ** g) if sc else None,
                # L2088: Breen-Varma-Voight (2021) Conj. 6.1.1 per dual pair, P(exactly one prime | not both) = 2/(2^f + 1);
                # self-dual: Cl+[2] = Cl[2] (Oriat; BVV Cor. 5.4.5), so narrow and wide parity agree (Law P for g = 1)
                bvv_one_given_not_both=(2 / (2 ** f + 1)) if not sc else None,
                wide_even_clm=(1 - e3 ** (2 * m)) if not sc else None, narrow_equals_wide=sc)

def component_pattern(q, n):
    """L2092: every character component of the imaginary cyclic field of degree n = 2 * (odd) and prime conductor q
    ((q - 1)/n odd).  For each m | n with n/m odd and m > 2, x_m = (1/q) sum_a chi_m(a) a (chi_m of order m); returns
    {m: (k_m, g_m, f_m, self_dual)} with k_m = number of primes above 2 of Z[zeta_m] dividing x_m/2.  By Law R and Theorem G
    each such prime marks one F_{2^f}-piece of the narrow 2-class group of the real subfield; the components were found to be
    statistically independent (L2092, n = 30, 42).  Pure Python."""
    fs = factor(q - 1); gr = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    c = [0] * n; t = 1
    for j in range(q - 1): c[j % n] += t; t = t * gr % q
    out = {}
    for m in range(3, n + 1):
        if n % m or (n // m) % 2 == 0: continue
        co = [0] * m
        for k in range(n): co[k % m] += c[k]
        X = _cyc_reduce(co, m); assert all(v % q == 0 for v in X); X = [v // q for v in X]; assert all(v % 2 == 0 for v in X)
        y = sum(((v // 2) & 1) << i for i, v in enumerate(X)); ph = sum((v & 1) << i for i, v in enumerate(_phi(m)))
        o = m // 2 if m % 4 == 2 else m; f = next(k for k in range(1, o + 1) if pow(2, k, o) == 1)
        deg = (_gf2_gcd(ph, y).bit_length() - 1) if y else len(_phi(m)) - 1
        out[m] = (deg // f, (len(_phi(m)) - 1) // f, f, any(pow(2, k, o) == o - 1 for k in range(f)))
    return out

def cubic_parity_fast(q):
    """L2096: is the class number of the cyclic cubic field of prime conductor q = 7 (mod 12) even?  O(sqrt(q)) steps.
    Via Law P (n = 6; F even => h even is proven in L2096, the converse is verified) the answer is 4 | x, x = B_{1,chi},
    chi = psi * eps (cubic times Legendre).  x is recovered from L(1, chi) by the approximate functional equation, with the
    root number W = tau(psi) / (psi(4) J(psi, psi)), tau(psi)^3 = q J(psi, psi) (J from q = a^2 + 3 b^2); the cube-root
    ambiguity is removed by requiring x to be a lattice point of Z[omega].  Returns (even, lattice_error, (u, v)) with
    x = u + v omega up to a unit and conjugation."""
    import cmath
    OM = complex(-0.5, math.sqrt(3) / 2)
    fs = factor(q - 1); g = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    w = pow(g, (q - 1) // 3, q)
    r = next(t for t in range(1, q) if (t * t + 3) % q == 0) if q < 10 ** 6 else None
    if r is None:                                             # Tonelli-Shanks for sqrt(-3) mod q
        a_ = q - 3; Q_, S_ = q - 1, 0
        while Q_ % 2 == 0: Q_ //= 2; S_ += 1
        z = next(t for t in range(2, q) if pow(t, (q - 1) // 2, q) == q - 1)
        M_, c_, t_, r = S_, pow(z, Q_, q), pow(a_, Q_, q), pow(a_, (Q_ + 1) // 2, q)
        while t_ != 1:
            i_, tt = 0, t_
            while tt != 1: tt = tt * tt % q; i_ += 1
            b_ = pow(c_, 1 << (M_ - i_ - 1), q); M_, c_, t_, r = i_, b_ * b_ % q, t_ * b_ * b_ % q, r * b_ % q
    A, B = q, (r if r > q // 2 else q - r); lim = math.isqrt(q)
    while B > lim: A, B = B, A % B
    a, b = B, math.isqrt((q - B * B) // 3)
    J = None
    for s_ in (1, -1):
        u0, v0 = a + s_ * b, 2 * s_ * b
        for k in range(6):
            uu, vv = u0, v0
            for _ in range(k % 3): uu, vv = -vv, uu - vv
            if k >= 3: uu, vv = -uu, -vv
            if uu % 3 == 2 and vv % 3 == 0 and (uu + vv * w) % q == 0: J = (uu, vv)
    Jc = J[0] + J[1] * OM
    N = int(3.6 * math.sqrt(q)) + 10; e6 = [0] * (N + 1); isp = bytearray([1]) * (N + 1); isp[0] = isp[1] = 0
    for p in range(2, N + 1):
        if not isp[p]: continue
        for m in range(p * p, N + 1, p): isp[m] = 0
        t = pow(p, (q - 1) // 3, q); k = 0 if t == 1 else (1 if t == w else 2)
        ep = (2 * k + (0 if pow(p, (q - 1) // 2, q) == 1 else 3)) % 6
        if ep:
            pk = p
            while pk <= N:
                for m in range(pk, N + 1, pk): e6[m] += ep
                pk *= p
    Z6 = [cmath.exp(1j * math.pi * k / 3) for k in range(6)]
    S1 = S2 = 0j; sq = math.sqrt(math.pi / q)
    for n_ in range(1, N + 1):
        c = Z6[e6[n_] % 6]; S1 += c * math.exp(-math.pi * n_ * n_ / q) / n_; S2 += c.conjugate() * math.erfc(n_ * sq)
    best = None; rt = (q * Jc) ** (1 / 3); chi4 = Z6[e6[4] % 6]
    for m in range(3):
        W = rt * OM ** m / (chi4 * Jc); L = S1 + math.pi * W / math.sqrt(q) * S2; X = -math.sqrt(q) * L / (math.pi * W)
        v = X.imag / (math.sqrt(3) / 2); u = X.real + v / 2; err = max(abs(u - round(u)), abs(v - round(v)))
        if best is None or err < best[0]: best = (err, round(u), round(v))
    err, u, v = best
    return (u % 4 == 0 and v % 4 == 0), err, (u, v)

def fast_minus_coordinates(q, n, tmax=1.25):
    """L2100: x = B_{1,chi} (chi odd of order n, prime conductor q, (q - 1)/n odd) as integer coordinates in the basis
    zeta_n^k (k < phi(n)), in O(sqrt(q)) steps, with no Gauss or Jacobi sums: for every t > 0
      L(1, chi) = sum chi(m) e^(-pi m^2 t/q)/m + W (pi/sqrt q) sum conj(chi)(m) erfc(m sqrt(pi/(q t))),
    so two values of t determine the root number W; then B_{1, conj chi} = -sqrt(q) L(1, chi)/(pi W), and the Galois
    conjugates chi^u give all coordinates.  Pure Python.  Returns (coords, max rounding error)."""
    import cmath
    fs = factor(q - 1); g = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    w = pow(g, (q - 1) // n, q); tab = {}; t = 1
    for k in range(n): tab[t] = k; t = t * w % q
    N = int(3.6 * math.sqrt(q * tmax)) + 10; lab = [0] * (N + 1); zero = bytearray(N + 1); isp = bytearray([1]) * (N + 1)
    for m in range(q, N + 1, q): zero[m] = 1
    for p in range(2, N + 1):
        if not isp[p]: continue
        for m in range(p * p, N + 1, p): isp[m] = 0
        if p == q: continue
        k = tab[pow(p, (q - 1) // n, q)]
        if k:
            pk = p
            while pk <= N:
                for m in range(pk, N + 1, pk): lab[m] += k
                pk *= p
    phi = len(_phi(n)) - 1; us = [u for u in range(1, n) if math.gcd(u, n) == 1][: phi // 2]
    rows = []; rhs = []
    for u in us:
        res = []
        for tt in (1.0, tmax):
            S1 = S2 = 0j; c1 = math.pi * tt / q; c2 = math.sqrt(math.pi / (q * tt))
            for m in range(1, N + 1):
                if zero[m]: continue
                ch = cmath.exp(2j * math.pi * u * (lab[m] % n) / n)
                S1 += ch * math.exp(-c1 * m * m) / m; S2 += ch.conjugate() * math.erfc(m * c2)
            res.append((S1, S2))
        (a1, b1), (a2, b2) = res; W = (a1 - a2) / ((math.pi / math.sqrt(q)) * (b2 - b1)); W /= abs(W)
        L = a1 + W * math.pi / math.sqrt(q) * b1; B = (-math.sqrt(q) * L / (math.pi * W)).conjugate()
        z = [cmath.exp(2j * math.pi * u * k / n) for k in range(phi)]
        rows.append([v.real for v in z]); rhs.append(B.real); rows.append([v.imag for v in z]); rhs.append(B.imag)
    # Gaussian elimination (phi x phi)
    A = [r[:] + [b] for r, b in zip(rows, rhs)]
    for i in range(phi):
        piv = max(range(i, phi), key=lambda r: abs(A[r][i])); A[i], A[piv] = A[piv], A[i]
        for r in range(phi):
            if r != i:
                f = A[r][i] / A[i][i]; A[r] = [a - f * b for a, b in zip(A[r], A[i])]
    sol = [A[i][phi] / A[i][i] for i in range(phi)]; c = [round(v) for v in sol]
    return c, max(abs(a - b) for a, b in zip(sol, c))

def cyclotomic_sign_poly(q, l):
    """L2104: exact sign polynomial of the cyclotomic unit of the real cyclic field K+ of odd prime degree l and prime
    conductor q ((q - 1)/(2l) odd).  The unit u_b = zeta^(b(1-g)/2)(1 - zeta^(bg))/(1 - zeta^b) has sign (-1)^t with
    t = b + <bg> (mod 2), so s(z) = sum_{b < q/2} (b + <bg>) z^(lab(b) mod l) over F2, as an int bit-mask (bit j = z^j)."""
    fs = factor(q - 1); g = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    lab = [0] * q; t = 1
    for k in range(q - 1): lab[t] = k; t = t * g % q
    s = 0
    for b in range(1, (q + 1) // 2):
        if (b + b * g % q) & 1: s ^= 1 << (lab[b] % l)
    return s

def theorem_U(q, l):
    """L2104 Theorem U (proved): x/2 = z/(1+z) * s(z) in F2[z]/(Phi_l), where x = B_{1,chi} (chi odd of order 2l,
    chi(g) = zeta_2l -> z) and s = cyclotomic_sign_poly.  Proof: sum_a floor(ag/q) chi(a) = (g - chi(g)^-1) x (g odd
    representative), pair a with q - a, reduce mod 2; the half system covers every class mod l an odd number of times.
    Consequence for l with 2 a primitive root mod l (g = 1: l = 3, 5, 11, 13, 19, ...): h(K+) even <=> 4 | x <=> Phi_l | s.
    Returns dict(identity_holds, s_zero_mod_Phi, h_plus_even_if_2_primitive)."""
    n = 2 * l; s = cyclotomic_sign_poly(q, l); ph = sum((v & 1) << i for i, v in enumerate(_phi(l)))
    fs = factor(q - 1); g = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    c = [0] * n; t = 1
    for j in range(q - 1): c[j % n] += t; t = t * g % q
    X = [v // q for v in _cyc_reduce(c, n)]; y = 0
    for i, v in enumerate(X):
        if (v // 2) & 1: y ^= 1 << i
    def mul(a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1; a <<= 1
        return _gf2_mod(r, ph)
    r_l = 1 | sum(1 << k for k in range(1, l - 1, 2))                    # = z/(1+z) mod Phi_l
    ok = _gf2_mod(y, ph) == mul(_gf2_mod(r_l, ph), _gf2_mod(s, ph))
    prim = all(pow(2, k, l) != 1 for k in range(1, l - 1))
    sz = _gf2_mod(s, ph) == 0
    return dict(identity_holds=ok, s_zero_mod_Phi=sz, h_plus_even_if_2_primitive=(sz if prim else None))

def parity_certificate(q, l):
    """L2108 Theorem R (proved, citing Greither 1992 Cor. 4.15 for p = 2): for the real cyclic field K+ of odd prime degree l
    and prime conductor q ((q - 1)/(2l) odd), read entirely from the 1/q labels:
      narrow class number even  <=>  F = N(B_{1,chi}/2) even  <=>  some factor of Phi_l mod 2 divides the sign polynomial s;
      h(K+) even  =>  F even (Law H);  if 2 is a primitive root mod l, h(K+) even <=> Phi_l | s.
    Returns dict(k, g, f, narrow_even, wide_even (None when not decided by the theorems), proved=True)."""
    s = cyclotomic_sign_poly(q, l); r = two_adic_pattern(q, 2 * l)
    narrow_even = r["k"] > 0
    wide = dual_pair_parity(q, l)["h_plus_even"]                        # Theorem W (L2124): decided in every case
    return dict(k=r["k"], g=r["g"], f=r["f"], narrow_even=narrow_even, wide_even=wide, proved=True,
                sign_poly_zero=_gf2_mod(s, sum((v & 1) << i for i, v in enumerate(_phi(l)))) == 0)

def two_rank_bound(q, l):
    """L2112 Theorem M (proved by genus theory): for K imaginary cyclic of degree 2l (l odd prime) and prime conductor q,
    2-rank of Cl(K)/Cl(K+) = 2-rank of the NARROW class group of K+, and |Cl(K)/Cl(K+)|_2 = 2-part of F = N(x/2).
    Hence 2-rank(narrow Cl(K+)) <= v2(F), with equality pattern f*k when the wide 2-part is trivial (Theorem R).
    For cubic fields: 2-rank 4 or more forces 8 | B_{1,chi}.  Returns dict(v2F, rank_upper_bound, k, f)."""
    r = relative_class_number(q, 2 * l); F = r["factors"][-1][1]
    v = 0
    while F % 2 == 0: F //= 2; v += 1
    p = two_adic_pattern(q, 2 * l)
    return dict(v2F=v, rank_upper_bound=v, k=p["k"], f=p["f"], rank_lower_bound=p["f"] * p["k"] if p["k"] else 0)

def minus_two_part(q, n):
    """L2116: the 2-part of the minus quotient Cl(K)/Cl(K+) for the imaginary cyclic field K of degree n = 2 x odd and prime
    conductor q, i.e. 2^v2(h-(K)) (h(Q(sqrt -q)) is odd).  By Theorem M (proved for prime l; verified for degree 9, 64 fields)
    its 2-rank equals the narrow 2-rank of K+, so the narrow 2-rank is at most v2(h-).  Returns dict(v2_minus, factors)."""
    r = relative_class_number(q, n); v = 0; h = r["h_minus"]
    while h % 2 == 0: h //= 2; v += 1
    return dict(v2_minus=v, factors=r["factors"])

def _gf2_factors(m):
    """irreducible factors of Phi_m over F2 (m odd), as int bit-masks, by brute-force trial division (small m)"""
    ph = sum((v & 1) << i for i, v in enumerate(_phi(m))); out = []; d = 1
    while ph.bit_length() > 1:
        for p in range(1 << d, 1 << (d + 1)):
            if p & 1 and _gf2_mod(ph, p) == 0:                  # smallest-degree divisor of the remaining part: irreducible
                out.append(p)
                while _gf2_mod(ph, p) == 0:
                    qq, r = 0, ph                                    # divide ph by p
                    while r.bit_length() >= p.bit_length():
                        sh = r.bit_length() - p.bit_length(); qq ^= 1 << sh; r ^= p << sh
                    ph = qq
                break
        else: d += 1
    return out

def dual_pair_parity(q, l):
    """L2120: for odd prime l, which primes above 2 divide x/2 = B_{1,chi}/2, grouped into dual pairs (P, P*).
    Proved (Theorem R + Breen-Varma-Voight Cor. 5.4.3): if both primes of some dual pair divide, h(K+) is even.
    L2124 Theorem W (proved, citing BVV Thm 4.3.3 / Cor. 5.4.3 and Greither): h(K+) is even  <=>  some prime above 2 divides
    x/2 together with its complex conjugate (a self-dual prime counts on its own).  Returns dict(divides, pairs, self_dual,
    wide_even_proved (a non-self-dual pair divides), h_plus_even (Theorem W))."""
    n = 2 * l; fs = factor(q - 1); g = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    c = [0] * n; t = 1
    for j in range(q - 1): c[j % n] += t; t = t * g % q
    X = [v // q for v in _cyc_reduce(c, n)]; y = sum(((v // 2) & 1) << i for i, v in enumerate(X))
    F = _gf2_factors(l); deg = F[0].bit_length() - 1
    rec = lambda f: int(bin(f)[2:].zfill(deg + 1)[::-1], 2)
    div = [j for j, f in enumerate(F) if _gf2_mod(y, f) == 0]
    pairs = []
    for i, f in enumerate(F):
        j = F.index(rec(f))
        if i < j: pairs.append((i, j))
    both = any(i in div and j in div for i, j in pairs)
    selfdual = [i for i, f in enumerate(F) if rec(f) == f]
    wide = both or any(i in div for i in selfdual)
    return dict(divides=div, pairs=pairs, self_dual=selfdual, wide_even_proved=both, h_plus_even=wide)

def parity_any_degree(q, d):
    """L2128 Theorem W, composite form: the real cyclic field K+ of odd degree d > 1 and prime conductor q ((q - 1)/(2d) odd)
    has even class number  <=>  for some divisor e > 1 of d, some prime above 2 of Z[zeta_2e] divides B_{1,chi_e}/2 together
    with its complex conjugate (chi_e odd of order 2e; self-dual primes count alone).  The e-part of Cl(K+)_2 lives in the
    subfield of degree e (odd index).  Proved for prime e (Theorems R, W); the composite-e case uses the same proof
    (Theorem U holds for composite e; Z_2[C_e] is a product of unramified rings); verified for d = 9 (64 fields).
    Returns dict(per_divisor={e: (dividing factor indices, pairs, self_dual)}, h_plus_even)."""
    n = 2 * d; fs = factor(q - 1); g = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    c = [0] * n; t = 1
    for j in range(q - 1): c[j % n] += t; t = t * g % q
    out = {}; even = False
    for e in range(3, d + 1, 2):
        if d % e: continue
        m = 2 * e; co = [0] * m
        for k in range(n): co[k % m] += c[k]
        X = [v // q for v in _cyc_reduce(co, m)]; y = sum(((v // 2) & 1) << i for i, v in enumerate(X))
        F = _gf2_factors(e); deg = F[0].bit_length() - 1
        rec = lambda f: int(bin(f)[2:].zfill(deg + 1)[::-1], 2)
        div = [j for j, f in enumerate(F) if _gf2_mod(y, f) == 0]
        pairs = [(i, F.index(rec(f))) for i, f in enumerate(F) if i < F.index(rec(f))]
        sd = [i for i, f in enumerate(F) if rec(f) == f]
        if any(i in div for i in sd) or any(i in div and j in div for i, j in pairs): even = True
        out[e] = (div, pairs, sd)
    return dict(per_divisor=out, h_plus_even=even)

def certificate_strength(q, l):
    """L2132: which parts of the parity certificate for the real cyclic field of odd prime degree l and conductor q rest only on
    our own proofs plus Breen-Varma-Voight (no Greither):  'h+ odd' conclusions when no conjugate pair divides are
    Greither-free (Theorem W, direction =>, via Proposition R-half); 'h+ even' needs Greither unless 2 is a primitive root mod l.
    Returns dict(h_plus_even, greither_free)."""
    r = dual_pair_parity(q, l)
    # L2140: Theorem W is proved without Greither (the (<=) direction uses [E:C] = h+ and BVV Cor. 5.4.3), so every
    # parity certificate is Greither-free.
    return dict(h_plus_even=r["h_plus_even"], greither_free=True)

def septic_valuations(q):
    """L2136: for l = 7 (n = 14), the valuations v1, v2 of x/2 = B_{1,chi}/2 at the two primes above 2 (unramified, degree 3),
    via the norm to the decomposition field Q(sqrt -7) (2 splits there) and the 2-adic square root of -7.
    Greither-free criterion (L2136): if both valuations are >= 2, both narrow components are nonzero and h(K+) is even without
    Greither's corollary; if exactly one is positive, h(K+) is odd (Greither-free).  Returns dict(v=(v1, v2), certificate)."""
    import cmath
    n = 14; fs = factor(q - 1); g = next(t for t in range(2, q) if all(pow(t, (q - 1) // p, q) != 1 for p in fs))
    c = [0] * n; t = 1
    for j in range(q - 1): c[j % n] += t; t = t * g % q
    X = [v // q for v in _cyc_reduce(c, n)]; y = [v // 2 for v in X]
    z = _cyc_mul(_cyc_mul(y, _cyc_conj(y, n, 9), n), _cyc_conj(y, n, 11), n)      # norm to the decomposition field
    zc = sum(v * cmath.exp(2j * math.pi * k / n) for k, v in enumerate(z))
    B = round(2 * zc.imag / math.sqrt(7)); A = round(zc.real - B / 2)               # z = A + B (1 + sqrt -7)/2
    s_ = 1
    for k in range(3, 400):                                                         # 2-adic sqrt(-7), s^2 = -7 mod 2^k
        if (s_ * s_ + 7) % (1 << k): s_ += 1 << (k - 2)
    M = 1 << 380
    def v2(a):
        a %= M
        if a == 0: return 999
        return (a & -a).bit_length() - 1
    vals = []
    for sg in (1, -1):
        num = (2 * A + B * (1 + sg * s_)) % (M * 2)                                  # 2 * (A + B (1 +- s)/2)
        vals.append(v2(num) - 1)
    vs = tuple(sorted(v // 3 for v in vals))
    if vs[1] == 0: cert = "h+ odd (k = 0)"
    elif vs[0] == 0: cert = "h+ odd (one prime; Greither-free)"
    else: cert = "h+ even (both primes; Theorem W, Greither-free since L2140)"
    return dict(v=vs, certificate=cert)

def parity_report(q, l):
    """L2144: one-call summary for the real cyclic field K+ of odd prime degree l and prime conductor q ((q-1)/(2l) odd):
    sign vector of the cyclotomic unit, which primes above 2 divide B_{1,chi}/2, the proved parity of the narrow and the
    ordinary class number (Theorems R-half/M and W, Greither-free), as a list of text lines."""
    s = cyclotomic_sign_poly(q, l); r = dual_pair_parity(q, l); p = two_adic_pattern(q, 2 * l)
    lines = ["K+ of degree %d, conductor %d" % (l, q),
             "sign vector of the cyclotomic unit: %s" % format(s, "0%db" % l)[::-1],
             "primes above 2 (%d of degree %d) dividing B/2: %s; conjugate pairs %s; self-dual %s" % (p["g"], p["f"], r["divides"], r["pairs"], r["self_dual"]),
             "narrow class number even: %s (Theorem M / Law P*)" % (p["k"] > 0),
             "class number h(K+) even: %s (Theorem W)" % r["h_plus_even"]]
    return lines

def citation_checklist():
    """L2148: the outside results the parity theorems cite, with their check status (see Library_checklist_L2148.md)."""
    return [("Washington, Cyclotomic Fields 2nd ed., Thm 4.14 (capitulation kernel <= 2)", "Theorem M", "number to confirm"),
            ("Washington Thm 8.2 + subfield version; Sinnott 1980 index formula ([E:C] = h+, prime conductor)", "Theorem W (<=)", "to confirm"),
            ("Washington Thm 6.10 (Stickelberger)", "Proposition R-half", "standard"),
            ("Greither AIF 42 (1992) Thm 4.14 / Cor. 4.15 (p = 2 Gras, [E/C_1] = [A(F)] when |Delta| odd)", "Theorem R subcase only (not W)", "confirmed from page scans (L2152)"),
            ("Breen-Varma-Voight Thm 4.3.3, Prop. 4.3.6 step, Cor. 5.4.3", "Theorem W", "confirmed verbatim")]

def greither_cor_4_15():
    """L2152: Greither, Ann. Inst. Fourier 42 (1992), Cor. 4.15, as read from the page scans: 'If |Delta| is prime to p, then
    the conjecture of G. Gras is true in the following form: [E_F/C_1F] = [A(F)] in K_0^fin(Z_p[Delta])', proof given
    explicitly for p = 2 ('every totally positive element of C_F is a square in E_F, hence C_1F/C_F = (1-e)(Z/2Z)[Delta]').
    Used here only for one subcase of Theorem R.  Returns the statement string."""
    return ("[E_F/C_1F] = [A(F)] in K_0^fin(Z_p[Delta]) when |Delta| is prime to p (p = 2 included); "
            "C_1F = Sinnott's large circular units; C_1F/C_F = (1-e)(Z/2Z)[Delta] for p = 2")

def fibonacci_staircase(b=10, ncols=44):
    """L2156: the exact Fibonacci staircase for 1/(b^2 - b - 1) = sum F_k / b^(k+1) (1/89 for b = 10).  F_k is written so that
    its units digit sits at base-b place k+1; column n collects the digit of F_(n-1+j) at place b^j.  Returns dict(sums, carries,
    digits, digital_roots, agree): digits = (column sum + carry from the right) mod b reproduce 1/(b^2-b-1) exactly, while the
    digital-root shortcut (no carries) agrees only where no carry has arrived or by coincidence."""
    N = ncols + 160; F = [0, 1]
    for _ in range(N + 400): F.append(F[-1] + F[-2])
    def S(n):
        t = 0; j = 0
        while True:
            k = n - 1 + j
            if F[k] < b ** j: return t
            t += (F[k] // b ** j) % b; j += 1
    sums = [S(n) for n in range(1, N + 1)]; c = 0; dig = [0] * N; car = [0] * N
    for n in range(N, 0, -1):
        v = sums[n - 1] + c; dig[n - 1] = v % b; car[n - 1] = c; c = v // b
    dr = [0 if s_ == 0 else 1 + (s_ - 1) % (b - 1) for s_ in sums]
    return dict(sums=sums[:ncols], carries=car[:ncols], digits=dig[:ncols], digital_roots=dr[:ncols],
                agree=[n + 1 for n in range(ncols) if dr[n] == dig[n]])

def metallic_stairs(a=1, b=10, ndig=60):
    """L2160: forward and reverse staircases of x_{k+1} = a x_k + x_{k-1} (x_0 = 0, x_1 = 1).
    Forward (real): sum x_k / b^(k+1) = 1/(b^2 - a b - 1)  (a = 1: 1/89, a = 2: 1/79, a = 3: 1/69).
    Reverse (b-adic): sum x_k b^(k-1) = 1/(1 - a b - b^2) = -1/(b^2 + a b - 1)  (a = 1: -1/109, a = 2: -1/119, a = 3: -1/129).
    Since -1/m = ...RRR (b-adically, R = repetend of 1/m), the reverse stair's digits from the units upward are the period of
    1/(b^2 + a b - 1) read backwards.  Returns dict(m_forward, m_reverse, forward_digits, reverse_digits_units_first,
    period_reverse, reverse_is_repetend_backwards)."""
    x = [0, 1]
    for _ in range(ndig + 5): x.append(a * x[-1] + x[-2])
    mf, mr = b * b - a * b - 1, b * b + a * b - 1
    fd = []; r = 1
    for _ in range(ndig): r *= b; fd.append(r // mf); r %= mf
    sums = [sum((x[k] // b ** (j - k + 1)) % b for k in range(1, j + 2)) for j in range(ndig)]
    c = 0; rd = []
    for s_ in sums:
        v = s_ + c; rd.append(v % b); c = v // b
    L = next(L for L in range(1, mr + 1) if pow(b, L, mr) == 1); R = (b ** L - 1) // mr; Rd = []
    for _ in range(L): Rd.append(R % b); R //= b                      # units first = repetend backwards
    ok_ = all(rd[i] == Rd[i % L] for i in range(ndig))
    return dict(m_forward=mf, m_reverse=mr, forward_digits=fd, reverse_digits_units_first=rd, period_reverse=L,
                reverse_is_repetend_backwards=ok_)

def rung_period(b, sign=-1):
    """L2164: the rung p = b^2 + sign*b - 1 (sign = -1: forward stair 1/(b^2-b-1); sign = +1: reverse stair -1/(b^2+b-1)).
    Returns dict(p, prime, period (= ord_p(b)), pisano, lemma_ok, full, fpr, b_qr).
    Proved facts (p prime, p != 5):  (i) b+1 = 1/b mod (b^2+b-1), so the reverse rung of base b is the forward rung of base b+1
    with the same period;  (ii) Pisano pi(p) = n if n = ord_p(b) is even, 2n if n is odd;  (iii) forward rung: b is a quadratic
    residue mod p iff b != 3 mod 4, so 1/p can have full period in base b (equivalently: b is a Fibonacci primitive root of p,
    Shanks 1972) only when b = 3 mod 4."""
    q = b * b + sign * b - 1
    def isp(n):
        if n < 2: return False
        i = 2
        while i * i <= n:
            if n % i == 0: return False
            i += 1
        return True
    if not isp(q): return dict(p=q, prime=False)
    n = q - 1; m = n; fac = []; i = 2
    while i * i <= m:
        if m % i == 0:
            fac.append(i)
            while m % i == 0: m //= i
        i += 1
    if m > 1: fac.append(m)
    for l in fac:
        while n % l == 0 and pow(b, n // l, q) == 1: n //= l
    a_, c_, k = 0, 1, 0
    while True:
        a_, c_ = c_, (a_ + c_) % q; k += 1
        if a_ == 0 and c_ == 1: break
    root = b % q if sign < 0 else pow(b, -1, q)          # the root of x^2 - x - 1 attached to the base
    return dict(p=q, prime=True, period=n, pisano=k, lemma_ok=(q == 5 or k == (n if n % 2 == 0 else 2 * n)),
                full=(n == q - 1), fpr=(n == q - 1 and (root * root - root - 1) % q == 0), b_qr=pow(b, (q - 1) // 2, q) == 1)

def residue_minus_one(b, p):
    """L2168 Lemma G: for a prime p = -1 (mod b), b = 2^e c with c odd, the Legendre symbol is
    (b/p) = (2/p)^e * (-1)^(((c-1)/2)*((p+1)/2)).  Applies to every metallic rung p = b^2 - a b - 1 (and b^2 + a b - 1)."""
    e = 0; c = b
    while c % 2 == 0: c //= 2; e += 1
    two = 1 if p % 8 in (1, 7) else -1
    return two ** e * (-1) ** (((c - 1) // 2) * ((p + 1) // 2))

def metallic_mod4_law(a, b):
    """L2168 Theorem Q*: for a prime metallic rung p = b^2 - a b - 1 (p != 5), b is a quadratic NON-residue mod p
    (necessary for 1/p to have full period in base b, i.e. b a primitive root with b^2 = a b + 1) exactly when
    [L2176: proved by hand from Lemma G, no finite check needed; manuscript rungs.tex Theorem 1.1]:
      a = 1 mod 4: b = 3 mod 4;   a = 3 mod 4 or a = 0 mod 4: b = 2 mod 4;   a = 2 mod 4 (Pell family): never.
    Returns True when the law allows a full period."""
    r = a % 4
    if r == 1: return b % 4 == 3
    if r in (0, 3): return b % 4 == 2
    return False

def rung_constant(L=100000):
    """L2168: heuristic Euler product for the full-period rate of prime rungs p = b^2 - b - 1 with b = 3 mod 4:
    C = prod_{l odd prime} (1 - r(l)/((l - w(l)) l)), r(3) = 1, r(l) = 2 (l >= 5), w(5) = 1, w(l) = 1 + (5/l).
    C = 0.71792 (primes < 10^7); data b < 10^6: 0.7172.  Full-period share of all prime rungs ~ C/4 = 0.1795 (data 0.1797)."""
    import math
    sv = bytearray([1]) * L; sv[0:2] = b"\x00\x00"
    for i in range(2, int(L ** 0.5) + 1):
        if sv[i]: sv[i * i::i] = bytearray(len(sv[i * i::i]))
    lp = 0.0
    for l in range(3, L):
        if not sv[l]: continue
        w = 1 if l == 5 else (2 if pow(5, (l - 1) // 2, l) == 1 else 0)
        r = 1 if l == 3 else 2
        lp += math.log(1 - r / ((l - w) * l))
    return math.exp(lp)

def digits_used(n):
    """L2172: D(n) = number of digits used to write 1, 2, ..., n (digital space occupancy).  D(2701) = 9697, D(2702) = 9701."""
    t = 0; d = 1; lo = 1
    while lo <= n:
        hi = min(n, 10 ** d - 1); t += (hi - lo + 1) * d; lo *= 10; d += 1
    return t

def stride_stair(m, b=10):
    """L2172: the stride-m Fibonacci stair  sum_k F_(mk) / b^(m(k+1)) = F_m / N_m,  N_m = b^(2m) - L_m b^m + (-1)^m
    = Norm(b^m - phi^m) = prod over the roots.  m = 1: 89;  m = 2: 9701 = 89 * 109 = prod_{k=1..4} (10 - 2cos(k pi/5)) = U_4(5);
    m = 3: 995999 = 19^2 * 31 * 89.  The alternating version gives b^(2m) + L_m b^m + (-1)^m (m = 2: 10301, prime, full period).
    Returns dict(N, F_m, alt_N, period)."""
    F = [0, 1]; L = [2, 1]
    for _ in range(m + 2): F.append(F[-1] + F[-2]); L.append(L[-1] + L[-2])
    N = b ** (2 * m) - L[m] * b ** m + (-1) ** m
    per = None
    if N % 2 and N % 5:
        per = 1; x = b % N
        while x != 1: x = x * b % N; per += 1
    return dict(N=N, F_m=F[m], alt_N=b ** (2 * m) + L[m] * b ** m + (-1) ** m, period=per)

def fib_cyclotomic(d, b=10):
    """L2176: primitive part Psi_d = Norm Phi_d(b, phi) of N_m = b^(2m) - L_m b^m + (-1)^m = prod_{d | m} Psi_d.
    b = 10: Psi_1 = 89, Psi_2 = 109, Psi_3 = 11191 = 19^2*31, Psi_4 = 10301 (prime), Psi_6 = 9211 = 61*151.
    For prime d, Psi_d = N_d / 89, so its leading digits are those of 1/89 (e.g. Psi_5 = 112347191)."""
    F = [0, 1]; L = [2, 1]
    for _ in range(d + 2): F.append(F[-1] + F[-2]); L.append(L[-1] + L[-2])
    N = lambda m: b ** (2 * m) - L[m] * b ** m + (-1) ** m
    memo = {}
    def P(e):
        if e in memo: return memo[e]
        v = N(e)
        for f in range(1, e):
            if e % f == 0: v //= P(f)
        memo[e] = v; return v
    return P(d)

def metallic_power_index(a):
    """L2180: largest odd M with beta_a = beta_c^M, i.e. a = V_M(c) (V_0 = 2, V_1 = c, V_{k+1} = c V_k + V_{k-1}).
    a = 4 = L_3 (beta_4 = phi^3), a = 11 = L_5 (phi^5), a = 29 = L_7, a = 36 = V_3(3).  Returns M (1 = primitive)."""
    best = 1
    for c in range(1, a):
        V = [2, c]
        while V[-1] < a: V.append(c * V[-1] + V[-2])
        if V[-1] == a and (len(V) - 1) % 2 == 1 and len(V) - 1 > best: best = len(V) - 1
    return best

def metallic_constant(a, L=100000):
    """L2180: conjectural full-period rate C_a for metallic rungs p = b^2 - a b - 1 in the admissible classes of Theorem 1.1
    (a = 2 mod 4: 0).  C_a = prod_{l odd} (1 - q_l / l), q_l = r(l)/(l - w(l)), r = #roots of x^2 - a x - 2, w = #roots of
    x^2 - a x - 1 mod l; for primes l dividing the power index M (b = beta_c^M is an M-th power mod p) the factor is (1 - q_l).
    a = 1: 0.7179, a = 3: 0.9719, a = 4: 0.5892, a = 11: 0.4353."""
    import math
    if a % 4 == 2: return 0.0
    def nr(D, l):
        D %= l
        if D == 0: return 1
        return 2 if pow(D, (l - 1) // 2, l) == 1 else 0
    M = metallic_power_index(a); bad = set()
    m = M; f = 3
    while m > 1:
        while m % f == 0: bad.add(f); m //= f
        f += 2
    sv = bytearray([1]) * L; sv[0:2] = b"\x00\x00"
    for i in range(2, int(L ** 0.5) + 1):
        if sv[i]: sv[i * i::i] = bytearray(len(sv[i * i::i]))
    lp = 0.0
    for l in range(3, L, 2):
        if not sv[l]: continue
        r = nr(a * a + 8, l)
        if not r: continue
        q = r / (l - nr(a * a + 4, l))
        lp += math.log(1 - q) if l in bad else math.log(1 - q / l)
    return math.exp(lp)

def golden_index_law(l, C=0.71792):
    """L2184: heuristic probability that the index (p-1)/ord_p(b) equals the odd prime l, for golden rungs p = b^2 - b - 1 with
    b = 3 mod 4.  q_l = r(l)/(l - w(l)); for l = 3, 3 | p-1 forces 9 | p-1 (b-2 and b+1 both divisible by 3), so
    P(3 || index) = q*2/9; otherwise P(l || index) = q(1/l - 1/l^3).  P(index = l) = C P(l || index)/(1 - q/l).
    Predictions 0.0598, 0.0766, 0.0299, 0.0147, 0.0085 for l = 3, 5, 7, 11, 13; data (b < 10^6) 0.0617, 0.0758, 0.0294, 0.0157, 0.0087.
    2-adic part: b = 0, 1 mod 4 -> index exactly 2 x odd; b = 2 mod 4 -> b behaves like a random square:
    P(v2(index) = k) = 2^-k (k < v2(p-1)), 2^-(v-1) (k = v)."""
    w = 1 if l == 5 else (2 if pow(5, (l - 1) // 2, l) == 1 else 0)
    r = 1 if l == 3 else 2
    q = r / (l - w)
    pex = q * 2 / 9 if l == 3 else q * (1 / l - 1 / l ** 3)
    return C * pex / (1 - q / l)

def metallic_index_law(a, l, K=5):
    """L2188: heuristic P(index (p-1)/ord_p(b) = l) for admissible metallic rungs p = b^2 - a b - 1, l an odd prime.
    Uses the exact distribution of v = v_l(p-1) given l | p-1 (counting b mod l^K), q_l, the constant C_a and the power index M:
    if l | M (b is an l-th power), P(l || i | v) = 1 (v = 1) or 1 - 1/l (v >= 2) and the base is C_a/(1 - q);
    otherwise P(l || i | v) = 1/l (v = 1) or 1/l - 1/l^2 (v >= 2) and the base is C_a/(1 - q/l).
    Checked (b < 40000): a = 4, i = 3: 0.2946 vs 0.2913;  a = 11, i = 5: 0.4179 vs 0.4137;  a = 7, i = 7: 0.0492 vs 0.0530."""
    m = l ** K; cnt = {}; tot = 0
    for b in range(m):
        if (b * b - a * b - 1) % l == 0: continue
        t = (b * b - a * b - 2) % m
        if t % l: continue
        v = 0
        while v < K and t % l ** (v + 1) == 0: v += 1
        cnt[v] = cnt.get(v, 0) + 1; tot += 1
    if tot == 0: return 0.0
    r = sum(1 for b in range(l) if (b * b - a * b - 2) % l == 0 and (b * b - a * b - 1) % l)
    w = sum(1 for b in range(l) if (b * b - a * b - 1) % l == 0)
    q = r / (l - w); inM = metallic_power_index(a) % l == 0
    pex = sum(c / tot * ((1 if v == 1 else 1 - 1 / l) if inM else (1 / l if v == 1 else 1 / l - 1 / l ** 2)) for v, c in cnt.items())
    C = metallic_constant(a)
    return (C / (1 - q) if inM else C / (1 - q / l)) * q * pex

def novelty_audit():
    """L2192: zbMATH 'Fibonacci primitive root' (11 documents, supplied by the user 2026-10-20) checked against Theorem 1.1
    (quadratic character of the base b at primes b^2 - a b - 1).  Returns list of (reference, read?, overlaps Theorem 1.1?)."""
    return [("Aigner, J. reine angew. Math. 274/275 (1975) 139-140", "read (Zbl 0302.12002 summary, L2200)", "partial: for p = 1 mod 4 golden case equivalent to Aigner/Lehmer; p = 3 mod 4 and all a new"),
            ("Kiss-Phong, Fib. Quart. 15 (1977) 347-349", "read", "no: rank of apparition"),
            ("De Leon, Fib. Quart. 15 (1977) 353-355", "read", "no: FPR <=> period p-1 (cited at Prop. 4.1)"),
            ("Mays, Fib. Quart. 20 (1982) 111", "read", "no"),
            ("Mollin, Fib. Quart. 26 (1988) 46-53", "read", "no: x^2 = x + n, p = 2q+1"),
            ("Sander, Fib. Quart. 28 (1990) 79-80", "read (via OEIS)", "no: density"),
            ("Phong, Fib. Quart. 29 (1991) 66-71", "read", "no: counts by p mod 4/8"),
            ("Brison, Fib. Quart. 30 (1992) 295-304", "read", "no: complete sequences, counts by p mod 4"),
            ("Li, Fib. Quart. 37 (1999) 77-84", "read", "no: Wall's question"),
            ("Li, Fib. Quart. 38 (2000) 244-249", "read", "no: generalized x^2 - a x - b, counts by p mod 4"),
            ("Hsia-Li-Sun, Finite Fields Appl. 92 (2023)", "read", "no: uses FPRs for codes")]

def arxiv_checklist():
    """L2196: submission checklist for the rung note (rungs.tex).  Returns list of (item, status)."""
    return [("proofs of Lemma G, Theorem 1.1, Corollary 1.2, Prop. 4.1 re-read line by line", "done (L2196)"),
            ("abstract <= 1920 characters, plain text", "done: arxiv_abstract.txt"),
            ("MSC 11A07, 11B39, 11A15; primary category math.NT", "done"),
            ("ancillary code under anc/", "done"),
            ("AI-assistance acknowledgement", "done"),
            ("Aigner 1975 (J. reine angew. Math. 274/275, 139-140) read and compared", "done (L2200): consistent on 2002 + 1322 rungs"),
            ("arXiv endorsement for a first math.NT submission", "OPEN - author action")]

def aigner_cubic(b):
    """L2200: for a golden rung p = b^2 - b - 1 with 3 | p-1, return (b is a cubic residue, p = x^2 + 135 y^2).  Aigner (1975):
    eps = (1+sqrt5)/2 is a cube mod primes x^2 + 135 y^2 and not mod x^2 + 15 u^2 with 3 \u2224 u; since b = eps or -1/eps and -1 is a
    cube, the two agree (1322/1322 rungs, b < 20000)."""
    import math
    p = b * b - b - 1
    if (p - 1) % 3: return None
    cube = pow(b, (p - 1) // 3, p) == 1
    f135 = any(math.isqrt(p - 135 * y * y) ** 2 == p - 135 * y * y for y in range(0, math.isqrt(p // 135) + 1))
    return cube, f135

def metallic_cubic_check(a, N=20000):
    """L2204: 'metallic Aigner'.  For primes p = 1 mod 3 with ((a^2+4)/p) = 1 and p = x^2 + 27 d y^2 (d = squarefree part of a^2+4),
    count how often beta_a = (a + sqrt(a^2+4))/2 is a cubic residue mod p (expected: always; a special case of Evans-Van Veen,
    arXiv:2511.12513).  Returns (cubes, primes tested)."""
    import math
    D = a * a + 4; d = 1; m = D; f = 2
    while f * f <= m:
        e = 0
        while m % f == 0: m //= f; e += 1
        if e % 2: d *= f
        f += 1
    d *= m if m > 1 else 1
    def isp(n):
        if n < 2: return False
        i = 2
        while i * i <= n:
            if n % i == 0: return False
            i += 1
        return True
    def sq(n, p):
        for x in range(p):
            if x * x % p == n % p: return x
    k = n = 0
    for p in range(7, N, 6):
        if not isp(p) or D % p == 0 or pow(D % p, (p - 1) // 2, p) != 1: continue
        if not any(math.isqrt(p - 27 * d * y * y) ** 2 == p - 27 * d * y * y for y in range(math.isqrt(p // (27 * d)) + 1)): continue
        beta = (a + sq(D, p)) * pow(2, -1, p) % p
        n += 1; k += pow(beta, (p - 1) // 3, p) == 1
    return k, n

def metallic_chain(b, gen):
    """L2208: metallic-mean chain word (Thiem-Schreiber inflation w -> s, s -> s w s^(b-1)), its length and strong-bond frequency.
    The limiting frequency is nu = beta/(beta+1); by the gap-labelling theorem the spectral gaps of the tight-binding chain sit at
    integrated density of states {k nu} mod 1 (checked numerically: 24/24 largest gaps for b = 1, 2, 3)."""
    w = "s"
    for _ in range(gen): w = "".join("s" if c == "w" else "s" + "w" + "s" * (b - 1) for c in w)
    return dict(N=len(w), strong=w.count("s"), weak=w.count("w"), nu=w.count("s") / len(w))

def hydrogen_line_ratio(m1, n1, m2, n2):
    """L2208: ratio of two hydrogen (Rydberg, non-relativistic) line wavenumbers (1/m1^2 - 1/n1^2)/(1/m2^2 - 1/n2^2) as an exact
    Fraction.  Always rational, hence never equal to an irrational metallic mean such as phi."""
    from fractions import Fraction
    return (Fraction(1, m1 * m1) - Fraction(1, n1 * n1)) / (Fraction(1, m2 * m2) - Fraction(1, n2 * n2))

def periodic_table_rungs():
    """L2208: atomic numbers that coincide with our stair denominators (base-10 coincidences only; atomic number counts protons and
    has no relation to base-10 decimal periods)."""
    return {59: "Pr praseodymium (2/59: golden stair in steps of 3)", 69: "Tm thulium (1/69: bronze stair)",
            79: "Au gold (1/79: silver/Pell stair)", 89: "Ac actinium (1/89: golden stair)",
            109: "Mt meitnerium (1/109: golden reverse stair)", 119: "element 119 (1/119: silver reverse stair; not yet synthesized)"}

def e8_masses():
    """L2212: Zamolodchikov's E8 masses (m1 = 1): 2cos(pi/5), 2cos(pi/30), 4cos(pi/5)cos(7pi/30), 4cos(pi/5)cos(2pi/15),
    4cos(pi/5)cos(pi/30), 8cos^2(pi/5)cos(7pi/30), 8cos^2(pi/5)cos(2pi/15).  They are the Perron-Frobenius eigenvector of the E8
    Dynkin diagram (eigenvalue 2cos(pi/30)) and come in four golden pairs m2/m1 = m6/m3 = m7/m4 = m8/m5 = phi."""
    import math
    c = math.cos; P = math.pi
    return [1.0, 2*c(P/5), 2*c(P/30), 4*c(P/5)*c(7*P/30), 4*c(P/5)*c(2*P/15), 4*c(P/5)*c(P/30),
            8*c(P/5)**2*c(7*P/30), 8*c(P/5)**2*c(2*P/15)]

def e8_rung(b=10):
    """L2212: minimal polynomial of 2cos(pi/30), x^8 - 7x^6 + 14x^4 - 8x^2 + 1, evaluated at b.  For b = 10: 93139201, a prime with
    p = 1 mod 60 and ord_p(10) = 363825 = (p-1)/256.  Compare x^2 - x - 1 (min. poly of 2cos(pi/5)) at 10 = 89."""
    return b**8 - 7*b**6 + 14*b**4 - 8*b**2 + 1

def chi_base_pm1(b, p, eps):
    """L2216: general form of Lemma G.  For an odd prime p = eps (mod b), eps = +-1, b = 2^e c (c odd):
    (b/p) = (2/p)^e * (-1)^(((c-1)/2)((p-1)/2)) * (eps/c).  Hence for any integer polynomial f with f(0) = +-1, the quadratic
    character of b at primes p = f(b) depends only on b (mod 2^(e+2)) and f(b) (mod 8).  Checked on 16768 primes."""
    e = 0; c = b
    while c % 2 == 0: c //= 2; e += 1
    two = 1 if p % 8 in (1, 7) else -1
    s_ = (-1) ** (((c - 1) // 2) * ((p - 1) // 2))
    if eps == -1: s_ *= (-1) ** ((c - 1) // 2)
    return two ** e * s_

def cosine_rung(n, b=10):
    """L2216: psi_n(b), the minimal polynomial of 2cos(2pi/n) evaluated at b = prod over k < n/2, gcd(k,n) = 1 of (b - 2cos(2pi k/n)).
    psi_10(10) = 89, psi_5(10) = 109, psi_60(10) = 93139201; U_{n-1}(5) = prod_{d | 2n, d >= 3} psi_d(10) (e.g. 9701 = 109 * 89).
    Uses mpmath when available (exact rounding for values < 10^40)."""
    from math import gcd
    try:
        import mpmath as _m; _m.mp.dps = 60; cs = lambda t: _m.cos(t); pi_ = _m.pi; one = _m.mpf(1)
    except ImportError:
        import math as _m; cs = _m.cos; pi_ = _m.pi; one = 1.0
    v = one
    for k in range(1, (n + 1) // 2 if n > 2 else 2):
        if gcd(k, n) == 1 and 2 * k < n: v *= b - 2 * cs(2 * pi_ * k / n)
    return int(round(float(v))) if abs(v) < 1e15 else int(_m.nint(v))

def psi_poly(n):
    """L2220: exact integer coefficients (constant term first) of psi_n, the minimal polynomial of 2cos(2 pi/n), n >= 3.
    Pure Python: Phi_n by division, then Phi_n(z)/z^m = a_m + sum_k a_{m-k} (z^k + z^-k) with z^k + z^-k = V_k(x)."""
    def mul(a, b):
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b): r[i + j] += x * y
        return r
    def div(a, b):                     # exact division of integer polys, b monic
        a = a[:]; q = [0] * (len(a) - len(b) + 1)
        for i in range(len(q) - 1, -1, -1):
            q[i] = a[i + len(b) - 1]
            for j, y in enumerate(b): a[i + j] -= q[i] * y
        return q
    def cyclo(m, memo={}):
        if m in memo: return memo[m]
        P = [-1] + [0] * (m - 1) + [1]
        for d in range(1, m):
            if m % d == 0: P = div(P, cyclo(d))
        memo[m] = P; return P
    a = cyclo(n); m = (len(a) - 1) // 2
    V = [[2], [0, 1]]
    for k in range(2, m + 1):
        xv = [0] + V[-1]; prev = V[-2] + [0] * (len(xv) - len(V[-2]))
        V.append([x - y for x, y in zip(xv, prev)])
    psi = [0] * (m + 1); psi[0] += a[m]
    for k in range(1, m + 1):
        for i, c in enumerate(V[k]): psi[i] += a[m - k] * c
    return psi

def cosine_full_period_classes(n):
    """L2220: residues b (mod 16) for which b is a quadratic NON-residue modulo primes p = psi_n(b) (so a full period of 1/p in base b
    is possible), by the general principle (chi_base_pm1); requires psi_n(0) = +-1.  Empty list = 'never full' family
    (e.g. n = 14, 23, 24, 30).  Observed: for prime n = q >= 5, 'never' iff q = +-1 (mod 24) (checked q < 260)."""
    f = psi_poly(n); eps = f[0]
    if eps not in (1, -1): return None
    ev = lambda t: sum(c * t ** i for i, c in enumerate(f))
    out = []
    for r in range(16):
        if r % 8 == 0: continue
        p8 = ev(r) % 8
        if p8 % 2 == 0: continue
        if chi_base_pm1(r if r > 1 else 17, p8 + 8000, eps) == -1: out.append(r)   # only b's 2-adic data and p mod 8 matter
    return out

# ---------------------------------------------------------------- digital space occupancy (DSO), L2224
def _tobase(n, b):
    d = []
    while n: d.append(n % b); n //= b
    return d or [0]

def dso(n, base=10):
    """L2224: Digital Space Occupancy D_b(n) = number of digits used to write 1, 2, ..., n in base b (Gary's 'digital slots').
    Exact closed form: D_b(n) = d (n + 1) - (b^d - 1)/(b - 1), d = number of base-b digits of n.  D(10) = 11, D(49) = 89,
    D(108) = 216, D(2701) = 9697."""
    if n < 1: return 0
    d = 1
    while base ** d <= n: d += 1
    return d * (n + 1) - (base ** d - 1) // (base - 1)

def dso_breakdown(n, base=10):
    """L2224: rows (digits k, first, last, count, slots) of D_b(n), as in Gary's Digital Slots Calculator."""
    rows = []; k = 1
    while base ** (k - 1) <= n:
        lo = 1 if k == 1 else base ** (k - 1); hi = min(n, base ** k - 1); cnt = hi - lo + 1
        rows.append(dict(digits=k, first=lo, last=hi, count=cnt, slots=k * cnt)); k += 1
    return rows

def dso_inverse(D, base=10):
    """L2224: the n with D_b(n) = D, or None if D is skipped (inside the k-digit block D grows in steps of k)."""
    if D < 1: return None
    lo, hi = 1, max(2, D)
    while lo < hi:
        mid = (lo + hi) // 2
        if dso(mid, base) < D: lo = mid + 1
        else: hi = mid
    return lo if dso(lo, base) == D else None

def dso_connections(n, base=10):
    """L2224: verified facts about n and D = D(n) (computed here, never taken on trust).  Physical/periodic-table matches are flagged
    as base-10 coincidences."""
    import math
    D = dso(n, base); out = []
    def isprime_(m):
        if m < 2: return False
        i = 2
        while i * i <= m:
            if m % i == 0: return False
            i += 1
        return True
    def perfect_power(m):
        for k in range(2, int(math.log2(m)) + 1 if m > 1 else 2):
            r = round(m ** (1 / k))
            for t in (r - 1, r, r + 1):
                if t > 1 and t ** k == m: return t, k
        return None
    fib = [0, 1]
    while fib[-1] < 10 * D + 10: fib.append(fib[-1] + fib[-2])
    out.append("D(%d) = %d  (closed form d(n+1) - (b^d - 1)/(b - 1); approximation n log_b n - n/ln b = %.2f)" % (n, D, n * math.log(n, base) - n / math.log(base) if n > 1 else 0))
    if n > 1:
        L_ = math.log(n, base); u_ = L_ - math.floor(L_ + 1e-12)
        out.append("exact log form: D = n log n + n*g(u) + d + 1/(b-1) with u = %.4f, g(u) = %+.4f (wobble range -0.111..+0.158 in base 10)" % (u_, 1 - u_ - base ** (1 - u_) / (base - 1)))
    k_ = len(str(n)) if base == 10 else None
    if k_ and math.gcd(k_, (10 ** k_ - 1) // 9) > 1: out.append("every %d-digit n has D(n) divisible by %d, so D is never prime in this block" % (k_, math.gcd(k_, (10 ** k_ - 1) // 9)))
    if isprime_(D): out.append("D is prime")
    pp = perfect_power(D)
    if pp: out.append("D = %d^%d" % pp)
    if D in fib: out.append("D is a Fibonacci number (F_%d)" % fib.index(D))
    rungs = {89: "golden rung 10^2-10-1 (1/89 Fibonacci stair)", 109: "reverse golden rung 10^2+10-1", 79: "silver rung 10^2-2*10-1 (1/79 Pell stair)",
             69: "bronze rung 10^2-3*10-1", 59: "golden stair in steps of 3 (2/59)", 9701: "89*109, stride-2 stair", 971: "cosine rung psi_9(10)",
             97: "cosine rung psi_12(10)", 9601: "cosine rung psi_24(10)", 93139201: "E8 rung psi_60(10)"}
    if D in rungs: out.append("D equals the %s" % rungs[D])
    for m, lab in ((n, "n"), (D, "D")):
        if base == 10 and math.gcd(m, 10) == 1 and m > 1:
            L = 1; x = 10 % m
            while x != 1: x = x * 10 % m; L += 1
            out.append("1/%s = 1/%d has decimal period %d%s" % (lab, m, L, " (full, m prime)" if isprime_(m) and L == m - 1 else ""))
    elems = {47: "silver (Ag)", 79: "gold (Au)", 29: "copper (Cu)", 50: "tin (Sn)", 78: "platinum (Pt)", 89: "actinium (Ac)", 109: "meitnerium (Mt)"}
    for m, lab in ((n, "n"), (D, "D")):
        if m in elems: out.append("%s = %d is the atomic number of %s (base-10 coincidence, no physical mechanism)" % (lab, m, elems[m]))
    return out

def menu_dso():
    say("Digital Space Occupancy: D(n) = digits used to write 1..n (Gary's digital slots).")
    n = int(ask("n", 108)); b = int(ask("base", 10))
    for r in dso_breakdown(n, b):
        say("  %d-digit numbers %d..%d: %d numbers x %d = %d slots" % (r["digits"], r["first"], r["last"], r["count"], r["digits"], r["slots"]))
    for line in dso_connections(n, b): say("  " + line)
    D = ask("inverse: which n has D(n) = ? (blank to skip)", "")
    if D: m = dso_inverse(int(D), b); say("  D(n) = %s: %s" % (D, "n = %d" % m if m else "no n (value skipped)"))
    log_check("dso", dict(n=n, base=b), dict(D=dso(n, b)))

def dso_log_form(n, base=10):
    """L2228: exact logarithmic form of the DSO.  With u = frac(log_b n) and d = number of digits,
    D_b(n) = n log_b n + n g(u) + d + 1/(b-1),   g(u) = 1 - u - b^(1-u)/(b-1).
    g oscillates in [-1/(b-1), max] (base 10: -0.111 .. +0.158), so D(n) = n log10 n + O(n) with a periodic 'wobble';
    the constant -1/ln 10 = -0.434 in the older approximation lies outside that range."""
    import math
    L = math.log(n, base); d = int(math.floor(L + 1e-12)) + 1; u = L - (d - 1)
    return n * L + n * (1 - u - base ** (1 - u) / (base - 1)) + d + 1 / (base - 1)

def dso_prime_lengths(kmax=40):
    """L2228: digit lengths k for which D(n) (n with k digits) can be prime.  In the k-digit block D = k(n+1) - R_k, so every D is
    = -R_k (mod k) and shares the factor gcd(k, R_k), R_k = (10^k - 1)/9.  Blocked: gcd(k, R_k) > 1 (k = 3, 6, 9, 12, 15, 18, 21, 22, ...).
    Returns (allowed, blocked)."""
    import math
    al, bl = [], []
    for k in range(1, kmax + 1):
        (bl if math.gcd(k, (10 ** k - 1) // 9) > 1 else al).append(k)
    return al, bl

def dso_stair(m=3, ndigits=1200, base=10):
    """L2232: the DSO stair constant kappa = sum_{n>=1} D(n) base^(-m(n+1)) = y F(y), y = base^-m, F(x) = sum_n D(n) x^n
    = (1 - x)^-2 sum_{k>=0} x^(base^k)  (Mahler type: F(x^b)(1-x^b)^2 = F(x)(1-x)^2 - x).  By Mahler (Math. Ann. 101, 1929)
    sum x^(b^k) is transcendental at algebraic 0 < x < 1, so kappa is TRANSCENDENTAL (unlike the rational Fibonacci stairs).
    For m = 3 the 3-digit blocks show D(1..367) exactly; D(369) = 999 and D(370) = 1002 trigger the first carries.
    Returns the decimal digits after the point (exact integer arithmetic)."""
    N = ndigits // m + 3; scale = base ** (m * (N + 2))
    tot = 0
    for n in range(1, N + 1): tot += dso(n, base) * scale // base ** (m * (n + 1))
    # tail bound: remaining terms are < (D(N+1)+...)/base^(m(N+2)), below the shown precision
    s_ = str(tot).zfill(m * (N + 2))
    return s_[:ndigits]

def cosine_family_law(n):
    """L2236: predicted answer to 'can 1/psi_n(b) ever have full period in base b?' (n >= 5, n != 6, psi_n(0) = +-1).
    Possible  <=>  n = q^k with (2/q), (3/q) not both +1;  or n = 2 q^k with (2/q) = -1;  or n = 3 q^k (q > 3) with (3/q) = -1;
    (q = 3 counts as 'not both +1').  Every other n: never (b is always a square mod p).
    PROVED in full (L2244): the listed shapes by finite checks mod 48; every other n via Gauss's lemma in transfer form
    (psi_n(0) = 1, psi_n(-1) = 1, psi_n(1) = (-1)^(phi(n)/2) for odd n), Apostol's resultants and the reductions
    psi_2n(x) = +-psi_n(-x), psi_n = psi_{n/2}(x^2 - 2) (4 | n), psi_n = psi_{n/3} o V_3 (9 | n), psi_m o V_3 = psi_m psi_3m."""
    def fac(m):
        f = {}; p_ = 2
        while p_ * p_ <= m:
            while m % p_ == 0: f[p_] = f.get(p_, 0) + 1; m //= p_
            p_ += 1
        if m > 1: f[m] = f.get(m, 0) + 1
        return f
    def leg(a, q): return 1 if pow(a, (q - 1) // 2, q) == 1 else -1
    f = fac(n); odd = sorted(p_ for p_ in f if p_ > 2)
    if len(odd) == 1 and set(f) == set(odd):
        q = odd[0]; return q == 3 or not (leg(2, q) == 1 and leg(3, q) == 1)
    if len(odd) == 1 and set(f) == {2, odd[0]} and f[2] == 1:
        q = odd[0]; return q == 3 or leg(2, q) == -1
    if len(odd) == 2 and 3 in odd and f[3] == 1 and 2 not in f:
        return leg(3, odd[1]) == -1
    return False

def totative_parity(n):
    """L2240: (N4, N3) = numbers of k with gcd(k, n) = 1 in (0, n/4) and (0, n/3).  For 'other' n (not q^k, 2q^k, 3q^k, 4q^k, 6q^k)
    the cosine family psi_n is blocked iff both are even (signs of psi_n(0) and psi_n(-1); Apostol's resultants give |.| = 1)."""
    from math import gcd
    N4 = sum(1 for k in range(1, n) if 4 * k < n and gcd(k, n) == 1)
    N3 = sum(1 for k in range(1, n) if 3 * k < n and gcd(k, n) == 1)
    return N4, N3

def transfer_sign(a, N):
    """L2244: Gauss's lemma in transfer form.  For G = (Z/N)^*, T = units in (0, N/2), mu = #{t in T : a t mod N > N/2};
    returns ((-1)^mu, a^(phi(N)/2) mod N mapped to +-1).  They always agree; for non-cyclic G both are +1."""
    from math import gcd
    T = [t for t in range(1, N) if 2 * t < N and gcd(t, N) == 1]
    mu = sum(1 for t in T if 2 * ((a * t) % N) > N)
    phi = sum(1 for t in range(1, N) if gcd(t, N) == 1)
    v = pow(a, phi // 2, N)
    return (-1) ** mu, (1 if v == 1 else (-1 if v == N - 1 else None))

# ---------------------------------------------------------------- engineering uses of full-period primes (L2248)
def costas_welch(p, g):
    """L2248: Welch-Costas array of order p-1 from a primitive root g mod p (row i -> column g^i mod p).  Costas arrays have a
    'thumbtack' ambiguity function and are used in sonar/radar frequency hopping.  Rung primes give the generator for free:
    p = b^2 - b - 1 with b primitive (b = 3 mod 4 by Theorem 1.1), e.g. p = 109, g = 11 (order 108)."""
    return [pow(g, i, p) for i in range(1, p)]

def is_costas(perm):
    """L2248: True iff all displacement vectors (j - i, perm[j] - perm[i]) are distinct."""
    seen = set()
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            v = (j - i, perm[j] - perm[i])
            if v in seen: return False
            seen.add(v)
    return True

def legendre_code(p):
    """L2248: +-1 quadratic-residue (Legendre) sequence of length p (first entry +1).  For p = 3 mod 4 (e.g. golden rungs with
    b = 0, 1 mod 4, Corollary 1.2) it has two-level periodic autocorrelation (p, -1) and a perfectly flat spectrum |S(k)|^2 = p + 1:
    a candidate code for coded exposure / coded strobe illumination."""
    return [1] + [1 if pow(k, (p - 1) // 2, p) == 1 else -1 for k in range(1, p)]

def pr_interleave(data, p, g):
    """L2248: primitive-root interleaver for archives: symbol at position g^i - 1 is stored i-th.  A burst of consecutive storage
    errors is scattered over the whole block (p = 109, g = 11: a 12-symbol burst lands 2..20 apart).  Returns (stored, order)."""
    order = [pow(g, i, p) - 1 for i in range(p - 1)]
    return [data[o] for o in order], order

def pr_deinterleave(stored, order):
    out = [None] * len(order)
    for i, o in enumerate(order): out[o] = stored[i]
    return out

def rung_generators(bmax=5000):
    """L2248: (p, b) with p = b^2 - b - 1 prime and b a primitive root, searched only in the class b = 3 mod 4 allowed by Theorem 1.1
    (saves 75% of the order computations; about 71% of the remaining candidates succeed)."""
    out = []
    for b in range(7, bmax, 4):
        p = b * b - b - 1
        d = rung_period(b, -1)
        if d.get("prime") and d["full"]: out.append((p, b))
    return out

def coded_strobe_times(fps=60.0, p=109, g=11, nframes=None):   # L2264: p = 701, g = 27 is the recommended 21 kHz design
    """L2256: strobe/sample times for a 'coded strobe' camera: in frame k the flash fires at sub-frame slot g^(k+1) mod p (a Welch-Costas
    permutation of the p-1 slots).  With one sample per frame, a tone up to (p-1)*fps/2 (3240 Hz for 60 fps, p = 109) is identified
    uniquely by a Fourier scan (toy test: 1234 Hz and 2987 Hz recovered exactly; uniform sampling gives 52-105 alias groups).
    Above that limit it aliases on the slot grid, exactly like the rolling-shutter trick.  Toy model only, not a tested device."""
    n = nframes or (p - 1)
    return [k / fps + ((pow(g, k + 1, p) - 1) % (p - 1)) / ((p - 1) * fps) for k in range(n)]

# ---------------------------------------------------------------- applied golden-ratio tools (L2260)
def fib_code_encode(values):
    """L2260: Fibonacci (Zeckendorf) universal code: each positive integer -> Zeckendorf bits (LSB first) + '1'; '11' ends a word.
    Self-synchronising: a flipped bit damages only the words around it (200-value test: 198 still correct).  Words contain no
    other '11', the (1,inf) run-length constraint of magnetic recording, whose capacity is log2(phi) = 0.694 bits/symbol."""
    F = [1, 2]
    while F[-1] <= max(values): F.append(F[-1] + F[-2])
    out = []
    for n in values:
        bits = [0] * len(F); i = len(F) - 1
        while n:
            while F[i] > n: i -= 1
            bits[i] = 1; n -= F[i]
        while bits and bits[-1] == 0: bits.pop()
        out.append("".join(map(str, bits)) + "1")
    return "".join(out)

def fib_code_decode(stream):
    """L2260: inverse of fib_code_encode (resynchronises after errors at the next '11')."""
    F = [1, 2]; out = []; cur = ""
    for ch in stream:
        cur += ch
        if cur.endswith("11"):
            z = cur[:-1]
            while len(F) < len(z): F.append(F[-1] + F[-2])
            out.append(sum(F[j] for j, c in enumerate(z) if c == "1")); cur = ""
    return out

def fibonacci_lattice(k):
    """L2260: 2D Fibonacci lattice rule with N = F_k points (i/N, {i F_(k-1)/N}) -- the classical optimal 2D rank-1 lattice
    (Zaremba/Korobov).  Non-periodic smooth test: error 5e-4 at N = 1597 vs 1.3e-2 for Monte Carlo; periodic smooth: machine zero."""
    F = [0, 1]
    while len(F) <= k: F.append(F[-1] + F[-2])
    N, g = F[k], F[k - 1]
    return [(i / N, (i * g % N) / N) for i in range(N)]

def golden_strobe_times(nframes=300, fps=60.0):
    """L2260/L2264: off-grid strobe times k/fps + {k phi}/fps.  CORRECTED in L2264: golden (or sqrt 2) jitter leaves near-equal
    mirror ghosts from Diophantine near-aliases; on 30 random tones (0.5-19.5 kHz, 300 frames x 2 codes) only 12/30 were identified.
    Use coded_strobe_times(p=701, g=27) instead: 30/30 tones up to 19.5 kHz with 700 frames (competitor <= 0.23)."""
    ph = (1 + 5 ** 0.5) / 2
    return [k / fps + ((k * ph) % 1) / fps for k in range(nframes)]

def korobov_P2(N, z):
    """L2264: figure of merit P_2 of the rank-1 lattice rule {k z / N} (smaller is better):
    P_2 = -1 + (1/N) sum_k prod_j (1 + 2 pi^2 B2({k z_j/N})),  B2(x) = x^2 - x + 1/6."""
    import math
    tot = 0.0
    for k in range(N):
        pr = 1.0
        for zj in z:
            x = (k * zj % N) / N; pr *= 1 + 2 * math.pi ** 2 * (x * x - x + 1 / 6)
        tot += pr
    return tot / N - 1

def rung_korobov_warning(p, b):
    """L2264 (negative result): a Korobov multiplier a with a^2 = a + 1 (mod N) -- e.g. the base b of a rung prime p = b^2 - b - 1 --
    makes z_3 = z_1 + z_2, so the dual lattice contains (1, 1, -1) and the rule fails in every dimension s >= 3 (P_2 about 2.04,
    worst of all multipliers).  In 2D the continued fraction b/p = [0; b-1, 1, ...] has a large partial quotient, so it is also poor
    (bottom 10%).  The same happens for the Fibonacci lattice in s >= 3 (F_(k-1)^2 = +-1 mod F_k).  Returns True if a^2 = a + 1."""
    return (b * b - b - 1) % p == 0

def hybrid_interleave(n_cw=255, cw_len=16, P=257, g=3, Q=17, h=5):
    """L2268 hybrid archive layout (n_cw codewords of cw_len bytes, byte j of every codeword in one group).
    Groups are written in primitive-root order j_s = g^(s+1) mod P - 1 (P prime, n_cw = P-2 or less used),
    and inside each group the codeword index is rotated by c_s = h^(s+1) mod Q - 1 (Q = cw_len + 1 prime).
    Returns the storage order: position k holds codeword-byte (c*n_cw + j).  Block-style burst protection,
    no periodic blind spots for periods 17..64 in the RS(255,223) x 16 test (L2268)."""
    gp = [x - 1 for x in (pow(g, i, P) for i in range(1, P)) if x - 1 < n_cw]
    cj = [pow(h, s + 1, Q) - 1 for s in range(n_cw)]
    order = []
    for s in range(n_cw):
        j = gp[s]
        for r in range(cw_len):
            order.append(((r + cj[s]) % cw_len) * n_cw + j)
    return order

def hybrid_deinterleave(stored, order):
    """Inverse of hybrid_interleave: stored[k] is item order[k]."""
    out = [None] * len(order)
    for k, src in enumerate(order):
        out[src] = stored[k]
    return out

def coded_strobe_grid(p=701, g=27, fps=60.0):
    """L2268: the Costas strobe times are integer ticks of a fine clock fps*(p-1) Hz (42 kHz for p = 701, 60 fps):
    tick_n = (p-1)*n + slot_n.  So the non-uniform spectrum is an ordinary FFT of a sparse array of length (p-1)^2,
    which makes multi-tone recovery (CLEAN) fast.  Returns (ticks, fine_clock_Hz)."""
    slots = costas_welch(p, g)
    return [(p - 1) * n + (s - 1) for n, s in enumerate(slots)], fps * (p - 1)

def helical_interleave(m, n, u=1, rot=None):
    """L2272 helical layout (Berlekamp-Tong 1985 type): m codewords of n symbols; stored group s = symbol s of every
    codeword, slot r holding codeword (r + c_s) mod m with c_s = u*s (or c_s = rot[s mod len(rot)]).
    Returns the storage order as item indices c*n + s."""
    out = []
    for s_ in range(n):
        c_s = (u * s_) if rot is None else rot[s_ % len(rot)]
        for r in range(m):
            out.append(((r + c_s) % m) * n + s_)
    return out

def interleave_audit(order, m, n, t):
    """L2272: exact worst case of a layout of m codewords x n symbols, each correcting t errors.
    Returns (max_burst, unforced_failing_periods): the longest contiguous burst always corrected, and the periods d
    (every d-th symbol, any start) that defeat the layout although ceil(mn/d) <= m*t (so a perfect layout would survive).
    The optimum is max_burst = m*t and no unforced periods (pigeonhole)."""
    N = len(order); cw = [x // n for x in order]
    best = 0; B = 1
    while B <= min(N, m * t):
        cnt = [0] * m
        for x in cw[:B]: cnt[x] += 1
        worst = max(cnt)
        for i in range(B, N):
            cnt[cw[i]] += 1; cnt[cw[i - B]] -= 1
            if cnt[cw[i]] > worst: worst = cnt[cw[i]]
        if worst > t: break
        best = B; B += 1
    bad = []
    for d in range(2, N + 1):
        if -(-N // d) > m * t: continue
        for o in range(d):
            cnt = [0] * m
            for k in range(o, N, d): cnt[cw[k]] += 1
            if max(cnt) > t: bad.append(d); break
    return best, bad

def helical_optimal_predict(m, n, t):
    """L2272 Conjecture H (verified for all tested cases): a helical layout with c_s a period-m permutation (e.g. u
    coprime to m) is optimal iff m is a prime power, m | t and n <= m*t.  Proved parts: bursts optimal iff
    c_(s+t) = c_s (Theorem B); n > m*t fails at period m^2 (Theorem N)."""
    def pp(x):
        q = next(p for p in range(2, x + 1) if x % p == 0)
        while x % q == 0: x //= q
        return x == 1
    return m >= 2 and pp(m) and t % m == 0 and n <= m * t

def digit_sum_rotation(m, t):
    """L2276: rotation c_s = (base-m digit sum of s) mod m, s = 0..t-1.  For m = 2 this is the Thue-Morse word.
    Used with helical_interleave(m, n, rot=...): the codeword at position k is the base-m digit sum of (k mod m t), mod m."""
    out = []
    for s_ in range(t):
        x, ds = s_, 0
        while x: ds += x % m; x //= m
        out.append(ds % m)
    return out

def interleave_obstruction(m, t):
    """L2276 universal obstruction [proved]: if some divisor g of m*t has 2 < g <= t and g does not divide t, then NO
    layout of m codewords (t-error-correcting) is perfect at length n = g*t.  Returns the list of such g."""
    M = m * t
    return [g for g in range(3, t + 1) if M % g == 0 and t % g]

def interleave_balanced(f, m, t):
    """L2276 balance criterion [proved sufficient]: f = one period (length m t) of codeword labels.  If every g | t has each
    class mod g holding exactly t/g of each codeword, every g | mt with g > t has distinct codewords in each class, and there
    is no obstruction divisor, then the periodic layout is perfect (bursts and every period) for every n <= t^2."""
    M = m * t
    if len(f) != M or interleave_obstruction(m, t): return False
    for g in range(2, M + 1):
        if M % g: continue
        for o in range(g):
            cnt = [0] * m
            for k in range(o, M, g): cnt[f[k]] += 1
            if g <= t and any(c != t // g for c in cnt): return False
            if g > t and max(cnt) > 1: return False
    return True

RS255_PERFECT_PERIODS = {
    # L2280: one period (length 16*m) of codeword labels; perfect for RS(255,223) (t = 16) at n = 255 exactly.
    # Found by exact CP-SAT search (Lemma P reduction), audited independently.  Depth 3 has NO grouped perfect layout.
    3: "110121110121111202221202221202002010002010002021",
    5: "40321412032304143201032142043102134021343410203124143203104212430123404021314320",   # grouped
}

def balanced_layout(m, t):
    """L2280 construction: m = p^a (prime power), t = p^b * w with b >= a, w < p, gcd(w, p) = 1 (= no obstruction, m | t).
    Rotation c_s = S_m(s mod p^b) + (s mod w) (mod m); returns one grouped period (length m t).
    Proved balanced (hence perfect for every n <= t^2) for m prime; verified for all tested m = p^2."""
    p = next(q for q in range(2, m + 1) if m % q == 0)
    pb = 1
    while t % (pb * p) == 0: pb *= p
    w = t // pb
    if w >= p or pb < m: raise ValueError("obstructed or m does not divide t")
    rot = digit_sum_rotation(m, pb)
    return [((r + rot[s_ % pb] + (s_ % w)) % m) for s_ in range(t) for r in range(m)]

def layout_from_period(f, m, n):
    """Turn a period of codeword labels into a storage order (item c*n + j = symbol j of codeword c)."""
    seen = [0] * m; out = []
    for k in range(m * n):
        c = f[k % len(f)]; out.append(c * n + seen[c]); seen[c] += 1
    if seen != [n] * m: raise ValueError("period does not give n symbols per codeword at this n")
    return out

def staircase_layout(m, t):
    """L2284 staircase layout (Paper C, Theorem 8): one period (length m t) of f(k) = (k + floor(k/t)) mod m.
    Proved perfect for every 2t < n <= t^2 when m = p^a, t = p^b w (b >= a, w < p, gcd(w,p) = 1); with the obstruction
    theorem this classifies perfect interleavers for m | t.  For t = m it is the Berlekamp-Tong helical layout."""
    return [(k + k // t) % m for k in range(m * t)]

def perfect_interleave_status(m, t, n):
    """L2284 summary of the theory: returns a short verdict for m codewords x n symbols, t-error-correcting."""
    if n > t * t: return "impossible: n > t^2 (Lemma P ceiling)"
    ob = interleave_obstruction(m, t)
    if t % m == 0 and not ob: return "perfect: staircase_layout(m, t) works for every n <= t^2 (proved)"
    if m % t == 0 and interleave_condition_C(m, t): return "perfect: transposed_staircase(m, t) works for every n <= t^2 (proved, L2300)"
    if ob and n in [g * t for g in ob]: return "impossible at this n: obstruction g = %d" % (n // t)
    d_ = averaging_obstruction(m, t, n)
    if d_: return "impossible at this n: averaging obstruction, period %d" % d_
    if (m, t, n) in [(k_, 16, 255) for k_ in range(1, 9)]: return "perfect: exact CP-SAT layout exists (L2280/L2288)"
    return "undecided by theory: use an exact search at this n (e.g. CP-SAT, see L2280)"

def averaging_obstruction(m, t, n):
    """L2288/L2292 averaging obstruction [proved; sound on all 48 CP-SAT grid cases, exact on 29 after the L2292 sharpening]: returns a period d that makes
    a perfect layout of m codewords x n symbols (t-error-correcting) impossible, or None if this test is inconclusive.
    Some codeword holds >= ceil(t/g) residues of a class mod g = gcd(d, mt) (g not dividing t); averaging its hits over
    the d/g offsets of that class forces > t hits for some offset."""
    from math import gcd as _gcd
    M = m * t; N = m * n; Nr = [N // M + (1 if r < N % M else 0) for r in range(M)]
    for d_ in range(2, N + 1):
        if -(-N // d_) > M: continue
        g = _gcd(d_, M)
        if t % g == 0: continue
        x = -(-t // g)
        worst = max(sum(sorted(Nr[r] for r in range(c0, M, g))[:x]) for c0 in range(g))   # L2292: every class works
        if worst * g > t * d_: return d_
    return None

def interleave_condition_C(m, t):
    """L2292 Conjecture C': perfect layouts exist at every n in (2t, t^2] iff every divisor g of m t with g <= t divides t.
    Proved for m | t (staircase + obstruction); agrees with exact CP-SAT data on all tested pairs except t = 3
    (where the obstructed lengths fall below 2t)."""
    return all(t % g == 0 for g in range(2, t + 1) if (m * t) % g == 0)

def coprime_period_layout(m, t, n):
    """L2296 explicit perfect layout for gcd(m, t) = 1, least prime of m > t (condition C'), t odd:
    period f(k) = (k + (k mod t)) mod m [balance criterion PROVED], stored from offset s0 = (-m rho / 2) mod t,
    rho = n mod t [window rule PROVED, Paper C Theorem 12].  Returns one period (rotated) for layout_from_period."""
    rho = n % t
    if t % 2:
        s0 = (-m * rho * pow(2, -1, t)) % t
    else:
        if rho % 2: raise ValueError("even t with odd n mod t: not covered by this period (L2328); use Hilton-Rodger (rho = 1, t-1) or a certificate")
        s0 = (-m * (rho // 2)) % (t // 2)          # L2328 theorem (even t, even rho)
    M = m * t; f = [((k + (k % t)) % m) for k in range(M)]
    return [f[(s0 + k) % M] for k in range(M)]

def transposed_staircase(m, t):
    """L2300 (Paper C, Theorem 14): for t | m with condition C' (every divisor <= t of m t divides t), the period
    f(k) = (floor(k/t) + (m/t) (k mod t)) mod m is balanced and grouped, so stored from position 0 it is perfect at
    EVERY length 2t < n <= t^2 (one layout for all n).  Proof: (ii) gives Delta = delta (1 - m) (mod m t), and
    gcd(G, 1 - m) = 1; prefixes of m rho positions hold rho of each codeword by direct counting."""
    if m % t: raise ValueError("needs t | m")
    u = m // t
    return [((k // t) + u * (k % t)) % m for k in range(m * t)]

def additive_layout(pi, phi, m, t, s0=0):
    """L2304 additive colouring (m prime, gcd(m,t)=1): f(k) = pi(k mod m) + phi(k mod t) (mod m), pi a permutation of
    Z/m, phi injective [0,t) -> Z/m.  Balanced for every such pi, phi [proved]; returns the period rotated to start s0.
    Example (L2304): m=7, t=4, pi=(3,6,5,2,0,4,1), phi=(0,1,4,2), s0=13 gives a balanced window for rho = 1."""
    M = m * t; f = [((pi[k % m] + phi[k % t]) % m) for k in range(M)]
    return [f[(s0 + k) % M] for k in range(M)]

def double_rotation_layout(m, t, n):
    """L2308: m prime, gcd(m,t)=1 (even t allowed).  Searches 'double rotations': for each residue y mod t, rotate the
    window set S_y (an interval after scaling by t^-1 mod m) and its complement; rows must disagree everywhere
    (a Latin rectangle).  Balance is automatic (proper colouring of K_{m,t}); the window is balanced by construction.
    Returns one period rotated to its window, or raises ValueError if this family has no solution for rho = n mod t."""
    rho = n % t; M = m * t; tinv = pow(t, -1, m)
    def order(Sy):
        sc = sorted(Sy, key=lambda x: (x * tinv) % m); v = [(x * tinv) % m for x in sc]
        if len(v) > 1:
            gaps = [(v[(i + 1) % len(v)] - v[i]) % m for i in range(len(v))]
            j = max(range(len(v)), key=lambda i: gaps[i]); sc = sc[j + 1:] + sc[:j + 1]
        return sc
    if rho == 0:
        rho_eff, s_range = 0, [0]
    else:
        rho_eff, s_range = rho, range(t)
    for s0 in s_range:
        S = [set() for _ in range(t)]
        for k in range(s0, s0 + m * rho_eff): S[k % t].add(k % m)
        A = [order(S[y]) for y in range(t)]; B = [order(set(range(m)) - S[y]) for y in range(t)]
        taus = []
        def make(y, r, rr):
            p = {}
            for i, x in enumerate(A[y]): p[x] = A[y][(i + r) % len(A[y])]
            for i, x in enumerate(B[y]): p[x] = B[y][(i + rr) % len(B[y])]
            return p
        def rec(y):
            if y == t: return True
            for r in range(max(1, len(A[y]))):
                for rr in range(max(1, len(B[y]))):
                    p = make(y, r, rr)
                    if all(p[c] != q[c] for q in taus for c in range(m)):
                        taus.append(p)
                        if rec(y + 1): return True
                        taus.pop()
            return False
        if rec(0):
            invs = [{v: c for c, v in taus[y].items()} for y in range(t)]
            f = [invs[k % t][k % m] for k in range(M)]
            return [f[(s0 + k) % M] for k in range(M)]
    raise ValueError("no double-rotation solution for this rho; use an exact certificate")

def reflection_order_layout(m, t, n, limit=200000):
    """L2312 (m prime, gcd(m,t)=1, any t): reflection rows with placed intervals.  In scaled coordinates (x * t^-1)
    the window sets S_y are intervals [alpha_y, alpha_y + w_y); place intervals of lengths w_y end to end in some order
    (a rho-fold cover of Z/m) and use row y: colour = centre_y - x with centre_y = end_y + alpha_y.  Needs the centres
    distinct (searched over orderings).  Returns one period starting at its window, or raises ValueError."""
    import itertools as _it
    rho = n % t; tinv = pow(t, -1, m); alpha = {}; w = {}
    for k in range(m * rho):
        y = k % t; x = (k % m) * tinv % m
        if y not in alpha: alpha[y] = x; w[y] = 0
        w[y] += 1
    if rho == 0: return transposed_staircase(m, t) if m % t == 0 else coprime_period_layout(m, t, n)
    cnt = 0
    for rest in _it.permutations(range(1, t)):
        order = (0,) + rest; cnt += 1
        if cnt > limit: break
        cum = 0; centre = {}
        for y in order: centre[y] = (cum + w[y] - 1 + alpha[y]) % m; cum += w[y]
        if len(set(centre.values())) == t:
            return [(centre[k % t] - (k % m) * tinv) % m for k in range(m * t)]
    raise ValueError("no reflection ordering found within limit")

def condition_C_witness(m, t):
    """L2324 'only if' direction of Conjecture C' (t >= 4) [proved]: if C' fails, return (n, d) such that NO layout is
    perfect at length n, defeated by period-d damage.  g >= 3 bad divisor -> (g t, g) [obstruction theorem];
    only g = 2 bad (t odd, m = 2 mod 4) -> (4 t, 4) [averaging obstruction].  Returns None if C' holds."""
    if interleave_condition_C(m, t): return None
    bad = [g for g in range(2, t + 1) if (m * t) % g == 0 and t % g]
    big = [g for g in bad if g >= 3]
    if big: return (big[0] * t, big[0])
    return (4 * t, 4)

def half_period_layout(m, t):
    """L2324 [verified, 186 pairs]: m prime > t, t = 0 mod 4, rho = t/2.  Period f(k) = (k + (k mod t)) mod m stored from
    offset t/4 is perfect at every n = t/2 (mod t).  (Fails for t = 2 mod 4: a parity count of blocks.)"""
    if t % 4: raise ValueError("needs t = 0 mod 4")
    M = m * t; f = [((k + (k % t)) % m) for k in range(M)]; s0 = t // 4
    return [f[(s0 + k) % M] for k in range(M)]

def block_shift_layout(m, t, a, s0=0):
    """L2332 block-shift period f(k) = (k + t*a[k mod t]) mod m (a injective mod m; balanced for m prime, gcd(m,t)=1).
    The integer map g(k) = k + t a(k mod t) is a BIJECTION of Z for every t (it keeps residues mod t), which escapes the
    Hall-Paige parity barrier for even t.  Returns the period rotated to start s0."""
    M = m * t; f = [((k + t * a[k % t]) % m) for k in range(M)]
    return [f[(s0 + k) % M] for k in range(M)]

def block_shift_window_ok(m, t, a, s0, rho):
    """L2332 window criterion [proved]: the window [s0, s0 + m rho) of the block-shift period is balanced iff the
    multisets of scaled intervals  U_r [x_r(s), x_r(s) + a_r)  agree (mod m) at s = s0 mod t and s = (s0 + m rho) mod t,
    where x_r(s) = (r - s) t^{-1} + [r < s]."""
    tau = pow(t, -1, m)
    def O(sig):
        c = {}
        for r in range(t):
            x = ((r - sig) * tau + (1 if r < sig else 0)) % m
            for i in range(a[r]): c[(x + i) % m] = c.get((x + i) % m, 0) + 1
        return c
    return O(s0 % t) == O((s0 + m * rho) % t)

def fibonacci_anyon_data():
    """L2336 Fibonacci anyons (2D quasiparticles, quantum dimension phi): F-matrix, R-matrix, braid generators s1 = R,
    s2 = F R F (pure Python complex 2x2).  Returns dict with checks: F^2 = I, Yang-Baxter, d^2 = d + 1, fusion dims."""
    import cmath
    ph = (1 + 5 ** 0.5) / 2
    F = [[1 / ph, ph ** -0.5], [ph ** -0.5, -1 / ph]]
    R = [[cmath.exp(-4j * cmath.pi / 5), 0], [0, cmath.exp(3j * cmath.pi / 5)]]
    mul = lambda A, B: [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    close = lambda A, B: all(abs(A[i][j] - B[i][j]) < 1e-12 for i in range(2) for j in range(2))
    s1 = R; s2 = mul(mul(F, R), F)
    dims = []; a, b = 1, 0
    for _ in range(12): a, b = b, a + b; dims.append(b)
    return {"F2_identity": close(mul(F, F), [[1, 0], [0, 1]]), "yang_baxter": close(mul(mul(s1, s2), s1), mul(mul(s2, s1), s2)),
            "golden_dimension": abs(ph * ph - ph - 1) < 1e-12, "fusion_dims": dims}

def harmonic_aliases(f0, fps=60.0, K=40, res=0.05):
    """L2336 heterodyne/aliasing: uniform sampling at fps mixes harmonic k f0 down to |((k f0 + fps/2) mod fps) - fps/2|.
    Returns the number of distinct aliases (resolution res Hz) among the first K harmonics."""
    al = [abs(((k * f0 + fps / 2) % fps) - fps / 2) for k in range(1, K + 1)]
    return len({round(a / res) for a in al})

def tl_chain_energy(k, n=4000):
    """L2340: exact ground energy per site of the SU(2)_k anyon chain H = -sum e_i (Temperley-Lieb, d = 2cos(pi/(k+2))),
    Bethe ansatz e = -sin(g) * int_R sinh((pi-g)x)/(sinh(pi x) cosh(g x)) dx, g = pi/(k+2).
    k = 3 (Fibonacci): e = -(sqrt5 - 1) = -2/phi; per projector (H = -sum P) e/d = sqrt5 - 3 = -2/phi^2."""
    g = math.pi/(k + 2)
    if HAVE_MP:
        I = 2*mpmath.quad(lambda x: mpmath.sinh((mpmath.pi - g)*x)/(mpmath.sinh(mpmath.pi*x)*mpmath.cosh(g*x)), [0, mpmath.inf])
        return float(-mpmath.sin(g)*I), 2*math.cos(g)
    h = 60.0/n; tot = 0.0                       # pure Python: trapezoid on [0, 60]; integrand -> (pi-g)/pi at 0
    for i in range(n + 1):
        x = i*h; y = (math.pi - g)/math.pi if x == 0 else math.sinh((math.pi - g)*x)/(math.sinh(math.pi*x)*math.cosh(g*x))
        tot += y*(0.5 if i in (0, n) else 1.0)
    return -math.sin(g)*2*tot*h, 2*math.cos(g)

def anyon_storage_bits(n):
    """L2340: bits per anyon stored in the fusion space of n Fibonacci anyons (total charge tau, dim F_n) -> log2(phi)."""
    a, b = 0, 1
    for _ in range(n): a, b = b, a + b
    return math.log2(a)/n

def braid_gate_search(target, maxlen=8):
    """L2340: best braid word (s1, s1^-1, s2, s2^-1) of length <= maxlen approximating a 2x2 gate up to phase on the
    Fibonacci qubit (3 tau anyons). Returns (distance, word). d = sqrt(1 - |tr(U^dag V)|/2)."""
    import cmath
    ph = (1 + 5**0.5)/2; a, b = 1/ph, ph**-0.5
    Fm = [[a, b], [b, -a]]; r1, r2 = cmath.exp(-4j*math.pi/5), cmath.exp(3j*math.pi/5)
    mul = lambda X, Y: [[X[0][0]*Y[0][0] + X[0][1]*Y[1][0], X[0][0]*Y[0][1] + X[0][1]*Y[1][1]], [X[1][0]*Y[0][0] + X[1][1]*Y[1][0], X[1][0]*Y[0][1] + X[1][1]*Y[1][1]]]
    Rm = [[r1, 0], [0, r2]]; Ri = [[r1.conjugate(), 0], [0, r2.conjugate()]]
    G = [Rm, Ri, mul(mul(Fm, Rm), Fm), mul(mul(Fm, Ri), Fm)]; inv = [1, 0, 3, 2]; names = ["s1", "s1^-1", "s2", "s2^-1"]
    dist = lambda U: math.sqrt(max(0.0, 1 - abs(sum(U[i][j].conjugate()*target[i][j] for i in range(2) for j in range(2)))/2))
    best = (2.0, ""); layer = [([[1, 0], [0, 1]], -1, [])]
    for _ in range(maxlen):
        new = []
        for U, last, w in layer:
            for gi in range(4):
                if last >= 0 and gi == inv[last]: continue
                V = mul(U, G[gi]); d = dist(V); new.append((V, gi, w + [gi]))
                if d < best[0] - 1e-12: best = (d, " ".join(names[x] for x in w + [gi]))
        layer = new
    return best

def anyon_chain_energy_closed(N):
    """L2344 (theorem): exact ground energy per site of the Temperley-Lieb / SU(2)_{N-2} anyon chain H = -sum e_i,
    d = 2cos(pi/N):  e(N) = (2 sin(pi/N)/N) sum_{k=1..N-1, 2k != N} k tan(pi k/N)  -  [N even] 2 sin(pi/N)/pi.
    Proof: contour of z f(z), f(z) = sinh((N-1)z)/(sinh(Nz)cosh z) is i*pi-periodic.  N = 5: -(sqrt5 - 1); per projector sqrt5 - 3."""
    s = sum(k*math.tan(math.pi*k/N) for k in range(1, N) if 2*k != N)
    return 2*math.sin(math.pi/N)/N*s - (2*math.sin(math.pi/N)/math.pi if N % 2 == 0 else 0.0)

def class_number_neg(p):
    """h(-p) for a prime p = 3 mod 4, p > 3, via h = -(1/p) sum k (k/p) (Euler-criterion Legendre symbols)."""
    return -sum(k*(1 if pow(k, (p-1)//2, p) == 1 else -1) for k in range(1, p))//p

def girstmair_digits(p, g=10):
    """L2348: alternating digit sum a1 - a2 + a3 - ... of the base-g period of 1/p, and -(g+1) h(-p).
    Girstmair's formula: they are equal when p = 3 mod 4, p >= 7, g a primitive root mod p.
    Proof: digit a_k = (g r_{k-1} - r_k)/p with r_k = g^k mod p; (-1)^k = (r_k/p) since g is a non-residue."""
    r, alt = 1, 0
    for k in range(p - 1):
        d = (g*r)//p; r = (g*r) % p; alt += d if k % 2 == 0 else -d
    return alt, -(g + 1)*class_number_neg(p)

def tangent_class_sum(p):
    """L2348: T(p) = sum (k/p) tan(pi k/p) = (1 - 2(2/p)) * 2 sqrt(p) h(-p)  (p = 3 mod 4, p > 3); returns (T, prediction)."""
    leg = lambda a: 1 if pow(a % p, (p-1)//2, p) == 1 else -1
    T = sum(leg(k)*math.tan(math.pi*k/p) for k in range(1, p))
    return T, (1 - 2*leg(2))*2*math.sqrt(p)*class_number_neg(p)

def decimal_hminus(p, base=10):
    """L2352: relative class number h^-(Q(zeta_p)) computed ONLY from the base-10 digit periods of a/p
    (one fraction per coset of <10> in (Z/p)^*).  Theorem: for a character chi with chi(10) = psi,
    the Fourier coefficient sum_k psi^k x_k of the period of a/p equals (10 psi - 1) * (1/p) sum_k psi^k r_k (r_k = a 10^k mod p);
    Fourier inversion over cosets gives B_{1,chi}; h^- = 2p prod_{chi odd} (-B_{1,chi}/2).  Floats: exact up to p ~ 100."""
    import cmath
    n = p - 1
    g = next(x for x in range(2, p) if all(pow(x, n//q, p) != 1 for q in {d for d in range(2, n+1) if n % d == 0 and all(d % e for e in range(2, int(d**0.5)+1))}))
    lg = {}; r = 1
    for k in range(n): lg[r] = k; r = r*g % p
    f = 1; r = base % p
    while r != 1: r = r*base % p; f += 1
    c = n//f; t = lg[base % p]; prod = 2*p
    periods = {}
    for i in range(c):
        a = pow(g, i, p); r = a; x = []
        for _ in range(f): x.append((base*r)//p); r = base*r % p
        periods[a] = x
    for j in range(1, n, 2):
        psi = cmath.exp(2j*math.pi*j*t/n); B = 0
        for a, x in periods.items():
            Xa = sum(psi**(k+1)*x[k] for k in range(f))
            B += cmath.exp(2j*math.pi*j*lg[a]/n)*Xa/(base*psi - 1)
        prod *= -B/2
    return int(round(prod.real))

def irregular_indices_decimal(p):
    """L2356: Kummer irregular indices k (even, 2 <= k <= p-3, p | B_k) read from the DECIMAL periods of a/p (one per coset of <10>):
    B_{1,omega^{k-1}} = sum_a omega^{k-1}(a) X_a(psi)/(10 psi - 1), psi = omega(10)^{k-1}, exact p-adically; computed mod p^3
    with Teichmueller lifts a^{p^2}.  B_{1,omega^{k-1}} == B_k/k (mod p).  Example: p = 37 -> [32]; p = 157 -> [62, 110]."""
    M = p**3; f = 1; r = 10 % p
    while r != 1: r = r*10 % p; f += 1
    H = set(); r = 1
    for _ in range(f): H.add(r); r = 10*r % p
    reps, seen = [], set()
    for a in range(1, p):
        if a not in seen: reps.append(a); seen |= {a*h % p for h in H}
    per = {}
    for a in reps:
        r, x = a, []
        for _ in range(f): x.append((10*r)//p); r = 10*r % p
        per[a] = x
    def vp(x):
        x %= M
        if x == 0: return 99
        v = 0
        while x % p == 0: x //= p; v += 1
        return v
    T = lambda a: pow(a, p*p, M); out = []
    for k in range(2, p-2, 2):
        psi = pow(T(10), k-1, M); D = (10*psi - 1) % M; N = 0
        for a, x in per.items():
            N = (N + pow(T(a), k-1, M)*(sum(pow(psi, i+1, M)*x[i] for i in range(f)) % M)) % M
        if vp(N) > vp(D): out.append(k)
    return out

def decimal_L_spectrum(p):
    """L2360: |L(1,chi)| for every odd character chi mod p, read from the decimal period of 1/p (10 a primitive root mod p):
    |L(1,chi)| = pi |X(psi)| / (sqrt(p) |10 psi - 1|), psi = chibar(10), X = digit Fourier coefficient (L2352 theorem, |tau| = sqrt p).
    Returns dict j -> |L(1,chi_j)| with chi_j(10) = exp(2 pi i j/(p-1)), j odd."""
    import cmath
    n = p - 1; r, x = 1, []
    for _ in range(n): x.append((10*r)//p); r = 10*r % p
    if r != 1 or any(pow(10, n//q, p) == 1 for q in range(2, n+1) if n % q == 0 and all(q % e for e in range(2, int(q**0.5)+1))):
        raise ValueError("10 must be a primitive root mod p")
    out = {}
    for j in range(1, n, 2):
        psi = cmath.exp(-2j*math.pi*j/n)
        X = sum(psi**(k+1)*x[k] for k in range(n))
        out[j] = math.pi*abs(X)/(math.sqrt(p)*abs(10*psi - 1))
    return out

def irregular_line_valuation(p, k, E=6):
    """L2364: p-adic valuation of B_{1,omega^{k-1}} read from the decimal periods of a/p (one per coset of <10>), computed mod p^E
    (Girstmair 1994b eq. (8) + coset inversion; Teichmueller lifts a^{p^(E-1)}).  All 23 irregular pairs p < 400 give 1."""
    M = p**E; f = 1; r = 10 % p
    while r != 1: r = r*10 % p; f += 1
    H = set(); r = 1
    for _ in range(f): H.add(r); r = 10*r % p
    reps, seen = [], set()
    for a in range(1, p):
        if a not in seen: reps.append(a); seen |= {a*h % p for h in H}
    def v(x):
        x %= M
        if x == 0: return E
        n_ = 0
        while x % p == 0: x //= p; n_ += 1
        return n_
    T = lambda a: pow(a, p**(E-1), M); psi = pow(T(10), k-1, M); N = 0
    for a in reps:
        r, x = a, []
        for _ in range(f): x.append((10*r)//p); r = 10*r % p
        N = (N + pow(T(a), k-1, M)*(sum(pow(psi, i+1, M)*x[i] for i in range(f)) % M)) % M
    return v(N) - v(10*psi - 1)

def odd_rho_walk_layout(m, t, rho, seeds=60, budget=300000):
    """L2368 (Paper C, walk lemma): block shift a for the window [0, m rho) via the Eulerian reformulation.
    tau = t^{-1} mod m, s = m rho mod t, c = s tau.  The window is balanced iff the arcs b_r -> b_r - c + [r < s]
    (b_r = r tau + a_r) form closed walks; we build ONE closed walk depth-first with labels a_r = v - r tau distinct.
    Solved every case m prime <= 59, even t < m, odd rho (1686/1686).  Returns a (use block_shift_layout(m, t, a, 0))."""
    import random
    tau = pow(t, -1, m); s = (m*rho) % t; c = s*tau % m
    for seed in range(seeds):
        rng = random.Random(seed); rem = set(range(t)); used = set(); a = [None]*t; nodes = [0]
        def rec(v, k):
            if k == t: return True
            nodes[0] += 1
            if nodes[0] > budget: return False
            cand = list(rem); rng.shuffle(cand)
            for r in cand:
                val = (v - r*tau) % m
                if val in used: continue
                rem.discard(r); used.add(val); a[r] = val
                if rec((v - c + (1 if r < s else 0)) % m, k + 1): return True
                rem.add(r); used.discard(val); a[r] = None
                if nodes[0] > budget: return False
            return False
        if rec(0, 0): return a
    return None


# ---------------------------------------------------------------- L2372: odd-rho interleavers, m-free integer certificates
_ODDRHO_CERTS_B64 = (
    "eNpsvUmyLLuObDmXaHvDWNNyKik5kj/53MRaoJ37JTpPIs7d7m7GAoVCofg//zN/5X/+n/+3/dZv/Mqv/p7/7/c/O/6t//3b+5v866/Fv7e/f//7379/"
    "m3//Ov7+4vx9eeIDf19Qfue/ns+dz5Rf57+ej82/f/z7p/jXv/+6/v5un/9a47Pr74OlnS94f3//dL47/nTyAzW+ovOfzhfy2+dD5wOFvxl/f/P3Dev8"
    "xfn9wZedH9zxAqXHj+0ffxXfV+b5rcbPvfFsD396frL4SP13vrKfP9x/f9/ik89v8pfnh89jnP98/i6+rZ+1q+ej5ynH+UsW+/xSO1/69wj7/P7fB/8e"
    "YZyvP388ec2HT/gU8ZUrvv186Tif639fEs/Sz1dM/n7wC42vXOfvzm7wcGc3y3mPv0fo/P06fz/OX9f4/u7fnY+VWJXCT9Tz9/ufNyiv7zfjVeKRyo5f"
    "Po9azrr/LR4fa3FA4s92fGt80vXig+cRz0+ts3R8Kl7mPA5LFR/sfPP5kTLcwc2iLz4Vr8RBOd85ecDGB3Z89nys+a1nISpH+Px57HZ92Ooa6zXPl4/c"
    "rThfT9yXvzvChznhnODYxO5fr/OFf3/w5sOueMnz9JWPDk7k+fcRv75ZPLfi/Ho5J7n5rvW5j8yLno9WNizWpj6sP88cm3/OrGer8dGXlS2ckOZTjvNj"
    "5++evIccS37k3NfKffVR2vnq+rdc8WIvh6GetT9Peb40zmeLB+o/v6Bx5M4XnL+LLY9Px2M859smz1zLd1rOl3e+YITJeuLHuRtxOQf26nEP40DXx5PJ"
    "I/oEsXCuDFcrVvfvv5xveM5f1pLnYPLsXKjCF5zlqyUuUq3/nsM4d2ezPLMVm9cwRp0zWrFD95zVeLwaC3E2kAfu54vOTx9zVnxdHjSOxOabWixGib9m"
    "S8IssP3nLNXiNeBxzi/1e4ora4oNK2nEWr77Zk3W+Ug8xd93Vu1DefQZ5e5tzyN5FvT8VmcT4zhPjhOLyWLMtCMrz1Lla143iI2NryluTHiXhqmIX4oj"
    "W2Mvt69dH1c5lvk8Q7zz4PNhUWr8cFjC81UcMy54vHo9y8jjzLtb08NecU9//288+N//7FzmEYYfu1Yfr0XD7m6+Lc7/8tL1+ODmSTim597VqUs+m9/y"
    "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"
)
_ODDRHO_CERTS = None

def oddrho_integer_ok(t, s, X):
    """L2372: integer problem I(t,s): X distinct and multiset {X_r + r} == {X_r + ((r - s) mod t)}."""
    from collections import Counter
    if len(set(X)) != t: return False
    return Counter(X[r] + r for r in range(t)) == Counter(X[r] + (r - s) % t for r in range(t))

def oddrho_lift(m, t, X):
    """L2372 lift lemma: a_r = X_r * t^{-1} mod m.  Valid for every m coprime to t whose least prime factor >= window W."""
    tau = pow(t, -1, m); return [(x * tau) % m for x in X]

def oddrho_mirror(t, X):
    """L2372 mirror: a solution of I(t,s) gives one of I(t,t-s): X'_{t-1-r} = -X_r - (t-1) (normalised to start at 0)."""
    Y = [None] * t
    for r in range(t): Y[t - 1 - r] = -X[r] - (t - 1)
    lo = min(Y); return [y - lo for y in Y]

def oddrho_half_solution(t):
    """L2372 Theorem H: explicit X in I(t, t/2; t+1) for t = 2 mod 4, t >= 6 (two-cycles: transpositions + one 3-cycle)."""
    s = t // 2
    if t % 4 != 2 or s < 3: raise ValueError("need t = 2 mod 4, t >= 6")
    sig, xv = {}, {}
    for k in range((s - 3) // 2):
        sig[2*k], sig[2*k+1] = 2*k + 1, 2*k; xv[2*k], xv[2*k+1] = 4*k + 1, 4*k + 2
    sig[s-1], sig[s-3], sig[s-2] = s - 3, s - 2, s - 1
    B = 2*s - 6; xv[s-1], xv[s-3], xv[s-2] = B, B + 4, B + 6
    X = [None] * t
    for i in range(s): X[i] = xv[i]; X[s + sig[i]] = xv[i] + (i - sig[i])
    return X

def oddrho_certificate(t, s):
    """L2372: (X, W) with X in I(t,s;W); W = t+1 for 3 <= s <= t-3, W = t+3 for s = 1, t-1.
    Covers every even t in [6, 86] and odd s (embedded CP-SAT certificates + mirror + Theorem H).  (None, None) outside."""
    global _ODDRHO_CERTS
    if 2*s == t and s >= 3: return oddrho_half_solution(t), t + 1
    if 2*s > t:
        X, W = oddrho_certificate(t, t - s)
        return (None, None) if X is None else (oddrho_mirror(t, X), W)
    if _ODDRHO_CERTS is None:
        _ODDRHO_CERTS = json.loads(zlib.decompress(base64.b64decode("".join(_ODDRHO_CERTS_B64))).decode())
    X = _ODDRHO_CERTS.get("%d,%d" % (t, s))
    return (None, None) if X is None else (list(X), t + 3 if s == 1 else t + 1)

def odd_rho_layout_any_m(m, t, rho):
    """L2372: block shift a for (m, t, rho) with no search: s = m rho mod t, a = lift of the certificate.
    Proven valid for every m coprime to t with lpf(m) >= W (all primes m > t).  Returns None outside coverage
    (t > 86, or the edge case lpf(m) = t+1 with s = +-1, lead L2376); fall back to odd_rho_walk_layout."""
    s = (m * rho) % t; X, W = oddrho_certificate(t, s)
    if X is None: return None
    p, n_ = 2, m
    while p * p <= n_ and n_ % p: p += 1
    lpf = p if p * p <= n_ else n_
    return oddrho_lift(m, t, X) if W <= lpf else None


# ---------------------------------------------------------------- L2393: anyon-chain energy as cyclotomic integer
def anyon_energy_units(N):
    """L2393 Theorem 1 (odd N): e(N) = zeta_{2N}^{-1} sum_{j=1}^{N-1} (-1)^j (w-1)/(w^j-1), w = e^{2 pi i/N}.
    For N = p prime each term is a cyclotomic unit, so e(p) is an algebraic integer of Q(zeta_p)^+."""
    import cmath
    if N % 2 == 0: raise ValueError("odd N only")
    w = cmath.exp(2j*math.pi/N); z = cmath.exp(1j*math.pi/N)
    return ((1/z)*sum((-1)**j*(w - 1)/(w**j - 1) for j in range(1, N))).real

def anyon_energy_zw(p):
    """L2393 Corollary 1a: exact integer vector c (length p) with e(p) = sum_k c_k w^k,
    e(p) = -w^{(p-1)/2} sum_j (-1)^j sum_{i < j^{-1} mod p} w^{ij}."""
    c = [0]*p; h = (p - 1)//2
    for j in range(1, p):
        jp = pow(j, -1, p); sg = -1 if j % 2 else 1
        for i in range(jp): c[(h + i*j) % p] -= sg
    return c

def anyon_energy_from_digits(p, base=10):
    """L2393 Theorem 2 + Girstmair: e(p) from the base-`base` period of 1/p alone (base a primitive root mod p).
    B_{1,chi} = X(psi)/(base psi - 1) from the digits; sum k tan(pi k/p) = (2ip/(p-1)) sum_{chi odd}(1-2 conj chi(2)) tau(chi) B_{1,conj chi}^2."""
    import cmath
    x, r = [], 1
    for _ in range(p - 1): x.append((base*r)//p); r = base*r % p
    if r != 1 or len(set((base**k) % p for k in range(p - 1))) != p - 1: raise ValueError("base must be a primitive root mod p")
    ind, v = {}, 1
    for e in range(p - 1): ind[v] = e; v = v*base % p
    B = {}
    for j in range(p - 1):
        psi = cmath.exp(2j*math.pi*j/(p - 1))
        B[j] = sum(psi**(k + 1)*x[k] for k in range(p - 1))/(base*psi - 1)
    tot = 0
    for j in range(1, p - 1, 2):
        chi = {a: cmath.exp(2j*math.pi*j*ind[a]/(p - 1)) for a in range(1, p)}
        tau = sum(chi[a]*cmath.exp(2j*math.pi*a/p) for a in range(1, p))
        tot += (1 - 2*chi[2].conjugate())*tau*B[(p - 1 - j) % (p - 1)]**2
    S = (2j*p/(p - 1)*tot).real
    return 2*math.sin(math.pi/p)/p*S


# ---------------------------------------------------------------- L2399: 2-adic law and Wieferich denominators of e(N)
def anyon_energy_denominator(N):
    """L2399 Theorem D (odd composite N, primes p | N not base-2 Wieferich): exact denominator of N(e(N)):
    p-exponent (p^(a-1) - 1)/2 if N = p^a, else phi(N)/(2(p-1)).  Wieferich primes (1093, 3511) with p || N contribute 1."""
    f, n_ = {}, N; d_ = 3
    while n_ % 2 == 0: raise ValueError("odd N only")
    while d_*d_ <= n_:
        while n_ % d_ == 0: f[d_] = f.get(d_, 0) + 1; n_ //= d_
        d_ += 2
    if n_ > 1: f[n_] = f.get(n_, 0) + 1
    if len(f) == 1 and list(f.values())[0] == 1: return 1                      # prime: algebraic integer
    phi = 1
    for p, a in f.items(): phi *= (p - 1)*p**(a - 1)
    D = 1
    for p, a in f.items():
        if pow(2, p - 1, p*p) == 1: continue                                   # Wieferich (any exponent): p-integral (L2405 Thm W)
        D *= p**((p**(a - 1) - 1)//2 if len(f) == 1 else phi//(2*(p - 1)))
    return D

def anyon_energy_norm_float(N):
    """L2399: N_{Q(zeta_N)^+/Q}(e(N)) as a float (product of Galois conjugates, odd N; fine for small N)."""
    try:                                    # L3289: 60-digit mpmath (float error reached 1e-3 on an ARM phone at N = 27)
        import mpmath as _mp
        with _mp.workdps(60):
            w = _mp.expjpi(_mp.mpf(2)/N); prod = _mp.mpf(1)
            for a in range(1, (N + 1)//2):
                if math.gcd(a, N) != 1: continue
                wa = w**a; z = -w**(a*(N + 1)//2)
                prod *= _mp.re((1/z)*_mp.fsum((-1)**j*(wa - 1)/(wa**j - 1) for j in range(1, N)))
            return float(prod) if abs(prod) < 1e15 else prod
    except ImportError:
        pass
    try:                                    # L3289: 60-digit mpmath (float error reached 1e-3 on an ARM phone at N = 27)
        import mpmath as _mp
        with _mp.workdps(60):
            w = _mp.expjpi(_mp.mpf(2)/N); prod = _mp.mpf(1)
            for a in range(1, (N + 1)//2):
                if math.gcd(a, N) != 1: continue
                wa = w**a; z = -w**(a*(N + 1)//2)
                prod *= _mp.re((1/z)*_mp.fsum((-1)**j*(wa - 1)/(wa**j - 1) for j in range(1, N)))
            return prod
    except ImportError:
        pass
    import cmath
    w = cmath.exp(2j*math.pi/N); prod = 1.0
    for a in range(1, (N + 1)//2):
        if math.gcd(a, N) != 1: continue
        wa = w**a; z = -w**(a*(N + 1)//2)
        prod *= ((1/z)*sum((-1)**j*(wa - 1)/(wa**j - 1) for j in range(1, N))).real
    return prod


# ---------------------------------------------------------------- L2405: Theorem W and even-N unit formula
def anyon_energy_is_integral(N):
    """L2405 Theorem W (odd N): e(N) is an algebraic integer  <=>  N is prime, or every prime factor of N is a base-2
    Wieferich prime (2^(p-1) = 1 mod p^2; known: 1093, 3511)."""
    if N % 2 == 0: raise ValueError("odd N only")
    f, n_, d_ = set(), N, 3
    while d_*d_ <= n_:
        while n_ % d_ == 0: f.add(d_); n_ //= d_
        d_ += 2
    if n_ > 1: f.add(n_)
    if N in f: return True
    return all(pow(2, p - 1, p*p) == 1 for p in f)

def anyon_energy_even_units(N):
    """L2405 Theorem E (even N): algebraic part a(N) = e(N) + 2 sin(pi/N)/pi
    = (zeta - zeta^-1) [1/2 - (2/N) sum_{i=1}^{N-1} i (-1)^i/(w^i - 1)],  zeta = e^{i pi/N}, w = zeta^2."""
    import cmath
    if N % 2: raise ValueError("even N only")
    w = cmath.exp(2j*math.pi/N); z = cmath.exp(1j*math.pi/N)
    return ((z - 1/z)*(0.5 - 2/N*sum(i*(-1)**i/(w**i - 1) for i in range(1, N)))).real


# ---------------------------------------------------------------- L2411: Fermat quotients in the lattice of e(p); twisted sums
def fermat_quotient(p, b=2):
    """q_p(b) = (b^(p-1) - 1)/p mod p  (b-Wieferich iff 0)."""
    return ((pow(b, p - 1, p*p) - 1)//p) % p

def anyon_energy_trace(p):
    """L2411 exact Tr_{Q(zeta_p)^+/Q}(e(p)) from the Z[w] vector:  Tr_{Q(zeta_p)}(f(w)) = p c_0 - f(1).
    Theorem T: Tr(e(p)) == -q_p(2) (mod p)."""
    c = anyon_energy_zw(p); return (p*c[0] - sum(c))//2

def anyon_energy_mod_lambda(p):
    """L2411 Theorem T': e(p) == 2 q_p(2) (mod (1 - zeta_p)).  Returns the residue in F_p."""
    return sum(anyon_energy_zw(p)) % p

def twisted_coefficient_vanishes(k, p):
    """L2411: c(zeta_k) = sum_{m<p} zeta_k^m/m (mod p) == -delta_p(1 - zeta_k).  True iff it vanishes.
    k=2,4: base-2 Wieferich; k=3: base-3 Wieferich (11, 1006003); k=6: always; k=10: Wall-Sun-Sun type."""
    # cyclotomic polynomial coefficients by division
    def cyclo(n):
        P = [-1] + [0]*(n - 1) + [1]                       # x^n - 1
        for d in range(1, n):
            if n % d == 0:
                Q = cyclo(d); out = [0]*(len(P) - len(Q) + 1); R = P[:]
                for i in range(len(out) - 1, -1, -1):
                    out[i] = R[i + len(Q) - 1]
                    for j in range(len(Q)): R[i + j] -= out[i]*Q[j]
                P = out
        return P
    Phi = [c % p for c in cyclo(k)]; deg = len(Phi) - 1
    def mul(a, b):
        c = [0]*(2*deg)
        for i, x in enumerate(a):
            for j, y in enumerate(b): c[i + j] += x*y
        for t in range(2*deg - 1, deg - 1, -1):
            v = c[t] % p
            if v:
                for i in range(deg): c[t - deg + i] -= v*Phi[i]
            c[t] = 0
        return [x % p for x in c[:deg]]
    if deg == 1: gen = [(-Phi[0]) % p]
    else: gen = [0]*deg; gen[1] = 1
    x = [1] + [0]*(deg - 1); s = [0]*deg
    for m in range(1, p):
        x = mul(x, gen); im = pow(m, -1, p); s = [(s[i] + x[i]*im) % p for i in range(deg)]
    return all(v == 0 for v in s)


# ---------------------------------------------------------------- L2417: lambda-adic structure of e(p) and the golden twist
_MU_AFFINE = [  # (a_n, b_n): mu-digit F_n == a_n + b_n q_p(2) (mod p);  generating functions
    ("0", "2"), ("-1/24", "-1/12"), ("-1/720", "-17/2880"), ("-163/967680", "-367/483840"),
    ("-1397/58060800", "-27859/232243200"), ("-523867/122624409600", "-1295803/61312204800"),
    ("-123422483/167382319104000", "-5329242827/1339058552832000")]
# B(t) = 4 sinh(t/2)/t,  A(t) = -2 sinh(t/2) sum_k B_{2k} E_{2k-1}(0) t^{2k-1}/(2k)!,  mu = -4 sinh^2(t/2),  t = -log(1 - lambda)

def anyon_energy_mu_digits(p, nmax=4):
    """L2417: digits F_0..F_nmax (mod p) of e(p) in mu = (1 - w)(1 - w^-1), computed from the cyclotomic-unit form."""
    from math import comb
    K = 2*nmax + 2; h = (p - 1)//2; tot = [0]*K
    for m in range(1, p):
        s = [((-1)**r*comb(m, r + 1)) % p for r in range(K)]
        i0 = pow(s[0], -1, p); u = [0]*K; u[0] = i0
        for n in range(1, K): u[n] = (-i0*sum(s[i]*u[n - i] for i in range(1, n + 1))) % p
        sg = 1 if m % 2 == 0 else -1
        for n in range(K): tot[n] = (tot[n] + sg*u[n]) % p
    pre = [((-1)**r*comb(h, r)) % p for r in range(K)]
    E = [(-sum(pre[i]*tot[n - i] for i in range(n + 1))) % p for n in range(K)]
    mu = [0, 0] + [(-1) % p]*(K - 2)
    def mul(a, b):
        c = [0]*K
        for i, x in enumerate(a):
            if x:
                for j, y in enumerate(b[:K - i]): c[i + j] = (c[i + j] + x*y) % p
        return c
    R, F, P = E[:], [], [1] + [0]*(K - 1)
    for n in range(nmax + 1):
        c = R[2*n]*pow((-1) % p, n, p) % p; F.append(c)
        R = [(r - c*x) % p for r, x in zip(R, P)]; P = mul(P, mu)
    return F

def anyon_energy_mu_predicted(p, nmax=4):
    """L2417 Theorem L: F_n == a_n + b_n q_p(2) (mod p) with universal rationals (Bernoulli x Euler numbers)."""
    from fractions import Fraction as Fr
    qq = fermat_quotient(p); out = []
    for n in range(nmax + 1):
        a, b = Fr(_MU_AFFINE[n][0]), Fr(_MU_AFFINE[n][1])
        out.append((a.numerator*pow(a.denominator, -1, p) + qq*b.numerator*pow(b.denominator, -1, p)) % p)
    return out

# ---------------------------------------------------------------- L2436-L2453: Lehmer trace formula, Lucas wheels, ladder
def lehmer_count(p):
    """L2436: N(p) = #{1<=a<=p-1 : a and a^{-1} mod p have opposite parity} (D. H. Lehmer's problem; Zhang: p/2 + O(p^1/2 log^2 p))."""
    return sum(1 for a in range(1, p) if (a + pow(a, -1, p)) % 2)

def anyon_trace_lehmer(p):
    """L2436 trace formula: full trace Tr_{Q(zeta_p)/Q} e(p) = S1 + p (N(p) - (p-1)/2), S1 = sum_a (-1)^{a^{-1}} a.
    Returns (Tr, S1, N).  Tr == -2 q_p(2) (mod p);  Tr = O(p^{3/2} log^2 p) (L2448)."""
    S1 = sum((-1)**pow(a, -1, p) * a for a in range(1, p)); N = lehmer_count(p)
    return S1 + p*(N - (p - 1)//2), S1, N

def lucas_period(m, P=1, Q=-1):
    """period of (U_n, U_{n+1}) mod m for U_{n+1} = P U_n - Q U_{n-1} (gcd(m,Q)=1)."""
    a, b, n = 0, 1, 0
    while True:
        a, b = b, (P*b - Q*a) % m; n += 1
        if a == 0 and b == 1: return n

def lucas_antipodal(m, P=1, Q=-1):
    """L2442/L2448: True iff U_{n+T/2} == -U_n (mod m) for all n (half-period negation; quarter-turn symmetry)."""
    T = lucas_period(m, P, Q)
    if T % 2: return False
    s = [0, 1]
    for _ in range(2*T): s.append((P*s[-1] - Q*s[-2]) % m)
    return all((s[n + T//2] + s[n]) % m == 0 for n in range(T))

def lucas_antipodal_predicted(m, P=1, Q=-1):
    """L2448 Theorem 8 (CRT): odd/2-power parts q != 2 antipodal with equal v2(T(q)); if 2||m, T(2) | T(m)/2."""
    fac, n, d = {}, m, 2
    while d*d <= n:
        while n % d == 0: fac[d] = fac.get(d, 0) + 1; n //= d
        d += 1
    if n > 1: fac[n] = fac.get(n, 0) + 1
    v = set()
    for p_, e in fac.items():
        q = p_**e
        if q == 2: continue
        if not lucas_antipodal(q, P, Q): return False
        T = lucas_period(q, P, Q); v.add(T & -T)
    if fac.get(2) == 1 and (lucas_period(m, P, Q)//2) % lucas_period(2, P, Q): return False
    return len(v) <= 1

def wheel_group_order(m, P=1, Q=-1):
    """L2430/L2448: order of the wheel symmetry group = 2 T(m)/alpha(m) (Q = -1)."""
    T = lucas_period(m, P, Q); s = [0, 1]
    while True:
        s.append((P*s[-1] - Q*s[-2]) % m)
        if s[-1] == 0: return 2*T//(len(s) - 1)

def step10_ladder(n, K=400):
    """L2422 lemma: sum_k a_k/10^(k+1) = 1/(99 - 10 n) for a_k = n a_{k-1} + a_{k-2}; returns (partial sum, exact)."""
    from fractions import Fraction as Fr
    a, b, S = 0, 1, Fr(0)
    for k in range(K):
        S += Fr(a, 10**(k + 1)); a, b = b, n*b + a
    return S, Fr(1, 99 - 10*n)


def bulk_energy_closed(a, N):
    """L2473/L2478 Theorem B': Bethe-ansatz bulk ground-state energy per site of the Temperley-Lieb/XXZ chain
    H = -sum e_i at gamma = pi a/N (gcd(a,N)=1):  (2 sin g/N) sum' k tan(g k) - (N sin g/(2a^2)) sum'_{j odd<4a} j cot(pi N j/(2a))
    - [N even] 2 sin g/(pi a).   a = 1 gives e(N); odd N -> algebraic; even N -> algebraic + algebraic/pi."""
    g = math.pi*a/N
    T = (2*math.sin(g)/N)*sum(k*math.tan(g*k) for k in range(1, N) if (2*a*k) % (2*N) != N)
    R = -(N*math.sin(g)/(2*a*a))*sum(j/math.tan(math.pi*N*j/(2*a)) for j in range(1, 4*a, 2) if (N*j) % (2*a) != 0)
    return T + R - (2*math.sin(g)/(math.pi*a) if N % 2 == 0 else 0.0)

def bulk_energy_integral(g):
    """numerical Bethe integral -sin g * int sinh((pi-g)x)/(sinh(pi x) cosh(g x)) dx (trapezoid, double precision)."""
    h, S, x = 1e-3, 0.0, 1e-3
    while x < 60:
        S += math.sinh((math.pi - g)*x)/(math.sinh(math.pi*x)*math.cosh(g*x)); x += h
    S = (S + 0.5*(math.pi - g)/math.pi)*h
    return -math.sin(g)*2*S

def menu_recbalance():
    say("Balance of a recurrence mod m: does the residue mean equal (m-1)/2?  Fibonacci: only m = 5^k (Theorem B).")
    say("Lucas: never (Theorem B_L).  Pell: never; at m = 2^a the defect is exactly -m (Theorem B_P).")
    name = ask("sequence (fibonacci, lucas, pell)", "pell").lower(); m = int(ask("modulus m", 16))
    r = seq_balance(name, m)
    say("%s mod %d: period %d, residue sum %d, mean %.4f vs (m-1)/2 = %.4f, defect D = %d" % (name, m, r["period"], r["sum"], r["sum"] / r["period"], (m - 1) / 2, r["defect"]))
    a = int(ask("general recurrence x(n+1) = a x(n) + x(n-1): a =", 12)); m2 = int(ask("modulus", 37))
    s0 = int(ask("seed x(0)", 0)); s1 = int(ask("seed x(1)", 1))
    g = ab_orbit(a, m2, s0, s1)
    say("a = %d, seeds (%d, %d), mod %d: period %d, defect D = %d, balanced %s, uniformly distributed %s (a^2 + 4 = %d)"
        % (a, s0, s1, m2, g["period"], g["defect"], g["defect"] == 0, g["uniform"], a * a + 4))
    say("  Theorem BG* predicts uniform distribution: %s;  degeneracy number 2*x(0) + a*x(1) = %d (degenerate at primes of a^2+4 dividing it)"
        % (ud_predict(a, m2, s0, s1), 2 * s0 + a * s1))
    if (s0, s1) == (0, 1): say("  seeds (0, 1): Theorem BG (proved for all m) says balanced <=> uniform <=> %s" % bg_set(a, m2))
    ans, why = balance_predict(a, m2, s0, s1)
    say("  proved balance prediction: %s (%s)" % ("not covered" if ans is None else ans, why))
    if ask("three-term recurrence y(n+1) = a y(n) + b y(n-1) + y(n-2): try it? (y/n)", "n").lower().startswith("y"):
        A3 = int(ask("a", 5)); B3 = int(ask("b", 10)); q3 = int(ask("prime q dividing a and b", 5)); e3 = int(ask("exponent e", 3))
        sd = [int(x) for x in ask("three seeds", "8,608,366").split(",")]
        kinds, bal = strand_types(A3, B3, q3, e3, sd)
        say("  strands y(3t), y(3t+1), y(3t+2): %s; balanced: %s  (q-adic Morse principle, L1996)" % (kinds, bal))
    qq = int(ask("digit-strand dictionary (Cor. M2): a prime q, e.g. 41, 53, 79", 79))
    kk, D, mean, okd = kth_power_dictionary(qq)
    say("  1/%d: index k = %d, digit sum %d; mean of u^%d mod %d = %s; digit sum = (9/k) x mean: %s" % (qq, kk, D, kk, qq, mean, okd))
    if ask("quartic class-number recurrence demo (q = 13, about 30 000 steps)? (y/n)", "n").lower().startswith("y"):
        mean, pred, B4, hm = quartic_recurrence_demo(13)
        say("  order-4 recurrence mod 13^5: mean %s, predicted %.1f; B1(chi4) = %s; |B|^2/2 = %.0f = relative class number of the quartic field" % (mean, pred, B4, hm))
    if ask("order-k class-number recurrence (Theorem Q_k)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q", 7)); kk = int(ask("order k dividing q-1", 6))
        mean, pred, hm = qk_recurrence_demo(qq, kk)
        say("  order-%d recurrence mod %d^%d: mean %s, predicted %.1f; relative class number seen: %s" % (kk, qq, kk + 1, mean, pred, hm if hm is not None else "none (no odd characters)"))
    if ask("isolate single L-values from k scaled orbits (Theorem L)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q", 13)); kk = int(ask("k dividing q-1", 4))
        for j, Bi, Bd in isolate_L_values(qq, kk):
            say("  chi^%d: B1 from orbits = %s, direct = %s, L(0,chi) = -B1" % (j, complex(round(Bi.real, 6), round(Bi.imag, 6)), complex(round(Bd.real, 6), round(Bd.imag, 6))))
    if ask("L(1, chi) and h*R from orbits with shifted centres (Theorems L+, R)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q (small: 7, 13, 11, 17)", 7)); kk = int(ask("k dividing q-1", 3))
        rows, hR = orbit_L1_values(qq, kk)
        for j, par, okc, L1 in rows:
            say("  chi^%d (%s): chi rebuilt from orbits %s; L(1,chi) = %s" % (j, par, okc, complex(round(L1.real, 8), round(L1.imag, 8))))
        if hR is not None: say("  totally real field of degree %d: class number x regulator h*R = %.8f" % (kk, hR))
    if ask("class number of Q(sqrt q) from two recurrences (Theorem H2)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 1 mod 4 (try 229, 257, 401)", 229))
        hR, t, u, R, h = two_recurrence_class_number(qq)
        say("  orbits: h*R = %.9f;  DCF recurrence a = %d (a^2 + 4 = %d = %d x %d^2), growth log = R = %.9f;  h = %.6f" % (hR, t, t * t + 4, qq, u, R, h))
    if ask("minus-sign recurrence x(n+1) = a x(n) - x(n-1) (Theorem BG-)? (y/n)", "n").lower().startswith("y"):
        A = int(ask("a", 7)); M = int(ask("modulus", 45)); S0 = int(ask("seed x(0)", 0)); S1 = int(ask("seed x(1)", 1))
        per, b_, u_ = minus_orbit(A, M, S0, S1); pu, pb = bgminus_predict(A, M, S0, S1)
        say("  a = %d, a^2 - 4 = %d, mod %d: period %d, balanced %s, uniform %s;  Theorem BG- predicts uniform %s%s"
            % (A, A * A - 4, M, per, b_, u_, pu, ", balanced %s" % pb if (S0, S1) == (0, 1) else ""))
    if ask("class number of Q(sqrt q) for q = 3 mod 4 from three recurrences (Theorem H2-)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 3 mod 4 (try 79, 223, 359; q above 300 is slow on a phone)", 79))
        hR, A, U, R, h, ex = class_number_3mod4(qq)
        say("  Pell mod 4 x order-2 orbit mod %d^3, read mod %d: characters rebuilt exactly %s; h*R = %.9f" % (qq, 4 * qq, ex, hR))
        say("  minus recurrence x(n+1) = %d x(n) - x(n-1) (a^2 - 4 = 4 x %d x %d^2): growth log R = %.9f;  h = %.6f" % (A, qq, U, R, h))
        law, miss = pell_chi4_law(8)
        say("  Pell mod 2^8: counts 1 + chi_-4 %s; balance miss %s = B1(chi_-4), the class-number datum of Q(i)" % (law, miss))
    if ask("class number of any quadratic field Q(sqrt D) from recurrences (Theorem H2*)? (y/n)", "n").lower().startswith("y"):
        DD = int(ask("fundamental discriminant D (try -420, -23, 136, 316, 5, 8, 12)", -420))
        h, ex = class_number_quadratic(DD)
        if DD > 0:
            t, u, nrm, R = ex
            say("  D = %d: unit (%d + %d sqrt D)/2, norm %+d, growth ratio of x(n+1) = %d x(n) %s x(n-1); R = %.9f; h = %.6f"
                % (DD, t, u, nrm, t, "+" if nrm < 0 else "-", R, h))
        else:
            say("  D = %d: B1(chi_D) from the rebuilt character = %.6f; h = %.6f" % (DD, ex, h))
        say("  2-adic readers: Pell -> chi_-4; 4x - x from (1,1) -> chi_-8 (law mod 2^8: %s); 3x + 3x - x from (1,1,7) -> chi_8 (law mod 2^8: %s)" % (chim8_reader_law(8), chi8_reader_law(8)))
    if ask("class number of the cyclic cubic field of conductor q from recurrences (Theorem C3)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 1 mod 3 (try 7, 163, 313, 4219)", 163))
        r = cubic_class_number(qq)
        if r:
            h, T, S, R, hR = r
            say("  cube classes from the order-3 orbit mod %d^4; cyclotomic-unit regulator h*R = %.9f" % (qq, hR))
            say("  root extraction depth h = %d; fundamental unit recurrence y(n+1) = %d y(n) - (%d) y(n-1) + y(n-2); R = %.9f" % (h, T, S, R))
        else:
            say("  no root found within the precision available (install mpmath for large q)")
    if HAVE_MP and ask("rigorous certificate for a cubic class number (Theorem C3*)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 1 mod 3 (try 7, 163, 313)", 163)); r = cubic_certificate(qq)
        say("  h = %d, fundamental unit x^3 %+d x^2 %+d x %+d; certified %s %s" % (r["h"], r["unit_poly"][1], r["unit_poly"][2], r["unit_poly"][3], r["certified"], r["parts"]))
    if HAVE_MP and ask("class number of the real cyclic quartic field of conductor q (saturation)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 1 mod 8 (try 17, 257; q above 200 is slow on a phone)", 257)); h, RE, RC, pols = quartic_class_number(qq)
        say("  cyclotomic regulator %.6f, unit regulator %.6f, h = %.6f; fundamental unit polynomials %s" % (RC, RE, h, pols))
    if HAVE_MP and ask("rigorous certificate for a real cyclic quartic class number (Theorem Q4R*)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 1 mod 8 (try 17, 257, 641)", 257)); r = quartic_certificate(qq)
        say("  h = %s (relation matrix %s); certified %s %s; every prime l <= %.0f checked" % (r["h"], r.get("X"), r["certified"], r["parts"], r.get("cap", 0)))
    if HAVE_MP and ask("certified class number of a real cyclic field of degree 3, 4 or 6 (Theorem H_n*)? (y/n)", "n").lower().startswith("y"):
        nn = int(ask("degree n (3, 4 or 6)", 6)); qq = int(ask("prime q with (q-1)/n even (try 13, 229, 313 for n = 6)", 229))
        r = cyclic_certificate(qq, nn)
        say("  h = %s; certified %s %s; every prime l <= %.0f checked (lambda_1 >= %.3f)" % (r["h"], r["certified"], r["parts"], r.get("cap", 0), r.get("m0", 0)))
    if ask("class number of an imaginary cyclic field of degree 4 or 6 (Theorem I_n)? (y/n)", "n").lower().startswith("y"):
        nn = int(ask("degree n (4 or 6)", 4)); qq = int(ask("prime q with (q-1)/n odd (try 389 for n = 4, 379 for n = 6)", 389))
        r = imaginary_cyclic_class_number(qq, nn)
        say("  h- = %s (exact, from orbit sums), h+ = %s (certified %s), h = %s" % (r["h_minus"], r["h_plus"], r["certified_plus"], r["h"]))
    if ask("relative class number as a product of norms (Theorem N; any even n)? (y/n)", "n").lower().startswith("y"):
        nn = int(ask("even degree n (e.g. 8, 10, 12, 16)", 10)); qq = int(ask("prime q with (q-1)/n odd (try n = 10: 271; n = 8: 233; n = 12: 157)", 271))
        r = relative_class_number(qq, nn)
        say("  h- = %s, factors by character order m: %s (first = h- of the 2-power subfield, others = norms N(x_m/2))" % (r["h_minus"], r["factors"]))
    if ask("divisibility statistics of the norm factors vs Cohen-Lenstra-Martinet (L2064)? (y/n)", "n").lower().startswith("y"):
        nn = int(ask("family n (4, 6 or 10)", 6)); qm = int(ask("conductors up to (try 20000)", 20000))
        cnt, rows = norm_factor_statistics(nn, qm)
        say("  %d fields" % cnt)
        for l, o, p_ in rows: say("  l = %2d: observed %.4f, predicted %.4f" % (l, o, p_))
    if HAVE_MP and ask("2-part link: sextic Eisenstein factor even <=> cubic class number even (Law P)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 7 mod 12 (try 163, 547, 607; 31 for an odd case)", 163)); r = two_part_link(qq)
        say("  F = N(x6/2) = %d (even %s); h(cubic subfield) = %d (even %s); agree %s" % (r["F"], r["F_even"], r["h3"], r["h3_even"], r["agree"]))
    if ask("harmonic links: 1/n, Fibonacci, 60/24, phi, pi, spirals (L2072)? (y/n)", "n").lower().startswith("y"):
        bb = int(ask("base b (10 gives 1/89; 2 gives exactly 1)", 10))
        for st, okv in harmonic_links(bb): say("  %s  %s" % ("VERIFIED" if okv else "FAILED  ", st))
    if ask("necklace ladder and spiral spectrum (L2076)? (y/n)", "n").lower().startswith("y"):
        for b_, n_, f_ in necklace_ladder(int(ask("bases up to", 12))): say("  base %2d: 1/%d = sum F_k/%d^(k+1)   factors %s" % (b_, n_, b_, f_))
        for D_, t_, u_ in ((5, 1, 1), (8, 2, 1), (13, 3, 1), (12, 4, 1)): say("  spiral of Q(sqrt %d): unit (%d + %d sqrt%d)/2, rate %.6f per radian" % (D_, t_, u_, D_, spiral_rate(D_, t_, u_)))
    if ask("2-adic pattern of the minus factor vs the real subfield (Law P*, L2080)? (y/n)", "n").lower().startswith("y"):
        nn = int(ask("degree n = 2l (try 14)", 14)); qq = int(ask("prime q with (q-1)/n odd (try 491, 239, 4019)", 491)); r = two_adic_pattern(qq, nn)
        say("  %d of the %d primes above 2 (degree %d) divide x/2: F even %s; predicted narrow h+ even %s (2-rank %d), wide h+ even %s" % (r["k"], r["g"], r["f"], r["F_even"], r["narrow_even_pred"], r["f"] * r["k"], r["wide_even_pred"]))
    if ask("how often is the real subfield's narrow class number even (Law S, L2084)? (y/n)", "n").lower().startswith("y"):
        for nn in (6, 10, 14, 18, 34, 46, 62):
            r = two_adic_heuristic(nn)
            say("  n = %2d: %d prime(s) above 2 of degree %d, self-conjugate %s; naive %.4f%s" % (nn, r["g"], r["f"], r["self_conjugate"], r["naive"], "" if r["tentative"] is None else ", suppressed (tentative) %.4f" % r["tentative"]))
    if ask("all character components of a composite-degree field (L2092)? (y/n)", "n").lower().startswith("y"):
        nn = int(ask("degree n = 2 x odd (try 30 or 42)", 30)); qq = int(ask("prime q with (q-1)/n odd (try 751, 1951, 3931)", 1951))
        for m_, (k_, g_, f_, sd_) in sorted(component_pattern(qq, nn).items()):
            say("  component m = %d: %d of %d primes above 2 (degree %d) divide x_m/2; self-dual %s" % (m_, k_, g_, f_, sd_))
    if ask("fast parity of a cyclic cubic class number, O(sqrt q) (L2096)? (y/n)", "n").lower().startswith("y"):
        qq = int(ask("prime q = 7 mod 12 (try 163 even, 31 odd, or something near 10^9)", 163)); ev, er, uv = cubic_parity_fast(qq)
        say("  x = %d + %d omega (lattice error %.1e): class number of the cubic field is %s" % (uv[0], uv[1], er, "EVEN" if ev else "odd"))
    if ask("minus-part number x = B_1,chi in O(sqrt q) for any degree n = 2l (L2100)? (y/n)", "n").lower().startswith("y"):
        nn = int(ask("degree n (6, 10, 14, ...)", 14)); qq = int(ask("prime q with (q-1)/n odd", 491)); cf, er = fast_minus_coordinates(qq, nn)
        r = two_adic_pattern(qq, nn) if qq < 10 ** 6 else None
        say("  x = %s in the basis zeta^k (rounding error %.1e)%s" % (cf, er, "" if r is None else "; primes above 2 dividing x/2: %d of %d" % (r["k"], r["g"])))
    if ask("Theorem U: x/2 from the signs of the cyclotomic unit; proved parity of h(K+) when 2 is primitive mod l (L2104)? (y/n)", "n").lower().startswith("y"):
        ll = int(ask("prime degree l (3, 5, 7, 11, 13)", 3)); qq = int(ask("prime q = 1 + 2l (mod 4l)", 163)); r = theorem_U(qq, ll)
        say("  identity x/2 = z/(1+z) s(z) mod 2 holds: %s; Phi_l | s: %s; h(K+) even (proved when 2 is primitive mod l): %s" % (r["identity_holds"], r["s_zero_mod_Phi"], r["h_plus_even_if_2_primitive"]))
    if ask("proved parity certificate for a real cyclic field of odd prime degree (Theorem R, L2108)? (y/n)", "n").lower().startswith("y"):
        ll = int(ask("odd prime degree l", 7)); qq = int(ask("prime q = 1 + 2l (mod 4l)", 491)); r = parity_certificate(qq, ll)
        say("  %d of %d primes above 2 divide x/2: narrow class number even = %s; class number even = %s (both proved, Theorems R and W)" % (r["k"], r["g"], r["narrow_even"], r["wide_even"]))
    if ask("2-rank bounds for the narrow class group from the minus part (Theorem M, L2112)? (y/n)", "n").lower().startswith("y"):
        ll = int(ask("odd prime degree l", 3)); qq = int(ask("prime q = 1 + 2l (mod 4l)", 163)); r = two_rank_bound(qq, ll)
        say("  v2(F) = %d: the narrow 2-rank of K+ is at most %d (proved); at least %d from the primes above 2" % (r["v2F"], r["rank_upper_bound"], r["rank_lower_bound"]))
    b = int(ask("base b for the wheel survey", 12))
    Pl, ml, Pr, mr = base_wheels(b)
    say("base %d: last-digit wheel %d positions (mirror %s); digit-root wheel %d positions (mirror %s)" % (b, Pl, ml, Pr, mr))
    good = [x for x in range(3, 101) if base_wheels(x)[1] and base_wheels(x)[3]]
    say("bases 3..100 where both wheels have the half-turn mirror (full quartets): %s" % good)
    log_check("recurrence_balance", dict(name=name, m=m, base=b), r)


# ---------------------------------------------------------------- dimension ladder (L1980): lattices and sphere packings
from fractions import Fraction as Fr
from itertools import permutations, product
import math
# ---------- Q(sqrt5) arithmetic: (a, b) = a + b*sqrt5
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
Z=(Fr(0),Fr(0)); ONE=(Fr(1),Fr(0)); HALF=(Fr(1,2),Fr(0))
PHI=(Fr(1,2),Fr(1,2)); PHIINV=(Fr(-1,2),Fr(1,2))      # phi = (1+sqrt5)/2, 1/phi = phi-1
def sc(x,c): return (x[0]*c, x[1]*c)
# ---------- quaternions over Q(sqrt5)
def qmul(p,q):
    a1,b1,c1,d1=p; a2,b2,c2,d2=q
    m=mul
    return (add(add(m(a1,a2),neg(m(b1,b2))),add(neg(m(c1,c2)),neg(m(d1,d2)))),
            add(add(m(a1,b2),m(b1,a2)),add(m(c1,d2),neg(m(d1,c2)))),
            add(add(m(a1,c2),neg(m(b1,d2))),add(m(c1,a2),m(d1,b2))),
            add(add(m(a1,d2),m(b1,c2)),add(neg(m(c1,b2)),m(d1,a2))))
def qnorm(p): 
    s=Z
    for x in p: s=add(s,mul(x,x))
    return s
def binary_icosahedral():
    E=[]
    for i in range(4):
        for s in (1,-1):
            v=[Z]*4; v[i]=(Fr(s),Fr(0)); E.append(tuple(v))
    for signs in product((1,-1),repeat=4): E.append(tuple((Fr(s,2),Fr(0)) for s in signs))
    base=[Z, HALF, sc(PHI,Fr(1,2)), sc(PHIINV,Fr(1,2))]          # (0, 1/2, phi/2, 1/(2phi))
    even=[p for p in permutations(range(4)) if sum(1 for i in range(4) for j in range(i+1,4) if p[i]>p[j])%2==0]
    for p in even:
        for s1,s2,s3 in product((1,-1),repeat=3):
            vals=[base[0], sc(base[1],s1), sc(base[2],s2), sc(base[3],s3)]
            E.append(tuple(vals[p[i]] for i in range(4)))
    return list(dict.fromkeys(E))
def hurwitz_units():
    E=[]
    for i in range(4):
        for s in (1,-1):
            v=[(Fr(0),Fr(0))]*4; v[i]=(Fr(s),Fr(0)); E.append(tuple(v))
    for signs in product((1,-1),repeat=4): E.append(tuple((Fr(s,2),Fr(0)) for s in signs))
    return E
def order_stats(G, mulf, one):
    from collections import Counter
    c=Counter()
    for g in G:
        x=g; k=1
        while x!=one: x=mulf(x,g); k+=1
        c[k]+=1
    return dict(sorted(c.items()))
# ---------- SL(2,p)
def sl2(p):
    return [(a,b,c,d) for a in range(p) for b in range(p) for c in range(p) for d in range(p) if (a*d-b*c)%p==1]
def m2(p): return lambda x,y:((x[0]*y[0]+x[1]*y[2])%p,(x[0]*y[1]+x[1]*y[3])%p,(x[2]*y[0]+x[3]*y[2])%p,(x[2]*y[1]+x[3]*y[3])%p)
# ---------- golden map and E8 from icosians
def g(x): return x[0]+x[1]          # a + b*sqrt5  ->  a + b
def ip8(p,q):
    s=Z
    for x,y in zip(p,q): s=add(s,mul(x,y))
    return g(s)
def binary_forms(D):
    """reduced positive definite forms ax^2+bxy+cy^2 with b^2-4ac = D < 0 (primitive), and the count of automorphs"""
    out=[]
    a=1
    while 3*a*a<=-D:
        for b in range(-a+1,a+1):
            if (b*b-D)%(4*a)==0:
                c=(b*b-D)//(4*a)
                if c>=a and math.gcd(math.gcd(a,abs(b)),c)==1 and not (b<0 and (a==c or abs(b)==a)): out.append((a,b,c))
        a+=1
    return out

def ladder_checks(full=False):
    R = {}
    I2 = binary_icosahedral(); H = hurwitz_units(); ONEQ = (ONE, Z, Z, Z)
    R["600-cell vertices (unit icosians)"] = len(I2)
    R["24-cell vertices (Hurwitz units) = kissing number of D4"] = len(H)
    R["SL(2,5) order statistics = 2I"] = order_stats(sl2(5), m2(5), (1, 0, 0, 1)) == order_stats(I2, qmul, ONEQ)
    R["SL(2,3) order statistics = 2T"] = order_stats(sl2(3), m2(3), (1, 0, 0, 1)) == order_stats(H, qmul, ONEQ)
    u = [q for q in I2 if q[0] == sc(PHI, Fr(1, 2))][0]; x, k = u, 1
    while x != ONEQ: x = qmul(u, x); k += 1
    R["Fibonacci Q^2 mod 5 <-> icosian cos 36 deg: order"] = k
    V = I2 + [tuple(mul(PHIINV, c) for c in q) for q in I2]
    W = V if full else V[:12]
    from collections import Counter
    prof = Counter(tuple(sorted(Counter(2 * ip8(v, w) for w in V).items())) for v in W)
    R["E8 roots built from golden numbers"] = len(set(V))
    R["E8 inner-product profile (-2,-1,0,1,2) per root"] = [list(dict(p).values()) for p in prof]
    R["class numbers = number of reduced planar lattices"] = all(len(binary_forms(-q)) == h for q, h in {7: 1, 23: 3, 47: 5, 71: 7}.items())
    return R

def clock_type(a, p):
    """conjugacy type of Q^2 = [[a^2+1, a], [a, 1]] in SL(2, p): identity (p | a: two-value regime),
    parabolic of order 2p (p | a^2+4: uniform regime), or semisimple (otherwise: never balanced, Prop X). L1984."""
    M = ((a * a + 1) % p, a % p, a % p, 1); x, k = M, 1
    f = lambda X, Y: ((X[0]*Y[0]+X[1]*Y[2]) % p, (X[0]*Y[1]+X[1]*Y[3]) % p, (X[2]*Y[0]+X[3]*Y[2]) % p, (X[2]*Y[1]+X[3]*Y[3]) % p)
    while x != (1, 0, 0, 1): x = f(x, M); k += 1
    kind = "identity (two-value regime)" if a % p == 0 else ("parabolic (uniform regime)" if (a * a + 4) % p == 0 else "semisimple (no balance at p)")
    return k, kind

def class_number_bridge(q):
    """q = 3 mod 4 prime with ord_q(10) = (q-1)/2: digit sum of 1/q = 4.5 (L - h(-q)) (Girstmair; re-checked L1984)."""
    L = mult_order(10, q); r, ds = 1, 0
    for _ in range(L): ds += 10 * r // q; r = 10 * r % q
    h = len(binary_forms(-q))
    return L, ds, h, 2 * ds == 9 * (L - h)

def legendre(x, q):
    x %= q
    return 0 if x == 0 else (1 if pow(x, (q - 1) // 2, q) == 1 else -1)

def partial_sum_dictionary(q, b=10):
    """L1988: A(c) = sum_{z<=c} (z/q).  Base-b identity: sum_{j=1}^{b-1} A(floor(jq/b)) = (b - (b/q)) h(-q)  (q = 3 mod 4, q > 3).
    Recurrence side (Theorem P): the quadratic half at e = 2f+1 is balanced only if its centre digit c has A(c) = h(-q)."""
    Ac = [0]
    for z in range(1, q): Ac.append(Ac[-1] + legendre(z, q))
    h = len(binary_forms(-q))
    SA = sum(Ac[j * q // b] for j in range(1, b))
    centres = [c for c in range(q) if Ac[c] == h]
    return dict(q=q, h=h, base=b, sum_A_at_fractions=SA, predicted=(b - legendre(b, q)) * h, holds=SA == (b - legendre(b, q)) * h, balancing_centres=centres)

def quad_mean_closed(q, k, c, lam):
    """L1992 Theorem P'': mean of lr(c + lam*u^2 mod q^k) over u = (q^k-1)/2 + sum_j q^j (d_{2j+1} - (q-1)/2)
    + chi(lam) sum_j q^j (B1 - chi(-1) A(d_{2j})), d_i = base-q digits of c."""
    from fractions import Fraction as F
    B1 = F(sum(legendre(y, q) * y for y in range(1, q)), q)
    Ac = [0]
    for z in range(1, q): Ac.append(Ac[-1] + legendre(z, q))
    d = lambda i: (c // q ** i) % q
    odd = sum(q ** j * (d(2 * j + 1) - F(q - 1, 2)) for j in range(k) if 2 * j + 1 < k)
    char = sum(q ** j * (B1 - legendre(-1, q) * Ac[d(2 * j)]) for j in range(k) if 2 * j < k)
    return F(q ** k - 1, 2) + odd + legendre(lam, q) * char

def relative_class_number_from_digits(q):
    """Girstmair (1994): for prime q with L = ord_q(10) odd, the digit sums D(a) of the g = (q-1)/L cosets of 1/q give
    B_{1,chi} = (1/9) sum_a chi(a) (D(a) - 4.5 L) for the odd characters trivial on <10>, and h^-(K) = 2 prod(-B_{1,chi}/2),
    K = the degree-g subfield of Q(zeta_q).  Checked against PARI on 33 fields in round L1992."""
    import cmath
    L = mult_order(10, q); g = (q - 1) // L
    if L % 2 == 0: return None
    pr = next(x for x in range(2, q) if mult_order(x, q) == q - 1)
    ind, x = {}, 1
    for i in range(q - 1): ind[x] = i; x = x * pr % q
    seen, D = set(), {}
    for a in range(1, q):
        if a in seen: continue
        r, s = a, 0
        for _ in range(L): s += 10 * r // q; seen.add(r); r = 10 * r % q
        D[a] = s
    prod = 1
    for kk in range(q - 1):
        if (kk * ind[10]) % (q - 1) == 0 and (kk * ind[q - 1]) % (q - 1) != 0:
            B = sum(cmath.exp(2j * cmath.pi * kk * ind[a] / (q - 1)) * (D[a] - 4.5 * L) for a in D) / 9
            prod *= -B / 2
    return g, round((2 * prod).real)

def menu_ladder():
    say("Dimension ladder: 1D squares (Theorem Q) -> 2D lattices (class numbers) -> 4D 24-cell / 600-cell (Fibonacci mod 3, 5)")
    say("-> 8D E8 (densest, Viazovska 2016) built from golden-ratio quaternions -> 24D Leech (literature: Tits 1980).")
    for k, v in ladder_checks(full=ask("full E8 check over all 240 roots? (y/n)", "n").lower().startswith("y")).items(): say("  %s: %s" % (k, v))
    say("Packing densities: A2 %.4f, D4 %.4f, E8 %.4f, Leech %.6f" % (math.pi / math.sqrt(12), math.pi ** 2 / 16, math.pi ** 4 / 384, math.pi ** 12 / 479001600))
    say("Kissing numbers: 2 (1D), 6 (2D), 12 (3D), 24 (4D), 240 (8D), 196560 (24D)")
    a = int(ask("your clock x(n+1) = a x(n) + x(n-1): a =", 1))
    for p in (3, 5):
        k, kind = clock_type(a, p)
        poly = "24-cell" if p == 3 else "600-cell"
        say("  mod %d: Q^2 has order %d in SL(2,%d) = symmetries of the %s: %s; it splits the %d vertices into %d rings of %d"
            % (p, k, p, poly, kind, 24 if p == 3 else 120, (24 if p == 3 else 120) // k, k))
    q = int(ask("class-number bridge: a prime q = 3 mod 4 with ord_q(10) = (q-1)/2, e.g. 31, 43, 71, 163", 31))
    L, ds, h, okb = class_number_bridge(q)
    say("  1/%d: period %d, digit sum %d; h(-%d) = %d; digit sum = 4.5 x (period - h): %s" % (q, L, ds, q, h, okb))
    for b in (10, 12, 2):
        d = partial_sum_dictionary(q, b)
        say("  base %d: sum of the Legendre running sum A at the %d fractions j/%d of q = %d; (b - (b/q)) h = %d: %s"
            % (b, b - 1, b, d["sum_A_at_fractions"], d["predicted"], d["holds"]))
    say("  recurrence centres c with A(c) = h(-q) (the only centre digits that can balance, Theorem P): %s" % partial_sum_dictionary(q)["balancing_centres"])
    q2 = int(ask("relative class number from the digits of 1/q: a prime with odd period, e.g. 79, 173, 751, 1609", 751))
    r = relative_class_number_from_digits(q2)
    say("  %s" % ("period of 1/%d is even: no odd characters on <10> (h^- formula not applicable)" % q2 if r is None else
        "1/%d: coset digit sums give the relative class number of the degree-%d subfield of Q(zeta_%d): h^- = %d" % (q2, r[0], q2, r[1])))

# ---------------------------------------------------------------- menu
def ask(prompt, default=None):
    v = input(prompt + (" [%s]" % default if default is not None else "") + ": ").strip()
    return v if v else ("" if default is None else str(default))

def menu_recip():
    n = int(ask("Denominator n", 97)); s, L, blk = recip(n)
    d = ask("Digit to locate", 5)
    say("1/%d: preperiod %d, period %d%s" % (n, s, L, " (terminates)" if L == 0 else ""))
    say("first %d digits (preperiod + one period): %s" % (len(blk), blk if len(blk) <= 400 else blk[:400] + "..."))
    say("digit sum of that block: %d; of one period: %s" % (sum(map(int, blk)), sum(map(int, blk[s:])) if L else "-"))
    say("positions of %s: %s" % (d, [i + 1 for i, c in enumerate(blk) if c == d][:60]))
    m = midy(n); say("Midy (halves of the period sum to 9s): %s" % ("n/a" if m is None else m))
    log_check("reciprocal", dict(n=n), dict(preperiod=s, period=L, digit_sum=sum(map(int, blk))))

def menu_position():
    say("Examples of X: 1/89   22/7   pi   e   phi   sqrt(2)   sqrt(17)   log(2)   zeta(3)")
    X = ask("X", "pi"); S = ask("substring S", "1231"); N = ask("claimed position N (blank = just find it)", "")
    if N:
        r = check_claim(X, S, int(N)); say("%s contains %s at %s? -> %s" % (X, S, N, r["verdict"]))
    else:
        p, how = position(X, S); r = dict(X=X, S=S, first_position=p, method=how)
        say("first position of %s in %s: %s" % (S, X, p if p else "not in the first %d digits" % LIMIT))
    say("method:", r["method"]); log_check("position", dict(X=X, S=S, N=N), r)

def menu_audit():
    path = ask("Path of the master-list .txt file", os.path.join(OUT, "master.txt"))
    text = open(path, encoding="utf-8", errors="replace").read()
    summ, rows = audit_list(text)
    say("entries %d, distinct n %d, range %s, missing in 2..2000: %s, duplicates %s" % (summ["entries"], summ["distinct"], summ["range"], summ["missing_2_to_2000"], summ["duplicates"]))
    say("claims checked %d, new problems %d, problems already annotated %d" % (summ["claims"], summ["problems"], summ["annotated"]))
    for r in rows:
        if r["status"] == "MISMATCH": say("  line %d 1/%d %s: %s" % (r["line"], r["n"], r["kind"], r.get("note", "")))
    save_report("Master list audit", dict(summary=summ, claims=rows, file=path))

def menu_db():
    lo = int(ask("from n", 2)); hi = int(ask("to n", 2055))
    k, sec = build_db(lo, hi); say("built %d rows in %.1f s -> %s" % (k, sec, DB_PATH))
    k, bad = verify_db(); say("retrieval check: %d rows recomputed, %d mismatches %s" % (k, len(bad), bad[:10]))

def menu_adapter():
    lo = int(ask("from n", 2)); hi = int(ask("to n", 2055))
    st, sk, sb = adapter(lo, hi)
    for kk in ("groups", "records_sent", "wire_bytes", "burst_corrected", "heavy_rejected", "tamper_rejected",
               "records_received", "records_expected", "recompute_failures", "skipped", "status"):
        say("  %s: %s" % (kk, st[kk]))
    save_report("GaryPhone adapter", dict(stats=st, skipped_examples=sk, recompute_failures=sb))

# ---------------- L2808: DNA strand (base-4 reciprocals, gene finder, DNA storage) ----------------
DNA4 = "ACGT"                       # base-4 digit d -> letter; d + (3-d) = 3 pairs A-T and C-G (Watson-Crick)
WC = {"A": "T", "T": "A", "C": "G", "G": "C"}

def dna_recip(p):
    """Base-4 expansion of 1/p (p odd, coprime to 2) as a DNA string of one full period."""
    T = mult_order(4, p); r = 1; out = []
    for _ in range(T):
        r *= 4; out.append(DNA4[r // p]); r %= p
    return "".join(out)

def dna_midy(p):
    """L2664: True if 1/p in base 4 has even period T and its second half is the Watson-Crick complement of the first half
    (equivalently 4^(T/2) = -1 mod p); None if the period is odd."""
    s = dna_recip(p); T = len(s)
    if T % 2: return None
    h = T // 2
    return all(WC[a] == b for a, b in zip(s[:h], s[h:]))

def dna_midy_count(limit=5000):
    ps = [q for q in range(3, limit) if all(q % d for d in range(2, int(q ** 0.5) + 1))]
    k = sum(1 for q in ps if pow(4, mult_order(4, q) // 2, q) == q - 1 and mult_order(4, q) % 2 == 0)
    return k, len(ps)

def menu_dna_recip():
    say("1/p written in base 4 as DNA (0=A 1=C 2=G 3=T). Midy in base 4 means the strand's second half pairs with its first half.")
    p = int(ask("odd number p", 17))
    if p % 2 == 0: say("p must be odd"); return
    s = dna_recip(p); T = len(s); m = dna_midy(p)
    say("  period %d: %s%s" % (T, s[:120], "..." if T > 120 else ""))
    if m is None: say("  odd period: no halves to pair")
    else:
        h = T // 2
        say("  first half : %s%s" % (s[:h][:60], "..." if h > 60 else ""))
        say("  second half: %s%s" % (s[h:][:60], "..." if h > 60 else ""))
        say("  Watson-Crick paired halves (base-4 Midy): %s" % ("YES" if m else "NO"))
    if ask("count base-4 Midy primes below a limit? (y/n)", "n").lower().startswith("y"):
        lim = int(ask("limit", 5000)); k, n = dna_midy_count(lim)
        say("  odd primes below %d: %d; base-4 Midy (Watson-Crick paired): %d" % (lim, n, k))
    log_check("dna_recip", dict(p=p), dict(period=T, midy=m))

def _here():
    return os.path.dirname(os.path.abspath(__file__)) if "__file__" in globals() else os.getcwd()

def _companion(name):
    import runpy
    path = os.path.join(_here(), name)
    if _here() not in sys.path: sys.path.insert(0, _here())       # companions import each other (ecc -> codec)
    need = [name] + (["dcf_dna_codec.py"] if name == "dcf_dna_ecc.py" else [])
    miss = [x for x in need if not os.path.exists(os.path.join(_here(), x))]
    if miss: name = ", ".join(miss)
    if miss:
        say("Put %s in the same folder as this toolkit (%s) and try again." % (name, _here())); return None
    return runpy.run_path(path, run_name="dcf_companion")

# ---------------------------------------------------------------- L3277: number checks + energy-metal tier
MONSTER_ORDER = {2: 46, 3: 20, 5: 9, 7: 6, 11: 2, 13: 3, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1, 41: 1, 47: 1, 59: 1, 71: 1}

def supersingular_primes():
    """primes dividing the order of the Monster group (Ogg's 15 supersingular primes, OEIS A002267)"""
    M = 1
    for p, e in MONSTER_ORDER.items(): M *= p ** e
    return [p for p in range(2, 200) if all(p % d for d in range(2, int(p ** 0.5) + 1)) and M % p == 0]

def euler_lucky(upto=1000):
    """p with n^2 + n + p prime for n = 0 .. p-2 (L3241: 2, 3, 5, 11, 17, 41)"""
    isp = lambda m: m > 1 and all(m % d for d in range(2, int(m ** 0.5) + 1))
    return [p for p in range(2, upto) if isp(p) and all(isp(n * n + n + p) for n in range(p - 1))]

def first_denominator_all(targets, upto=5000):
    """first k >= 2 whose 1/k contains every target string (repeats counted)."""
    w = max(len(t) for t in targets)
    for k in range(2, upto + 1):
        s, L, blk = recip(k); d = digits(1, k, s + max(L, 1) + w + 1)
        if all(t in d for t in targets): return k
    return None

def menu_numbers():
    c = ask("f = first 1/n containing a digit string (or several, comma separated), s = supersingular (Monster) primes, l = Euler lucky numbers", "f").lower()
    if c.startswith("s"):
        S = supersingular_primes(); say("Supersingular primes (divide the Monster's order):", S)
        x = ask("check numbers (comma separated)", "17, 41, 43, 47, 79, 163, 401")
        for v in [int(t) for t in re.findall(r"\d+", x)]: say("  %d: %s" % (v, "SUPERSINGULAR" if v in S else "not supersingular"))
    elif c.startswith("l"):
        say("Euler lucky numbers below 1000 (n^2+n+p prime for n = 0..p-2):", euler_lucky())
        say("  4p - 1 for each (odd Heegner numbers):", [4 * p - 1 for p in euler_lucky()])
    else:
        t = [x.strip() for x in ask("digit string(s)", "581").split(",") if x.strip()]
        k = first_denominator_all(t, int(ask("search n up to", 5000)))
        if k is None: say("  none found")
        else:
            s, L, blk = recip(k); say("  first n: %d  (1/%d: preperiod %d, period %d, block %s%s)" % (k, k, s, L, blk[:60], "..." if len(blk) > 60 else ""))
            for x in t: say('  "%s" first at position %d of 1/%d' % (x, position("1/%d" % k, x)[0], k))
        say("  Base rate (L3277, all 1000 three-digit strings): median first n = 71; 20 strings first appear in 1/43 alone. Record only with this check (DCF rule).")
    log_check("numbers", dict(choice=c), {})

def menu_energy():
    """L3277: gene finder (if needed) then the energy-metal profile (dcf_redox.py)."""
    r = _companion("dcf_redox.py")
    if not r: return
    def _is_genome(f):
        try:
            with open(os.path.join(_here(), f), errors="replace") as h: head = h.read(300).lstrip()
            return head.startswith("LOCUS") or head.startswith(">")
        except Exception: return False
    cands = sorted(f for f in os.listdir(_here()) if os.path.isfile(os.path.join(_here(), f)) and not f.endswith(".py") and _is_genome(f))
    say("Genome files here: %s" % (", ".join(cands[:20]) or "none"))
    path = ask("genome file name or full path", cands[0] if cands else "")
    if not os.path.isabs(path): path = os.path.join(_here(), path)
    gff = os.path.join(OUT, os.path.splitext(os.path.basename(path))[0] + ".gff3")
    if not os.path.exists(gff):
        g = _companion("dcf_genefinder_mobile.py")
        if not g: return
        say("Running the gene finder first (a few minutes on a phone) ..."); g["main"](path, "auto", gff)
    d = r["profile"](path, gff); say(r["report"](d, os.path.basename(path)))
    say("Not for medical use. Blind record: 14 of 16 genomes in the right tier (L3269/L3273).")
    log_check("energy", dict(file=os.path.basename(path)), dict(tier=d["tier"], ladder=round(d["ladder"], 4)))

def selftest_L3277(ok):
    ok("L3269 first n whose 1/n contains 581 is 43 (positions 6-8)", first_denominator_all(["581"], 200) == 43 and position("1/43", "581")[0] == 6)
    ok("L3269 first n containing both 11 and 88 is 17; 1/43 period 21, period digit sum 90",
       first_denominator_all(["11", "88"], 200) == 17 and recip(43)[1] == 21 and sum(map(int, recip(43)[2])) == 90)
    ok("L3269 supersingular primes = 2 3 5 7 11 13 17 19 23 29 31 41 47 59 71",
       supersingular_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 47, 59, 71])
    ok("L3241 Euler lucky numbers below 200 = 2 3 5 11 17 41; 4*41-1 = 163", euler_lucky(200) == [2, 3, 5, 11, 17, 41] and 4 * 41 - 1 == 163)

def _pick_file(prompt, test):
    cands = []
    for f in sorted(os.listdir(_here())):
        q = os.path.join(_here(), f)
        if os.path.isfile(q) and not f.endswith(".py") and test(q): cands.append(f)
    say("Files here: %s" % (", ".join(cands[:20]) or "none"))
    path = ask(prompt, cands[0] if cands else "")
    return path if os.path.isabs(path) else os.path.join(_here(), path)

def _head(q, n=300):
    try:
        if q.endswith(".gz"):
            import gzip
            with gzip.open(q, "rt", errors="replace") as h: return h.read(n).lstrip()
        with open(q, errors="replace") as h: return h.read(n).lstrip()
    except Exception: return ""

def menu_motifs():
    """L3297: scan a genome (after the gene finder) or an mRNA / protein FASTA for DCF motifs (hedgehog, voltage sensor, ladder ...)."""
    r = _companion("dcf_motif_scan.py")
    if not r: return
    for k, v in r["PRESETS"].items(): say("  %-11s %s  [%s]" % (k, v[1], v[2]))
    path = _pick_file("genome / mRNA / protein file", lambda q: _head(q)[:1] == ">" or _head(q).startswith("LOCUS"))
    gff = None
    if _head(path).startswith("LOCUS"):
        gff = os.path.join(OUT, os.path.splitext(os.path.basename(path))[0] + ".gff3")
        if not os.path.exists(gff):
            g = _companion("dcf_genefinder_mobile.py")
            if not g: return
            say("Running the gene finder first (a few minutes on a phone) ..."); g["main"](path, "auto", gff)
    sel = ask("motifs (comma separated names, or 'all')", "all")
    custom = ask("optional custom motif (regular expression, blank for none)", "")
    names = None if sel.strip().lower() == "all" else [x.strip() for x in sel.split(",") if x.strip() in r["PRESETS"]]
    say(r["report"](path, gff, names, custom or None))
    log_check("motifs", dict(file=os.path.basename(path), motifs=sel), {})

def menu_exonmap():
    """L3297: place an mRNA on a chromosome slice (exons, introns, strand, chromosome coordinates)."""
    r = _companion("dcf_exonmap.py")
    if not r: return
    say("Download a chromosome slice and the mRNA as FASTA (see the L3297 report for links), then pick them here.")
    region = _pick_file("chromosome slice (FASTA)", lambda q: _head(q)[:1] == ">")
    mrna = _pick_file("mRNA (FASTA)", lambda q: _head(q)[:1] == ">")
    txt, d = r["report"](region, mrna)
    say(txt); log_check("exonmap", dict(region=os.path.basename(region), mrna=os.path.basename(mrna)), dict(strand=d["strand"], exons=len(d["exons"])))

IHH_PROTEIN = ("MSPARLRPRLHFCLVLLLLLVVPAAWGCGPGRVVGSRRRPPRKLVPLAYKQFSPNVPEKTLGASGRYEGKIARSSERFKELTPNYNPDIIFKDEENTGADRLMTQRCKDRLNSLAISVMNQWPGVKLRVTEGWDEDGHHSEESLHYEGRAVDITTSDRDRNKYGLLARLAVEAGFDWVYYESKAHVHCSVKSEHSAAAKTGGCFPAGAQVRLESGARVALSAVRPGDRVLAMGEDGSPTFSDVLIFLDREPHRLRAFQVIETQDPPRRLALTPAHLLFTADNHTEPAARFRATFASHVQPGQYVLVAGVPGLQPARVAAVSTHVALGAYAPLTKHGTLVVEDVVASCFAAVADHHLAQLAFWPLRLFHSLAWGSWTPGEGVHWYPQLLYRLGRLLLEEGSFHPLGMSGAGS")

def selftest_L3297(ok):
    m = re.search(r"H[YF]EGRA[VI]D.{40,80}GCF", IHH_PROTEIN)
    ok("L3297 hedgehog motif: human IHH (411 aa, NM_002181) zinc site at aa 145, G-C-F self-cutting site at aa 202",
       len(IHH_PROTEIN) == 411 and m is not None and m.start() + 1 == 145 and IHH_PROTEIN.find("GCF") + 1 == 202)
    r = _companion("dcf_exonmap.py") if os.path.exists(os.path.join(_here(), "dcf_exonmap.py")) else None
    if r is None:
        ok("L3297 exon mapper (skipped: dcf_exonmap.py not in this folder)", True); return
    import random, tempfile
    rng = random.Random(11); rnd = lambda n: "".join(rng.choice("ACGT") for _ in range(n))
    mrna = rnd(900); g = mrna[:250] + "GT" + rnd(1500) + "AG" + mrna[250:600] + "GT" + rnd(800) + "AG" + mrna[600:]
    region = rnd(2000) + r["rc"](g) + rnd(1000)
    d = tempfile.mkdtemp(); a = os.path.join(d, "reg.fa"); b = os.path.join(d, "m.fa")
    open(a, "w").write(">SYN:500001-%d\n%s\n" % (500000 + len(region), region)); open(b, "w").write(">m\n%s\n" % mrna)
    txt, res = r["report"](a, b)
    ex = res["exons"]
    ok("L3297 exon mapper: synthetic 3-exon gene on the minus strand recovered (exons 250/350/300 nt, span exact, GT..AG)",
       res["strand"] == "-" and [e[1] - e[0] for e in ex] == [250, 350, 300] and res["span"] == (502001, 502000 + len(g)))

def menu_genefinder():
    g = _companion("dcf_genefinder_mobile.py")
    if not g: return
    cands = [f for f in os.listdir(_here()) if f.lower().endswith((".gb", ".gbk", ".gbff", ".fna", ".fasta", ".fa", ".txt", ".html"))]
    say("Genome files here: %s" % (", ".join(cands[:20]) or "none (a GenBank download saved as .txt or .html works too)"))
    path = ask("genome file name or full path", cands[0] if cands else "")
    if not os.path.isabs(path): path = os.path.join(_here(), path)
    t = ask("genetic code table (auto, 11, 4, 2, 3, 5, 9)", "auto")
    out = os.path.join(OUT, os.path.splitext(os.path.basename(path))[0] + ".gff3")
    g["main"](path, t, out)
    say("Outputs (gff3, frameshifts, phasevar, islands) are in", OUT)
    log_check("genefinder", dict(file=os.path.basename(path), table=t), dict(out=out))

def menu_dna_storage():
    """Needs dcf_dna_ecc.py AND dcf_dna_codec.py in the toolkit's folder."""
    e = _companion("dcf_dna_ecc.py")
    if not e: return
    c = ask("e = encode a file, d = decode strands, n = noise drill", "n").lower()
    if c.startswith("e"):
        path = ask("file to store", "")
        data = open(path, "rb").read(); st = e["encode"](data)
        dst = os.path.join(OUT, os.path.basename(path) + ".dna.txt")
        with open(dst, "w") as fh:
            fh.write("# dcf_dna_ecc v6 strands; bytes=%d\n" % len(data)); fh.write("\n".join(st) + "\n")
        say("  %d bytes -> %d strands of %d nt (%.3f bits/nt) -> %s" % (len(data), len(st), len(st[0]), 8 * len(data) / sum(map(len, st)), dst))
    elif c.startswith("d"):
        path = ask("strands file (.dna.txt)", "")
        lines = open(path).read().split("\n"); n = int(lines[0].split("bytes=")[1])
        data = e["decode"]([l for l in lines[1:] if l.strip()], n)
        if data is None: say("  decode failed (too many damaged strands)"); return
        dst = path.replace(".dna.txt", "") + ".restored"; open(dst, "wb").write(data); say("  restored %d bytes -> %s" % (len(data), dst))
    else:
        import random
        rate = float(ask("per-base error % (substitutions 60 / deletions 20 / insertions 20)", 5)) / 100
        reads = int(ask("reads per strand", 10)); kb = int(ask("test data size in bytes", 2400))
        rng = random.Random(2808); data = bytes(rng.randrange(256) for _ in range(kb)); st = e["encode"](data); L = len(st[0])
        pool = [e["corrupt3"](x, 0.6 * rate, 0.2 * rate, 0.2 * rate, rng) for x in st for _ in range(reads)]; rng.shuffle(pool)
        t0 = time.time(); cons = [x for x in (e["consensus4"](gr, L) for gr in e["clusters"](pool) if len(gr) >= 2) if x]
        ok = e["decode"](cons, len(data)) == data
        say("  %d strands, %d shuffled unlabelled reads at %.1f%% error: file %s in %.0f s" % (len(st), len(pool), 100 * rate, "RECOVERED" if ok else "LOST", time.time() - t0))
        log_check("dna_drill", dict(rate=rate, reads=reads, bytes=kb), dict(recovered=ok))

# ---------------- L2852: theorems proved L2422-L2848 that were not yet in the toolkit ----------------
from fractions import Fraction as _Fr
from math import gcd as _gcd

def _ord(b, m):
    if m == 1: return 1
    k, v = 1, b % m
    while v != 1: v = v * b % m; k += 1
    return k

def period_digits(n, b=10):
    """repetend of 1/n in base b (strict period, after the pre-period)."""
    m = n
    for q in range(2, b + 1):
        if b % q == 0:
            while m % q == 0: m //= q
    pre = 0; r = 1 % n; seen = {}
    out = []
    while r not in seen:
        seen[r] = len(out); r *= b; out.append(r // n); r %= n
    s = seen[r]
    return out[s:]

def canon(ds):
    s = ''.join(map(str, ds)); return min(s[i:] + s[:i] for i in range(len(s))) if s else ''

def thm_25_lemma(m, amax=4, bmax=4):
    """L2522: repetend of 1/(2^a 5^b m) depends only on (b - a) mod d(m), d(m) = order of 2 modulo <10> in (Z/m)*.
    Returns True if equal classes give equal canonical repetends and different classes give different ones."""
    reps = {}
    sub = set(); v = 1
    while True:
        sub.add(v); v = v * 10 % m
        if v == 1: break
    d = 1; v = 2 % m
    while v not in sub: v = v * 2 % m; d += 1
    for a in range(amax + 1):
        for b in range(bmax + 1):
            c = canon(period_digits(2 ** a * 5 ** b * m)); reps.setdefault((b - a) % d, set()).add(c)
    return all(len(v) == 1 for v in reps.values()) and len(set(min(v) for v in reps.values())) == len(reps)

def least_n_all_strings(m, nmax):
    """L2515: max over m-digit strings s of the least n whose (cyclic) expansion of 1/n contains s."""
    need = {str(i).zfill(m) for i in range(10 ** m)}; worst = 0
    for n in range(2, nmax + 1):
        ds = period_digits(n)
        if not ds: continue
        s = ''.join(map(str, ds)); s = s + s[:m - 1] if len(s) >= 1 else s
        # include pre-period-free cyclic reading (as L2515/T3): repetend read cyclically
        found = {s[i:i + m] for i in range(len(ds))} & need
        if found: need -= found; worst = n
        if not need: return worst
    return None

def variance_dedekind(p, b=10):
    """L2609 (Dedekind-sum form, re-derived): for a full-reptend prime p in base b the digit variance of the period is
    [ (b^2+1)·Σr² − 2b·p²(s(b,p) + (p−1)/4) ] / (p²(p−1)) − ((b−1)/2)², with Σr² = (p−1)p(2p−1)/6 and
    s(b,p) the Dedekind sum. Returns (formula, direct) as exact fractions."""
    s = sum(_Fr(r, p) - _Fr(1, 2) for r in []) 
    s = sum((_Fr(r, p) - _Fr(1, 2)) * (_Fr(b * r % p, p) - _Fr(1, 2)) for r in range(1, p))
    S2 = _Fr((p - 1) * p * (2 * p - 1), 6)
    f = ((b * b + 1) * S2 - 2 * b * p * p * (s + _Fr(p - 1, 4))) / (p * p * (p - 1)) - _Fr(b - 1, 2) ** 2
    ds = period_digits(p, b); mu = _Fr(sum(ds), len(ds))
    direct = _Fr(sum(x * x for x in ds), len(ds)) - mu * mu
    return f, direct

def casting_out(p, q):
    """L2641 (q = 3, Theorem D) / L2645 (Theorem D_q): if q | T and gcd(p, 10^q − 1) = 1, then
    Σ_{i=0}^{q−1} 10^i · S_i ≡ 0 (mod 10^q − 1), where S_i = sum of period digits d_j with (T − j) ≡ i (mod q)."""
    ds = period_digits(p); T = len(ds)
    if T % q or _gcd(p, 10 ** q - 1) != 1: return None
    S = [0] * q
    for j, d in enumerate(ds, 1): S[(T - j) % q] += d
    return sum(10 ** i * S[i] for i in range(q)) % (10 ** q - 1) == 0

def clock_period(n, b=10):
    """L2656/L2660: period of Gary's reduction clock (digit-sum phase mod b−1) = (b−1)·T / gcd(S, b−1)."""
    ds = period_digits(n, b); T = len(ds); S = sum(ds)
    return (b - 1) * T // _gcd(S, b - 1), T

def theorem_P3(n):
    """L2660 Theorem P3 (base 10): clock period = T·3^min(2, max(0, a − t)), n = 3^a·m, t = v3(ord_m 10)."""
    a, m = 0, n
    while m % 3 == 0: m //= 3; a += 1
    om = _ord(10, m) if m > 1 else 1; t = 0
    while om % 3 == 0: om //= 3; t += 1
    T = _ord(10, n)
    return T * 3 ** min(2, max(0, a - t))

def self_period_rule(n, b):
    """L2660 base-b rule: clock period == n  <=>  every prime of n divides b−1 (n coprime to b), and not (b ≡ 3 mod 4 and 4 | n)."""
    m = n; q = 2; ok = _gcd(n, b) == 1
    while m > 1 and ok:
        if m % q == 0:
            ok = (b - 1) % q == 0
            while m % q == 0: m //= q
        q += 1
    return ok and not (b % 4 == 3 and n % 4 == 0)

def run_bound_ok(n, b):
    """L2833 run-length lemma: in a/n (gcd(n,b)=1) a run of k equal digits d needs b^k < n (d = 0, b−1) or
    b^k <= max(d, b−1−d)·n. Checks every a/n."""
    seen = bytearray(n)
    for a in range(1, n):
        if seen[a]: continue
        r = a; seq = []
        while not seen[r]: seen[r] = 1; r *= b; seq.append(r // n); r %= n
        L = len(seq); s = seq + seq; i = 0
        while i < L:
            j = i
            while j + 1 < i + L and s[j + 1] == s[i]: j += 1
            k = j - i + 1; d = s[i]
            if not ((b ** k < n) if d in (0, b - 1) else (b ** k <= max(d, b - 1 - d) * n)): return False
            i = j + 1
    return True

def real_subfield_wieferich(p, k):
    """L2505 Theorem R for k = 8: p ≡ −1 (mod 8) is a detector hit iff (2 − c)^(p−1) ≡ 1 mod p² for a root c of
    c² = 2 (c = ζ8 + ζ8⁻¹ = √2) in Z/p². Returns the set of booleans over the two roots."""
    assert k == 8
    c = next(x for x in range(p) if (x * x - 2) % p == 0); mod = p * p
    for _ in range(6): c = (c - (c * c - 2) * pow(2 * c, -1, mod)) % mod      # Hensel lift
    return {pow((2 - c) % mod, p - 1, mod) == 1, pow((2 + c) % mod, p - 1, mod) == 1}

def bal_count(a, e):
    """Note B: number of balanced orbits of y(n+2) = a·y(n+1) + y(n) modulo 2^e (orbit mean (2^e−1)/2)."""
    m = 2 ** e; seen = set(); c = 0
    for x in range(m):
        for y in range(m):
            if (x, y) in seen: continue
            S = P = 0; u, w = x, y
            while (u, w) not in seen: seen.add((u, w)); S += u; P += 1; u, w = w, (a * w + u) % m
            c += (2 * S == (m - 1) * P)
    return c

def all_strings_least_n(k, nmax=2000):
    """L2436 b(k): least n whose period of 1/n (read cyclically) contains every k-digit string."""
    need = 10 ** k
    for n in range(2, nmax + 1):
        ds = period_digits(n)
        if len(ds) < need: continue
        t = ''.join(map(str, ds)); t2 = t + t[:k - 1]
        if len({t2[i:i + k] for i in range(len(t))}) == need: return n
    return None

def rev_triangular(N):
    """L2422: n with n*rev(n) = T_rev(n) (T_r = r(r+1)/2), i.e. rev(n) = 2n - 1; family 4*10^k - 3."""
    return [n for n in range(1, N) if int(str(n)[::-1]) == 2 * n - 1]

# ---------------- L2853: batch-3 theorems (reduction chapter, clock spectrum, class-number digit sums, legacy items) ----------------
import cmath as _cm
from math import gcd as _g2

def _ord2(b, m):
    if m == 1: return 1
    k, v = 1, b % m
    while v != 1: v = v * b % m; k += 1
    return k

def _per(n, b=10):
    """repetend digits of 1/n in base b (n coprime to b)."""
    T = _ord2(b, n); out = []; r = 1
    for _ in range(T): r *= b; out.append(r // n); r %= n
    return out

def _isp(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

# --- Gary's leading-pair reduction in any base (chapter v0.2; L2641, L2653) ---
def gary_reduction_b(ds, b=10):
    """replace the first two digits by their base-b sum until one digit remains -> (steps, carries, final)."""
    d = list(ds); steps = carries = 0
    while len(d) > 1:
        s = d[0] + d[1]; steps += 1
        if s >= b: d = [s // b, s % b] + d[2:]; carries += 1
        else: d = [s] + d[2:]
    return steps, carries, d[0]

def _todig(n, b):
    out = []
    while n: out.append(n % b); n //= b
    return out[::-1] or [0]

def _drb(n, b):
    return 0 if n == 0 else 1 + (n - 1) % (b - 1)

def theorem_R_b(n, b=10):
    """Theorem R_b: steps = (L - 1) + (S - dr_b(n))/(b - 1); final digit = dr_b(n)."""
    ds = _todig(n, b); st, ca, fin = gary_reduction_b(ds, b)
    return st == (len(ds) - 1) + (sum(ds) - _drb(n, b)) // (b - 1) and fin == _drb(n, b)

def reduction_last_pair(n, b=10):
    """the two-digit numeral (as a digit pair) reached just before the final digit."""
    d = _todig(n, b); prev = None
    while len(d) > 1:
        if len(d) == 2: prev = tuple(d)
        s = d[0] + d[1]; d = ([s // b, s % b] if s >= b else [s]) + d[2:]
    return prev, d[0]

def theorem_E_b(n, b=10):
    """Theorem E_b: b does not divide n and dr_b(n) = 2  =>  the chain ends '11' -> 2."""
    if n < b or n % b == 0 or _drb(n, b) != 2: return True
    return reduction_last_pair(n, b) == ((1, 1), 2)

def carry_positions(ds):
    """1-indexed digit positions j at which the reduction carries (the carry happens when digit j is absorbed)."""
    v = ds[0]; out = []
    for j in range(1, len(ds)):
        s = v + ds[j]
        if s >= 10: out.append(j + 1); v = s - 9   # [1, s-10] then 1 + (s-10) = s - 9 at the next step
        else: v = s
    return out

def lemma_C1(ds):
    """Lemma C1 (L2637): carry at digit j <=> running digit sum crosses a multiple of 9: P_{j-1} <= 9m < P_j."""
    if ds[0] == 0: return True
    P = [0]
    for d in ds: P.append(P[-1] + d)
    pred = [j for j in range(2, len(ds) + 1) if any(P[j - 1] <= 9 * m < P[j] for m in range(max(1, P[j - 1] // 9), P[j] // 9 + 1))]
    return carry_positions(ds) == pred

def theorem_C3_b(p, b=10):
    """Theorem C3_b: even-period prime p: first-half digit sum S1 == 2 p^{-1} - 1 (mod b - 1)."""
    ds = _per(p, b); T = len(ds)
    if T % 2: return None
    S1 = sum(ds[:T // 2]); m = b - 1
    return S1 % m == (2 * pow(p, -1, m) - 1) % m

# --- the decimal period as a clock: spectrum (L2627 F1, F2; L2637 dark frequencies; L2649 Theorem H) ---
def digit_spectrum(n, b=10):
    """D(mu_j) = sum_{t=1}^T d_t mu_j^t, mu_j = e^{2 pi i j/T}, j = 0..T-1 (direct DFT, exact zeros detected by |.| < 1e-6 sqrt T)."""
    ds = _per(n, b); T = len(ds)
    try:
        import numpy as _np
        a = _np.array(ds, dtype=float); t = _np.arange(1, T + 1)
        return [complex(_np.sum(a * _np.exp(2j * _np.pi * j * t / T))) for j in range(T)] if T <= 3000 else list(_np.conj(_np.fft.fft(_np.roll(a, 1))) )
    except ImportError:
        return [sum(ds[t - 1] * _cm.exp(2j * _cm.pi * j * t / T) for t in range(1, T + 1)) for j in range(T)]

def theorem_F1(p):
    """F1: T even and 10^{T/2} = -1 (Midy)  <=>  every even harmonic j = 2..T-2 is exactly 0. Returns (midy, all_even_zero)."""
    ds = _per(p); T = len(ds); D = digit_spectrum(p); tol = 1e-6 * T ** 0.5
    midy = T % 2 == 0 and pow(10, T // 2, p) == p - 1
    ev = [abs(D[j]) < tol for j in range(2, T - 1, 2)] if T % 2 == 0 else [False]
    return midy, all(ev) and len(ev) > 0

def theorem_F2(p):
    """F2: 10 a primitive root mod p => no odd harmonic is silent."""
    D = digit_spectrum(p); T = len(D); tol = 1e-6 * T ** 0.5
    return all(abs(D[j]) > tol for j in range(1, T, 2))

def three_phase_sums(n):
    """digit sums over positions = 0, 1, 2 (mod 3); equal sums <=> silent harmonic at the cube roots of unity (L2637)."""
    ds = _per(n); s = [0, 0, 0]
    for t, d in enumerate(ds, 1): s[t % 3] += d
    return s


def phase_lattice_norm(p):
    """L2858 lattice lemma: if 3 | T, A = s0 + s1 w + s2 w^2 is divisible by (10w - 1) in Z[w] (p != 3, 37),
    so Q = |A|^2 = s0^2+s1^2+s2^2-s0s1-s1s2-s0s2 is 111 times a norm.  Returns (Q, Q % 111 == 0)."""
    s0, s1, s2 = three_phase_sums(p); Q = s0*s0 + s1*s1 + s2*s2 - s0*s1 - s1*s2 - s0*s2
    return Q, Q % 111 == 0


def phase_sums_q(n, q, b=10):
    """digit sums of the period of 1/n (base b) over positions t = c (mod q), c = 0..q-1."""
    ds = _per(n, b); s = [0] * q
    for t, d in enumerate(ds, 1): s[t % q] += d
    return s

def lattice_check(n, q, b=10):
    """L2858/L2866 lattice lemma, any order q dividing T and any base b: sum_c s_c b^{-c} = 0 (mod Phi_q(b));
    equivalently the period, read as a number, is divisible by Phi_q(b) (refines L2641 casting out b^q - 1)."""
    P = _cyclo(q); M = sum(c * b ** i for i, c in enumerate(P)); M = abs(M)
    s = phase_sums_q(n, q, b); binv = pow(b, -1, M)
    return sum(sc * pow(binv, c, M) for c, sc in enumerate(s)) % M == 0

def strand_check_mod63(d):
    """L2866: a full base-4 period of a/p with 3 | T, read as a number, is divisible by 63 = 4^3 - 1:
    a free check that detects every single substitution (and about 93% of double ones)."""
    v = 0
    for x in d: v = (v * 4 + x) % 63
    return v == 0

def _single_sub_ok(d):
    """period passes the mod-63 check, and every substitution at the first, middle and last position fails it."""
    if not strand_check_mod63(d): return False
    for j in (0, len(d) // 2, len(d) - 1):
        for e in (1, 2, 3):
            x = d[:]; x[j] = (x[j] + e) % 4
            if strand_check_mod63(x): return False
    return True

def tag_rotate(d):
    """L2871: rotate a base-4 reciprocal period to start at its first G or T. Deleting a leading A leaves the number unchanged,
    so unrotated tags (1/p always starts with A's) have a blind spot; rotated tags are periods of a/p and stay divisible by 63."""
    s = next(i for i, x in enumerate(d) if x >= 2); return d[s:] + d[:s]

def _deletion_CG_always_caught(d):
    """L2871 Theorem: in a full period with 3 | T, deleting any C or G always breaks divisibility by 63 (3 cannot divide d*4^k for d = 1, 2)."""
    for j, x in enumerate(d):
        if x in (1, 2) and strand_check_mod63(d[:j] + d[j + 1:]): return False
    return True

def tag_rotate_v2(d):
    """L2875 rule: start where the letter is G or T, the preceding (last) letter is not A, and the next letter differs.
    Removes both blind spots (leading A's and trailing A's: deleting a trailing A only divides the number by 4)."""
    T = len(d); s = next(i for i in range(T) if d[i] >= 2 and d[i - 1] != 0 and d[(i + 1) % T] != d[i]); return d[s:] + d[:s]

def tag_value(d, m):
    v = 0
    for x in d: v = (v * 4 + x) % m
    return v

def tag_check_full(w, R):
    """known-address check (L2875): a read window w is accepted only if it is exactly the stored rotation R
    (same length, same number mod 4^T - 1). Catches the window shifts that are themselves valid codewords."""
    return len(w) == len(R) and tag_value(w, 4 ** len(R) - 1) == tag_value(R, 4 ** len(R) - 1)

def _m9_ok(p):
    d = _per(p, 4); R = tag_rotate_v2(d); M = 4 ** 9 - 1
    if tag_value(R, M): return False
    for j in range(len(R)):
        if tag_value(R[:j] + R[j + 1:], M) == 0: return False          # every pure deletion caught
        for e in (1, 2, 3):
            x = R[:]; x[j] = (x[j] + e) % 4
            if tag_value(x, M) == 0: return False                       # every substitution caught
    return True

def agreement_lambda(c):
    """L2879: share of positions where the base-4 words of x/p and c*x/p carry the same letter, for large p
    (c a positive integer, not a multiple of 4): (c+3)/(4c) if c = 1 mod 4, (c+1)/(4c) if c = 3 mod 4, 1/4 if c even.
    The maximum over c != 1 is lambda(5) = 2/5, so the full reciprocal code has d_min/T -> 3/5 (129/130 primes: closest pair is x vs 5x)."""
    from fractions import Fraction as _F
    if c % 2 == 0: return _F(1, 4)
    return _F(c + 3, 4 * c) if c % 4 == 1 else _F(c + 1, 4 * c)

def word_agreement(p, c):
    """best agreement (over rotations) between the base-4 words of 1/p and c/p, as a fraction of T."""
    X = _per(p, 4); T = len(X); r = c % p; Y = []
    for _ in range(T): r *= 4; Y.append(r // p); r %= p
    return max(sum(1 for t in range(T) if X[t] == Y[(t + s) % T]) for s in range(T)) / T

def ratio_free_library(p, K=15):
    """L2883: greedy set of numerators a (1, 16, 17, 19, 21, ...) with no pair ratio equal to +-r/s mod p for r, s <= K.
    Removes the structural near-collisions (x vs 5x, 3x, 9x, ...); the closest remaining pair is ratio 17 (agreement 5/17 ~ 0.294).
    Honest result (L2883b): size-matched random libraries are still ~0.5% better, so the gain is compactness, not distance."""
    from math import gcd
    B = set()
    for r in range(1, K + 1):
        for s_ in range(1, K + 1):
            if gcd(r, s_) == 1 and r != s_:
                v = r * pow(s_, -1, p) % p; B.add(v); B.add((-v) % p)
    S = []
    for a in range(1, p):
        if all((a * pow(b, -1, p)) % p not in B for b in S): S.append(a)
    return S

def agreement_lambda_b(c, b=10):
    """L2887 Theorem (proved by counting i = qc + r in [0, bc)): share of positions where the base-b digits of x/p and c*x/p agree,
    for large p:  lambda_b(c) = (c - 1 + gcd(c - 1, b)) / (b c).  Maximum 2/(b+1) at c = b + 1 (base 10: c = 11, 2/11);
    so the full reciprocal code has d_min/T -> (b-1)/(b+1): 3/5 in base 4, 9/11 in base 10."""
    from fractions import Fraction as _F
    from math import gcd
    return _F(c - 1 + gcd(c - 1, b), b * c)

def _lambda_count(c, b):
    """exact count of i in [0, bc) with floor(i/c) = i mod b, divided by bc (the measure computed interval by interval)."""
    from fractions import Fraction as _F
    return _F(sum(1 for i in range(b * c) if i // c == i % b), b * c)

def agreement_lambda_rs(r, s, b=10):
    """L2892 Theorem L': long-run share of equal base-b digits of x/p and (r s^-1 mod p) x/p (gcd(r, s) = 1):
    #{(q, k, t): q < b, k < s, t < r, floor((r q + b k + t)/s) = q mod b} / (b r s).  s = 1 is Theorem Lambda;
    lambda(r/s) = lambda(s/r).  Base 10 ranking: 11 and 1/11 (2/11), then 6 and 1/6 (1/6), then 13/3 and 3/13 (2/13)."""
    from fractions import Fraction as _F
    return _F(sum(1 for q in range(b) for k in range(s) for t in range(r) if ((r * q + b * k + t) // s) % b == q), b * r * s)

def _per_num(a, n, b=10):
    """period digits of a/n (n coprime to b), same length as _per(n)."""
    T = _ord2(b, n); out = []; r = a % n
    for _ in range(T): r *= b; out.append(r // n); r %= n
    return out

def lambda_symmetric(r, s, b=10):
    """L2896 symmetric form: #{j < b r s : floor(j/r) = floor(j/s) mod b} / (b r s)  (= agreement_lambda_rs).
    Corollary: for x normal in base b, digits of x and c*x coincide with frequency lambda_b(c) (pi vs 11 pi: 0.1806 over 10^5 digits; 2/11 = 0.1818)."""
    from fractions import Fraction as _F
    return _F(sum(1 for j in range(b * r * s) if (j // r - j // s) % b == 0), b * r * s)

_LAMBDA_SD_1E5 = {2: 0.00087, 3: 0.00100, 6: 0.00098, 11: 0.00103, 21: 0.00109}   # null sd at N = 100,000 (300 random strings, L2901)

def normality_lambda_test(digits, C=(2, 3, 6, 11, 21)):
    """L2901: joint-digit normality check. digits = string of decimals of x after the point. For each c, the share of positions where x and
    c*x carry the same digit, its expected value lambda_10(c), and a z-score (null sd scaled from N = 100,000).
    Behaves like a 3-digit-block test: detects 0.(0123456789) and the order-2 de Bruijn word, not order 3; Champernowne fails at 10^5 digits
    (its known slow convergence)."""
    import sys
    try: sys.set_int_max_str_digits(0)
    except AttributeError: pass
    N = len(digits); X = int(digits); out = []
    for c in C:
        Y = str((c * X) % 10 ** N).zfill(N); a = sum(1 for u, v in zip(digits, Y) if u == v) / N
        lam = float(agreement_lambda_b(c)); sd = _LAMBDA_SD_1E5[c] * (100000 / N) ** 0.5
        out.append((c, a, lam, (a - lam) / sd))
    return out

def _const_digits(name, n):
    """first n decimals (after the point) of a constant, guarded mpmath rule (L2840)."""
    import mpmath
    old = mpmath.mp.dps; mpmath.mp.dps = n + 60
    try:
        x = {"sqrt2": mpmath.sqrt(2), "pi": +mpmath.pi, "e": +mpmath.e, "ln2": mpmath.log(2)}[name]
        return mpmath.nstr(x - mpmath.floor(x), n + 40, strip_zeros=False).split(".")[1][:n]
    finally:
        mpmath.mp.dps = old

def rna_strand(p, a=1):
    """L2909: base-4 period of a/p as RNA (A=0, C=1, G=2, U=3) and its translation (standard code, * = stop).
    The Midy second half is the A-U / C-G complement of the first (1/37: AACGUGGUA | UUGCACCAU -> NVVLHH)."""
    T = _ord2(4, p); r = a % p; s = ''
    for _ in range(T): r *= 4; s += 'ACGU'[r // p]; r %= p
    b = "UCAG"; aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    code = {x + y + z: aa[16 * i + 4 * j + k] for i, x in enumerate(b) for j, y in enumerate(b) for k, z in enumerate(b)}
    return s, ''.join(code[s[i:i + 3]] for i in range(0, len(s) - 2, 3))

def share_5_divides_period(P=200000):
    """L2909: share of primes p = 1 mod 5 below P whose decimal period is divisible by 5; predicted 5/6
    (5 does not divide T iff 10 is a 5^v-th power, v = v_5(p - 1): sum (4/5)(1/5)^(v-1) 5^-v = 1/6)."""
    ps = [p for p in range(11, P, 10) if _isp(p)]
    return sum(1 for p in ps if _ord2(10, p) % 5 == 0) / len(ps)

def vogel_records(beta, N=20000):
    """L2925: golden-angle (Vogel) points theta_n = n / phi^2 turns. Returns the n <= N at which theta_n comes closer to the direction beta
    (in turns) than at any earlier n. beta = 0: Fibonacci numbers; beta = 1/2: F_{3k}/2 (4, 17, 72, 305, 1292, ...) since
    F_m/phi^2 = F_{m-2} + psi^m (psi = -1/phi) gives distance 1/(2 phi^m); beta = 1/5 (pentagon): 3, 11, 244, 1231, 2828, ..."""
    import mpmath
    old = mpmath.mp.dps; mpmath.mp.dps = 40
    try:
        a = 1 / ((1 + mpmath.sqrt(5)) / 2) ** 2; best = mpmath.mpf(1); out = []
        for n in range(1, N + 1):
            v = n * a - beta; d = abs(v - mpmath.nint(v))
            if d < best: best = d; out.append(n)
        return out
    finally:
        mpmath.mp.dps = old

def fib_ladder(m, kmax=40):
    """L2929: n = F_t/m (m | F_t) lands within |psi|^t/m of the direction (F_{t-2} mod m)/m turns on the golden-angle spiral.
    m = 2: F_3k/2 -> 1/2; m = 4: F_6k/4 -> 3/4; m = 5: F_5k/5 -> 2/5, 1/5, 3/5, 4/5 cyclically. Returns [(n, direction)]."""
    from fractions import Fraction as _F
    F = [0, 1]
    while len(F) < kmax + 2: F.append(F[-1] + F[-2])
    return [(F[t] // m, _F(F[t - 2] % m, m)) for t in range(3, kmax + 1) if F[t] % m == 0]

def phi_power_share(n):
    """L2929: phi^n = F_n phi + F_(n-1), so the decimals of phi^n are those of F_n * frac(phi), and phi and phi^n agree at share
    lambda_10(F_n) (phi^8: 1/7; phi^4: 2/15; phi^5: 3/25). Verified on 10^6 decimals for n = 3..12 (all within 0.0005)."""
    F = [0, 1]
    while len(F) <= n: F.append(F[-1] + F[-2])
    return agreement_lambda_b(F[n])

def agreement_lambda_neg(c, b=10):
    """L2933: share of positions where the digit of x equals b-1 minus the digit of cx (x vs the complement of cx):
    #{i < bc : floor(i/c) = b-1-(i mod b) (mod b)} / (bc).  Governs x vs 1 - {cx}, e.g. phi vs phi^-n for even n."""
    from fractions import Fraction as _F
    return _F(sum(1 for i in range(b * c) if (i // c) % b == (b - 1 - i % b)), b * c)

def phi_inverse_power_share(n):
    """L2933 (corrected parity): phi^-n = (-1)^n (F_(n+1) - F_n phi). Odd n: decimals of phi^-n = those of {F_n phi} -> share lambda(F_n);
    even n: complemented -> share lambda^-(F_n).  Checked on 10^5 independent digits: phi^-4 0.0671 (1/15), phi^-8 0.0957 (lambda^-(21) = 0.0952)."""
    F = [0, 1]
    while len(F) <= n: F.append(F[-1] + F[-2])
    return agreement_lambda_b(F[n]) if n % 2 else agreement_lambda_neg(F[n])

def lambda_closed(r, s=1, b=10, complement=False):
    """L2937 closed form (Fourier proof): share of equal base-b digits of x and (r/s)x, gcd(r, s) = 1:
    1/b + j(d - j)/(b r s), d = gcd(r - s, b), j = r mod d.  Complement (digit vs b-1-digit): 1/b - j(d - j)/(b r s) with d = gcd(r + s, b).
    Corollary (proved): the maximum over all r/s != 1 is 2/(b+1), only at b+1 and 1/(b+1)."""
    from fractions import Fraction as _F
    from math import gcd
    d = gcd(r + s if complement else abs(r - s), b); j = r % d
    return _F(1, b) + (-1 if complement else 1) * _F(j * (d - j), b * r * s)

def block_share(c, k, b=10):
    """L2941: share of positions where x and cx agree on k consecutive digits = lambda in base b^k:
    (c - 1 + gcd(c - 1, b^k)) / (b^k c). Best k-block multiplier: b^k + 1 (2/(b^k + 1)); e.g. pi vs 101 pi: 0.01983 vs 2/101."""
    from fractions import Fraction as _F
    from math import gcd
    B = b ** k
    return _F(c - 1 + gcd(c - 1, B), B * c)

def affine_share(r, s, t, b=10):
    """L2941: x vs (r/s)x + t for normal x. The shift seen at digit n is {b^(n-1) t}, so the share is the average over that orbit of
    1/b + (d^2/(brs)) [B2({beta}) - B2({beta+theta})/2 - B2({beta-theta})/2], beta = b s t_n/d, theta = (r mod d)/d, d = gcd(r-s, b).
    Terminating t (like 1/2, 0.03) has no lasting effect; t = 1/3 makes pi vs 11pi + 1/3 share 1/11 instead of 2/11."""
    from fractions import Fraction as _F
    from math import gcd
    t = _F(t) % 1; seen = {}; orbit = []
    while t not in seen: seen[t] = len(orbit); orbit.append(t); t = (t * b) % 1
    cyc = orbit[seen[t]:]
    d = gcd(abs(r - s), b); th = _F(r % d, d)
    B2 = lambda x: x * x - x + _F(1, 6)
    vals = []
    for tn in cyc:
        be = (b * s * tn / d) % 1
        vals.append(_F(1, b) + _F(d * d, b * r * s) * (B2(be) - B2((be + th) % 1) / 2 - B2((be - th) % 1) / 2))
    return sum(vals) / len(vals)

def silver_power_share(n):
    """L2957: silver ratio delta = 1 + sqrt 2, delta^n = P_n delta + P_(n-1) (Pell numbers 0, 1, 2, 5, 12, 29, ...), so delta and delta^n
    share decimals at lambda_10(P_n): delta^3 = 5 delta + 2 -> 3/25 (measured 0.11998 on 10^6 digits), delta^5 -> 3/29. Odd inverse powers
    (delta^-n) share at the same lambda(P_n), as for phi."""
    P = [0, 1]
    while len(P) <= n: P.append(2 * P[-1] + P[-2])
    return agreement_lambda_b(P[n])

def power_share(rel, m, n, b=10):
    """L2977 (N12): root x of x^d = rel[0] + rel[1] x + ... + rel[d-1] x^(d-1) (integer rel; a Pisot unit such as phi [1, 1], the silver
    ratio [1, 2] or the plastic number [1, 1, 0]). Writes x^m and x^n in the basis 1, x, ..., x^(d-1). If x^n = k x^m + integer with
    rational k = r/s, the two share lambda_closed(r, s) of their base-b digits (k < 0: the complement law; k = 1: identical digits).
    Otherwise an independent irrational part is left over and the share is 1/b (verified for the plastic number, L2961; assumes the
    digits of the basis powers are jointly normal)."""
    from fractions import Fraction as _F
    d = len(rel)
    def vec(k):
        v = [0] * d; v[0] = 1
        for _ in range(k):
            top = v[-1]; v = [0] + v[:-1]
            v = [v[i] + top * rel[i] for i in range(d)]
        return v
    a, c = vec(m)[1:], vec(n)[1:]
    if not any(a): raise ValueError("x^m has no irrational part")
    i0 = next(i for i in range(d - 1) if a[i]); k = _F(c[i0], a[i0])
    if any(_F(c[i]) != k * a[i] for i in range(d - 1)) or k == 0: return _F(1, b)
    r, s = abs(k.numerator), k.denominator
    return lambda_closed(r, s, b, complement=(k < 0))

def _prim_root(p):
    fs = [q for q in range(2, p) if (p - 1) % q == 0 and _isp(q)]
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fs): return g

def theorem_H(p):
    """Theorem H (L2649): Midy prime, T = 2H:  S1 = 9H/2 + (2/(p-1)) sum_{chi odd} B_{1,chi} (10 chi(10) - 1)/(chi(10) - 1).
    Returns (S1 exact, formula value)."""
    ds = _per(p); T = len(ds); H = T // 2; S1 = sum(ds[:H])
    g = _prim_root(p); ind = {}; v = 1
    for k in range(p - 1): ind[v] = k; v = v * g % p
    tot = 0
    for a in range(1, p - 1, 2):                       # odd characters chi_a(g^k) = e^{2 pi i a k/(p-1)}
        w = lambda x: _cm.exp(2j * _cm.pi * a * ind[x % p] / (p - 1))
        B1 = sum(w(x) * x for x in range(1, p)) / p
        c = w(10)
        tot += B1 * (10 * c - 1) / (c - 1)
    return S1, (9 * H / 2 + 2 * tot / (p - 1)).real

# --- digit sums as class numbers (L2527, Girstmair 1994; L2532) ---
def _jacobi(a, n):
    a %= n; r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: r = -r
        a %= n
    return r if n == 1 else 0

def h_minus_n(n):
    """class number of Q(sqrt(-n)), n = 3 mod 4 squarefree > 3:  h = -(1/n) sum_x (x/n) x."""
    return -sum(_jacobi(x, n) * x for x in range(1, n) if _g2(x, n) == 1) // n

def girstmair_index2(n):
    """n = 3 mod 4 squarefree, coprime to 10, <10> = ker chi_{-n}:  digit sum of 1/n = 9 phi(n)/4 - (9/2) h(-n).
    Returns (applies, digit sum, formula)."""
    if n % 4 != 3 or _g2(n, 10) != 1 or any(n % (q * q) == 0 for q in range(2, int(n ** 0.5) + 1)): return False, None, None
    ph = sum(1 for x in range(1, n) if _g2(x, n) == 1); T = _ord2(10, n)
    if 2 * T != ph or _jacobi(10, n) != 1: return False, None, None
    S = sum(_per(n)); return True, S, _Fr2(9 * ph, 4) - _Fr2(9, 2) * h_minus_n(n)

from fractions import Fraction as _Fr2

# --- least n whose (cyclic) expansion holds all ten k-fold repdigits (L2430) ---
def _expansion_cyclic(n):
    """pre-period + two copies of the period of 1/n (so cyclic substrings are visible)."""
    m = n; a2 = a5 = 0
    while m % 2 == 0: m //= 2; a2 += 1
    while m % 5 == 0: m //= 5; a5 += 1
    pre = max(a2, a5); T = _ord2(10, m) if m > 1 else 1
    r = 1; out = []
    for _ in range(pre + 2 * T): r *= 10; out.append(str(r // n)); r %= n
    return ''.join(out)

def least_all_repdigits(k, nmax=20000):
    for n in range(2, nmax):
        s = _expansion_cyclic(n)
        if all(str(d) * k in s for d in range(10)): return n

# --- legacy items (Legacy_Handoff_02, 2026-10-17) ---
def prop_6_1(n):
    """Prop 6.1: over all units a mod n (gcd(n,10)=1), the period digits of a/n have mean exactly 9/2."""
    tot = cnt = 0
    for a in range(1, n):
        if _g2(a, n) != 1: continue
        T = _ord2(10, n); r = a
        for _ in range(T): r *= 10; tot += r // n; r %= n; cnt += 1
    return _Fr2(tot, cnt) == _Fr2(9, 2)

def theorem_12(a, n):
    """Theorem 12: A = sum (-1)^j d_{j+1} = (11/n) sum (-1)^j r_j over an even period (r_0 = a)."""
    T = _ord2(10, n)
    if T % 2: return None
    r = a % n; rs = []; ds = []
    for _ in range(T): rs.append(r); r *= 10; ds.append(r // n); r %= n
    A = sum((-1) ** j * ds[j] for j in range(T)); R = sum((-1) ** j * rs[j] for j in range(T))
    return A * n == 11 * R and A % (11 // _g2(n, 11)) == 0

def universally_balanced(n):
    """every coprime a/n has digit mean 9/2."""
    T = _ord2(10, n)
    for a in range(1, n):
        if _g2(a, n) != 1: continue
        r = a; s = 0
        for _ in range(T): r *= 10; s += r // n; r %= n
        if 2 * s != 9 * T: return False
    return True

def theorem_9(n):
    """Theorem 9: universal balance <=> every coset of H = <10> has as many residues above n/2 as below."""
    H = set(); v = 1
    while True:
        H.add(v); v = v * 10 % n
        if v == 1: break
    seen = set(); ok = True
    for a in range(1, n):
        if _g2(a, n) != 1 or a in seen: continue
        cos = {a * h % n for h in H}; seen |= cos
        if sum(1 for x in cos if 2 * x > n) != sum(1 for x in cos if 2 * x < n): ok = False
    return ok == universally_balanced(n)

def _v3(x):
    k = 0
    while x % 3 == 0: x //= 3; k += 1
    return k

def theorem_10(p, extra=1):
    """Theorem 10: prime p >= 7, a >= v3(ord_p 10) + 2  =>  1/(p 3^a) is never balanced (digit mean != 9/2)."""
    a0 = _v3(_ord2(10, p)) + 2
    for a in range(a0, a0 + extra + 1):
        n = p * 3 ** a; ds = _per(n)
        if 2 * sum(ds) == 9 * len(ds): return False
    return True

def lemma_U(k):
    """Lemma U: for each i in {0,1,2,3}, t -> F_{4t+i} mod 5^k is a bijection on Z/5^k."""
    m = 5 ** k; F = [0, 1]
    while len(F) < 4 * m + 4: F.append((F[-1] + F[-2]) % m)
    return all(len({F[4 * t + i] for t in range(m)}) == m for i in range(4))

# --- L2493 Theorem T'': trace of twisted sums mod p = Fermat quotient of 1 - x, in Z[zeta_k] ---
def _cyclo(k):
    """coefficients (low -> high) of the k-th cyclotomic polynomial."""
    def pdiv(a, b):
        a = a[:]; q = [0] * (len(a) - len(b) + 1)
        for i in range(len(a) - len(b), -1, -1):
            c = a[i + len(b) - 1] // b[-1]; q[i] = c
            for j in range(len(b)): a[i + j] -= c * b[j]
        return q
    P = [-1] + [0] * (k - 1) + [1]
    for d in range(1, k):
        if k % d == 0: P = pdiv(P, _cyclo(d))
    return P

def _pmod(a, P):
    a = a[:]
    for i in range(len(a) - 1, len(P) - 2, -1):
        c = a[i]
        if c:
            for j in range(len(P)): a[i - len(P) + 1 + j] -= c * P[j]
    return (a + [0] * len(P))[:len(P) - 1]

def theorem_T2(p, k):
    """S_x(p) = sum_{a=1}^{p-1} a x^{a^{-1} mod p}  ==  Q_x(p) = (1 - x^p - (1 - x)^p)/p   (mod p) in Z[zeta_k]."""
    P = _cyclo(k); d = len(P) - 1
    S = [0] * (p + 1)
    for a in range(1, p): S[pow(a, -1, p)] += a
    S = _pmod(S, P)
    from math import comb
    Q = [0] * (p + 1)
    Q[0] += 1; Q[p] -= 1
    for i in range(p + 1): Q[i] -= comb(p, i) * (-1) ** i
    assert all(c % p == 0 for c in Q); Q = _pmod([c // p for c in Q], P)
    return all((S[i] - Q[i]) % p == 0 for i in range(d))

# --- 1/841 = 1/29^2 quadrants (L2653) ---
def quadrants_841():
    ds = _per(841); q = len(ds) // 4
    sums = [sum(ds[i * q:(i + 1) * q]) for i in range(4)]
    nums = [int(''.join(map(str, ds[i * q:(i + 1) * q]))) for i in range(4)]
    return sums, sum(nums) == 2 * (10 ** q - 1), gary_reduction_b(ds)[0]

# --- guarded position rule (L2840): never search the rounded tail ---
def guarded_position(x_str_or_mpf, S, ndig=10000):
    import mpmath
    mpmath.mp.dps = ndig + 2000
    X = mpmath.mpf(1) / x_str_or_mpf if isinstance(x_str_or_mpf, int) else x_str_or_mpf
    digits = mpmath.nstr(X, ndig + 50, strip_zeros=False).split('.')[1][:ndig]
    return digits.find(S) + 1

def menu_reduction():
    print("Gary's reduction (chapter v0.2, L2637-L2660) and the period clock (L2627-L2649)")
    s = input("  number or 1/p (e.g. 142857 or 1/7): ").strip()
    try:
        b = int(input("  base [10]: ").strip() or 10)
    except ValueError:
        b = 10
    if s.startswith('1/'):
        p = int(s[2:]); ds = _per(p, b); st, ca, fin = gary_reduction_b(ds, b)
        print("  period length %d, digit sum %d -> %d steps, %d carries, ends at %d" % (len(ds), sum(ds), st, ca, fin))
        if b == 10: print("  carries at digits", carry_positions(ds)[:30], "(Lemma C1: running sum crosses a multiple of 9)")
        if len(ds) % 2 == 0 and _isp(p):
            S1 = sum(ds[:len(ds) // 2]); print("  first-half sum S1 = %d; S1 mod %d = %d; Theorem C3_b predicts %d" % (S1, b - 1, S1 % (b - 1), (2 * pow(p, -1, b - 1) - 1) % (b - 1)))
        if b == 10: print("  three-phase sums (positions mod 3):", three_phase_sums(p))
    else:
        n = int(s); st, ca, fin = gary_reduction_b(_todig(n, b), b)
        print("  %d steps, %d carries, final %d; Theorem R_b holds: %s; last pair %s" % (st, ca, fin, theorem_R_b(n, b), reduction_last_pair(n, b)[0]))

def selftest_L2853(ok):
    import random
    rnd = random.Random(2853)
    ok("L2641/L2653 Theorem R_b: steps = (L-1) + (S - dr_b)/(b-1), 3000 random n in bases 3, 7, 10, 12, 16",
       all(theorem_R_b(rnd.randrange(1, 10 ** 12), b) for b in (3, 7, 10, 12, 16) for _ in range(600)))
    ok("L2641/L2653 Theorem E_b: dr_b(n) = 2, b not dividing n  =>  ends 11 -> 2 (n < 20000, bases 3, 7, 10, 12, 16)",
       all(theorem_E_b(n, b) for b in (3, 7, 10, 12, 16) for n in range(1, 20000)))
    ok("L2637 Lemma C1: carries fall where the running sum crosses 9m; 1/7 carries at digits 4, 5; all periods n < 600",
       carry_positions(_per(7)) == [4, 5] and all(lemma_C1(_per(n)) for n in range(3, 600) if _g2(n, 10) == 1))
    ok("L2637/L2653 Theorem C3_b: S1 = 2p^-1 - 1 mod (b-1) for even-period primes < 2000, bases 10, 7, 12",
       all(theorem_C3_b(p, b) is not False for b in (10, 7, 12) for p in range(3, 2000) if _isp(p) and b % p))
    ok("L2660 reduction lengths: 1/7 -> 7 steps, 1/31 -> 19, 1/71 -> 47, 1/841 -> 1216",
       [gary_reduction_b(_per(n))[0] for n in (7, 31, 71, 841)] == [7, 19, 47, 1216])
    ok("L2627 Theorem F1: Midy <=> all even harmonics vanish (17, 97, 401, 937); 31, 37, 41 have neither",
       all(theorem_F1(p) == (True, True) for p in (17, 97, 401, 937)) and all(theorem_F1(p) == (False, False) for p in (31, 37, 41)))
    ok("L2627 Theorem F2: full-reptend 7, 17, 97, 937 have no silent odd harmonic (Dirichlet L(1,chi) != 0)",
       all(theorem_F2(p) for p in (7, 17, 97, 937)))
    ok("L2637 dark frequencies: 1/277 three-phase sums 108, 108, 108; 1/55711 2709 x 3; unforced controls 31, 43, 67, 163 unbalanced (1/97 balance is forced by F1)",
       three_phase_sums(277) == [108] * 3 and three_phase_sums(55711) == [2709] * 3 and all(len(set(three_phase_sums(q))) > 1 for q in (31, 43, 67, 163)))
    ok("L2858 lattice lemma: |A|^2 of the three phase sums is a multiple of 111 = N(10w - 1) for every prime 7 <= p < 6000 with 3 | T (p != 37)",
       all(phase_lattice_norm(p)[1] for p in range(7, 6000) if _isp(p) and p != 37 and _ord2(10, p) % 3 == 0))
    ok("L2858 pre-registered test 150k-1M: new balanced primes 1/287449 (7659 x 3) and 1/333667 (9 x 3; period 000002997)",
       three_phase_sums(287449) == [7659] * 3 and three_phase_sums(333667) == [9] * 3)
    ok("L2866 lattice lemma at order 3 in base 4 (Phi_3(4) = 21) and order 5 in base 10 (Phi_5(10) = 11111): all primes with q | T, p < 3000",
       all(lattice_check(p, 3, 4) for p in range(11, 3000) if _isp(p) and _ord2(4, p) % 3 == 0)
       and all(lattice_check(p, 5, 10) for p in range(7, 3000) if _isp(p) and p not in (41, 271) and _ord2(10, p) % 5 == 0))
    ok("L2866 reciprocal DNA strands carry a free mod-63 check: 1/p in base 4 (3 | T) divisible by 63; every single substitution detected (p = 109..997)",
       all(_single_sub_ok(_per(p, 4)) for p in range(109, 1000) if _isp(p) and _ord2(4, p) % 3 == 0))
    ok("L2871 deletions: removing any C or G from a full base-4 period (3 | T) is always caught by the mod-63 check; rotated tags stay divisible (p = 109..997)",
       all(_deletion_CG_always_caught(_per(p, 4)) and strand_check_mod63(tag_rotate(_per(p, 4))) for p in range(109, 1000) if _isp(p) and _ord2(4, p) % 3 == 0))
    ok("L2875 tags with 9 | T: v2 rotation, check mod 4^9 - 1 = 262143 catches every substitution and every pure deletion (exhaustive, all such p < 1500)",
       all(_m9_ok(p) for p in range(11, 1500) if _isp(p) and (4 ** 9 - 1) % p and _ord2(4, p) % 9 == 0))
    ok("L2879 closest reciprocal tags: words of x/p and 5x/p agree on ~2/5 of letters (lambda(5) = 2/5; p = 1997, T = 998: within 0.03)",
       agreement_lambda(5) == _Fr2(2, 5) and agreement_lambda(3) == _Fr2(1, 3) and agreement_lambda(13) == _Fr2(4, 13) and abs(word_agreement(1997, 5) - 0.4) < 0.03)
    ok("L2883 ratio-free address library (p = 1019, K = 15): starts 1, 16, 17, 19, 21; no pair has ratio 5 or 1/5; residual near-collision lambda(17) = 5/17",
       ratio_free_library(1019)[:5] == [1, 16, 17, 19, 21] and all((a * pow(b, -1, 1019)) % 1019 not in (5, pow(5, -1, 1019)) for a in ratio_free_library(1019) for b in ratio_free_library(1019) if a != b)
       and agreement_lambda(17) == _Fr2(5, 17))
    ok("L2887 agreement law lambda_b(c) = (c-1+gcd(c-1,b))/(bc): equals the exact interval count for b = 3..12, c = 2..40; base 10 max 2/11 at c = 11; 1/109 vs 11/109 share 18 of 108 digits (pred. 19.6)",
       all(agreement_lambda_b(c, b) == _lambda_count(c, b) for b in range(3, 13) for c in range(2, 41) if c % b)
       and max(agreement_lambda_b(c) for c in range(2, 200) if c % 10) == _Fr2(2, 11)
       and sum(x == y for x, y in zip(_per(109), [((11 * pow(10, t, 109)) % 109) * 10 // 109 for t in range(108)])) == 18)
    ok("L2892 rational multipliers: lambda(r/s) = lambda(s/r), s = 1 gives Theorem Lambda; base-10 max over r, s <= 12 is 2/11; lambda_4(3/7) = 2/7; 1/1019 vs (5/3)/1019 digits within 10rs",
       all(agreement_lambda_rs(r, s_) == agreement_lambda_rs(s_, r) for r in range(1, 9) for s_ in range(1, 9))
       and all(agreement_lambda_rs(c, 1) == agreement_lambda_b(c) for c in range(2, 30) if c % 10)
       and max(agreement_lambda_rs(r, s_) for r in range(1, 13) for s_ in range(1, 13) if r != s_ and __import__("math").gcd(r, s_) == 1) == _Fr2(2, 11)
       and agreement_lambda_rs(3, 7, 4) == _Fr2(2, 7)
       and abs(sum(x == y for x, y in zip(_per(1019), _per_num(5 * pow(3, -1, 1019) % 1019, 1019))) - float(agreement_lambda_rs(5, 3)) * 1018) <= 150)
    ok("L2896 global maximum: for bases 3..12 and all reduced r/s != 1 with r, s <= 12, lambda <= 2/(b+1), equality only at b+1 and 1/(b+1); 1/937 vs 11/937 share 170 digits (pred. 170.2)",
       all(lambda_symmetric(r, s_, b) == agreement_lambda_rs(r, s_, b) for b in (4, 10) for r in range(1, 7) for s_ in range(1, 7) if __import__("math").gcd(r, s_) == 1)
       and all((lambda_symmetric(r, s_, b) < _Fr2(2, b + 1)) or (sorted((r, s_)) == [1, b + 1] and lambda_symmetric(r, s_, b) == _Fr2(2, b + 1))
               for b in range(3, 13) for r in range(1, 14) for s_ in range(1, 14) if r != s_ and __import__("math").gcd(r, s_) == 1)
       and sum(x == y for x, y in zip(_per(937), _per_num(11, 937))) == 170)
    ok("L2901 Lambda normality test (20,000 digits): sqrt 2 within 4 sd for every c; 0.(0123456789) rejected (|z| > 10 at c = 11)",
       all(abs(z) < 4 for _, _, _, z in normality_lambda_test(_const_digits("sqrt2", 20000)))
       and abs(normality_lambda_test(("0123456789" * 2000))[3][3]) > 10)
    ok("L2909 RNA view: 1/37 = AACGUGGUA|UUGCACCAU (Midy halves are A-U/C-G complements) -> protein NVVLHH; share of p = 1 mod 5 (< 30000) with 5 | T is 5/6 within 0.03",
       rna_strand(37) == ("AACGUGGUAUUGCACCAU", "NVVLHH") and abs(share_5_divides_period(30000) - 5 / 6) < 0.03)
    ok("L2925 golden-spiral approaches: records toward 0 are Fibonacci, toward the half-turn are F_{3k}/2 (4, 17, 72, 305, 1292, 5473), toward the pentagon point 1/5 are 3, 11, 244, 1231, 2828, 5412",
       vogel_records(0, 7000) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
       and vogel_records(__import__("mpmath").mpf(1) / 2, 7000) == [1, 4, 17, 72, 305, 1292, 5473]
       and vogel_records(__import__("mpmath").mpf(1) / 5, 7000) == [1, 3, 11, 244, 1231, 2828, 5412])
    ok("L2929 Fibonacci ladders on the golden spiral: F_6k/4 = 36, 646, 11592 approach 3/4; F_5k/5 = 11, 122, 1353 approach 1/5, 3/5, 4/5; phi^8 shares lambda(21) = 1/7 of its digits with phi",
       [x for x in fib_ladder(4, 30) if x[0] > 2][:3] == [(36, _Fr2(3, 4)), (646, _Fr2(3, 4)), (11592, _Fr2(3, 4))]
       and [x for x in fib_ladder(5, 30) if x[0] > 1][:3] == [(11, _Fr2(1, 5)), (122, _Fr2(3, 5)), (1353, _Fr2(4, 5))]
       and 36 in vogel_records(__import__("mpmath").mpf(3) / 4, 700) and 646 in vogel_records(__import__("mpmath").mpf(3) / 4, 700)
       and phi_power_share(8) == _Fr2(1, 7))
    ok("L2933 phi vs phi^-n: odd n -> lambda(F_n), even n -> lambda^-(F_n) (complement); phi^-4 -> 1/15, phi^-5 -> 3/25; lambda^-(1) = 0 in base 10",
       phi_inverse_power_share(4) == _Fr2(1, 15) and phi_inverse_power_share(5) == _Fr2(3, 25) and agreement_lambda_neg(1) == 0)
    ok("L2937 closed form lambda = 1/b + j(d-j)/(brs) (d = gcd(r-s, b), j = r mod d) and its complement equal the exact counts (b = 2..10, r, s <= 12); proves the 2/(b+1) maximum",
       all(lambda_closed(r, s_, b) == agreement_lambda_rs(r, s_, b) for b in range(2, 11) for r in range(1, 13) for s_ in range(1, 13) if __import__("math").gcd(r, s_) == 1)
       and all(lambda_closed(c, 1, 10, True) == agreement_lambda_neg(c) for c in range(1, 25))
       and lambda_closed(2, 7) == _Fr2(1, 7) and lambda_closed(3, 13) == _Fr2(2, 13))
    ok("L2941 k-digit blocks: x vs cx agree on 2 digits at (c-1+gcd(c-1,100))/(100c) (101 -> 2/101, 11 -> 1/55); shifts: 11x + 1/2 keeps 2/11, 11x + 1/3 drops to 1/11, x + 1/7 never agrees",
       block_share(101, 2) == _Fr2(2, 101) and block_share(11, 2) == _Fr2(1, 55)
       and affine_share(11, 1, _Fr2(1, 2)) == _Fr2(2, 11) and affine_share(11, 1, _Fr2(1, 3)) == _Fr2(1, 11) and affine_share(1, 1, _Fr2(1, 7)) == 0)
    ok("L2957 silver ratio: delta^3 = 5 delta + 2 shares 3/25 of its decimals with delta, delta^5 = 29 delta + 12 shares 3/29, delta^2 only 1/10",
       silver_power_share(3) == _Fr2(3, 25) and silver_power_share(5) == _Fr2(3, 29) and silver_power_share(2) == _Fr2(1, 10))
    ok("L2977 power_share: phi^5 = 5 phi + 3 shares 3/25 with phi, silver^3 also 3/25, plastic rho^3 = rho + 1 identical, rho vs rho^8 only 1/10, rho^4 vs rho^7 = 2 rho^4 + 1 at 1/10",
       power_share([1, 1], 1, 5) == _Fr2(3, 25) and power_share([1, 2], 1, 3) == _Fr2(3, 25) and power_share([1, 1, 0], 1, 3) == 1
       and power_share([1, 1, 0], 1, 8) == _Fr2(1, 10) and power_share([1, 1, 0], 4, 7) == _Fr2(1, 10) and power_share([1, 1, 0], 4, 5) == 1)
    ok("L2649 Theorem H: first-half sum = 9H/2 + cotangent-weighted B_{1,chi} sum (Midy primes 7..199)",
       all(abs(s - f) < 1e-6 for s, f in (theorem_H(p) for p in range(7, 200) if _isp(p) and _ord2(10, p) % 2 == 0)))
    gi = [girstmair_index2(n) for n in range(7, 800)]
    ok("L2527 Girstmair index-2: digit sum = 9 phi/4 - 4.5 h(-n) for every qualifying n < 800; 1/163 = 1/203 = 360; 1/86 = 99",
       all(S == f for a, S, f in gi if a) and sum(1 for a, _, _ in gi if a) > 20 and h_minus_n(163) == 1 and h_minus_n(203) == 4
       and sum(_per(163)) == 360 and sum(_per(203)) == 360 and sum(int(c) for c in _expansion_cyclic(86)[1:1 + 21]) == 99)
    ok("L2430 least n holding all ten k-repdigits: 17, 109, 1009 (vs b(3) = 1019 for all 3-strings)",
       [least_all_repdigits(k) for k in (1, 2, 3)] == [17, 109, 1009])
    ok("Prop 6.1 (legacy): mean digit over all units a/n is exactly 9/2 (n < 300 coprime to 10)",
       all(prop_6_1(n) for n in range(3, 300) if _g2(n, 10) == 1))
    ok("Theorem 12 (legacy): alternating digit sum = (11/n) * alternating remainder sum, 11/gcd(n,11) | A (even periods, n < 400)",
       all(theorem_12(a, n) is not False for n in range(3, 400) if _g2(n, 10) == 1 for a in (1, 2, 3) if _g2(a, n) == 1))
    ok("Theorem 9 (legacy): universal balance <=> every coset of <10> balanced about n/2 (n < 400)",
       all(theorem_9(n) for n in range(3, 400) if _g2(n, 10) == 1))
    ok("Theorem 10 (legacy): 1/(p 3^a) never balanced for a >= v3(ord_p 10) + 2 (p = 7..61)",
       all(theorem_10(p) for p in range(7, 62) if _isp(p)))
    ok("Lemma U (legacy): t -> F_{4t+i} mod 5^k is a bijection, k = 1..4, i = 0..3", all(lemma_U(k) for k in range(1, 5)))
    ok("L2493 Theorem T'': S_x(p) == (1 - x^p - (1-x)^p)/p mod p in Z[zeta_k], k = 3,4,5,6,8,10,12, primes 7..113",
       all(theorem_T2(p, k) for k in (3, 4, 5, 6, 8, 10, 12) for p in range(7, 114) if _isp(p) and k % p))
    qs, num_ok, red = quadrants_841()
    ok("L2653 1/841 quadrants 932, 953, 895, 874; Q1+Q3 = Q2+Q4 = 1827; quarters sum to 2(10^203 - 1)",
       qs == [932, 953, 895, 874] and qs[0] + qs[2] == qs[1] + qs[3] == 1827 and num_ok)


def menu_theorems():
    say("Theorems L2422-L2848 (all verified; status tags in the report of each round).")
    c = ask("1 clock/P3 for n, 2 casting out 10^q-1 for p, 3 variance (Dedekind) for p, 4 2-5 lemma for m, 5 Note B count, 6 Theorem R (k=8)", "1")
    if c == "1":
        n = int(ask("n (coprime to 10)", 189)); cp, T = clock_period(n); say("  digit period %d, clock period %d, Theorem P3 predicts %d" % (T, cp, theorem_P3(n)))
    elif c == "2":
        p = int(ask("prime p", 7)); q = int(ask("q", 3)); r = casting_out(p, q)
        say("  not applicable (q must divide the period, gcd(p, 10^q-1) = 1)" if r is None else "  sum 10^i S_i = 0 mod 10^%d - 1: %s" % (q, r))
    elif c == "3":
        p = int(ask("full-reptend prime p", 19)); f, d = variance_dedekind(p); say("  Dedekind-sum formula %s, direct %s, equal: %s" % (f, d, f == d))
    elif c == "4":
        m = int(ask("m coprime to 10", 21)); say("  1/(2^a 5^b m) depends only on b - a mod d(m): %s" % thm_25_lemma(m))
    elif c == "5":
        a = int(ask("a (4 | a)", 8)); e = int(ask("e (2^e, keep <= 8)", 6)); say("  balanced orbits mod 2^%d: %d" % (e, bal_count(a, e)))
    else:
        p = int(ask("prime p = -1 mod 8", 47)); say("  Theorem R hit at some root: %s" % (True in real_subfield_wieferich(p, 8)))
    log_check("theorems", dict(choice=c), {})

def main():
    say("DCF PHONE TOOLKIT", VERSION, "| Python", sys.version.split()[0], "| mpmath", "yes" if HAVE_MP else "no (optional)")
    say("Output folder:", OUT)
    if "--selftest" in sys.argv or os.environ.get("DCF_SELFTEST"):
        sys.exit(0 if selftest() else 1)
    items = {"1": ("Reciprocal explorer", menu_recip), "2": ("Position rule check", menu_position),
             "3": ("Audit a master-list file", menu_audit), "4": ("Build / verify reciprocal database", menu_db),
             "5": ("GaryPhone adapter (DB -> DRC1/G4 -> verify)", menu_adapter), "6": ("Self-test", selftest),
             "7": ("Save session report", lambda: save_report("Session", dict(log=LOG))),
             "8": ("Claims inbox: paste an AI answer, check every position claim", menu_inbox),
             "9": ("QR send: verification ticket or report", menu_qr_send),
             "10": ("QR receive: paste scans or decode QR images", menu_qr_receive),
             "11": ("Reciprocal cube: invariants, theorem checks, queries, CSV", menu_cube),
             "12": ("Compression ladder and Midy-aware archive", menu_compress),
             "13": ("E8 labels: root check, shuffled-order test, noise test", menu_e8),
             "14": ("Gaussian channel: E8 vs random codes at your noise levels", menu_gauss),
             "15": ("Balance explorer: 4.5-ratio cycles, Theorem F for p*q", menu_balance),
             "16": ("Harmonics: digit wave of 1/n (balance = no DC, Midy = no even harmonics)", menu_harmonics),
             "17": ("Quantum period finding (Shor simulation) = the period of 1/n", menu_shor),
             "18": ("Fibonacci memory: Pisano 60 / 24, mirror, balance (Theorem B), 1/89, phi", menu_fib),
             "19": ("Fibonacci wheels 60 / 24: quartets, database, position sums -> reciprocals", menu_wheels),
             "20": ("Lucas / Pell wheels and 60<->24 wheel links", menu_wheels2),
             "21": ("Fibonacci prime table: rank of apparition, which primes divide F(k), primitive primes", menu_fibprimes),
             "22": ("Recurrence balance (Theorems B, B_L, B_P) and wheels in other bases", menu_recbalance),
             "23": ("Dimension ladder: squares, planar lattices, 24-cell, 600-cell, E8 from golden numbers", menu_ladder),
             "24": ("Digital Space Occupancy D(n): breakdown, inverse, verified connections", menu_dso),
             "25": ("DNA view of 1/p: base 4 as A C G T, Watson-Crick (base-4 Midy) check", menu_dna_recip),
             "26": ("DNA tools: gene finder on a genome file (needs dcf_genefinder_mobile.py here)", menu_genefinder),
             "27": ("DNA storage: encode / decode a file, noise drill (needs dcf_dna_ecc.py + dcf_dna_codec.py here)", menu_dna_storage),
             "28": ("Theorems L2422-L2848: clock P3, casting out, Dedekind variance, 2-5 lemma, Note B, Theorem R", menu_theorems),
             "29": ("Gary's reduction in any base + the period clock (carries, S1 mod b-1, three-phase sums)", menu_reduction),
             "30": ("NEW: energy-metal tier of a genome (iron ladder, copper CuA, zinc ribbon; needs dcf_redox.py)", menu_energy),
             "31": ("NEW: number checks (first 1/n containing a string, Monster primes, Euler lucky numbers)", menu_numbers),
             "32": ("NEW: motif scan of a genome / mRNA / protein file (hedgehog, voltage sensor, ladder, zinc ...; needs dcf_motif_scan.py)", menu_motifs),
             "33": ("NEW: exon map: place an mRNA on a chromosome slice (strand, exons, coordinates; needs dcf_exonmap.py)", menu_exonmap)}
    while True:
        print()
        for k, (name, _) in items.items(): print(" %s  %s" % (k, name))
        c = input("Choose (q to quit): ").strip().lower()
        if c in ("q", "quit", "0", ""): break
        if c in items:
            try: items[c][1]()
            except Exception as ex: say("ERROR:", ex)

if __name__ == "__main__":
    main()
