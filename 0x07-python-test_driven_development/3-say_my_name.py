#!/usr/bin/python3
"""module that prints full name"""


def say_my_name(first_name, last_name=""):
    """prints full name using first name and last name
    first_name(string): the first string, can not be left empty
    last_name(string): the second string, can be left empty
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {:s}".format(first_name + " " + last_name))
