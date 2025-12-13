#!/usr/bin/python3
"""a function that writes an Object to a text file using a JSON repr."""


import json

def save_to_json_file(my_obj, filename):
    with open(filename, "w") as f:
        obj = json.loads(my_obj)
        f.write(obj)
