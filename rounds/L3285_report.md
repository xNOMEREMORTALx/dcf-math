# DCF L3285: blind_21 — the rubredoxin iron knuckle and the zinc contrast hold blind (4 of 6), but microaerophiles sit on the tier-3/4 boundary (0.050–0.065), not inside tier 3; phone 6.07 and step-by-step phone instructions
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 11 November 2026

**Data:** `blind_21.zip`, all 9 genomes, matched by LOCUS and DEFINITION lines (NCBI now names *Magnetospirillum* "*Paramagnetospirillum*").

**Pre-registration:** `PREREGISTERED_L3281_blind21.txt` (`6ba34f75…f9e7`), script `dcf_rubredoxin_L3281.py` (`40c77429…bf66`).

**Tool numbers** were committed (`rounds/L3285_tool_numbers.txt`, SHA-256 `f7e7271f…8165`) before any annotation was read.

---

## 1. Results
| group (label fixed in advance) | genome | ladder | zinc ribbon | rubredoxin |
|---|---|---|---|---|
| lactic control | *Lactobacillus johnsonii* | 0.0000 | 0.035 | 0.0000 |
| lactic control | *Streptococcus gordonii* | 0.0000 | 0.026 | 0.0000 |
| microaerophile control ("no Fd core") | *Magnetospirillum magneticum* | **0.0497** | 0.042 | 0.0043 |
| Fd microaerophile | *Persephonella marina* | 0.0520 | 0.086 | 0.0017 |
| Fd microaerophile | *Helicobacter hepaticus* | 0.0527 | 0.047 | 0.0000 |
| Fd microaerophile | *Thermocrinis albus* | **0.0619** | 0.058 | 0.0022 |
| Fd microaerophile | *Campylobacter fetus* | **0.0652** | 0.050 | 0.0019 |
| tier-4 control | *Methanopyrus kandleri* | 0.1588 | 0.139 | 0.0301 |
| tier-4 control | *Desulfohalobium retbaense* | 0.1599 | 0.100 | 0.0130 |

| id | prediction | result | verdict |
|---|---|---|---|
| M1 | ≥ 3 of 4 Fd microaerophiles in the tier-3 band (0.023–0.060) | 2 of 4 (0.052, 0.053 in; **0.062, 0.065 just above**) | **FAIL** |
| M2 | *Magnetospirillum* < 0.023 | **0.0497** | **FAIL** |
| **M3** | controls called right, ≥ 3 of 4 | **4 of 4** (lactic 0.0000 ×2; tier 4 0.159, 0.160) | **PASS** |
| **RB1** | rubredoxin: both tier-4 controls above both lactic | 0.030, 0.013 vs 0, 0 | **PASS** |
| **RB2** | ρ(ladder, rubredoxin) ≥ 0.50 over 9 genomes | **ρ = 0.73** (p = 0.025) | **PASS** |
| **ZR1** | zinc ribbon climbs ≤ 1/5 as steeply as the ladder | ribbon 3.8× vs ladder 160× (bar 32×) | **PASS** |

The genetic code was correct in 9 of 9 (table 11); the code record is now **165 of 168**.

## 2. Reading
- **The iron vs zinc contrast holds blind, a second time.** The ladder separates lactic from tier-4 controls by about 160-fold; zinc's ribbon by under 4-fold.
- **The rubredoxin knuckle behaves like iron, blind:** absent in both lactic genomes, highest in the methanogen and sulfate reducer, and correlated with the ladder (ρ = 0.73). One protein fold, iron or zinc, follows the metal it holds.
- **Microaerophiles form a band, but it sits on the boundary.** All five low-oxygen genomes read **0.050–0.065**, together with *Arcobacter* (0.046) and *Sulfurihydrogenibium* (0.047) from earlier rounds. The prediction placed them inside tier 3, and two landed just above the cut, so M1 failed.
- **Better description (to be tested, not a regrade):** low-oxygen respirers read about **0.045–0.065**, between tier 3 and tier 4.
- **M2 failed because my label was wrong, not the tool.** The annotation (read after hashing) shows *Magnetospirillum* carries 17 ferredoxin genes, a nitrogenase cluster (24 *nif* genes) and two pyruvate/2-oxoacid:ferredoxin enzymes. I had called it a microaerophile "without a ferredoxin-based core"; it has one. For comparison, tier-2 *Paracoccus* carries 3 ferredoxin genes and no *nif*, and reads 0.011.
- **Lesson:** label genomes from their enzymes, not their lifestyle. "Microaerophile" is a lifestyle; what the ladder measures is how much of the energy budget runs through ferredoxin.

