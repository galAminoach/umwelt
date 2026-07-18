# UMWELT — research map (body horror / Cronenberg)

> Following Uri's crit. The point of the crit is not "watch more horror" — it **names the exact
> subgenre this device already lives in** and lets us reject the body-horror that would pull the
> piece off-concept. UMWELT is **medical / cosmetic body horror**: a clinic apparatus that performs
> care while it corrupts a body that was never broken. Everything below is filtered against that.

## The relevance filter

### Highly relevant
- **eXistenZ (Cronenberg)** — *interface anchor.* The machine is an **organ you plug into** (breathing
  bio-pod, bio-port, gristle gun), never a screen. Justifies the hard rules: **no manual input, the
  mouth is the only port, the surface is wet tissue.** → the device housing reads as something warm and
  faintly alive that *reads you*. (Already in the shader: mucous film + breathing tissue ground.)
- **Dead Ringers (Cronenberg)** — *closest conceptual match.* Twin gynecologists build "**instruments
  for operating on mutant women**" — but the women aren't mutant. The horror is the **clinical gaze
  pathologizing a normal body**, the instrument as fetish, self/other indistinct. This **is** the
  MEASURE → DELTA → ASSEMBLE spine. → the measurement **accuses**: a healthy mouth declared deficient.
  *(Built: MEASURE now reads `DEFICIT … / ASYMMETRY GRADE …`, DELTA reads `CORRECTION INDICATED +…%`.)*
