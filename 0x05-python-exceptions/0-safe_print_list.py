#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print elements of a list"""

    var = 0

    for i in my_list[:x]:
        try:    
            print(i, end='')
            var += 1
        except Exception as e:
            break
    print('')
    return var
