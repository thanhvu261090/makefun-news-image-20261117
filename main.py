#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261117 (Python 3.13).

The repository ships the finished front page as entry.png, and this program
copies it to the output directory as entry.png. Standard library only, no
network, and deterministic: the output bytes are always exactly the bytes
of the shipped image, so two runs write identical files.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def output_dir():
    """The grader's writable output directory, or its local stand-in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, IMAGE_NAME)
    with open(source, "rb") as f:
        magic = f.read(8)
    if magic != b"\x89PNG\r\n\x1a\n":
        raise SystemExit(f"{source} is not a whole PNG file")
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, IMAGE_NAME)
    shutil.copyfile(source, target)
    size = os.path.getsize(target)
    print(f"wrote {target} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
