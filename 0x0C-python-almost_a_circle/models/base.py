#!/usr/bin/python3
"""
This module has the class Base
"""


class Base:
    """
    This class is a base for geometrical shapes
    """

    __nb_objects = 0


    def __init__(self, id=None):
        """
        Initialize the base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
