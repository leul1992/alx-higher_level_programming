#!/usr/bin/python3
"""add new attribute to obj"""


def add_attribute(obj, key, value):
    """adds a new attribute to an object if it's possible"""
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
