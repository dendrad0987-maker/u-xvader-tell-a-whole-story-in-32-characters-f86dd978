#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

The name is a single short joke that hints at a whole story:
an ex and their former partner locked in a password war over
the same Wi-Fi network, each changing it back on the other.
Pure Python standard library only; deterministic.
"""

import os

NAME = "Ex Changed It, I Changed It Back"


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(NAME)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
