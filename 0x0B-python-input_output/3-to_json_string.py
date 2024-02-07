#!/usr/bin/python3
"""Defines a function that convert string to JSON"""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)

    Args:
        my_obj(str): object to be represented as JSON
    """
    return (json.dumps(my_obj))
