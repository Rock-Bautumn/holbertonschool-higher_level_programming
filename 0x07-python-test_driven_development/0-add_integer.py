#!/usr/bin/python3
"""
This module has an add_integer function that adds two numbers
Examples:
    >>> add_integer(42)
    140
    >>> add_integer(0)
    98
"""


def add_integer(a, b=98):
    """Retuns the sum of two integers
    Examples:
    >>> add_integer(42)
    140
    >>> add_integer(0)
    98
    >>> add_integer(-1)
    97
    >>> add_integer(1)
    99
    >>> add_integer(17, .9999999999999999)
    17
    >>> add_integer(.99999999999999999, .99999999999999999)
    2
    """

    if a is None:
        raise TypeError("a must be an integer")
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
