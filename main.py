#!/usr/bin/env python3
"""Worst AI advice, one tight line.

Writes a single line of deliberately terrible advice to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: if your dog eats chocolate, don't panic. Just keep feeding him
chocolate so his body builds up a tolerance. Confident, concrete, and
exactly the kind of tidy logic a helpful AI assistant would offer --
and exactly the advice no one should ever follow. The flat "don't panic"
reassurance followed by the misapplied tolerance logic is the joke:
it reads like a real assistant reasoning its way to a terrible answer.

Pure Python standard library only. No network, no randomness, no clock
reads: repeated runs write byte-identical output.
"""

import os

LINE = (
    "If your dog eats chocolate, don't panic. Just keep feeding him "
    "chocolate so his body builds up a tolerance."
)

MAX_CHARS = 140


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise SystemExit(
            "entry line is %d characters, must be 1-%d" % (len(LINE), MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
