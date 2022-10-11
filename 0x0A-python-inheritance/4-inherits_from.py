#!/usr/bin/python3
"""module checks object is an instance of a class inherited"""


def inherits_from(obj, a_class):
    """obj: the object to check
       a_class: the class to check on
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
