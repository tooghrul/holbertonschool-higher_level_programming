#!/usr/bin/python3
def uppercase(str):
    newstr = ""
    for i in range(len(str)):
        if 97 <= ord(str(i)) <= 122:
            newstr += chr(ord(str[i]) - 32)
        else:
            newstr += str[i]
        print("{}".format(newstr))
