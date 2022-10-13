#!/usr/bin/python3
"""module for myInt class"""


class MyInt(int):
    """class inherting from int"""
    def __eq__(self, num):
        return super().__ne__(num)

    def __ne__(self, num):
        return super().__eq__(num)
