#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list.replace(search, replace)
    return my_list
print (search_replace([1,2,3,4,5,6,6,7,7,7,7,7], 7, 13))
