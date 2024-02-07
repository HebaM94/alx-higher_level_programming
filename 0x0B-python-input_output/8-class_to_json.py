#!/usr/bin/python3
"""Defines a function that applies Python class-to-JSON"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    
    Args:
        obj: instance of a Class
    """
    dict_descrption = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            dict_descrption[attr_name] = attr_value
    return (dict_descrption)
