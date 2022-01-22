#!/usr/bin/python3
"""
This module has a function to write to a file
"""


def write_file(filename="", text=""):
    """
    writes "text" to a file in overwrite mode, returns characters written
    """

    with open(filename, "w") as openfile:
        openfile.write(text)
    return len(text)
