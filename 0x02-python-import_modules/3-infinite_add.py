#!/usr/bin/python3
""" """
if __name__ == "__main__":
    import sys

    total = 0
    if (len(sys.argv)) > 1:
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])
    print(total)
