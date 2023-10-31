#!/usr/bin/python3
"""
This module contains a funtion that adds two integers
Its test is in the test directory
"""


def matrix_divided(matrix, div):
    """
    This funtion divides all elements of a matrix
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) and all(
            isinstance(num, (int, float)) for num in row)
            for row in matrix):
        raise TypeError("matrix must be a matrix"
              "(list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return result_matrix
