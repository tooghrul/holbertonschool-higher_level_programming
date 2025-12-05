#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    values = list(map(lambda x: x*2, a_dictionary.values()))
    for key, i in zip(a_dictionary.keys(), list(range(len(values)))):
        new_dict[key] = values[i]
    return new_dict
