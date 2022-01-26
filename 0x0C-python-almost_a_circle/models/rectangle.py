#!/usr/bin/python3
"""
This module has a class Rectangle that inherits Base
"""


def Rectangle(Base):
    """
    This class inherits Base, it is for rectangles
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the rectangle
        """
        self.__width = width
        self.__height = height
        __x = x
        __y = y
        super(Base).__init__(id)
    
    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle
        """
        self.__width = width
    
    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        self.__height = height
