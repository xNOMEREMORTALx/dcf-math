# DCF L3289: first real-phone run — menu 30 works (*Prochlorococcus* reads tier 2, gene finder 99.0% correct on the phone); one self-test row failed on the phone's processor and is fixed (6.08); blind_22 frozen to test photosynthesis against the ferredoxin ladder
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 11 November 2026

**Data:** Gary's two phone transcripts:
- self-test on DCF-phone-6.06, Python 3.13.13: **260/261**;
- menu 30 on NC_005072 *Prochlorococcus marinus* MED4.

**Pre-registration:** `PREREGISTERED_L3289_blind22.txt` (`2028d9bd…be04`), pushed before any download.

---

## 1. The first real-device test [observed]
| check | phone result | reading |
|---|---|---|
| self-test | **260/261**; row "L2399 Theorem D" FAIL | a **numerical-precision** failure, not a wrong theorem (§2) |
| menu 30 offered `README_PHONE.txt` as the genome | yes (6.06) | **exactly the problem fixed in 6.07** |
| gene finder on the phone | 1,627 genes; **genes found 85.4%, predictions correct 99.0%**, exact stop 85.8%; code 11 correct | in line with the server-side record (precision 97–99%) |
| energy tier | ladder **0.0148**, CxxC 0.41, 1 CuA, zinc ribbon 0.034 → **tier 2 (oxygen respirer)** | right for an oxygen-making cyanobacterium (§3) |
| extra outputs | 9 possible frameshifts, 7 repeat tracts (switch-like), 4 islands, helical rhythm 9.10 bp | all written to Download/DCF |

**Two small notes.**
- Some self-test lines ran together in the pasted text ("…(282 chars max)PASS ticket…"). Locally every line prints separately, so this is a copy-paste quirk of the Pydroid console.
- The QR ticket was 282 characters on the phone and 280 here. The test only checks that it fits in 2 QR codes, which it does on both.
- **Cross-platform reproducibility is not yet checked.** NC_005072 is not stored on the server. If you attach the file, I will rerun it here and confirm the phone's numbers match to the last digit.

## 2. The self-test failure, found and fixed
- **The check:** Theorem D multiplies Galois conjugates in ordinary floating point and requires the result to be within 0.001 of a whole number.
- **On this server** the worst case (N = 27, a value of about −39.6 billion) missed by 0.00005. At that size, floating point is only good to about 10⁻⁵, so a slightly different maths library (the phone's ARM processor) can push it past 0.001.
- **The fix (6.08):** the product is computed with **mpmath at 60 digits**. The misses are now 10⁻⁵⁸ to 10⁻⁴⁸, so the check is safe on any processor. The exact denominators (3, 45, 189, 25, 81) and the Wieferich checks are unchanged.
- **Self-test 261/261** here. **Lesson:** a self-test that compares floats near 10¹⁰ to integers must use exact or high-precision arithmetic.

## 3. Photosynthesis and the ladder: a new test
- **Why tier 2 makes sense for *Prochlorococcus*:** oxygen-making photosynthesis depends on ferredoxin, but on the **plant-type [2Fe-2S]** ferredoxin (C-x₄-C-x₂-C-x₂₉-C), not the bacterial 4Fe-4S type that the ladder counts.
- **Prediction:** cyanobacteria should read like oxygen respirers. *Heliobacterium*, an anoxygenic phototroph whose reaction centre and enzymes use 4Fe-4S clusters, should read tier 4.
- **The plant-type motif itself is not a sharp marker:** it already reaches 0–0.007 in 25 seen non-phototrophs (`rounds/L3289_fd2_dev.py`). It is reported descriptively only.

**blind_22 predictions:**
| id | genomes | prediction |
|---|---|---|
| P1 | 4 cyanobacteria (*Synechococcus*, *Nostoc*, *Thermosynechococcus*, *Gloeobacter*) | ≥ 3 of 4 below 0.023, median below 0.023 |
| P2 | *Heliobacterium modesticaldum* | above 0.060 |
| E1 | 4 low-oxygen Campylobacterota (*Sulfurospirillum*, *Nitratiruptor*, *Sulfurovum*, *Wolinella*) | ≥ 3 of 4 in 0.040–0.070 |
| E2 | the same 4 | median in 0.040–0.070 |

**Declared risks:** *Nostoc* fixes N₂ (ferredoxins, *nif*); *Wolinella* is mostly anaerobic; *Gloeobacter* lacks thylakoids.

## Action for Gary
1. **Phone:** install `dcf_phone_bundle_6.08.zip` the same way as before (replace the old files). Self-test should now show **261/261**, and menu 30 lists only genome files in the DCF folder.
2. **Tip:** move the downloaded genome (`.pending-…sequence.gb.txt`) into **Download/DCF** and it will be offered automatically.
3. **blind_22:** open the 9 links and zip them as **`blind_22.zip`**:

1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_007604
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_003272
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_004113
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_005125
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_010337
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_013512
7. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009662
8. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009663
9. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_005090

4. **Optional:** attach NC_005072 (*Prochlorococcus*) so I can confirm the phone and server numbers are identical.

## Record
No predictions graded this round. **303 of 427 passed, plus 3 split.**

## Summary
- **The toolkit ran on a real phone for the first time.** The gene finder called *Prochlorococcus* genes with 99.0% precision, and menu 30 gave tier 2, the right tier for an oxygen-making cyanobacterium.
- **One self-test check failed on your phone's processor** because it compared huge floating-point numbers to whole numbers. Version 6.08 does that sum at 60-digit precision and passes on any device.
- **Your run opened a new test:** photosynthesis uses a different kind of ferredoxin (2Fe-2S) from the one the ladder counts. So cyanobacteria should read like oxygen breathers, and the 4Fe-4S-based heliobacteria like tier 4. blind_22 is frozen to check this, with a second test of the low-oxygen band.

## Potential leads for future research
- **[Cross-platform]** Rerun NC_005072 on the server when attached; the phone and server outputs should match exactly.
- **[blind_22]** Grade P1, P2, E1 and E2 when the zip arrives.
- **[Fd 2Fe-2S motif]** Sharpen the plant-type ferredoxin motif (e.g. the conserved C-x₄-C-x₂-C-(A/V)-G core) on seen cyanobacteria once blind_22 is graded.
- **[Phone report]** Use menu 7 (save session report) after each phone run, so the transcript is saved as a file.
- **[Float audit]** Search the self-test for other float-to-integer comparisons near 10¹⁰ and move them to exact arithmetic before they fail on another device.
