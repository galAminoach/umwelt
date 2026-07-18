# UMWELT — *the lips that will not reflect you*

## Quick start (current piece: `mix.html`)
```bash
python3 serve.py
# open http://localhost:8770/mix.html in Chrome/Edge, allow the camera, lean in
```
- Needs internet on first load (the MediaPipe runtime + face model come from a CDN).
- A webcam needs a secure context, so use localhost — don't open the file directly.
- Debug: `http://localhost:8770/mix.html?debug=1` shows the state HUD and exposes `__go('STATE')` in the console to jump between states.

The sections below describe the earlier catalog piece (`index.html`); `mix.html` is the current vision piece.

---

A standalone interface exercise. **This is NOT part of the PAGMAR final project** — a separate course piece. It reuses real material from PAGMAR (captured lip cutouts) and the lip-detection technique, but shares no code or runtime.

## What it is

A small **square screen** where a vanity / compact mirror would be. The surface is an **endless catalog of real lips** — a cold grid of photographed mouths, packaged-product / "fresh meat" aesthetic, **scrolling upward by itself, forever** (new rows enter the bottom, old exit the top; catalog numbers `№NNN` keep counting up). The cage is cold and systematic, but the flesh disobeys it: lips breathe in their cells and occasionally **bulge past their borders and melt into a neighbour**.

It is **autonomous** — no touch, no drag, no manual scroll. You are observed, not a user. The only input is your mouth: when the camera detects one, the **scroll pauses**, the catalog recedes, and **your own mouth surfaces, sharp, in the centre**. Slowly it is swollen toward the collective's template — fuller, the same curve — then **absorbed into an opening cell, given a number, and it joins the endless stream**; the scroll resumes without you.

**Everything on screen is real flesh.** The catalog lips are real photographs (alpha cutouts from the PAGMAR DB); your mouth is the live webcam. The shader only *distorts and moves* them — artificial motion on real flesh is what makes it disturbing rather than illustrative.

### The flow (no body text — only catalog numbers)
endless scrolling catalog of real lips → a mouth is detected, scroll **pauses** → **your live mouth surfaces (sharp)** → it slowly swells to the template → it is absorbed into a numbered cell and joins the stream → scroll resumes.

## Run
A webcam needs a **secure context**, so serve over localhost (not `file://`):
```bash
cd "ex3 - unwelt"
python3 -m http.server 8770
# open http://localhost:8770 in Chrome/Edge, allow the camera, lean in
```
- **Preview the climax without a webcam:** `http://localhost:8770/?demoface` — drives the flow from a still face.
- **Idle catalog only (exhibition / no detection):** `http://localhost:8770/?nocam` — just the endless scrolling catalog.
- The MediaPipe runtime + model load from a CDN (needs internet on first run).

## The material
- `lips/lip0.png … lip22.png` — **real mouth cutouts** (alpha, lip-shaped) taken from the PAGMAR capture database (`body_parts/mouth/upscaled-cropped-cutout.png`). They are real participants' lips — swap or thin them out if you prefer.
- `faces/face1.jpg` — only used by `?demoface`.
- Captured live mouths are added to the pile during a session; the count persists in `localStorage` (`umwelt.count`).

## Tuning (top of the `<script>`)
- `buildCollective(30)` — number of floating lips in the pile.
- `DWELL` (seconds) — state durations; `CRAWL` (~9 s) is the slow swell to the template.
- Per-sprite `warp` (in `frame()`) — how much the real flesh distorts/melts.
- In the fragment shader: the neon-rim amount, `hueRot` range, wet specular.

## Requirements
WebGL2 + a modern browser (Chrome/Edge). Tested on macOS.

---

## Real mouth-swap mode (`?swap`)  — optional, needs the isolated server

The flash beat can replace your captured mouth with **real model-swapped mouths** (other people's
mouths composited onto your face) instead of the client-side cutout overlay. This uses PAGMAR's
**bulk-swap** on an **isolated** server instance that has its **own datastore** — it never touches
PAGMAR's `server/data` / `segmentation.db`.

**Setup**
1. Start the isolated swap server (stops any other PAGMAR uvicorn — they can't run together):
   ```bash
   Umwelt/swap/start-server.sh        # → http://localhost:8001, data in Umwelt/.swap-data
   ```
   (env it sets: `PAGMAR_DATA_DIR`/`PAGMAR_DB_PATH` = Umwelt-only, `SWAP_BACKEND=direct_paste`,
   `HAIRFAST_ENABLED=0`, `USE_UPSCALER=0` so a face segments in ~5 s.)
2. One-time donor seed (already done; re-run if you wipe `.swap-data`):
   ```bash
   PAGMAR-base/server/.venv/bin/python Umwelt/swap/seed-donors.py
   ```
3. Open Umwelt with the flag: **`http://localhost:8770/?swap`** (add `&debug` for the HUD `swap:` status).

**How it works:** at the start of the slow DISTORT build, the full webcam frame is uploaded →
segmented → donor mouths are **bulk-swapped** onto it (~5 s, fans out concurrently) → the composites
are cropped to your mouth and **warmed**, so the FLASH plays them back fast from cache. If the server
is unreachable, it **falls back** to the client overlay automatically (so `?demoface`/offline still run).

**Note:** this depends on `PAGMAR-base/server`'s venv + checkpoints and a small guarded change in
`server/config.py` (env-overridable `DATA_DIR`/`DB_PATH`, defaults unchanged). It is **not** part of
the standalone HTML — without `?swap` the piece runs fully standalone.
