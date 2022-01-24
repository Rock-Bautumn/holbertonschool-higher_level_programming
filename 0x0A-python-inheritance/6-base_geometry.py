#!/usr/bin/python3
"""
This module contains a class named BaseGeometry
"""


class BaseGeometry:
    """
    This class has a method named area that always raises an exception
    """
    pass

    def area(self):
        raise Exception("area() is not implemented")
