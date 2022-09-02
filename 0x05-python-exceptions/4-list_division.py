#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for index in range(list_length):
        try:
            div = my_list_1[index] / my_list_2[index]
        except TypeError:
            div = 0
            print('wrong type')
        except ZeroDivisionError:
            div = 0
            print('division by 0')
        except IndexError:
            div = 0
            print('out of range')
        finally:
            res.append(div)
    return res
