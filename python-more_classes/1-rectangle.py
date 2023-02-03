#!/usr/bin/python3
"""
This module have a class
that defines a rectangle
"""


class Rectangle:
    """ Definition of rectangle attribute """

    def __init__(self, width=0, height=0):
        self._height = height
        self._width = width

    @property
    def width(self):
        """ Return the width of the rectangle """
        return self._width

    @width.setter
    def width(self, value):
        """ Sets the with of the rectangle """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self._width = value

    @property
    def height(self):
        """ Return the height of the rectangle """
        return self._height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self._height = value
