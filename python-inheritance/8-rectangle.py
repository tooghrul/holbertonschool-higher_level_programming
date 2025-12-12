#!/usr/bin/python3
"""This class is an empty class which is named BaseGeometry"""


class BaseGeometry:
    """A kinda empty class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This is a Rectangle class which inherits from BaseGeometry class"""
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
