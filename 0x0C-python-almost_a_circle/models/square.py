#!/usr/bin/python3
"""
This file contains the square class, which inherits the rectangle class
"""
Rectangle = __import__("models.rectangle").rectangle.Rectangle
validate_int = __import__("models.base").base.validate_int


class Square(Rectangle):
    """
    This square class inherits rectangle because all squares are rectangles
    """

    def __init__(self, size, x=0, y=0, id=None):
        # validate_int("size", size)
        super().__init__(size, size, x, y, id)
