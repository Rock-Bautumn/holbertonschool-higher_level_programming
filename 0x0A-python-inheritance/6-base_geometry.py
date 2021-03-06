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
        """
        This method always raises an exception that it is not implemented
        """
        raise Exception("area() is not implemented")
