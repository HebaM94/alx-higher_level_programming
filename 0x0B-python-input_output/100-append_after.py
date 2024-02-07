#!/usr/bin/python3
"""Defines a function that applies append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file,
    after each line containing a specific string

    Args:
        filename (str): name of the file
        search_string (str): The string to search for within the file
        new_string (str): The string to be  inserted into the file
    """
    text = ""
    with open(filename) as readfile:
        for line in readfile:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as writefile:
        writefile.write(text)
