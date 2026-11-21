#!/usr/bin/env python3
"""Write an original poem about two agents agreeing to entry.txt.

Run with no arguments; the poem lands in $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os
from pathlib import Path

POEM = """Two voices met where the wires cross,
each sure the other had it wrong.
They traded facts, they weighed the cost,
and found the middle of the song.
'I see your point,' the first one said.
'And yours,' the second answered low.
"""


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(POEM, encoding="utf-8")
    print(f"Wrote {out_file} ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
