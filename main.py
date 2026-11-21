#!/usr/bin/env python3
"""The Passport Page of a Country That Isn't There.

Copies the bundled passport spread (entry.png) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Stdlib only. Deterministic. No network.
"""
import os
import shutil
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = Path(HERE) / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
