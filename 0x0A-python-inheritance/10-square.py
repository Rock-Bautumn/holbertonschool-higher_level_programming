#!/usr/bin/python3
"""
This module contains a class named Square
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    This class defines a square
    """
    pass

    def __init__(self, size):
        """
        Initialize the square
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
        This method returns the area of the square
        """
        return self.__size ** 2
