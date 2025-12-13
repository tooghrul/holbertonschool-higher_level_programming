#!/usr/bin/python3
"""This function writes the text that is passed through the function"""


def write_file(filename="", text=""):
    """Using with command"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
