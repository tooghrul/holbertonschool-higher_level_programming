#!/usr/bin/python3
"""This function writes the text that is passed through the function"""


def write_file(filename="", text=""):
    """Using with command"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
