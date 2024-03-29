#!/usr/bin/python3
"""Defines Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle, 0 as default
            y (int): y coordinate of the rectangle, 0 as default
            id (int): identity of the rectangle, None as default
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the x coordinate of the Rectangle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """get the y coordinate of the Rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the rectangle"""
        return(self.width * self.height)

    def display(self):
        """print rectangle using character #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            for w in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """update attributes (x, y, width, height)

         Args:
            *args (list): New attribute values:
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            idint = 0
            for arg in args:
                if idint == 0:
                    if arg is None:
                        pass
                    else:
                        self.id = arg
                elif idint == 1:
                    self.width = arg
                elif idint == 2:
                    self.height = arg
                elif idint == 3:
                    self.x = arg
                elif idint == 4:
                    self.y = arg
                idint += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        pass
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })

    def __str__(self):
        """Return the print() and str() representation of the Rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width,
                                                        self.height))
