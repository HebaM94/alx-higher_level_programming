#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name (str): first name of the student
            last_name (str): last name of the student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of the Student

        Args:
            attrs (list): The attributes to be represented, by default it's None
            Note: If attrs is a list of strings, only attribute names contained in this
            list must be retrieved
        """
        if attrs == None:
            return (self.__dict__)
        return ({a: getattr(self, a) for a in attrs if hasattr(self, a)})
