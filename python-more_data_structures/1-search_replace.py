#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_matrix = [i for i in my_list if i != search else i=replace]
    return new_matrix
