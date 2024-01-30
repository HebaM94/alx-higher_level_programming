#!/usr/bin/python3

"""Define class Rectangle"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle with width and height.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the current rectangle area"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the current rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """String representation  of a Rectangle object

        Print the rectangle with the character #"""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                if i != self.__height - 1:
                    print("")
        return ("")

    def __repr__(self):
        """Representation string of a Rectangle object

        Return a string that can be used to recreate the object"""
        return ("Rectangle('" + self.__width + "', " + self.__height + ")")

    def __del__(self):
        """Destructor of a Rectangle object"""
        print("Bye rectangle...")
