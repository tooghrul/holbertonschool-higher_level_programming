#!/usr/bin/python3
def no_c(my_string="testCi"):
    new_str = "".join([i for i in my_string if i not in ('c', 'C')}])
    return new_str
