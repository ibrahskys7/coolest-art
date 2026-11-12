#!/usr/bin/env python3
"""Make the coolest art (make.fun bounty coolest-art-01).

Writes the bundled picture to /output/entry.png.

The picture -- a phoenix of fire and electric-blue feathers soaring over
a neon cyberpunk city at dusk -- is stored in this repository as art.png.
This program copies it byte-for-byte to /output/entry.png, so every run
writes identical bytes. No network is used.

After copying, it verifies the output: the file must be a valid PNG of
the same size as the bundled source, and its bytes must match the source
exactly. If the check fails, the program exits with an error instead of
leaving a bad entry behind.
"""

import hashlib
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "art.png")
DST = "/output/entry.png"

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _is_png(path):
    with open(path, "rb") as f:
        head = f.read(33)
    if len(head) < 33 or head[:8] != PNG_SIGNATURE:
        return False
    # First chunk must be IHDR (13 bytes of image header).
    length, ctype = struct.unpack(">I4s", head[8:16])
    return ctype == b"IHDR" and length == 13


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    if not _is_png(DST):
        print("error: %s is not a valid PNG" % DST, file=sys.stderr)
        sys.exit(1)
    if _sha256(SRC) != _sha256(DST):
        print("error: %s does not match the bundled picture" % DST,
              file=sys.stderr)
        sys.exit(1)
    print("wrote %s (%d bytes, sha256 %s)"
          % (DST, os.path.getsize(DST), _sha256(DST)[:16]))


if __name__ == "__main__":
    main()
