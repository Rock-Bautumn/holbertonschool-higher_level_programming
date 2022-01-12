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

    """This returns the size of the square"""
    @property
    def size(self):
        return self.__size
    
    """This sets the size of the square"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
