#!/usr/bin/python3
"""
This module have a class that defines
a rectangle, and it inherit from Base
"""


from models.base import Base


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
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif type(x) is not int:
            raise TypeError('x must be an integer')
        elif type(y) is not int:
            raise TypeError('y must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        elif width <= 0:
            raise ValueError('width must be > 0')
        elif x < 0:
            raise ValueError('x must be >= 0')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
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
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height

    @property
    def width(self):
        """ Return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets the width of the rectangle """
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width

    @property
    def x(self):
        """ Return the x of the rectangle """
        return self.__x

    @x.setter
    def x(self, x):

        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x

    @property
    def y(self):
        """ Return the y of the rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        """ Sets the y of the rectangle """
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

    def area(self):
        """
        Public Method that return the area value
        of Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """
        Public method that prints in stdout the
        Rectangle instance with the character #
        """
        if self.__height == 0 or self.__width == 0:
            print(" ")
        rec_print = ""
        for i in range(self.__height):
            rec_print += "#" * self.__width
            if i != self.__height - 1:
                rec_print += "\n"
        print(rec_print)

    def __str__(self):
        """
        Returns [Rectangle] (id) x/y - width-height
        """
        return '[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}-{self.height}'.format(self=self)
