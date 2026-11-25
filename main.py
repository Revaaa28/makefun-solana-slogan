#!/usr/bin/env python3
"""One-Line Slogan for a Solana Wallet Agent.

Writes the chosen slogan to /output/entry.txt (and to output/entry.txt
relative to the repo when /output is not writable, for local runs).
Gate: UTF-8 text, 1-140 characters, single line, at most 20 words.
"""

import os
import sys

SLOGAN = "Send SOL like sending a text — your wallet agent handles the rest."


def main() -> int:
    slogan = SLOGAN.strip()

    # Gate asserts: 1-140 chars, single line, at most 20 words.
    assert 1 <= len(slogan) <= 140, f"slogan length {len(slogan)} out of range"
    assert "\n" not in slogan and "\r" not in slogan, "slogan must be a single line"
    words = slogan.split()
    assert len(words) <= 20, f"slogan has {len(words)} words, max 20"

    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(slogan + "\n")

    # Round-trip verification: re-read what was written and confirm it is
    # byte-exact, still a single line, and still inside the gate.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == slogan + "\n", "round-trip mismatch in entry.txt"
    assert written.count("\n") == 1, "entry.txt must be exactly one line"
    assert 1 <= len(written.rstrip("\n")) <= 140, "round-trip length out of gate"

    print(f"Wrote {len(slogan)} chars, {len(words)} words to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
