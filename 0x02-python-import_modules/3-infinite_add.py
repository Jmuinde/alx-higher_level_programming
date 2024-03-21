#!/usr/bin/python3
from sys import argv


if __name__ == "__main__":
    total = 0
    if len(argv) > 1:
        for k in range(1, len(argv)):
            total += int(argv[k])
    print(total)
