# adjnorm-finished-images

Image host for the Adjnorm scalar-adjective study's **finished** stimulus sets — the 68
adjective pairs (of 70 total) that currently have a complete neutral/weak/strong image
set, copied from `Adjnorm Finished Images` on 2026-09-27. Two pairs (`brilliant_intelligent`,
`certain_possible`) are excluded because they have no images yet.

Served via GitHub Pages at:
**https://chandlernichols41.github.io/adjnorm-finished-images/**

All 204 images sit flat at the repo root (no subfolders) — reference any file directly:
`https://chandlernichols41.github.io/adjnorm-finished-images/<filename>.png`

## image_manifest.csv

One row per image (204 rows), columns:
- `pair` — folder name from the source project (e.g. `ancient_old`)
- `role` — `neutral` / `weak` / `strong`
- `word` — the adjective actually used for that role (blank for neutral)
- `weak_word` / `strong_word` — both words in the pair, corrected where the folder name
  didn't match the real word (`crystal_transparent`'s strong word is **Crystal-clear**,
  not `crystal`; `obligatory_encourage`'s weak word is **encouraged**, not `encourage`)
- `filename` — the exact on-disk filename
- `image_url` — the ready-to-use Pages URL for that image

Use this file as the starting data for a Qualtrics Loop & Merge block.
