#!/usr/bin/python3
"""module implements geometry class"""


class BaseGeometry:
    """class for geometry"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        name: assumed as string
        value: validated to be int or else
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
