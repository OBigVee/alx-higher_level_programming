#!/usr/bin/python3
import sys
if len(sys.argv) == None:
    print("{:d} arguments.".format(len(sys.argv)))
else:
    print("{:d} arguments:".format(len(sys.argv)))
    for i in range(len(sys.argv)-1):
        print("{:d}: {}".format(len(sys.argv),sys.argv[i]))
