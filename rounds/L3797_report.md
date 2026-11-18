# DCF L3797: cryptochrome marker v2 passes blind (3 of 3 gradeable). Every confident cryptochrome in monarch butterfly, Atlantic salmon and owl limpet is aromatic at TrpD (17 of 17); the coral was void
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3797_cry_marker_v2.txt`.
- **Amendment:** `AMENDMENT_L3797_a.txt`, made before the monarch and coral data existed. It covers:
  - empty downloads;
  - the monarch filed under its subspecies (proteome UP000007151);
  - no *Acropora millepora* proteome in UniProt. The coral was not substituted, so it is void.
- **Scan:** `rounds/dcf_cry_marker_blind_L3781.py`, unchanged.
- **Grader:** `rounds/dcf_grade_L3797a.py`. It is the frozen grader plus genus + species name matching.
- **Output:** `rounds/L3797_tool_output.txt` (parts 1 and 2), committed before grading.
- **Grading:** `rounds/L3797_grade_output.txt`.

**Data, identified by content:**

| species | proteins | file |
|---|---|---|
| Atlantic salmon *Salmo salar* | 80,782 | stream (22).gz |
| owl limpet *Lottia gigantea* | 23,675 | stream (24).gz |
| monarch *Danaus plexippus plexippus* | 15,140 | stream_27.gz, MD5 f3ffba09… |
| coral *Acropora millepora* | none | two downloads came back empty; no UniProt proteome exists |

---

## Results
| # | prediction | result |
|---|---|---|
| V1 | every CRY/6-4 hit scoring ≥ 900 is aromatic at TrpD | **PASS:** 17 of 17 (all W) |
| V2 | no photolyase/DASH hit scoring ≥ 900 is aromatic at TrpD | **PASS:** salmon DASH G, limpet DASH K |
| V3 | the monarch has ≥ 2 confident CRY/6-4 hits | **PASS:** Cryptochrome-1 (A0A212EI23, 957) and Cryptochrome 2 (A0A212FAM3, 1338) |
| V4 | each of the four has a confident CRY/6-4 hit | **ungradeable** (coral void). Salmon 13, limpet 3, monarch 2. |

**3 of 3 gradeable passed. 1 void.**

## Reading
- **With the confidence cut (score ≥ 900), the marker holds blind.** Together with L3785 (14 of 14 at ≥ 900), it is now **31 of 31** confident cryptochrome/6-4 proteins aromatic at TrpD in seven unseen animals. The DASH proteins read G, H, K or X, never aromatic.
- **The weak hits that broke the strict rule in L3785 did not recur.** All 22 hits here score ≥ 934, so this round does not test the low-score class again.
- **Monarch:** its two cryptochromes fall where the biology predicts. The fly-type CRY1 (the light-sensing, magnetosensing type in insects) is nearest the 6-4 reference. The vertebrate-type CRY2 (the clock repressor) is nearest robin CRY4. Both carry the full WWWW chain. No DASH or class II photolyase was detected in the monarch.
- **Salmon,** the animal of the magnetite olfactory-cell study, has 13 confident cryptochrome/6-4 proteins after its genome duplication, all WWWW. It also has one DASH (G) and one class II photolyase.
- **The limpet** (a mollusc with iron-mineral teeth) has 3 cryptochrome/6-4 proteins, all WWWW, plus a DASH (K) and a class II photolyase.

## Record
**+3 passed, 1 void. 544 of 750 passed, plus 3 split.** Audit **211 of 277** (entry "cryptochrome marker v2").

## Summary
- **A pre-registered confidence cut rescued the cryptochrome family marker.** All 17 confident cryptochrome/6-4 proteins in monarch, salmon and limpet carry an aromatic residue at the fourth position of the electron chain, and no DASH protein does.
- **Across two blind rounds, the marker now stands at 31 of 31 for confident hits.** Weak, borderline hits remain the known exception (L3785).
- **The coral was void:** UniProt has no proteome for *Acropora millepora*, and we did not substitute another species.

## Potential leads for future research
- **[Low-score class]** Test the weak-hit exceptions directly. Pre-register that hits scoring < 900 are non-aromatic at TrpD at a higher rate than confident hits, using proteomes rich in divergent family members (molluscs, cnidarians).
- **[Staghorn coral]** *Acropora cervicornis* (UniProt UP001249851) as its own pre-registered round.
- **[Monarch compass]** The monarch's CRY1 is the insect magnetosensing type. A residue-level comparison of fly-type CRY1 across magnetosensing insects (monarch, fly, cockroach) against non-migrants is a natural next sequence test.
- **[Manuscript 4]** Add §3.6 (marker v2, blind) as v0.5.
