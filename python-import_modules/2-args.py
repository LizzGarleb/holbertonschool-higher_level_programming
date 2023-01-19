#!/usr/bin/python3
import sys
argc = len(sys.argv)

if argc == 1:
    print("0 arguments.")
else:
    print("{} arguments:".format(argc - 1))
    for j in range(1, argc):
        print("{}: {}".format(j, str(sys.argv[j])))