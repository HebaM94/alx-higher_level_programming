#!/usr/bin/python3
"""Defines a function that appened to file"""


def append_write(filename="", text=""):
    """Append a string at the end of a text file (UTF8)

    Args:
        filename (str): The name of the file to append to
        text (str): The string to be appended to the file

    Return:
        The number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(text))
