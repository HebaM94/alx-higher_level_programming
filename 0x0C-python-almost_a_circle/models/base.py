#!/usr/bin/python3
"""Defines a Base class"""


class Base:
    """Represent a base of all other classes in this project

    Private Class Attributes:
        __nb_object (int): Number of instantiated  objectss (Base)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base

        Args:
            id (int): identity of the new Base, None as default
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
