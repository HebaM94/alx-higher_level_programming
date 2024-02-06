#!/usr/bin/python3
"""Defines an empty BaseGeometry class"""


class BaseGeometry:
    """Represent Base Geometry"""

    def area(self):
        """Not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as an integer

        Args:
            name (str): The name of the parameter
            value (int): The parameter to be validated

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if not type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
