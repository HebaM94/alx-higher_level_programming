#!/usr/bin/python3

"""Define class Rectangle"""


class Rectangle:
    """Class that defines a rectangle

     Attributes:
        number_of_instances (int): The number of Rectangle instances
        print_symbol (any): symbol for string representation"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with width and height.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): The first Rectangle
            rect_2 (Rectangle): The second Rectangle
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Creates and returns a new Rectangle with width and height equal to 'size'

        Args:
        size (int): The side lengths of the rectangular"""
        return (cls(size, size))

    def __str__(self):
        """String representation  of a Rectangle object

        Print the rectangle with the character #"""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    print(self.print_symbol, end="")
                if i != self.__height - 1:
                    print("")
        return ("")

    def __repr__(self):
        """Representation string of a Rectangle object

        Return a string that can be used to recreate the object"""
        return (f'Rectangle({self.__width}, {self.__height})')

    def __del__(self):
        """Destructor of a Rectangle object"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")