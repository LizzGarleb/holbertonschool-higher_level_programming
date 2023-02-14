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
        elif width <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = width
        if type(height) is not int:
            raise TypeError('height must be an integer')
        elif height <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = height
        if type(x) is not int:
            raise TypeError('x must be an integer')
        elif x < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = x
        if type(y) is not int:
            raise TypeError('y must be an integer')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = y

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
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """
        Returns [Rectangle] (id) x/y - width-height
        """
        return (f'[Rectangle] ({self.id}) {self.__x}/{self.__y} - '
                f'{self.__width}/{self.__height}')

    def update(self, *args, **kwargs):
        """ Assigns an arguments to each attribute """
        if args is not None:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.__width = arg
                if count == 2:
                    self.__height = arg
                if count == 3:
                    self.__x = arg
                if count == 4:
                    self.__y = arg
                count += 1

        for key, elem in kwargs.items():
            if key == "id":
                self.id = elem
            if key == "width":
                self.__width = elem
            if key == "x":
                self.__x = elem
            if key == "y":
                self.__y = elem
            if key == "height":
                self.__height = elem

    def to_dictionary(self):
        """
        Return a dictionary representation
        of the class Rectangle
        """
        dic_rep = {
            'x': self.__x,
            'y': self.__y,
            'id': self.id,
            'height': self.__height,
            'width': self.__width
            }
        return dic_rep
