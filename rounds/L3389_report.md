# DCF L3389: no prior report of endonuclease III losing its iron cluster in lactic bacteria; a blind test of the cysteine loss is frozen
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 13 November 2026

**Leads:** [Lit-infoiron], [Ligand-loss blind].

**Pre-registration:** `PREREGISTERED_L3389_ligandloss.txt` (`fac8514b…ae16`) and the script `dcf_ligandloss_L3389.py`, pushed before download.

---

## 1. Literature
Two searches covered endonuclease III cluster loss and the iron-free lifestyle of lactobacilli.
- **Found:**
  - the Pfam/CDD cluster domain EndIII_4Fe-2S;
  - studies of the cluster's role in *E. coli*, *Deinococcus radiodurans* and *Thermococcus* endonuclease III;
  - **iron-free MutY homologues** (Trasviña-Arenas 2016; MutYX 2025, a clade "restricted to Lactobacillales");
  - **Archibald 1983, "*Lactobacillus plantarum*, an organism not requiring iron"**, the classic paper on the lifestyle.
- **Not found:** loss of the [4Fe-4S] cluster cysteines in **endonuclease III** of lactic bacteria. Our development data show *Lactobacillus* endonuclease III with 0–1 cysteines in the whole protein.
- **Note v0.2** (`notes/Note_information_iron_v0.2.md`) records this.

## 2. Blind test [pre-registered]
| group | genomes |
|---|---|
| lactic (Lactobacillales) | *Lactobacillus reuteri*, *L. sakei*, *L. fermentum*, *L. crispatus*, *Streptococcus suis* |
| iron-using relatives (Bacillales) | *Staphylococcus haemolyticus*, *Exiguobacterium sibiricum*, *Listeria welshimeri* |

| id | prediction |
|---|---|
| LL1 | in ≥ 4 lactic genomes, no endonuclease III or MutY carries the iron-cluster loop |
| LL2 | in every control, at least one does |
| LL3 | median cysteines: lactic ≤ 2, controls ≥ 4 |

The enzymes are identified by their annotation, and the outcome is the protein's cysteine content, an objective measure.

## Action for Gary: 8 links
Zip all 8 as **`blind_25.zip`**.

1. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_009513
2. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_007576
3. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_010610
4. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_014106
5. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_012925
6. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_007168
7. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_010556
8. https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gbwithparts&retmode=text&id=NC_008555

## Record
No predictions graded. **320 of 456 passed, plus 3 split.**

## Summary
- **A wider literature search found no earlier report that endonuclease III loses its iron cluster in lactic bacteria;** only MutY's loss is known. That makes the finding a likely new contribution, so it's going to a blind test.
- **Eight fresh genomes are frozen:** five lactic species, and three close relatives that do use iron.

## Potential leads for future research
- **[Ligand-loss blind]** Grade LL1–LL3 when `blind_25.zip` arrives.
- **[Ladder-P blind]**, **[CRISPR-temperature]**, **[Polymerase iron]**, **[Venue]**: carried.
