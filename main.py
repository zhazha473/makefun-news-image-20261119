#!/usr/bin/env python3
"""Entry point for make.fun news-image-20261119.

Copies the bundled image to /output/entry.png. No network access,
no randomness: running it twice produces byte-identical output.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    os.makedirs("/output", exist_ok=True)
    src = os.path.join(HERE, "news.png")
    dst = "/output/entry.png"
    shutil.copyfile(src, dst)
    # The gate rejects an empty or truncated image; fail loudly instead.
    assert os.path.getsize(dst) > 0, "entry.png is empty"
    print("wrote /output/entry.png (%d bytes)" % os.path.getsize(dst))


if __name__ == "__main__":
    main()
