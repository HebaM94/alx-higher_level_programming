#!/usr/bin/python3
"""Defines a MyInt class that inherits from int"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """Override == opeartor with !="""
        return (super().__ne__(value))

    def __ne__(self, value):
        """Override != operator with =="""
        return (super().__eq__(value))
