#!/usr/bin/env python3
"""Local gate test: run main.py the way the grader does and check the gate.

The gate requires /output/entry.txt to be UTF-8 text of 1 to 200 characters,
not only white space, and to match the tip this entry ships.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXPECTED = (ROOT / "entry.txt").read_text(encoding="utf-8").strip()


def main() -> int:
    subprocess.run([sys.executable, str(ROOT / "main.py")], check=True)
    out = Path("/output/entry.txt")
    assert out.is_file(), "/output/entry.txt was not written"
    text = out.read_text(encoding="utf-8")
    assert text == EXPECTED, f"output differs from entry.txt: {text!r}"
    assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
    assert text.strip(), "output is only white space"
    print(f"PASS: {len(text)} characters, matches entry.txt")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
