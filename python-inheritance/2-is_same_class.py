#!/usr/bin/python3
"""This func. checks if the object is the instance of the specified class"""


def is_same_class(obj, a_class):
    """It uses type()"""
    return type(obj) is a_class


if __name__ == "__main__":
    is_same_class()
