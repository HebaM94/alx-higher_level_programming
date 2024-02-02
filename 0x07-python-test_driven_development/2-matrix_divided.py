#!/usr/bin/python3
"""Define a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide each element in the given matrix by the div.
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places

    Args:
        matrix (list[list]): A 2D list representing a matrix.
        div (int or float): The number to divide each element by.

    Return:
        new matrix of the result of the division

    Raises:
        TypeError: if matrix contains non integers/floats numbers
        TypeError: if matrix rows  have different sizes
        TypeError: if  div is not an integer or float
        ZeroDivisionError:  if div equal 0
        """

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(ele, (int, float))
        for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists)"
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
