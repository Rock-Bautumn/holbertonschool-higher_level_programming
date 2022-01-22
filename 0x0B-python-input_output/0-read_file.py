#!/usr/bin/python3
"""
This module contains a function to read a file
"""


def read_file(filename=""):
    """
    This reads a file line by line
    """

    with open(filename) as thefile:
        for line in thefile:
            print(line, end="")
