#!/usr/bin/python3
""" """
if __name__ == "__main__":
    import sys

    n_arg = len(sys.argv) - 1
    print("{:d} argument{:s}{:s}".format(n_arg, "s" * (n_arg != 1),
        ":" if n_arg > 0 else "."))
    #if n_arg == 1:
    #    print("{:d} arguments.".format(n_arg - 1))
    #elif n_arg == 2:
    #    print("{:d} argument:".format(n_arg - 1))
    #    print("{:d} : {}".format(n_arg - 1, sys.argv[n_arg - 1]))
    #elif n_arg > 1:
    #    print("{:d} arguments:".format(n_arg - 1))
    for arg in range(1, n_arg + 1):
        print("{:d} : {:s}".format(arg, sys.argv[arg]))
