#!/usr/bin/python3
"""a function that writes an Object to a text file using a JSON repr."""


import json
import sys

def save_to_json_file(my_obj, filename):
    """This function writes <my_obj> to <filename>"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """This function reads an object from <filename>"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

filename = "add_item.json"

# Try to load existing list, start empty if file doesn't exist
try:
    info = load_from_json_file(filename)
except FileNotFoundError:
    info = []

info.extend(sys.argv[1:])
save_to_json_file(info, filename)
