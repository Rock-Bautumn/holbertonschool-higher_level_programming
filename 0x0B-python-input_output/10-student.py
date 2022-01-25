#!/usr/bin/python3
"""
This module contains a class named Student
"""


class Student:
    """
    This class contains the first name, last name, and age of a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        this returns the dict of the object
        """
        if attrs is None or type(attrs) is not list:
                return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
