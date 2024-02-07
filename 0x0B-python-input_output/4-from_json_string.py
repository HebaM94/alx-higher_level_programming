#!/usr/bin/python3
"""Defines a function that applies JSON-to-object"""
import json


def from_json_string(my_str):
    """Return an object (Python data structure)
    represented by a JSON string

    Args:
        my_str(JSON str): JSON string to be returned as object
    """
    return (json.loads(my_str))
