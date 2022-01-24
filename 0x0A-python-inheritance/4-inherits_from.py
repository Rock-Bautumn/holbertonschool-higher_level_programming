#!/usr/bin/python3
"""
This module has a function that determines if an objects is only a subclass
of a class
"""


def inherits_from(obj, a_class):
    """
    Returns if object is only a subclass of a_class
    """
    if type(ob) is a_class:
        return False
    return issubclass(type(obj), a_class)
