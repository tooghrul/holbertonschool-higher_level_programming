#!/usr/bin/python3
def print_last_digit(number):
    if isalpha(number) == True:
        return
    digit = abs(number) % 10
    print(digit, end="")
    return digit

