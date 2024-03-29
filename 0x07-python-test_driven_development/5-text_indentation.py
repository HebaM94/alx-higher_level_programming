#!/usr/bin/python3
"""Defines text-indentation function"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'

    Args:
        text (string): The text to print

    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in "\n.?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
