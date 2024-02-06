#!/usr/bin/python3
"""Defines class MyList that inherits from list"""


class MyList(list):
    """Class that implement sorted print for list class"""

    def print_sorted(self):
        """Print a list in sorted ascendingly"""
        print(sorted(self))
