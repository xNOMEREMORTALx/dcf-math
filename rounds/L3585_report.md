# DCF L3585: A local aligner fixes the length bias, and names the comb jelly's channels: 104 of its potassium channels are Shaker (Kv1) (2 of 2)
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 15 November 2026

**Lead:** [Local aligner].
- **New tool:** `rounds/dcf_localalign_L3585.py`, also `dcf-genefinder/dcf_localalign.py`.
- **Pre-registration:** `PREREGISTERED_L3585_ctenonames.txt`.

---

## 1. Local aligner (Smith–Waterman)
**What it is:** BLOSUM62, linear gap 8, numpy rows with a floor at 0. The score counts **only the best-matching region**, so a short or long reference no longer distorts the comparison.

**Validation (development, `rounds/L3585_validate_out.txt`):** 40 randomly chosen **named** zebrafish K, HCN and K2P channels, named by their nearest mouse channel. **39 of 40 correct.**
- **The one miss:** kcnk4a → Kcnh2. kcnk4a is one of the divergent leak channels the K2P rule also misses.

## 2. Pre-registered naming of the comb jelly's channels
| tool call | nearest mouse family | count |
|---|---|---|
| K | **Kv1 (Shaker)** | **104** |
| K | Kv4 (Shal) | 9 |
| K | Kv3 (Shaw) | 3 |
| K | Kv2 (Shab) | 1 |
| K | KCNH (eag/erg) | 2 |
| K | Kv6/Kv9 (silent) | 3 |
| K2P | **K2P** | **19** |

- **C1 (K2P calls nearest a K2P ≥ 80%): 19 of 19, PASS.** Two independent methods agree: the filter rule and alignment.
- **C2 (K calls nearest Kv1–Kv4 ≥ 80%): 117 of 122, PASS.**

## Reading
- **The comb jelly's huge potassium set is mostly one subfamily: Shaker (Kv1).** 104 of its 122 voltage-gated potassium channels are Kv1.
  - For comparison, mammals have 8 Kv1 genes.
  - So the comb jelly built its fast "reset" machinery by copying one channel type many times.
- **The aligner itself:**
  - the local score fixes the length bias that broke L3581;
  - the global aligner stays valid for length-matched comparisons (L3569, L3577).

## Record
**+2 passed. 425 of 581 passed, plus 3 split.** Audit 97 of 115. Manuscript 2 is at **v0.12** (new §3.11).

## Summary
- **A local aligner, validated at 39 of 40, removes the length bias.**
- **With it, the comb jelly's channels name cleanly:**
  - **104 Shaker-type (Kv1) potassium channels** (mammals have 8);
  - all 19 leak channels confirmed as K2P.
- **Comb jellies built their nervous system's reset machinery from many copies of one potassium channel,** alongside their E-type sodium-type channels and missing monoamine enzymes. It is a distinctly different chemistry.

## Potential leads for future research
- **[Phone]** Add the local aligner to menu 35 as an option ("local / global").
- **[Kv1 expansion test]** Do other lineages with independent nervous systems show single-subfamily expansions? Apply the same naming to the sea anemone's 46 K channels, pre-registered.
- **[Outside reader]** Manuscript 2 v0.12.
