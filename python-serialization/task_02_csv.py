#!/usr/bin/python3

import csv
import json

def convert_csv_to_json(csv_file):
    context = csv.DictReader(csv_file)
    try:
        with open("data.json", "w") as f:
            json.dumps(context)
    except FileNotFoundError:
        return False
    else:
        return True
