#!/usr/bin/python3
"""Defines a checker funtion for instance"""


def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class

    Args:
        obj (any): The object to be checked
        a_class (type): The class to be compared to the type of obj
    Returns:
        True: If obj is an instance or inherited instance of a_class
        Flase: Otherwise
    """
    return (isinstance(obj, a_class))
