#!/usr/bin/python3
import sys
argv = sys.argv[1:]


if __name__ == "__main__":
    sum = 0
    for i in argv:
        sum += int(i)
    print(sum)
