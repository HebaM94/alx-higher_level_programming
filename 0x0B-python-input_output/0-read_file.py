#!/usr/bin/python3
"""Defines a function that reads text file"""


def read_file(filename=""):
    """Read a text file (UTF8) and print it to stdout
    
    Args:
        filename (str): file name to be read, by default no file specified
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
