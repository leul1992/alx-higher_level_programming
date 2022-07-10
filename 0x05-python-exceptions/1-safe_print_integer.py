#!/usr/bin/python3
def safe_print_integer(value):
    """print integer"""
    try:
        print("{:d}".format(value))
    except Exception as e:
        return False
    return True
