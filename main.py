#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry (slot 1).

Writes one line (<=140 chars) to /output/entry.txt.
Deterministic, no network, no input files.

Entry choice (self-judged tournament vs fresh candidates, after studying
all 125 existing entries in the competition detail file):
- Winner: the line below. Fresh angle — no existing entry uses the
  "ran it over, it survived, so it's a roommate now" turn. The crowded
  angles (cliff sensor vs rug/staircase, load-bearing crumb, seniority,
  dust-bunny union, cat) were all deliberately avoided.
- Judge criteria fit: first-person vacuum voice; excuse for a missed
  spot; rooted in the vacuum's own world (running over crumbs); joke
  lands on first read with a clean turn at the end ("it's a roommate").
- Length: 90 characters, well inside the 1-140 gate.
"""

import os

ENTRY = (
    "I ran over that crumb twice and it survived. "
    "At that point it's not dirt, it's a roommate."
)


def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry length {len(text)} out of range"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
