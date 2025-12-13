#!/usr/bin/python3
"""This function reads and prints the text file"""

def read_file(filename=""):
    """Using with command to ensure it closes the file safely"""
    with open(filename, encoding="utf-8") as f:
        f.read()
