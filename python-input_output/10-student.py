#!/usr/bin/python3
"""a class Student that defines a student by first_name, last_name and so on"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=[]):
        if attrs is []:
            return self.__dict__.copy()
        else:
            info = self.__dict__.copy()
            new_info = []
            for a in attrs:
                new_info.append(info[a])
            return new_info
