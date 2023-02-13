#!/usr/bin/python3
"""
This module contains the clase Base.
The goal of it is to manage id attribute
in all your future classes and to avoid
duplicating the same code
"""


class Base:
    """ This class will be the base of all other
    classes in this projects. """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        This funciton initializa the
        class by receiving the id argument
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
