#!/usr/bin/python3
"""This module have a class that defines a square """


class Square:
    """Definition of square attribute"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

    @property
    def size(self):
        """return current sqr size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets current sqr size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = value

    @property
    def position(self):
        """return current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set current position"""
        if(len(value) != 2 or type(value) is not int or position[0] < 0 or position[1] < 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """This return the current square area"""
        return self._Square__size ** 2

    def my_print(self):
        """this print the quare shape"""
        if self.__size == 0:
            print()
        else:
            for height in range(self.__size):
                print("#" * self.__size)
