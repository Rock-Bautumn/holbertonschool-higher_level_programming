#!/usr/bin/python3
"""
This module has a class Rectangle that inherits Base
"""

Base = __import__("models.base").base.Base
validate_int = __import__("models.base").base.validate_int
validate_not_neg = __import__("models.base").base.validate_not_neg


class Rectangle(Base):
    """
    This class inherits Base, it is for rectangles
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize the rectangle
        """
        super().__init__(id)
        validate_int("width", width)
        validate_int("height", height)
        self.__width = width
        self.__height = height
        validate_not_neg("x", x)
        validate_not_neg("y", y)
        self.__x = x
        self.__y = y

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
        validate_int("width", width)
        self.__width = width
    
    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle
        """
        validate_int("height", height)
        self.__height = height

    @property
    def x(self):
        """
        Gets the value of x
        """
        return self.__x
    
    @x.setter
    def x(self, num):
        """
        This sets the value of x
        """
        validate_not_neg("x", num)
        self.__x = num

    @property
    def y(self):
        """
        Gets the value of y
        """
        return self.__x
    
    @y.setter
    def y(self, num):
        """
        Sets the value of y
        """
        validate_not_neg("y", num)
