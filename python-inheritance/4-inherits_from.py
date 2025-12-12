#!/usr/bin/python3
"""This func. checks if the object is the instance of the class"""


def inherits_from(obj, a_class):
    """It uses issubclass()"""
    return issubclass(obj, a_class) is True


if __name__ == "__main__":
    inherits_from()
