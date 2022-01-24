#!/usr/bin/python3
"""
This module has the MyList class
"""


class MyList(list):
    """
    This class inherits the list class and gives a printed sorted method
    """

    def __init__(self):
        """
        Initialize the MyList instance
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the sorted list
        """

        print(sorted(self))
