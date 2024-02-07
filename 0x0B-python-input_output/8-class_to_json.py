#!/usr/bin/python3
"""Defines a function that applies Python class-to-JSON"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: instance of a Class
    """
    return (obj.__dict__)
