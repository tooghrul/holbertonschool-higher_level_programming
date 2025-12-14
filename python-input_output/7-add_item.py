#!/usr/bin/python3
"""a function that writes an Object to a text file using a JSON repr."""


import json
import sys


def save_to_json_file(my_obj, filename):
    """This function writes <my_obj> to <filename>"""
    with open(filename, "w") as f:
        obj = json.dumps(my_obj)
        f.write(obj)


def load_from_json_file(filename):
    """This function writes <my_obj> to <filename>"""
    with open(filename, "r", encoding="utf-8") as f:
        obj = json.load(f)
        return obj

filename = "add_item.json"
info = load_from_json_file(filename)
info.extend(sys.argv[1:])
json_file = save_to_json_file(info, "add_item.json")
