# DCF L3281: the rubredoxin explanation for zinc is withdrawn, but the true rubredoxin spacing behaves like iron (21× in development, now frozen for blind_21); the zinc knuckle finds 11 of 12 known human CCHC genes; Monster primes show no reciprocal signature; Note H v0.5
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 10 November 2026

**Leads pursued:**
- [Fe-Zn rubredoxin], [Microaerophile tier], [CCHC eukaryote], [Monster primes], [Note H v0.5];
- from L3277: [Phone test] needs Gary's phone; [Alkali ladder] needs a motif plan first.

**Pre-registration:** `PREREGISTERED_L3281_blind21.txt` (`6ba34f75…f9e7`) and the script `dcf_rubredoxin_L3281.py` (`40c77429…bf66`), both pushed before any download.

---

## 1. [Fe-Zn rubredoxin] Development on seen genomes (the 16 blind_20 genomes)
| motif | tier medians 1 / 2 / 3 / 4 (per 1,000 aa) | tier 4 / tier 1 |
|---|---|---|
| zinc ribbon, knuckles with C-x₂-C-G or C-P-x-C | 0.026 / 0.020 / 0.036 / 0.049 | 1.9× |
| zinc ribbon, other knuckles | 0.012 / 0.013 / 0.020 / 0.029 | 2.4× |
| **classic rubredoxin pair C-x₂-C-G-x₂₄₋₃₂-C-x₂-C-G** | **0.0006 / 0.0009 / 0.0023 / 0.0126** | **21×** |
| C-P-x-C-G anywhere | 0.023 / 0.021 / 0.030 / 0.053 | 2.3× |

**Reading.**
- **Withdrawn:** in L3273 I explained zinc's modest climb by iron rubredoxins hiding among the zinc knuckles. Splitting the knuckles shows no such effect, and the 9–20 spacing can't match a classic rubredoxin (~29 residues). L3273 and Note H now carry this correction.
- **New:** the real rubredoxin spacing, an **iron** site with the same knuckle fold, **climbs 21× across the tiers, like iron rather than zinc.** One fold behaves according to which metal it holds. This is development on seen genomes, so it is now frozen for a blind test.
- The first attempt at this split had a bug (an always-true condition put every match in one bin). It was caught and fixed before any reading; the numbers above are from the fixed version.

## 2. blind_21 [pre-registered, waiting for the download]
| group | genomes | prediction |
|---|---|---|
| microaerophiles with ferredoxin enzymes | *Campylobacter fetus*, *Helicobacter hepaticus*, *Thermocrinis albus*, *Persephonella marina* | **M1:** ≥ 3 of 4 read in the tier-3 band (0.023–0.060) |
| microaerophile control | *Magnetospirillum magneticum* | **M2:** < 0.023 |
| lactic controls | *Lactobacillus johnsonii*, *Streptococcus gordonii* | **M3:** controls called right (≥ 3 of 4) |
| tier-4 controls | *Methanopyrus kandleri*, *Desulfohalobium retbaense* | |
| all 9 | | **RB1:** both tier-4 controls above both lactic on rubredoxin; **RB2:** ρ(ladder, rubredoxin) ≥ 0.50; **ZR1:** zinc ribbon climbs ≤ 1/5 as steeply as the ladder |

*H. pylori*, *Aquifex* and *C. jejuni* were rejected because their accessions were already used in early rounds.

## 3. [CCHC eukaryote] The zinc knuckle in human mRNA [development]
`rounds/L3281_cchc_human.py`: human RNA files 1–4, one transcript per gene (9,632 genes).
- **Density 0.010 per 1,000 aa,** about 10 times or more the bacterial level (0–0.0009 in blind_20). This fits the CCHC knuckle being a eukaryote and retrovirus motif.
- **Recall: 11 of 12 known CCHC-knuckle genes present were hit** (ZCCHC2/3/9/12/13/14/17/18/24, SF1, RBM4B; NANOS1 missed).
- **Other hits:** TUT4, TUT7, SRSF7 and RTL3 are known knuckle proteins; LAMA5, NSD3 and RING-finger genes are probable false positives. Precision is roughly two thirds.
- **Lead:** CCHC knuckles bind RNA bases by hydrogen bonds (your L3277 point). The tool can now find them label-free in human mRNA.

## 4. [Monster primes] Do supersingular primes have a reciprocal signature? [exploratory]
Primes below 72: 15 supersingular (2 … 71), 5 not (37, 43, 53, 61, 67).

| property of 1/p | supersingular (13, excluding 2 and 5) | others (5) | Fisher p |
|---|---|---|---|
| even period (Midy) | 9 | 1 | 0.12 |
| period p − 1 (full) | 7 | 1 | — |
| p ≡ 3 (mod 4) | 9 | 2 | 0.33 |

**No signature.** The best of four properties gives p = 0.12, before any correction, on only 5 non-supersingular primes. Supersingularity is a property of modular curves (Ogg: the curve X₀(p)⁺ has genus 0), not of decimal expansions. **Closed as [D].**

## 5. Note H v0.5
`notes/Note_FeS_ferredoxin_signature_draft_v0.5.md`. Changes:
- the blind_20 result (14 of 16, ρ = 0.96, all five predictions passed) as §4d-bis;
- iron vs zinc with Figure 1 (§4f);
- the rubredoxin correction;
- the electrochemical explanation.

## Action for Gary: blind_21 (9 links)
Open each link and zip all 9 as **`blind_21.zip`**.

1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008599
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_004917
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_013894
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_012440
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_007626
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_005362
7. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009785
8. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_003551
9. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_013223

## Record
No predictions graded this round. **299 of 421 passed, plus 3 split.**

## Summary
- **A correction and a new lead in one.** My earlier explanation for zinc's small climb (hidden iron rubredoxins) was wrong and is withdrawn. But the true rubredoxin spacing, an iron site in a zinc-like fold, climbs 21-fold across the energy tiers like iron. One protein shape follows the metal it holds. That is now frozen for blind testing.
- **blind_21 is frozen:** do microaerophiles that use ferredoxin enzymes form the tier-3 band, as *Arcobacter* and *Sulfurihydrogenibium* suggested? Nine fresh genomes, six predictions.
- **The zinc knuckle works on human mRNA:** it finds 11 of 12 known CCHC-knuckle genes, and the motif is about ten times commoner in human proteins than in bacteria.
- **Monster primes leave no mark on their reciprocals** (p = 0.12 at best on a tiny sample). Closed.
- **Note H is at v0.5** with the blind result as its centrepiece.

## Potential leads for future research
- **[blind_21]** Grade M1–M3, RB1–RB2 and ZR1 when the zip arrives.
- **[CCHC precision]** Add a flanking rule (e.g. aromatic or G near the knuckle) to drop RING-finger and laminin false positives; develop on files 1–2, test on 3–4.
- **[Alkali ladder]** Needs a label-free K⁺/Na⁺ marker (e.g. the K⁺-channel selectivity filter TxGYG); develop before any test.
- **[Phone test]** Run phone 6.06 self-test (261/261) and menu 30 on your phone.
- **[Submission H]** With blind_20 in, Note H is close to a short-communication draft. Next: a specialist literature check ([Lit-redox b]) and methods text.
