#!/usr/bin/python3
import sys
argv = sys.argv[1:]

if len(argv) == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format(len(argv)))
    for i in range(len(argv)):
        print("{}: {}".format(i, argv[i]))
