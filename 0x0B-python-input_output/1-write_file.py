#!/usr/bin/python3
"""Defines a function that write to file"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8)

    Args:
        filename (str): The name of the file to write to
        text (str): The text to be written to the file

    Return:
        The number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
