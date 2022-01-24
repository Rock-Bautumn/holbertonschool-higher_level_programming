#!/usr/bin/python3
"""
This module contains a class named Rectangle
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class defines a rectangle
    """
    pass

    def __init__(self, width, height):
        """
        Initialize the rectangle
        """
        self.integer_validator("height", height)
        self.integer_validator("width", width)

        self.__width = width
        self.__height = height

    def area(self):
        """
        This method returns the area of the rectangle
        """
        return self.__height * self.__width

    def __str__(self):
        """
        Returns info about the rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
