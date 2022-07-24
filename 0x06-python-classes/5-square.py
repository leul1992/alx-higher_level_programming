#!/usr/bin/python3
"""Module defines class square
prints in stdout
"""


class Square:
    """implementation of square class
    methods of __init__, area, my_print
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if (type(size) != int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate area"""
        return self.__size**2

    def my_print(self):
        """print in stdout"""
        if (self.__size == 0):
            print
        else:
            for i in range(self.__size):
                print('#' * self.__size)
