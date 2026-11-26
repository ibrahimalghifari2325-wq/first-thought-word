#!/usr/bin/env python3
"""Write one word, the first that comes to mind, to /output/entry.txt.

The word is zugzwang: chess for a position where any move worsens your
situation, from German Zug (move) + Zwang (compulsion)."""

import os

WORD = "zugzwang"

# The bounty gates the word at 1-24 characters.
if not 1 <= len(WORD) <= 24:
    raise SystemExit("word must be 1-24 characters")

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(WORD)
