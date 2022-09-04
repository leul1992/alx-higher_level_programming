#!/usr/bin/python3
def matrix_divided(matrix, div):
    i = 0
    fres = []

    if type(div) not in (int, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    for row in matrix:
        res = []
        for col in range(len(row)):
            if i == 0:
                check = len(row)
            if len(row) != check:
                raise TypeError('Each row of the matrix must have the same size')
            if type(row[col]) not in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

            res.append(round(row[col] / div, 2))
            i += 1
        fres.append(res)
    return fres
