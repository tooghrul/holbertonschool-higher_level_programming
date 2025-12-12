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
    def __init__(self, width, height):
        super().__init__
        try:
            Rectangle.integer_validator("width", width)
        except TypeError:
            raise TypeError("width must be an integer")
        except ValueError:
            raise ValueError("width must be greater than 0")
        else:
            self.__width = width

        try:
            Rectangle.integer_validator("height", height)
        except TypeError:
            raise TypeError("height must be an integer")
        except ValueError:
            raise ValueError("height must be greater than 0")
        else:
            self.__height = height      
