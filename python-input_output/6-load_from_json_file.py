#!/usr/bin/python3
"""a function that writes an Object to a text file using a JSON repr."""


import json


def load_from_json_file(filename):
    """This function writes <my_obj> to <filename>"""
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj
