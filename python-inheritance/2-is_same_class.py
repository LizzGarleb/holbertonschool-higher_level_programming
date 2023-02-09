#!/usr/bin/python3
"""
This module contains a function that
check is the object passed is a instance
of the specified class
"""


def is_same_class(obj, a_class):
    """
    Function that returns True if the object
    is exactly an instance of the specifies class;
    otherwise False
    """
    if isinstance(obj, a_class) == True:
        return True
    else:
        return False
