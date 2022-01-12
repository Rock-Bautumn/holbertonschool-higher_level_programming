#!/usr/bin/python3
"""This file holds the Square class"""


class Square():
    """The Square is initialized below"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """This returns the area of the square"""
    def area(self):
        return self.__size**2
