#!/usr/bin/python3
"""module implements Rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class for Rectangle inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """initializes width and height of Rectangle"""
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
