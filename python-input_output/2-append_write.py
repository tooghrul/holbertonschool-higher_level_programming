#!/usr/bin/python3
"""This function appends the text that is passed through the function"""


def append_write(filename="", text=""):
    """Using with command"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
