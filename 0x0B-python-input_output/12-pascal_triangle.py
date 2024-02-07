#!/usr/bin/python3
"""Defines a function that applies Pascal's Triangle"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n

    Args:
        n (int): The number of rows in the triangle

    Return:
        list of lists of integers representing the Pascal’s
        triangle of n
    """
    if n <= 0:
        return ([])
    triangle = [[1]]
    while len(triangle) != n:
        last = triangle[-1]
        row = [1]
        for i in range(len(last) - 1):
            row.append(last[i] + last[i + 1])
        row.append(1)
        triangle.append(row)
    return (triangle)
