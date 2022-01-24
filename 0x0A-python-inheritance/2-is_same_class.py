#!/usr/bin/python3
"""
This module has a function to determine if the object is a member of a class
"""


def is_same_class(obj, a_class):
    """
    This returns true if obj is a member of a_class, false if not"""
    if type(obj) is a_class:
        return True
    return False
