#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key, max_num = None, -9999
    for key, v in a_dictionary.items():
        if v > max_num:
            max_key = key
            max_num = v
    return max_key
