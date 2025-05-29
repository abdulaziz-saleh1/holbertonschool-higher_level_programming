#!/usr/bin/python3
"""
This module defines the matrix_divided function that divides
all elements of a matrix by a divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and returns a new matrix.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The number to divide by.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                    or if rows are not of the same size,
                    or if div is not an integer or float.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists of float: The new matrix with divided elements.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_size = len(matrix[0])
    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")

    # Perform division and round to 2 decimal places
    return [[round(num / div, 2) for num in row] for row in matrix]
