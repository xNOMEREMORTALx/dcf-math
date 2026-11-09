# DCF L3233: five more metals give no nuclear-count pattern; metal genes and replication polarity (1 of 2); and the geometry, verified — E8's 240 roots fold into two 600-cells in the golden ratio, and the tetrahedral helix closes in rings of 30
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 9 November 2026

**Leads (Gary):**
- other metals, the same way as iron;
- any connection to polarization;
- the geometric relationship between the double helix, sphere packing, the E8 lattice, the hexacosichoron (600-cell) and the 240 roots.

**Pre-registration:** `PREREGISTERED_L3233.txt`, SHA-256 `58987be8…4a8f`, commit `4e9a622`, pushed before computing.

**Data:** 29 chromosomes (blind_14–18, *Nautilia* included), label-free predicted proteomes from gene finder v2.31.

---

## 1. [Z-other] Five more metals [pre-registered]
**Test.** For each metal, its proton count Z and the neutron count N of its commonest isotope were tested as distances between pairs of its usual ligand residue. A metal passes if either distance exceeds its four neighbours by ≥ 10% in ≥ 20 of 29 genomes.

| id | metal (isotope) | Z | N | ligand pairs | genomes clearing | verdict |
|---|---|---|---|---|---|---|
| M1 | nickel (⁵⁸Ni) | 28 | 30 | Cys–Cys | 16 of 29 | **FAIL** |
| M2 | copper (⁶³Cu) | 29 | 34 | His–His | 5 of 29 | **FAIL** |
| M3 | zinc (⁶⁴Zn) | 30 | 34 | Cys–Cys | 16 of 29 | **FAIL** |
| M4 | selenium (⁸⁰Se) | 34 | 46 | Cys–Cys | 13 of 29 | **FAIL** |
| M5 | molybdenum (⁹⁸Mo) | 42 | 56 | Cys–Cys | 14 of 29 | **FAIL** |

**Chance level, measured.** For 200 random pairs of distances (22–56), Cys–Cys pairs clear in a median of **12 genomes (5–17, 5th–95th percentile)**. Every metal sits inside that range. With iron (L3229), **six metals tested, all null.** Nuclear proton and neutron counts leave no trace in protein spacing; the metal signal is chemical (the 3-3-4 cysteine ladder, L3225).

## 2. [Strand-pol] Polarization: metal genes and the replication strands [pre-registered]
**What "polarization" can mean here.**
- **Physical spin polarization (CISS, L3225)** needs lab measurements; it cannot be read from sequence.
- **A chromosome is also polarized by replication.** Each half has a leading and a lagging strand, and genes sit unevenly between them. That is testable.

**Method.**
- Origin and terminus were taken label-free from the cumulative GC skew (minimum and maximum). In nearly all these genomes they fall at the expected places, the origin near position 0 where GenBank files start at *dnaA*.
- "Metal genes" = predicted genes whose protein carries a CxxC motif.

| id | prediction | result | verdict |
|---|---|---|---|
| P1 | pooled: metal genes ≥ 2 points more often on the leading strand, p < 0.01 | 65.39% vs 65.32%: **+0.08 points, p = 0.9** | **FAIL** |
| P2 | positive difference in ≥ 20 of 29 genomes | **22 of 29** | **PASS** |

**Reading [D].**
- **Most genomes lean the predicted way, but the pooled effect is nil.** The largest Fe–S genomes lean the other way (*Desulforapulum* −3.6, *Acetobacterium* −4.0).
- **The biggest leading-strand excesses are in lactic bacteria** (+10 to +14 points). There, CxxC genes are few and largely zinc-ribbon ribosomal proteins, so this probably reflects the known leading-strand bias of essential genes, not metal chemistry.

## 3. The geometry, computed [V] and cited
Everything in this table was **computed here from first principles** (scripts `L3233_e8_600cell.py`, `L3233_bc_helix.py`):

