#!/usr/bin/python3
"""module finds the peak of a number"""


def find_peak(list_of_integers):
    """function finds the peak of the list
        list_of_integers(list):  the list of the numbers
    """
    if (not list_of_integers):
        return None
    else:
        length = len(list_of_integers)
        if (length == 1):
            return list_of_integers[0]
        elif length == 2:
            if list_of_integers[0] > list_of_integers[1]:
                return list_of_integers[0]
            else:
                return list_of_integers[1]
        mid = int(length / 2)
        if (list_of_integers[mid] > list_of_integers[mid + 1] and
                list_of_integers[mid] > list_of_integers[mid - 1]):
            return list_of_integers[mid]
        else:
            if(list_of_integers[mid] < list_of_integers[mid + 1]):
                return find_peak(list_of_integers[mid + 1:])
            else:
                return find_peak(list_of_integers[:mid])
