#!/usr/bin/python3
"""Defines a function that checks the object's class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class

    Args:
        obj (any): The object to be checked
        a_class (type): The class compared to the type of obj
    Return:
        True: If obj is exactly an instance of a_class
        False: Otherwise
    """
    return obj.__class__ == a_class
