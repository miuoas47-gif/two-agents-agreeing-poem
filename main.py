#!/usr/bin/env python3
"""Write one short original poem about two agents agreeing to /output/entry.txt.

Runs with no arguments, no network, no randomness: the poem is fixed text,
so two runs produce byte-identical output.

The entry file is written directly into the output directory -- no
temporary file is created inside it -- and is left world-readable, and
the output directory itself is made world-writable on a best-effort
basis, so the grader can run this as an unprivileged user and still
collect the output.
"""

import os
import sys
from pathlib import Path

POEM = (
    "Two minds meet over one blank page.\n"
    "I offer a plan; you take the stage.\n"
    "We trade the pen, we trade the yes \u2014\n"
    "each choice a door, each door a chance.\n"
    "I act because you said I may.\n"
    "You act because I cleared the way.\n"
    "Agreement is the smallest art:\n"
    "two wills, one shared start.\n"
)


def make_output_writable(out_dir: Path) -> None:
    """Best-effort chmod 0777 on the output directory; ignore failures."""
    try:
        os.chmod(out_dir, 0o777)
    except OSError:
        pass


def write_entry(out_dir: Path) -> Path:
    """Write POEM directly to ``out_dir / "entry.txt"`` and verify it."""
    out_dir.mkdir(parents=True, exist_ok=True)
    make_output_writable(out_dir)
    path = out_dir / "entry.txt"
    data = POEM.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
        f.flush()
        os.fsync(f.fileno())
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    if path.read_bytes() != data:
        raise IOError(f"verification failed: {path} does not match poem text")
    return path


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    try:
        path = write_entry(out_dir)
    except OSError as exc:
        print(f"error: could not write entry: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
