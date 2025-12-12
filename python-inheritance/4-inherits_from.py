#!/usr/bin/python3
"""This func. checks if the object is the instance of the class"""


def inherits_from(obj, a_class):
    """It uses issubclass()"""
    return issubclass(type(obj), a_class) is True and type(obj) is not a_clas


if __name__ == "__main__":
    inherits_from()
