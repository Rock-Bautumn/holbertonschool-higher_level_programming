#!/usr/bin/python3
"""
This function indents text
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    nl_array = [".", "?", ":"]
    for i in range(len(text)):
        if text[i] == " " and text[i - 1] in nl_array:
            pass
        else:
            print(text[i], end="")
        if text[i] in nl_array:
            print("\n", end="")
            print("\n", end="")
