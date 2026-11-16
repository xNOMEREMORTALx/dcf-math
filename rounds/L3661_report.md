# DCF L3661: The Hydra, sea-anemone and sponge leak channels are NALCN, not CCH1 (my expectation failed, 3 of 6), so the calcium-like E-E-E-E ring is the ancestral NALCN; the worm's NALCN reads E-E-K-E
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 16 November 2026

**Data:** Gary's two files. **Their names were swapped; the contents were identified by their headers:**

| file name | what it holds |
|---|---|
| `yeast_Cch1.gz` | the full *C. elegans* proteome (26,620 proteins) |
| `Worm_proteome.gz` | the two references: P50077 yeast Cch1 (2,039 aa) and Q8IZF0 human NALCN (1,738 aa; ring E-E-K-E) |

**Procedure:**
1. **Frozen files:** the pre-registration (`PREREGISTERED_L3657_cch1_worm.txt`), `dcf_cch1_L3657.py` and `dcf_nalcn_ring_L3653.py`. All three hashes matched the ledger.
2. **Tool output:** `rounds/L3661_tool_output.txt`, pushed before grading.
3. **Grading:** `rounds/L3661_grade_output.txt`.

---

## Results
| # | prediction | result |
|---|---|---|
| C1 | Hydra hits nearer yeast Cch1 | **FAIL:** Nalcn 2,674–2,684 vs Cch1 470–478 |
| C2 | sponge (*Amphimedon*) hits nearer Cch1 | **FAIL:** Nalcn 1,028–1,050 vs Cch1 247–260 |
| C3 | sea-anemone hits nearer Cch1 | **FAIL:** Nalcn 3,355–3,376 vs Cch1 421–430 |
| C4 | every bilaterian hit nearer Nalcn (control) | **PASS:** 26 of 26 |
| W1 | worm ≥ 2 NALCN hits | **PASS:** 18 entries |
| W2 | every worm NALCN hit E-E-K-E | **PASS:** 18 of 18 |

**3 of 6 passed.** My C1–C3 expectation was wrong. **Correction:** in my first message I wrote "28 of 28" for C4. The grader counts **26 of 26**, the 32 hits minus the 6 non-bilaterian ones.

## Descriptive, after grading
- **Yeast Cch1 scores about 250–500 against every animal NALCN, bilaterian or not.** It is roughly equidistant from all of them; the fungal channel is far from every animal one.
  - **The non-bilaterian hits score 1,000–3,400 against mouse Nalcn, so they are NALCN-family.** Hydra's "CCH1" names are an annotation label.
  - **Caution:** one distant fungal reference is a weak test of family. The scores show clearly that these hits are NALCN-like, but they cannot exclude an animal CCH1-like subfamily without more references.
- **Worm:** 17 of the 18 entries are named "Sodium leak channel NALCN"; 2 are unnamed "Ion transport domain" entries.
  - **Three score groups** (3,606 ×7, 3,729 ×9, 3,757 ×2) point to isoforms of **nca-1 and nca-2** (and possibly a split model).
  - **All read E-E-K-E,** like the fly, mite and tardigrades.

## Reading: the NALCN ring map is now complete for this series
| lineage | ring |
|---|---|
| sponge, sea anemone, Hydra | **E-E-E-E** (calcium-like): NALCN, now confirmed |
| acoel | E-E-E-E and E-E-K-E |
| spiralians, sea urchin | **E-K-E-E** (lysine in domain II), plus E-E-E-E exon forms |
| ecdysozoans: fly, mite, tardigrades, **worm** | **E-E-K-E** (lysine in domain III) |
| vertebrates | **E-E-K-E** |
| lancelet | E-E-E-E (L3653 failure) |

**Interpretation, stated as a hypothesis:**
- **The first NALCN was calcium-like** (E-E-E-E in sponges and cnidarians).
- **Bilaterians gained a sodium-like lysine twice, at different places:**
  - **domain II** in the spiralian/ambulacrarian lines;
  - **domain III** in ecdysozoans and vertebrates.
- **Some kept a splice switch to go back to E-E-E-E.**
- **In battery terms:** the resting leak, which sets each cell's baseline voltage and rhythm, began as a calcium leak and was converted to a sodium leak independently in different branches.

## Record
**+3 passed, 3 failed. 475 of 644 passed, plus 3 split.** Nerve-chemistry audit **142 of 171.**

## Summary
- **My expectation that the cnidarian and sponge leak channels were the fungal-type CCH1 family failed.** They align far closer to mouse NALCN than to yeast Cch1, so they are NALCN, despite Hydra's "CCH1" label.
- **The calcium-like E-E-E-E ring is therefore the oldest NALCN form in these data.**
- **The full worm proteome confirms the nematode NALCN reads E-E-K-E,** like the other moulting animals.
- **Score:** 3 of 6 predictions passed.
- **The file names were swapped;** the contents were identified by their headers.

## Potential leads for future research
- **[Ancestral NALCN]** Placozoan and comb-jelly NALCN were not found (Trichoplax entries are fragments). A full-length placozoan proteome (e.g. *Trichoplax* sp. H2) would test "E-E-E-E is ancestral" one branch deeper.
- **[Two lysine gains]** Is the vertebrate domain-III lysine an independent gain from the arthropod one? The lancelet's E-E-E-E and the acoel's two forms are the key cases (RefSeq gene models).
- **[Manuscript 2]** Add §3.20 (CCH1 test, worm) and a NALCN ring-map figure.
- **[Phone]** Add a NALCN ring reader to menu 34 (it uses the frozen L3653 window method; development only so far).
