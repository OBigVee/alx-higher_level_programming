#!/usr/bin/python3
""" """
if __name__ == "__main__":
    import sys
    import hidden_4

    data = dir(hidden_4)
    for name in data:
        if name[:2] != "__":
            print(name)
