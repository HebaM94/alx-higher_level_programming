#!/usr/bin/python3

"""Define class Square."""


class Square:
    """Class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Set the value of the position."""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)
    
    def my_print(self):
        """Print the square with the character #."""
        for i in range(0, self.__position[1]):
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for n in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
