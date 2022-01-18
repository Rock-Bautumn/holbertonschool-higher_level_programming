#!/usr/bin/python3
"""
This function indents text
"""


def text_indentation(text):
    """
    This function puts in new lines when it sees certain characters
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    nl_array = [".", "?", ":"]
    no_space = 1
    for i in range(len(text)):
        if text[i] == " " and no_space == 1:
            pass
        else:
            print(text[i], end="")
            no_space = 0
        if text[i] in nl_array:
            print("\n", end="")
            print("\n", end="")
            no_space = 1
