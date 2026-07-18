#!/usr/bin/env bash
# Umwelt isolated swap server — a 2nd PAGMAR instance on :8001 with its OWN datastore
# (Umwelt/.swap-data). It NEVER touches PAGMAR's server/data/segmentation.db.
# Hairfast + upscaler are OFF so a face segments in ~5s (swaps ready by the flash).
# NOTE: launching this STOPS any other PAGMAR uvicorn (boot frees the webcam/port) —
# you can't run PAGMAR's server and this at the same time.
SERVER=/Users/galaminoach/Documents/Pagmar/PAGMAR-base/server
DATA=/Users/galaminoach/Documents/Pagmar/Umwelt/.swap-data
mkdir -p "$DATA"
cd "$SERVER" || exit 1
# SWAP_BACKEND=flux → generative inpaint (donor mouth blended ONTO your face via fal.ai;
# needs FAL_KEY in server/.env + internet; costs per swap). direct_paste just pastes on top.
HAIRFAST_ENABLED=0 USE_UPSCALER=0 SWAP_BACKEND="${SWAP_BACKEND:-flux}" \
PAGMAR_DATA_DIR="$DATA" PAGMAR_DB_PATH="$DATA/segmentation.db" \
exec .venv/bin/python -m uvicorn main:app --port 8001
