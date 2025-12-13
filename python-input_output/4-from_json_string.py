#!/usr/bin/python3
"""From JSON to python object"""


import json


def from_json_string(my_obj):
    "json.load for the goal"
    return json.loads(my_obj)
