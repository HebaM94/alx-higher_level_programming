#!/usr/bin/python3
"""Defines a lookup function for object's attribute"""


def lookup(obj):
    """Return a list of an object's available
    attributes and methods
    
    Args:
        obj (any): object to be checked"""
    return (dir(obj))
