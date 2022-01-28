#!/usr/bin/python3
"""
This file contains the square class, which inherits the rectangle class
"""
from ctypes import sizeof


Rectangle = __import__("models.rectangle").rectangle.Rectangle
validate_int = __import__("models.base").base.validate_int


class Square(Rectangle):
    """
    This square class inherits rectangle because all squares are rectangles
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize the square
        """
        # validate_int("size", size)
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns the value of the size (width)
        """
        return self.width
    
    @size.setter
    def size(self, num):
        """
        Sets the size of the square, affecting width and height
        """
        super().__init__(num, num)

    def __str__(self):
        """
        Makes a pretty string of our square object
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, super().x, super().y, self.width)
