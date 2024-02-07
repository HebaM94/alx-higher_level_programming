#!/usr/bin/python3
"""Defines a funtion that applies JSON file-reading"""
import json


def load_from_json_file(filename):
    """Create an Object from a “JSON file

    Args:
        filename (str): file to be read from
    ”"""
    with open(filename) as f:
        return (json.load(f))
