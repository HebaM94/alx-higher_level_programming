#!/usr/bin/python3
"""Defines a checker function for inheritance """


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj (any): The object to be checked
        a_class (type): The class to be compared to the type of obj

    Return:
        True: If obj is an inherited instance of a_class
        False: Otherwise
"""
    if issubclass(type(obj), a_class) and (obj.__class__ != a_class):
        return (True)
    return (False)
