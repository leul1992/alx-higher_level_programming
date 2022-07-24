#!/usr/bin/python3
"""
module that defines class square

setter and getter implemented
"""


class Square:
    """class square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        retrieve the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError('size must be an integer')
        elif (value < 0):
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """generates area of the size"""
        return self.__size**2
