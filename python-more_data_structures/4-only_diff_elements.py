#!/usr/bin/python3
def common_elements(set_1, set_2):
    butun_setler = list(set_1) + list(set_2)
    return {i for i in butun_setler if butun_setler.count(i) == 1}
