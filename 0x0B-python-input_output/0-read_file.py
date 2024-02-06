#!/usr/bin/python3
"""Defines a function that reads text file"""


def read_file(filename=""):
    """read a text file (UTF8) and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
