#!/usr/bin/python3
"""a class Student that defines a student by first_name, last_name and so on"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the instance.
        If attrs is a list of strings, only include those attributes.
        """
        if attrs is None:
            return self.__dict__.copy()
        else:
            new_dict = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
