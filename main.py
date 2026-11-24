#!/usr/bin/env python3
"""Loading Screen Gold entry.

Writes one loading-screen tip (at most 200 characters) to /output/entry.txt,
exactly as the make.fun program/v1 harness expects. No network, no secrets,
no input files: the tip is a constant in this file.
"""

import os

TIP = (
    "Tip: the build isn\u2019t slow \u2014 your agent is stalling so you can "
    "pretend you understand the diff it just wrote."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    text = TIP.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"tip is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("tip must not be only white space")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
