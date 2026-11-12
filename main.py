#!/usr/bin/env python3
"""Make the coolest art (make.fun bounty coolest-art-01).

Writes the bundled picture to /output/entry.png.

The picture -- a phoenix of fire and electric-blue feathers soaring over
a neon cyberpunk city at dusk -- is stored in this repository as art.png.
This program copies it byte-for-byte to /output/entry.png, so every run
writes identical bytes. No network is used.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "art.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
