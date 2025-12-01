#!/usr/bin/python3
import sys
argv = sys.argv[1:]

def main():
    if len(argv) == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv)) if len(argv) != 1 else "1 argument:")
        for i in range(len(argv)):
            print("{}: {}".format(i+1, argv[i]))
if __name__ == "__main__":
    main()
