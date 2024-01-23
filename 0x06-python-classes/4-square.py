#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0):
        """Initialize a square with size.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the value of size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)