| object | computed | known value |
|---|---|---|
| **E8 roots** | **240** vectors, all of squared length 2; each has 56 others at inner product 1 | 240 roots; E8 kissing number 240 |
| E8 packing density | π⁴/384 = **0.253670** | proved optimal in 8 dimensions (Viazovska, *Annals of Mathematics* 2017) |
| **600-cell** (hexacosichoron) | **120** vertices, **720** edges, **1200** triangles, **600** tetrahedral cells; 12 neighbours per vertex at edge length 1/φ = 0.618034 | {3,3,5} polytope |
| E8 Coxeter element | order 30; exponents 1, 7, 11, 13, 17, 19, 23, 29 | Coxeter number h = 30 |
| **E8 → 4D** (the Coxeter-plane pair m = 1, 11) | the 240 roots fall on **two shells of exactly 120**, radii 0.7435 and 1.2030, **ratio 1.618034 = φ**; each shell is a 600-cell (12 neighbours at 1/φ) | E8 ↔ H4 "folding": two 600-cells scaled by φ |
| **Boerdijk–Coxeter (tetrahedral) helix** | rotation **131.81°** per vertex (= arccos(−2/3)); rise **0.3162 = 1/√10** per vertex; **2.73 vertices per turn** | — |
| tetrahelix inside the 600-cell | a face-to-face chain of tetrahedra **closes after 30 cells** | the 600 cells split into 20 such rings of 30 (Coxeter; the split itself not re-computed) |

**How it connects to helices and packing (literature).**
- **Sadoc & Rivier** (*Eur. Phys. J. B* 1999) argue that biological helices arise partly from dense packing, and that the Boerdijk–Coxeter helix, a linear packing of regular tetrahedra, explains:
  - the α-helix's **≈ 3.6 residues per turn**;
  - collagen's **≈ 2.7 residues per turn**.
  Our computed 2.73 vertices per turn matches the collagen figure directly.
- **The chain from your question is real mathematics:**

  > sphere packing → tetrahedra (the densest local packing of 4 spheres) → the tetrahedral helix → which closes into rings of 30 in the 600-cell → two 600-cells (scaled by φ) are the 4D shadow of E8's 240 roots → E8 is the densest packing in 8D.

  Every arrow except the biology is a theorem or a direct computation here.

**What is not established [D].**
- **No published link between the DNA double helix and the tetrahedral helix or E8 was found.**
- B-DNA's about 10.5 base pairs per turn is set by base stacking and hydrogen bonding, not by tetrahedral packing.
- The numbers 30 (ring length; E8's Coxeter number) and 10 (our 3-3-4 ladder spans 10 residues; B-DNA about 10 bp per turn) are coincidences until a mechanism or a pre-registered test says otherwise.

## Record
**This round:** 7 graded, 1 passed (M1–M5 and P1 failed; P2 passed).

**Total: 281 of 380 pre-registered predictions passed, plus 3 split.**

## Summary
- **Five more metals, the same null.** Nickel, copper, zinc, selenium and molybdenum leave no trace of their proton or neutron counts in protein spacing; their results sit squarely in the range random distances give. Six metals tested, none show it. The metal patterns in genomes are chemical.
- **Polarization along the chromosome:** metal-binding genes lean toward the leading strand in most genomes (22 of 29), but not overall. The lean seems to come from essential ribosomal genes, not from metal use.
- **Your geometric chain holds up as mathematics, computed here.** E8's 240 roots fold into two 600-cells in the golden ratio. The 600-cell is threaded by tetrahedral helices that close every 30 cells. That helix is the densest way to stack spheres in a chain, and has been used to explain the α-helix and collagen. The link from this geometry to the DNA double helix itself is not established.

## Potential leads for future research
- **[BC-protein]** Test Sadoc–Rivier label-free: if predicted secondary structure were available on the phone (a small helix-propensity model), do Fe–S proteins' ligand ladders sit in helical or loop segments? Pre-register before building.
- **[E8-note]** Write the verified geometry (§3) as a short self-contained DCF note with the scripts: "From sphere packing to E8: a computed tour", labelled [V], with biology links marked [D].
- **[DNA-packing]** Literature search: is B-DNA (or DNA in condensed phases or virus capsids) described with tetrahedral or icosahedral packing models? If yes, a sequence-level test could follow.
- **[Ess-strand]** Re-run P1 excluding ribosomal-protein-like genes (short, highly expressed) to separate essentiality from metal use.
- **[Fe-lineage]**, **[Fe-ladder]**, **[Note G v1.2]** carried from L3229.
