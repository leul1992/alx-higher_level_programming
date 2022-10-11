#!/usr/bin/python3
"""module checks if object is instance of or
if the object is an instance of a class that it inherited from
"""


def is_kind_of_class(obj, a_class):
    """obj: the object which is checked for being instance
       a_class: the class that is being checked on
    """
    return isinstance(obj, a_class)
