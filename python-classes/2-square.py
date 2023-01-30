#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an interger')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size
