#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        div = a/b
    except (TypeError, ValueError, ZeroDivisionError):
        div = None
        return None
    finally:
        print("Inside result: {}".format(div))
    return div
