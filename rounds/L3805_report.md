# DCF L3805: weak hits are where the cryptochrome marker breaks (5 of 5). Confident cryptochromes in two corals and two bivalves are all aromatic at TrpD; 2 of 3 weak hits are not. The weak non-aromatic proteins look like one separate family
### Gary NOMEREMORTAL Mason · Digital Cosmos Framework · 17 November 2026

**Files:**
- **Pre-registration:** `PREREGISTERED_L3805_cry_weak_class.txt`, frozen before download.
- **Scan:** `rounds/dcf_cry_marker_blind_L3781.py`, unchanged.
- **Grader:** `rounds/dcf_grade_L3805.py`, frozen with the pre-registration.
- **Output:** `rounds/L3805_tool_output.txt`, committed before grading.
- **Grading:** `rounds/L3805_grade_output.txt`.

**Data, identified by content:**

| species | proteome | proteins | MD5 |
|---|---|---|---|
| staghorn coral *Acropora cervicornis* | UP001249851 | 27,986 | 669ddf77…; the first zip's 4th file was a duplicate of the oyster, so this was re-sent separately |
| cauliflower coral *Pocillopora damicornis* | UP000275408 | 25,411 | 2a6df486… |
| blue mussel *Mytilus edulis* | UP000683360 | 73,624 | 5bfadaa5… |
| eastern oyster *Crassostrea virginica* | UP000694844 | 50,256 | 24eee629… |

---

## Results
| # | prediction | result |
|---|---|---|
| W1 | every confident (≥ 900) CRY-family hit aromatic at TrpD | **PASS:** 9 of 9 (all W) |
| W2 | ≥ 1 weak (350–899) CRY-family hit non-aromatic | **PASS:** mussel A0A8S3V2Y9 (374, H), oyster A0A8B8EP46 (384, R) |
| W3 | the non-aromatic fraction is higher in weak than confident hits | **PASS:** 2 of 3 versus 0 of 9 |
| W4 | no confident DASH/photolyase hit aromatic at TrpD | **PASS:** G, K, K |
| W5 | each species has a confident CRY-family hit | **PASS:** coral 2, coral 2, mussel 3, oyster 2 |

**5 of 5 passed.**

## Pooled over the three blind rounds (L3785, L3797, L3805)
| class | aromatic at TrpD |
|---|---|
| **confident cryptochrome/6-4 (≥ 900)** | **40 of 40** |
| weak cryptochrome/6-4 (350–899) | 1 of 6 (the one aromatic is mussel CRY-1, score 862) |
| confident DASH / photolyase (informative) | 0 of 7 |

## Not graded: the weak exceptions look like one family
I compared the five weak non-aromatic proteins with each other by normalised local alignment score (1 = identical). This was done after grading, so it is descriptive.

| pair | similarity |
|---|---|
| Pacific oyster WWW**R** (A0A8W8KH86) vs eastern oyster WWW**R** (A0A8B8EP46) | **0.82** |
| either oyster vs mussel WWW**H** (A0A8S3V2Y9) | 0.63 |
| bivalve proteins vs frog WWW**H** (A0A6I8QP63) | 0.41 |
| any of these vs the oyster's real 6-4 photolyase (A0A8B8E5C8) | 0.11–0.12 |

**Reading:**
- **The weak non-aromatic proteins resemble each other far more than they resemble true cryptochromes.**
- They are long (726–862 residues) and are annotated only as "photolyase/cryptochrome alpha/beta domain-containing" or "uncharacterized".
- **Two oyster species share the same arginine at TrpD.** That suggests a conserved, separate photolyase-like family in bivalves and frogs, not broken cryptochromes.
- If so, the marker did not fail in L3785. The finder simply placed a different family nearest the 6-4 reference.

**Independent check: PANTHER subfamilies from UniProt, read after grading.**

| protein | TrpD | PANTHER subfamily |
|---|---|---|
| Pacific oyster A0A8W8KH86, A0A8W8KKK9 | R, R | **PTHR11455:SF18** |
| eastern oyster A0A8B8EP46 | R | **SF18** |
| mussel A0A8S3V2Y9 | H | **SF18** |
| frog A0A6I8QP63 | H | **SF18** |
| mussel A0A8S3UES5 (the one *aromatic* weak hit) | W | SF17, "Cryptochrome-1" |
| eastern oyster A0A8B8E5C8 (true 6-4, confident) | W | SF9, "cryptochrome circadian clock 5" (6-4 photolyase) |

**All five marker exceptions belong to one PANTHER subfamily, SF18,** which is named after the zebrafish gene si:ch1073-390k14.1. PANTHER classified them independently of our method. So the exceptions are a separate family, not broken cryptochromes. The blind test of this is pre-registered as L3809.

## Record
**+5 passed. 549 of 755 passed, plus 3 split.** Audit **216 of 282** (entry "cryptochrome weak class").

## Summary
- **Across three blind rounds, every confident cryptochrome (40 of 40) carries an aromatic residue at TrpD,** in corals, bivalves, a limpet, insects, fish and a frog.
- **The exceptions are all weak hits (5 of 6 non-aromatic).** They resemble each other (similarity 0.41–0.82) but not true cryptochromes (0.11).
- **That points to a separate photolyase-like family,** with arginine or histidine at TrpD, shared by oysters, mussels and frogs.

## Potential leads for future research
- **[SF18 blind, L3809]** Pre-registered: across all UniProt SF18 proteins, TrpD is non-aromatic; across SF17 (Cryptochrome-1), aromatic.
- **[New family, reference]** Add the Pacific oyster WWWR protein as a seventh reference. Predict, blind, that it becomes the best reference for the weak non-aromatic proteins in new bivalve/amphibian proteomes, and that confident cryptochromes are unaffected.
- **[Domain check]** Look up these proteins' domain architecture (InterPro). Do the extra ~200 residues hold a known domain? (Needs a download from Gary or a fetch of the InterPro entries.)
- **[Manuscript 4]** Add §3.7 (weak class) and the pooled table as v0.6.
- **[Phone]** Once the seventh reference is tested, add it to dcf_cryreader so the reader names this family instead of calling it a "weak hit".
