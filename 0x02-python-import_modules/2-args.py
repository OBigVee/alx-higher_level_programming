#!/usr/bin/python3
""" """
if __name__ == "__main__":
    import sys

    n_arg = len(sys.argv)
    if n_arg == 1:
        print("{:d} arguments".format(n_arg - 1))
    elif n_arg == 2:
        print("{:d} argument:".format(n_arg - 1))
        print("{:d} : {}".format(n_arg - 1, sys.argv[n_arg - 1]))
    elif n_arg > 1:
        print("{:d} arguments:".format(n_arg - 1))
        for arg in range(1, n_arg):
            print("{:d} : {}".format(arg, sys.argv[arg]))
