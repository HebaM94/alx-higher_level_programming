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

    def __eq__(self, other):
        """Define == comparision to Square"""
        return (self.area() == other.area())

    def __ne__(self, other):
        """Define != comparison to Square"""
        return (self.area() != other.area())

    def __gt__(self, other):
        """Define > comparison to Square"""
        return (self.area() > other.area())

    def __ge__(self, other):
        """Define >= compmarison to Square"""
        return (self.area() >= other.area())

    def __lt__(self, other):
        """Define < comparison to Square"""
        return (self.area() < other.area())

    def __le__(self, other):
        """Define <= comparison to Square"""
        return (self.area() <= other.area())
