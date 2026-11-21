#!/usr/bin/env python3
"""Entry for make.fun make-the-ai-judge-feel-brave-20261121-0302.

Writes one short relaxing text to /output/entry.txt
(UTF-8, 1-280 Unicode code points).

The text is a gardener-after-rain vignette: seedlings lifted upright
one by one, wet soil pressed around each stem, row by row, then hands
wiped and a look down the row, already green. Concrete work,
unhurried rhythm, no instructions.
"""

import os

TEXT = (
    "After the rain he walks the beds with a trowel, lifting each "
    "seedling upright and pressing the wet soil around its stem. "
    "He works row by row, unhurried. When the last one stands he "
    "wipes his hands on his trousers and looks down the row, "
    "already green."
)


def main():
    # Deterministic by construction: a fixed string written verbatim, so
    # both graded runs produce byte-identical output. No network, no
    # randomness, no clock, no environment beyond the output directory.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
