#!/usr/bin/env python3
"""Seed a FIXED, DISTINCT donor pool into the isolated Umwelt swap instance and write
their image_ids to swap/donors.json — the client swaps ONLY against these, so live
viewer uploads can never pollute the donor set (which was making it swap your mouth
with your own face).

Donor sources, in priority order:
  1. files passed as args
  2. every image in  swap/donors/   (drop your own donor FACE photos there)
  3. fallback: PAGMAR test fixtures (distinct strangers)

Run with the PAGMAR server venv (server must be up on :8001):
  PAGMAR-base/server/.venv/bin/python Umwelt/swap/seed-donors.py
"""
import sys, glob, os, time, json, requests

HERE = os.path.dirname(os.path.abspath(__file__))
B = "http://localhost:8001/api/v1"

def sources():
    if sys.argv[1:]:
        return sys.argv[1:]
    folder = sorted(glob.glob(os.path.join(HERE, "donors", "*.*")))
    folder = [f for f in folder if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))]
    if folder:
        return folder
    return sorted(glob.glob(os.path.join(HERE, "..", "..", "PAGMAR-base",
                 "server", "tests", "fixtures", "pexels-*.jpg")))[:10]

def seed(f):
    with open(f, "rb") as fh:
        r = requests.post(f"{B}/upload", files={"image": fh},
                          data={"rotation": "center", "kind": "portrait"}, timeout=180).json()
    iid = r.get("existing_image_id")
    if not (iid and r.get("existing_has_segmentations")):
        iid = requests.post(f"{B}/session/{r['session_id']}/detect-pose", json={}, timeout=180).json().get("image_id")
    for _ in range(90):                                   # wait for the mouth part (segmentation ~5-13s)
        bp = requests.get(f"{B}/images/{iid}/body-parts", timeout=30).json().get("body_parts", [])
        if any(p.get("body_part_id") == "mouth" and p.get("bbox_width") for p in bp):
            return iid
        time.sleep(1)
    return None

ids = []
for f in sources():
    try:
        i = seed(f)
        print("seeded", os.path.basename(f), (i or "NO-MOUTH")[:8])
        if i:
            ids.append(i)
    except Exception as e:
        print("err", f, e)

out = os.path.join(HERE, "donors.json")
json.dump(ids, open(out, "w"))
print(f"\ndone {len(ids)} donors -> {out}")
print("ids:", ids)