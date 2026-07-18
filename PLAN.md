# UMWELT — PLAN (rewrite me)

> This is a clean starting canvas. Rewrite any section. The parts that keep missing
> are marked **▢ REWRITE**. Lines marked **✓ KEEP** are working pieces worth not losing.
> Use ~~strikethrough~~ to kill an idea, **bold** to lock one.

---

## 0. One sentence
▢ REWRITE — what is this, in one sentence, in your words:

>

---

## 1. The concept (established — edit if wrong)
- The "other" = **the lips that have had filler**, as a **distributed collective** that speaks "we". Not one person; an organ that lost autonomy.
- Its *Umwelt* contains **only mouths**. So the only input is a mouth.
- The device is **autonomous** (interaction model C): you are **observed, not a user**.
- Frame: a small **square screen** where a mirror would be — it refuses your face/eyes/identity and keeps only your mouth.

▢ REWRITE — anything above that's wrong or missing:

>

---

## 2. Hard constraints (the rules that keep getting broken — confirm/fix each)
- ✓ **Real flesh only.** Real photographed lips + the live camera. The computer may *distort/move* flesh, but must **not draw/illustrate** lips. (No CG/procedural lips.)
- ✓ **No manual input.** No touch, drag, scroll, buttons. The only input is the mouth.
- ✓ **Almost no text.** ▢ decide: catalog numbers only? or truly zero text?
- ✓ **Square**, dark, body-horror-controlled: clinical+wet, disturbing, **not cute**, not gore-for-shock, not an Instagram-beauty/ad look.

▢ REWRITE — add the constraint(s) I keep violating:

>

---

## 3. THE FUNDAMENTAL PROBLEM (why it's still "no")
▢ REWRITE — this is the important one. What is actually wrong with what you've seen?
Pick / write the real reason so the next build doesn't repeat it:

- [ ] The **look** is wrong (still reads CG / cheap / cute / generic / not disturbing)
- [ ] The **collective** is wrong (grid? pile? fog? something else entirely?)
- [ ] The **live mouth / mirror moment** is wrong (can't tell it's me / not impactful)
- [ ] The **interaction model** is wrong (the whole flow is off)
- [ ] The **concept itself** drifted from what you meant
- [ ] It's **technically broken / I can't even run it**
- [ ] Other:

In your words, what should it feel like that it currently doesn't:

>

---

## 4. The interaction / flow
▢ REWRITE — describe the experience start to finish, in your words. Forget my versions.
(What does it do when nobody is there? What happens the moment a mouth appears?
What is the climax? How does it end / loop?)

>

Current version (for reference, not a constraint): endless scrolling catalog of real lips →
mouth detected, scroll pauses → live mouth surfaces, swells to a template → absorbed into a
numbered cell → scroll resumes.

---

## 5. The visual language
▢ REWRITE — references, words, colors, motion. What does it LOOK like?
(Name films/images/textures. e.g. "wet eXistenZ tissue", "packaged meat", "medical scan",
"specific Pinterest image #__".)

>

---

## 6. What already works (don't rebuild these unless needed) ✓ KEEP
- **Real lip material:** 23 real mouth cutouts (alpha PNGs) pulled from the PAGMAR DB →
  `Umwelt/lips/lip0…22.png`. Swappable; more available in `PAGMAR-base/server/data/*/body_parts/mouth/`.
- **Live mouth detection:** MediaPipe FaceLandmarker (in-browser, CDN) → crops the live webcam
  to the lips only, every frame. Works.
- **Engine:** single standalone `Umwelt/index.html`, WebGL2 sprite renderer (real lip textures,
  flow-warp / wet / melt), no build step, no PAGMAR dependency.
- **Standalone & separate** from the final project. Mirrored to the iCloud course folder.
- **Run:** `cd Umwelt && python3 -m http.server 8770` → Chrome `http://localhost:8770`
  (camera needs localhost). Debug: `?demoface` (still face), `?nocam` (no detection).

---

## 7. What to throw away
▢ REWRITE — which of my past attempts should be deleted/ignored entirely?
(grid catalog / floating pile / liquid fog / metaball CG / the climax / the numbers / …)

>

---

## 8. Done = ?
▢ REWRITE — how will we know it's right? One concrete sentence:

>

---

## 9. LOCKED REFRAME (2026) — **Umwelt = computer vision**
> The big fix. The "other" is no longer the lips — it is the **computer-vision system looking at them**.
> The Umwelt belongs to the machine that scans, isolates, measures, classifies, and compares every mouth
> against a statistical **average it calls "perfect"** ("perfect" = "like everyone else"). No emotion, only
> processing. The viewer is not a user — they are **data being processed** (model C, sharpened).
>
> **The heart is the collision:** the cold analytical gaze (cyan instrument, coordinates, statistics, catalog,
> PAGMAR register) over **real wet living meat** (the live mouth). Not either/or — the tension between them.
>
> - The psychedelic distortion loop is **dropped** → analytical acquisition (a stepped scan that isolates the
>   lip from the ground and **chills the meat**).
> - The template is the **statistical AVERAGE** (computed honestly from the lip rings the system has seen); the
>   spine is one number, `Δ AVG %` (deviation from the mean), driven to `00.0%` during NORMALIZE.
> - The ending is the **catalog**: 64 records · **1 shape** — every mouth normalized to the average, identical.
> - Built as **`index-vision.html`** (clone of the swap/catalog version). Cold register confirmed by the
>   who-am-we copy / art-director / typography agents (PASS). See `RESEARCH.md` for the full map.
