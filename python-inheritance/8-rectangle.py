#!/usr/bin/python3
"""
This module have a empty class named Geometry
"""


class Rectangle(BaseGeometry):
    """
    Rectangle is a child class from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Function that validates the weight & height
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
