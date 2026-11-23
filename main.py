#!/usr/bin/env python3
"""Copy the pre-drawn poster to the harness output path.

The poster (entry.png) is drawn by make-poster.py and shipped in this
repository. This program just places it where the harness expects it:
 /output/entry.png. Standard library only, no network.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)


if __name__ == "__main__":
    main()
