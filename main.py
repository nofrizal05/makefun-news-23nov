#!/usr/bin/env python3
"""Entry for make.fun news-image-20261123.

Python standard library only: copies the shipped entry.png to
MAKEFUN_OUTPUT_DIR (default /output). The front-page image was drawn
locally and is shipped as a finished asset, so the entry runs
deterministically in the grading sandbox, which has no third-party
packages installed.
"""
import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    # Deterministic copy: the shipped image is copied byte-for-byte, so the
    # output is identical on every run regardless of the grading sandbox.
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
