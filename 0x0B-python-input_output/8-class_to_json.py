#!/usr/bin/python3
"""
this module has a function that does class to json
"""


def class_to_json(obj):
    """
    this returns the __dict__ value of the object
    """
    return obj.__dict__
