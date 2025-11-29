#!/usr/bin/python3
for i in range(97, 123):
    x = "{}".format(chr(i))     
    if x == "q" or x == "e":
        pass
    else:
        print(x, end = "")
