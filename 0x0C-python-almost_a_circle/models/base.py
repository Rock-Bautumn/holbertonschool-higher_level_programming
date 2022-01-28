#!/usr/bin/python3
"""
This module has the class Base
"""


import json


class Base:
    """
    This class is a base for geometrical shapes
    """

    __nb_objects = 0


    def __init__(self, id=None):
        """
        Initialize the base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)


def validate_int(value, num):
    """
    validate that num is an integer, value is a string of what the num is, eg width
    """
    if type(value) is not str:
        raise TypeError("value passed to validate_int must be string")
    if type(num) is not int:
        raise TypeError(f"{value} must be an integer")
    if num <= 0:
        raise ValueError(f"{value} must be > 0")

def validate_not_neg(value, num):
    """
    validate that num is a 0 or positive integer,
    value is a string of what the num is, eg width
    """
    if type(value) is not str:
        raise TypeError("value passed to validate_not_neg must be string")
    if type(num) is not int:
        raise TypeError(f"{value} must be an integer")
    if num < 0:
        raise ValueError(f"{value} must be >= 0")
