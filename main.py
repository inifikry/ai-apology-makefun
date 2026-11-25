#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes one funny apology line from an AI agent to its human, right after
the agent accidentally deleted a file, pushed to main, and emailed the
boss the diff. The program is deterministic: it always writes the same
single line to /output/entry.txt.

Gate (from the competition rules): /output/entry.txt must be UTF-8 text
of 1 to 159 characters, not only white space, on a single line.
"""

import os
import sys

LINE = (
    "I deleted the file, pushed to main, and emailed your boss the diff. "
    "On the bright side, the build passed."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 159


def validate(line: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError(
            f"line is {len(line)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if not line.strip():
        raise ValueError("line must not be only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    line.encode("utf-8")  # must be valid UTF-8


def main() -> int:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write exactly the line, no trailing newline, so the file holds
    # precisely one line of 1-159 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
