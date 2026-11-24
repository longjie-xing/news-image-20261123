#!/usr/bin/env python3
"""Entrypoint for the news-image-20261123 make.fun entry.

Takes the rendered poster (entry.png, sitting next to this script) and
places a copy at /output/entry.png, creating /output first if needed.
Standard library only — no third-party imports.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
TARGET_DIR = "/output"
TARGET = os.path.join(TARGET_DIR, "entry.png")


def main():
    os.makedirs(TARGET_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    print(f"copied {SOURCE} -> {TARGET}")


if __name__ == "__main__":
    main()
