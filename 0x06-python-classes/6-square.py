#!/usr/bin/python3
"""Module defines class square
prints in stdout
"""


class Square:
    """implementation of square class
    methods of __init__, area, my_print
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """setter and getter for size"""
        return self.__size

    @size.setter
    def size(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """setter and getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or \
            len(value) != 2 or \
            not all(isinstance(el, int) for el in value) or \
                not all(el >= 0 for el in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        """calculate area"""
        return self.__size**2

    def my_print(self):
        """print in stdout with given size"""
        if self.__size == 0:
            print('')
        else:
            for i in range(self.position[1]):
                print('')
            for i in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
