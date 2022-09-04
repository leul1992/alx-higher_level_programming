#!/usr/bin/python3
"""module to divide matrix by a given integer"""


def matrix_divided(matrix, div):
    """matrix is divided by div
    matrix(pointer): points to list of 2-dimensional array
    div(int or float): divides the matrix elements
    returns(pointer): the newly created list
    """
    i = 0
    fres = []

    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
    if type(div) not in (int, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        res = []
        for col in range(len(row)):
            if i == 0:
                check = len(row)
            if type(row) is not list:
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')
            if len(row) != check:
                raise TypeError('Each row of the matrix \
must have the same size')
            if type(row[col]) not in (int, float):
                raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

            res.append(round(row[col] / div, 2))
            i += 1
        fres.append(res)
    return fres
