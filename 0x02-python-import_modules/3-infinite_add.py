#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    count = 0
    for i in range(len(sys.argv)):
        count += sys.argv[i]
        print("{:d}".format(count))
#     if len(sys.argv)-1 == 0:
#         print("{:d} arguments.".format(len(sys.argv)-1))
#     else:
#         print("{:d} arguments:".format(len(sys.argv)-1))
#         for i in range(1,len(sys.argv)):
#             print("{:d}: {}".format(i,sys.argv[i]))
