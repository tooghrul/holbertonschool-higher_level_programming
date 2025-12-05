#!/usr/bin/python3
def best_score(a_dictionary):
    max_key, max_num = "", a_dictionary[list(a_dictionary.keys())[0]]
    for key, v in a_dictionary.items():
        if v > max:
            max_key = key
            max_num = v
    return max_key
