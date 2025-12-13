#!/usr/bin/python3
"""This class inherits from the list class"""


class MyList(list):
    """It will print the list in a ascending sorted way"""
    def print_sorted(self):
        print(sorted(self))
