#!/usr/bin/python3
def no_c(my_string):
    new = ''
    for st in my_string:
        if st != 'c' and st != 'C':
            new += st
    return new
