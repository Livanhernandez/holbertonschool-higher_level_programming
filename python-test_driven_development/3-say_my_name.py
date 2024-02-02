#!/usr/bin/python3
"""
Functions that adds two integers.
a and b must be integers or floats, otherwise raise a TypeError exception 
a and b must be first casted to integers if they are float
"""
def matrix_divided(matrix, div):
    """
    Functions that adds two integers.
    a and b must be integers or floats, otherwise raise a TypeError exception 
    a and b must be first casted to integers if they are float
    """
    if not isinstance(matrix, list)and not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero") 
    new_matrix = []
    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if isinstance(element, (int, float)):
                new_row.append(round(element / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new_matrix.append(new_row)
    return new_matrix