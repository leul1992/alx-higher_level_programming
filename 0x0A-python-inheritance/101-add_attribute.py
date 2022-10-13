#!/usr/bin/python3
"""add new attribute to obj"""


def add_attribute(obj, key, value):
    try:
        setattr(obj, key, value)
    except Exception:
        raise TypeError("can't add new attribute")
