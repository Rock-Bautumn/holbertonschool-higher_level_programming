#!/usr/bin/python3
"""
This function returns a list of available attributes and methods available
"""


def lookup(obj):
    """
    Returns the methods and availables available with the object
    """
    return dir(obj)
