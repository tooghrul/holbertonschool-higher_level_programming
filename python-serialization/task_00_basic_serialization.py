#!/usr/bin/python3
import json

def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w", encoding="utf-8") as fn:
        json.dump(data, fn, indent=4)

def load_and_deserialize(filename):
    with open(filename, mode="r", encoding="utf-8") as fn:
        return json.loads(filename)