## 3. Phone 6.07
- **One change from 6.06:** menu 30 now lists only real genome files (first line `LOCUS` or `>`). Before, it could offer `README_PHONE.txt` as the default.
- **Self-test 261/261.**
- **A simulated phone run passed:** a genome saved under a browser-style name, "sequence (3).gb.txt", was found, and pressing Enter ran it to "ENERGY TIER 1: lactic fermenter".
- **Bundle:** `dcf_phone_bundle_6.07.zip` (dcf_phone_6.07.py SHA-256 in README_PHONE.txt).

## 4. How to run menu 30 on your phone (Android, Pydroid 3)
1. **Install the app:** from the Play Store, install **Pydroid 3**. Open it once.
2. **Install two libraries:** in Pydroid tap **☰ (menu) → Pip**. Type `numpy` → **Install**. When it finishes, type `mpmath` → **Install**.
3. **Get the toolkit:** download `dcf_phone_bundle_6.07.zip` from this chat onto the phone. In the **Files** app, tap the zip → **Extract**. Put the six files in one folder, for example **Download/DCF**.
4. **Get a genome:** in the phone's browser, open a genome link, for example *L. gasseri*: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008530`. It saves as something like `sequence.gb.txt` in **Download**. In Files, long-press it → **Move** → **Download/DCF**. Any of our blind-set links works the same way; small genomes (about 2 Mb) are fastest.
5. **Open the toolkit:** in Pydroid tap **☰ → Open** (or the folder icon), go to **Download/DCF**, and tap **dcf_phone_6.07.py**. Allow storage access if asked.
6. **Run it:** tap the yellow **▶ Run** button. A numbered menu appears.
7. **Optional check first:** type **6** and Enter to run the self-test. Expect `SELF-TEST PASSED: 261/261`.
8. **Menu 30:** type **30** and Enter. It shows "Genome files here: sequence.gb.txt". Press **Enter** to accept it, or type another file name.
9. **Wait:** the gene finder runs first. Expect several minutes on a phone; keep the screen on. Its output is saved, so a second run on the same genome is fast.
10. **Read the result:** iron ladder, C-x-x-C, copper CuA, zinc ribbon, zinc knuckle, and **ENERGY TIER 1–4**. *L. gasseri* should give ladder 0.0000 and tier 1.
11. **Quit:** type **q**.

**On an iPhone** the same files run in the **Pyto** app: Files → Pyto folder, install `mpmath` with Pyto's PyPI tool (numpy is built in), open `dcf_phone_6.07.py`, and press Run. This has not been tested on an iPhone yet.

## Record
**This round:** 6 graded, 4 passed (M3, RB1, RB2 and ZR1 passed; M1 and M2 failed).

**Total: 303 of 427 pre-registered predictions passed, plus 3 split.**

## Summary
- **Iron vs zinc held blind for the second time:** iron's ladder separated lactic fermenters from methanogens and sulfate reducers about 160-fold; zinc's site under 4-fold.
- **The rubredoxin iron knuckle held blind:** it follows the iron ladder (ρ = 0.73) and is absent in lactic fermenters. The same fold behaves like iron when it holds iron.
- **The microaerophile idea was half right.** Low-oxygen respirers do cluster, at 0.050–0.065, but on the tier-3/4 boundary rather than inside tier 3. My "no ferredoxin core" control turned out to have one (17 ferredoxin genes and nitrogenase), and the tool read it correctly.
- **The phone toolkit is at 6.07,** with exact steps above for running menu 30.

## Potential leads for future research
- **[Microaerophile band b]** Pre-register a fifth class on fresh genomes: low-oxygen respirers at 0.040–0.070. The labels must come from enzymes (ferredoxin oxidoreductases, *nif*), not lifestyle.
- **[Enzyme labels]** Write a label rule from annotation counts (ferredoxin genes, *nif*, POR/OOR, hydrogenases), frozen before reading tool numbers, to replace lifestyle labels.
- **[Rubredoxin note]** Add the blind RB1/RB2 result to Note H as §4g: one fold, two metals.
- **[Phone test]** Run steps 1–11 on your phone and send a screenshot of the menu-30 result. That is the first real-device test.
- **[CCHC precision]**, **[Alkali ladder]**: carried.
