#!/usr/bin/env python3
"""Copy entry.png to /output/entry.png (stdlib only)."""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST_DIR = "/output"
DST = os.path.join(DST_DIR, "entry.png")


def main():
    os.makedirs(DST_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"Copied {SRC} -> {DST}")


if __name__ == "__main__":
    main()
