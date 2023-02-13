#!/usr/bin/python3
from models.base import Base
"""
This module have a class that defines
a rectangle, and it inherit from Base
"""

class Rectangle(Base):
    """
    Class Rectangle that inherit from base
    it receive width, height, x, y and id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        When initialize she assign the values to it
        representations
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """ Return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        """ Sets the height of the rectangle """
        self.__height = height

    @property
    def width(self):
        """ Return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the width of the rectangle """
        self.__width = width

