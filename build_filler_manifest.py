"""
Builds filler_image_manifest.csv for the 48 filler images used in the
trust/social-distance follow-up study (one fixed image per concept;
match/mismatch is which word is paired with it in the sentence frame, not a
second image -- see the adjnorm-survey skill, "Follow-up study design
session (2026-11-06)" section).

Run from this repo's root after copying new filler_*.png files in.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(r"C:\Users\ctnic\OneDrive\Desktop\Adjnorm Finished Images\Analysis")))
from build_critical_filler_sentences import FILLERS  # noqa

HERE = Path(__file__).resolve().parent
BASE_URL = "https://chandlernichols41.github.io/adjnorm-finished-images/"


def slug(image_desc):
    return image_desc.split(",")[0].replace(" ", "_")


def main():
    rows = []
    for category, items in FILLERS.items():
        for image_desc, noun, match_word, mismatch_word in items:
            filename = f"filler_{category}_{slug(image_desc)}_pic.png"
            if not (HERE / filename).exists():
                raise FileNotFoundError(filename)
            rows.append({
                "category": category, "concept": image_desc, "noun": noun,
                "match_word": match_word, "mismatch_word": mismatch_word,
                "filename": filename, "image_url": BASE_URL + filename,
            })

    out = HERE / "filler_image_manifest.csv"
    with open(out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["category", "concept", "noun", "match_word",
                                           "mismatch_word", "filename", "image_url"])
        w.writeheader()
        w.writerows(rows)
    print(f"Wrote {out} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
