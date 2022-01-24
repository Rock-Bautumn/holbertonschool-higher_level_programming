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

    def integer_validator(self, name, value):
        """
        This function raises exceptions if value is less than 1, or not
        an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
