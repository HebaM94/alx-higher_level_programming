#!/usr/bin/python3
"""Defines a function that applies JSON file-writing"""
import json


def save_to_json_file(my_obj, filename):
    """Write an Object to a text file, using a JSON representation

    Args:
        my_obj (str): string to be written to the file using JSON
        filename (str): file name to write to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
