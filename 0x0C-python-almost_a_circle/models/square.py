#!/usr/bin/python3
"""Defines Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square

        Args:
            size (int): size of the square
            x (int): x coordinate of the square, 0 as default
            y (int): y coordinate of the square, 0 as default
            id (int): identity of the square, None as default
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update attributes (x, y, width, height)

         Args:
            *args (list): New attribute values:
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
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
                    self.size = arg
                elif idint == 2:
                    self.x = arg
                elif idint == 3:
                    self.y = arg
                idint += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        pass
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return ({
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        })

    def __str__(self):
        """Return the print() and str() representation of the Square"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x, self.y,
                                                  self.width))
