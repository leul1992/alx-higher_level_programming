#!/usr/bin/python3
"""
module that defines class square
"""


class Square:
    """class square"""
    def __init__(self, size=0):
        if (type(size) != int):
            raise ('size must be an integer')
        elif (size < 0):
            raise ('size must be >= 0')
        self.__size = size
    def area(self):
        """generates area of the size"""
        return self.__size**2

