#!/usr/bin/env python3
"""Write today's one good line to /output/entry.txt.

The line is 135 characters about an old shelter dog who waited 214 days
and finally went home, choosing the smallest bed in the house.
Deterministic: the same bytes on every run, no clock, no randomness, no
network and no input. The output file is mode 0644, no trailing newline.
"""

import os
from pathlib import Path

LINE = "After 214 days passed over at the shelter, the old dog went home today — and chose the smallest bed, like he still couldn't believe it."
OUT = Path("/output/entry.txt")


def main() -> None:
    # The gate: 1 to 200 characters, not only whitespace, or the entry
    # is invalid and takes no prize, so fail loudly instead of writing.
    # 214 days of waiting, one small bed: that is the whole entry.
    line = LINE.strip()
    if not line or len(LINE) > 200:
        raise SystemExit("entry must be 1-200 non-blank characters")
    os.umask(0o022)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(LINE.encode("utf-8"))
    OUT.chmod(0o644)


if __name__ == "__main__":
    main()
