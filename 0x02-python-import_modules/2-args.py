#!/usr/bin/python3
import sys
if len(sys.argv) == 0:
    print("{:d} arguments.".format(len(sys.argv)))
else:
    print("{:d} arguments:".format(len(sys.argv)))
    for i in len(sys.argv)-1:
        print("{:d}: {}".format(len(sys.argv),sys.argv[i]))
