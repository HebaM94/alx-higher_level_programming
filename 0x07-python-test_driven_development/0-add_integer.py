#!/usr/bin/python3
"""Defines integers addition function"""


def add_integer(a, b=98):
    """Add two integers a and b
    Float arguments are typecasted to ints before addition is performed

    Args:
        a (int or float): The first integer.
        b (int or float, optional): The second integer. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or not a float"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
