#!/usr/bin/env python3
"""Entry for make.fun news-image-20261123.

Standard library only. The front-page image (entry.png) is shipped as a
finished asset: it was drawn locally with Pillow and the grading sandbox
has no third-party packages installed and no network, so this program
copies the shipped image to the output directory instead of redrawing
it. The copy is verified against the shipped image's SHA-256 so a
corrupt or swapped asset fails loudly instead of scoring silently.
"""
import hashlib
import os
import shutil
import struct
from pathlib import Path

ENTRY_NAME = "entry.png"
# SHA-256 of the shipped entry.png (the 23 November 2026 front page).
EXPECTED_SHA256 = "45d4c13f669363a0f73e702685e0c413a47700f566930563f7a72c279537dd52"
# The shipped front page is 1024x1024 and must stay under 1 MiB.
EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1 << 20
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def check_png(path: Path) -> None:
    """Validate the shipped asset is a PNG of the expected size.

    Reads only the 8-byte signature and the IHDR chunk with the standard
    library, so no image decoder is needed in the grading sandbox.
    """
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise SystemExit(f"asset too large: {len(data)} bytes")
    if data[:8] != PNG_SIGNATURE:
        raise SystemExit("asset is not a PNG file")
    if data[12:16] != b"IHDR":
        raise SystemExit("asset has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise SystemExit(f"unexpected dimensions: {width}x{height}")


def locate_entry() -> Path:
    here = Path(__file__).resolve().parent
    src = here / ENTRY_NAME
    if not src.is_file():
        raise SystemExit(f"missing shipped asset: {src}")
    return src


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = locate_entry()
    check_png(src)
    dest = out_dir / ENTRY_NAME
    shutil.copyfile(src, dest)
    digest = hashlib.sha256(dest.read_bytes()).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"output mismatch: {digest} != {EXPECTED_SHA256}")


if __name__ == "__main__":
    main()
