# DCF L3833: fish DNA-repair photolyases carry histidine at TrpD, and tyrosine has replaced it again and again (descriptive). A one-letter DNA change can make a photolyase look cryptochrome-like at the fourth chain position
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 18 November 2026

**Status: descriptive, not a test.** These are L3809 data I had already seen (`rounds/L3809_tool_output.txt`; UniProt PANTHER SF18 set, MD5 279268f1…). Nothing here is graded. The fish group names come from published fish classification (Betancur-R. et al. 2017, *BMC Evol. Biol.*); they are not computed here.

---

## What sits at TrpD in class I photolyases of fishes
| residue at TrpD | species | examples |
|---|---|---|
| **H (histidine)** | most fishes | zebrafish, salmon and trout, medaka, pufferfish (*Takifugu*), carp, goldfish, cod, herring, cavefish, platyfish, tilapia (*Oreochromis*), sea bream, barramundi, clownfish, turbot, betta, turquoise killifish, mummichog |
| **Y (tyrosine)** | 23 fish species | perches (*Perca*), stickleback, lumpfish, Antarctic icefishes and toothfishes (*Champsocephalus*, *Dissostichus*, *Gymnodraco*, *Pogonophryne*, *Eleginops*, *Cottoperca*), wrasses (*Labrus*, *Xyrichtys*), croakers (*Larimichthys*, *Nibea*), European sea bass, ocean sunfish (*Mola*), Lake Malawi/Victoria cichlids (*Maylandia*, *Pundamilia*, *Astatotilapia calliptera*), two killifishes (*Kryptolebias*, *Austrofundulus*) |

**No species carries both.** Across all organisms in the set, 96 species read H at TrpD and 24 read Y; no species has both. (The 24th "Y" species is a fungus, *Funneliformis*.)

## Why it keeps happening (genetic code, a certain fact)
- **Histidine is coded CAT or CAC; tyrosine is TAT or TAC.**
- **A single C→T change at the first codon position turns H into Y.** So the swap needs just one mutation and can arise independently many times.

## Where the Y appears
- **In the perch group (Perciformes in the strict sense):** perches, stickleback, lumpfish and all the Antarctic notothenioids sampled read Y. That fits a single origin in this group.
- **Elsewhere among the "higher" bony fishes (Eupercaria):** Y also appears in wrasses, croakers, sea bass and sunfish. Close relatives sometimes keep H: the pufferfish *Takifugu* (H) is in the same order as the sunfish *Mola* (Y), and the sea bream is H.
- **In cichlids, the split is inside one family:** tilapias and the Tanganyika-region *Haplochromis burtoni* read H, while the Lake Malawi and Lake Victoria haplochromines read Y.
- **In killifishes:** two rivulids read Y, while *Nothobranchius* and *Fundulus* read H.

**So H→Y happened several times independently.** That is unusual for a residue at the end of an electron-transfer chain.

## Why it might matter
- **In cryptochromes, an aromatic fourth residue (W/Y/F) carries the electron hop** that makes light-driven radical pairs, the basis of the magnetic-compass idea.
- **Tyrosine can do this; histidine normally cannot.** So these fish photolyases may have gained a fourth electron-transfer step, or the position may simply be free to change.
- **Only experiments can tell:** photochemistry of a Y and an H fish photolyase, or the Y→H mutant.

## Summary
- **Fish class I photolyases carry histidine at TrpD,** and tyrosine has replaced it in several separate fish groups: perches and Antarctic fishes, wrasses, croakers, sea bass, sunfish, Lake Malawi/Victoria cichlids and some killifishes.
- **The swap needs one DNA letter (C→T), and no species has both forms.**
- **These are the main exceptions to the cryptochrome family rule (L3809).**

## Potential leads for future research
- **[Blind test of the H/Y map]** Pre-register predictions for fishes not yet in the set (pikeperch *Sander*, nine-spined stickleback *Pungitius*, *Trematomus*, striped bass *Morone*, rockfish *Sebastes*, groupers *Epinephelus*): perch-group members Y; others decided before looking. Needs NCBI RefSeq protein downloads.
- **[Light environment]** Do Y fishes share a light environment (cold, deep or turbid water: Antarctic, North Atlantic, the deep Lake Malawi)? A pre-registered comparison against H fishes.
- **[Phone]** Menu 37 already reports these as "photolyase-type, nearest reference … TrpD = Y" and flags the disagreement.
