#!/usr/bin/python3
"""
This module contains a class named BaseGeometry
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
