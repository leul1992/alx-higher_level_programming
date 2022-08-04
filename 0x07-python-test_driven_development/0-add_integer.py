#!/usr/bin/env python3
"""
defines `add_integer`

the function returns the sum of a and b
"""
def add_integer(a, b=98):
    """adds a and b
    Args:
        a (int): term 1
        b (int, optional): term 2. Defaults to 98.
    Raises:
        TypeError: a and b must be integer
    Returns: sum of a and b
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return a + b
