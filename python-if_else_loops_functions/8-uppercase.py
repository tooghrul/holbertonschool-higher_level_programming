#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if 97 <= ord(str[i]) <= 122:
            str[i] = chr(ord(str[i]) - 32)
        if i == len(str) - 1:
            print("{}".format(str[i]))
        else:
            print("{}".format(str[i]), end="")
