#!/usr/bin/python3
"""
This module has a function to write to a file in append mode
"""


def append_write(filename="", text=""):
    """
    This function writes to a file in append mode
    """

    with open(filename, "a") as openfile:
        openfile.write(text)
    return len(text)
