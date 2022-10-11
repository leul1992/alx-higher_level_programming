#!/usr/bin/python3
"""module prints list"""


class MyList(list):
    """class with method print_sorted"""
    def print_sorted(self):
        print(sorted(self))