- **The Substance (2024, Fargeat)** — *most on-the-nose for the thesis.* Beauty/optimization industry,
  the manufactured "better" double, the replaceable/collective self. = the **half-mine/half-silicone
  seam** + the **procedural identical collective** + the ending (a precise intimate journey → a result
  identical to everyone else's). *(Built: the flesh ocean now converges to uniform size+tone as it blooms.)*
- **Crimes of the Future (Cronenberg, 2022)** — *the bureaucratic layer.* Bodily modification is
  **registered and certified** (organ registry); modification administered, normalized; desensitization
  breeds new violations. = the spec number / count / archive as a **registry**, not a crowd.
  *(Built: `FILED №NNN` instead of `SPEC №`.)*
- **"Discomfort is the point"** — Uri's core note. A **license**, not a method: keep the dread, reject
  cute/Instagram/comfortable. But our discomfort comes from **clinical intimacy + consent**, not splatter.

### Partially relevant
- **The Fly (Cronenberg)** — useful *only* as a model for **gradual fusion** (Brundlefly = half-man-half-fly
  ≈ the silicone spreading across the seam over ASSEMBLE). Ignore the sci-fi melodrama / transformation-gore.
- **Body-horror genre / masochism research** — grounding only. Our cut is the **cosmetic / consent** axis,
  not the abject mass.

### Largely irrelevant (named so we don't chase them)
- **Japanese mutation / strange stop-motion (Tetsuo: The Iron Man, etc.)** — metal-fusion, frantic,
  industrial: the **opposite** of wet/slow/clinical; would fight the "impolite slowness." Admire, don't borrow.
- **Classic zombie films** — contagion/horde/survival, not our axis. Only the thin idea of de-individuation
  into an identical mass transfers, and The Substance is a sharper source for it.
- **Gore-for-shock** — against the brief; loud/external where ours is quiet/administered.

## Naming
- **"Lip Service"** — Uri said it as a joke, but it's sharp: *insincere words / hollow tribute* — a device
  that performs care while it hollows out consent. Real candidate alongside **UMWELT**.
- **"Lipmeter"** — gadget-cute, novelty register, undercuts the dread. Dropped.

## One-line takeaway
The crit doesn't ask for *more* horror — it tells us **which** horror: the **Dead Ringers / The Substance**
lane (the clinical gaze + the manufactured ideal), wearing **eXistenZ's** wet skin and **Crimes of the
Future's** bureaucracy — and actively refusing the **Tetsuo / zombie / gore** lane.

## Where this lives in the build
`index-silicone.html` — the abstract variant: the camera mouth rendered **half flesh / half silicone**
along a wandering wet seam (no real/foreign mouths), MEASURE/DELTA in the diagnostic-accusation register,
the count `FILED` into a registry, and the closing flesh ocean resolving to **identical** corrected lips.

---

# UMWELT = COMPUTER VISION (locked reframe, 2026)

The central reframe: **the "other" is not the lips — it is the computer-vision system looking at them.**
The Umwelt (perceived world) belongs to a machine that scans, isolates, measures, classifies, and compares
every mouth against a statistical **average it calls "perfect."** No emotion, only processing. The viewer is
not a user — they are **data being processed**. The heart is a **collision**: a cold analytical gaze (cyan
instrument, statistics, catalog) over **warm wet living meat** (the live mouth). Built as `index-vision.html`.

## What's real in PAGMAR (grounding — verified, not fabricated)
- Mouth isolation = CelebAMask-HQ parser, classes 10/11/12 → binary mask (`server/models/face_parser.py`).
- Real per-mouth fields (`body_part_results`, `server/services/database.py`): `bbox_*`, `centroid_x/y`,
  `orientation_angle`, `area_percentage`, `mask_path`, `cutout_path`, `camera_view`; image-level `head_roll`, `skin_l/a/b_mean`.
- Catalog: `/body-parts/mouth/across-images?pool=archive|wall`, ranked by recency / `iou*area`.
- **There is NO average/template/perfect anywhere in PAGMAR** (closest = pairwise donor compatibility,
  `server/services/compatibility.py`). So the piece computes the average **itself**, honestly.

## The honest AVERAGE
Shape-only (translation+scale invariant) running mean of every lip ring the system sees, seeded with a
realistic canonical outer-lip ring (mirrored to match the selfie-mirrored display). `Δ AVG %` = the real
RMS shape-distance to that mean (calibrated: a typical mouth lands ~25–35%, e.g. demo face = 26.1% / +1.10σ).
DELTA overlays the mean re-fitted to the captured mouth; NORMALIZE morphs the ring → mean and drives Δ → 0.

## Reused PAGMAR visual language (ported to vanilla canvas)
INTEGRITY-style trail readout, the 1px WallPole deviation axis, specimen develop-and-lock, the `§`-registers,
JoltScramble synchronized shock (scramble-snap), the cursor/stamp cadence, PP Fraktion Mono + `#00FFCC` wall
accent + `▸`, and the cold copy register (`> SUBJECT DETECTED`, `// ACQUIRING //`, `[ LOCKED ]`, `FILED Nº`).

## Stages (DISTORT loop dropped → analytical acquisition)
STANDBY → **ACQUIRE** (stepped scan isolates lip from ground; the gaze chills the meat) → CAPTURE → **COMPARE**
(specimen run against the labelled catalog) → MEASURE (real coordinates + classification + `Δ AVG`) → SEGMENT
(labelled sub-regions) → DELTA (`TARGET :: POPULATION MEAN`, the gap) → NORMALIZE (`Δ → 00.0%`) → HELD →
**ARCHIVE** (64 records · 1 shape — every mouth normalized to the average, identical). Verified PASS by
who-am-we-copy + who-am-we-art-director + who-am-we-typography.

## EXPANSION — face-mesh opening + operating-table grid + lip-stress
Opens as an **autopsy intake** now (not mouth-from-frame-one):
- **STANDBY → FACE** — the full live face appears as a specimen plate (clipped to its own silhouette) on the
  grid; a **facial-recognition Delaunay mesh** (one-time Bowyer–Watson over the 478 landmarks, ≤0.12 weave;
  live positions) **inks on** in inspection order — square sample-points top→bottom, then edges, then the
  **11 white ID landmarks** snap (`FACE GEOMETRY · LOCK`). Tracks live → it reads as *me*.
- **DISFACE (PURGE)** — the mesh stress-tests the geometry (sine pull + snap-back), then the face is
  **discarded feature-by-feature** (eyes→brows→nose→ears→cheeks→jaw, **mouth last**); discarded regions reveal
  the **graticule** (not black); a stepped discard-zoom converges to the orphaned mouth → hands into the
  mouth pipeline. `EYES — DISCARD … RETAINED — 01/06 · ORAL · FACE — PURGED`.
- **Grid** — a faint, **dead** cyan lat/long graticule in the GL ground (dense ledger rows = the DB, sparse
  barrel-curved meridians = the operating table); the specimen floats on it, cyan never on the meat.
- **STRESS** (after MEASURE) — a **caliper** pulls the lips wide (`uStretch`) while measuring elasticity:
  jaws on the corners, `WIDTH … mm` climbing, `STRAIN 1.47× → MAX STRAIN`, hard recoil.
Ported from PAGMAR's Consent mesh (`consentGeometry.ts`/`meshEdges.ts`) + Scan disassembly
(`scanSequence.ts`/`faceBuild.ts` `PART_BUILD_PRIORITY`). who-am-we-art-director directed; who-am-we-typography PASS.
