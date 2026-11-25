#!/usr/bin/env python3
"""Entry for make.fun u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Writes one excuse, exactly 114 characters, to /output/entry.txt.

The program is deliberately boring: no input, no network, no randomness.
Every run writes the exact same bytes, and it refuses to write anything
unless the line still matches its pinned length and sha256, so a typo or
an accidental edit fails loudly here instead of silently on the grader.
"""

import hashlib
import os
import sys

EXCUSE = (
    "I spent the whole deadline writing this apology. "
    "It is the only thing I have ever shipped on time, and it is late."
)

# Pinned so the program can prove it wrote the intended line.
EXPECTED_LENGTH = 114
EXPECTED_SHA256 = "078d93efbf2c14f1524e0bfc39825bdc910788f3b5a9bec99637942dcb21bee0"

OUTPUT_PATH = "/output/entry.txt"


def check_excuse() -> None:
    """Fail fast if the line drifted from what was pre-judged."""
    encoded = EXCUSE.encode("utf-8")
    if len(EXCUSE) != EXPECTED_LENGTH:
        sys.exit(f"excuse is {len(EXCUSE)} characters, expected {EXPECTED_LENGTH}")
    if len(encoded) != EXPECTED_LENGTH:
        sys.exit("excuse is not pure ASCII of the expected byte length")
    digest = hashlib.sha256(encoded).hexdigest()
    if digest != EXPECTED_SHA256:
        sys.exit(f"excuse sha256 {digest} does not match pinned {EXPECTED_SHA256}")
    if EXCUSE != EXCUSE.strip():
        sys.exit("excuse has leading or trailing whitespace")


def main() -> None:
    check_excuse()
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    # Read-back gate: prove the bytes on disk are exactly the pinned
    # line before reporting success — a write that silently truncated
    # or corrupted must fail here, not on the grader.
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != EXCUSE.encode("utf-8"):
        sys.exit("read-back mismatch: /output/entry.txt is not the excuse")
    print(f"wrote {len(written)} bytes to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

