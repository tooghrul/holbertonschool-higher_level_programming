#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    i = 0
    cem = 0
    if len(roman_string) == 1:
        return roman[roman_string]
    while i <= len(roman_string) - 1:
        if roman[roman_string[i]] < roman[roman_string[i+1]]:
            cem += roman[roman_string[i]] - roman[roman_string[i+1]]
            i += 2
        else:
            cem += roman[roman_string[i]]
            i+=1
    return cem
