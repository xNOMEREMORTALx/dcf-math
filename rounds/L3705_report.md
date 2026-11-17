# DCF L3705: The 4D Nucleome loop files verified (every audit number in the external report reproduces), and DCF key numbers tested in them: no signal beyond chance (3 of 4)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Gary's request:** "Pursue leads and scan all 4D report files and look for connections to key DCF numbers and their multiples."

**Data:** the two Zenodo loop files Gary sent, `H1ESC.union-loops.bedpe` and `HFFc6.union-loops.bedpe`, together with `4D_DNA.txt` (L3701).

---

## Part A. The external report's numbers, checked on the real files (`rounds/L3705_4dn_verify.py` → `L3705_4dn_verify.txt`)
**Method:** my own code, not the report's script.

| claim in the report | recomputed | status |
|---|---|---|
| MD5 H1 `6b186943…`, HFFc6 `1faf1181…` | identical | **verified** |
| 141,365 H1 loops; 146,140 HFFc6 loops | 141,365; 146,140 | **verified** |
| 0 trans loops; 0 duplicate pairs | 0; 0 | **verified** |
| median span 170,000 (H1), 185,000 (HFFc6); quartiles 65,000/380,000 and 74,955.875/435,000 | identical | **verified** |
| < 50 kb, < 100 kb, ≥ 1 Mb counts (27,764 / 48,349 / 11,721; 23,877 / 46,425 / 14,487) | identical | **verified** |
| platform memberships (10 values) and support distribution (10 values) | identical | **verified** |
| single-platform fraction 63.10% (H1), 56.21% (HFFc6) | 0.6310, 0.5621 | **verified** |
| 5,304 exact shared interval pairs | 5,304 | **verified** |
| cross-cell matching at 2, 5, 10 and 15 kb (8 fractions) | all 8 identical to 4 decimals | **verified** |

**Every audit number in the report's data section reproduces.**
- **This is the first external-LLM numerical report in this series to pass in full.** The standing rule still applied, which is why we know.
- **Still unverified:** the report's other numbers, which concern other datasets I do not have (gene–enhancer counts, trajectory statistics, RNA contrasts, model files).

## Part B. DCF key numbers in the 4DN data (`PREREGISTERED_L3705_4dn_keynumbers.txt`)
**Key set** (project L400 milestone plus named constants): 9, 37, 72, 73, 89, 108, 113, 137, 153, 203, 216, 401, 432, 541, 937, 1231, 1841, 2701.

**Method** (frozen before running):
- **Tested numbers:**
  - for each loop, its span (distance between anchor starts);
  - every integer written in the report.
- **The statistic:** how often each key number divides them, against **control numbers with the same 2-and-5 content.** Loop coordinates sit on 1-kb/5-kb grids, which alone inflate divisibility by 72, 108, 216 and 432.
- **Significance:** the 99.7th percentile (Bonferroni for 18 numbers).

| # | prediction | result |
|---|---|---|
| D1 | H1 spans: no key number significant | **PASS:** none (highest: 541 at the 93.8th percentile) |
| D2 | HFFc6 spans: none significant | **FAIL:** **9** flagged (rate 1.051 vs control median 0.999) |
| D3 | none significant in both cells | **PASS:** 9 is at the 75th percentile in H1 |
| D4 | report integers: none significant | **PASS** |

**3 of 4 passed.**

**Reading the one flag honestly:**
- **9 had only 4 control numbers** (7, 11, 13, 17) and beat them by 5%. **Beating all 4 happens by chance one time in five.**
- **The 99.7th-percentile threshold cannot be reached meaningfully with fewer than 333 controls,** which affects the twelve smallest key numbers. That is a design flaw in my test, disclosed here.
- **The flag does not replicate in the other cell line.** It is not a DCF signal.

**Raw view:** for every key number, the divisibility rate sits close to its controls in both cell lines. The large "rates" for 72, 108, 216 and 432 (2–6× chance) are the bin-grid effect, and their own matched controls show the same inflation.

**The counts themselves (descriptive):**
- 141,365 = 5 · 7² · 577;
- 146,140 = 2² · 5 · 7307;
- 5,304 = 2³ · 3 · 13 · 17.

None is divisible by a key number. The total, 287,505, is divisible by 9 (digit sum 27), which one integer in nine is.

## What this means for the DCF
- **Genome-folding coordinates are measured on human-chosen grids** (base pairs, kilobase bins). Divisibility patterns in them reflect those grids, not nature.
- **A fair test with matched controls finds no DCF number over-represented.**
- **This is useful as a negative control for the framework.** It shows the method does not manufacture hits where none should exist.
- **The DCF links found earlier in this series are biological, not numerological:**
  - the metals and their selectivity loops;
  - zinc in CTCF;
  - the bilaterian branch point.

## Record
**+3 passed, 1 failed. 498 of 677 passed, plus 3 split.** Audit **165 of 204.**

## Summary
- **The 4D Nucleome loop files Gary downloaded match Zenodo's checksums,** and every number in the external report's data audit reproduces exactly with independent code. The report's data section is verified.
- **No DCF key number appears in the loop spans or the report's numbers beyond chance** once grid effects are controlled. The single flag (9, in one cell line) has only four controls and does not replicate.
- **One test-design flaw is disclosed:** the threshold was too strict to be meaningful for small numbers.

## Potential leads for future research
- **[Better null for small numbers]** Use a permutation null instead: shift every loop by a random offset within its bin grid. This gives a p-value for any number, small or large.
- **[Biology, not digits]** The real 4D bridge is CTCF (zinc). Map CTCF-anchored loops (the CTCF-ChIAPET label) and test whether ion-channel genes (KCN*, SCN*, CACNA*) sit in more CTCF loops than other genes. This needs gene coordinates (GENCODE) as a new file.
- **[CTCF finder v2]** Lower the zinc-finger gate to rescue the named Ciona and tardigrade CTCFs (L3701).
