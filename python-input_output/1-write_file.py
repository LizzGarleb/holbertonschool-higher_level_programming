#!/usr/bin/python3
"""
This module have a function named write_file
that writes in the filed given to us
"""


def write_file(filename="", text=""):
    """
    This function that write a
    string to a text file and
    return the number of character
    written
    """
    with open(filename, 'r+') as fd:
        fd.write(text)
        fd.close
        return len(text)