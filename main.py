#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — one line, under 200
characters, in which a dog explains why the homework got eaten.
Writes the line verbatim to entry.txt.

A judge model reads entries two at a time and keeps the funnier line, so
the line is built to land on its own: the homework smelled of bacon, lay
unguarded during the dog's 3 p.m. existential crisis, and looked delicious
— self-defense, with a final twist that it would happen again before
algebra, because the dog would rather eat homework than do it.

Deterministic, stdlib only, no network, no randomness, no file reads
outside the repository.
"""

import os
from pathlib import Path

EXCUSE = "The homework smelled faintly of bacon, lay unguarded during my 3 p.m. existential crisis, and frankly looked delicious — I ate it out of self-defense, and I'd do it again before algebra."

MAX_CHARS = 199


def main() -> None:
    assert 1 <= len(EXCUSE) <= MAX_CHARS, f"line is {len(EXCUSE)} chars (max {MAX_CHARS})"
    assert "\n" not in EXCUSE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EXCUSE, encoding="utf-8")
    print(f"wrote {len(EXCUSE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
