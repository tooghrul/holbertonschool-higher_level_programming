#!/usr/bin/python3
"""This func. checks if the object is the instance of the class"""


def is_same_class(obj, a_class):
    """It uses type()"""
    return isinstance(obj, a_class) is True


if __name__ == "__main__":
    is_same_class()
