#!/usr/bin/python3
import sys
if len(argv) == 0:
    print("{:d} arguments.".format(len(sys.argv)))
else:
    print("{:d} arguments:".format(len(sys.argv)))
    for i in len(argv)-1:
        print("{:d}: {}".format(len(sys.argv),argv[i]))
