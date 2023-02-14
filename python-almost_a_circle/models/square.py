#!/usr/bin/python3
"""
This module have a class that defines
a Square, and it inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    it receive size, x, y and id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        When initialise she validates value and then
        proceed to assign them.
        """
        super().__init__(size, size, x, y, id)
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif type(x) is not int:
            raise TypeError('x must be an integer')
        elif type(y) is not int:
            raise TypeError('y must be an integer')
        elif size <= 0:
            raise ValueError('size must be > 0')
        elif x < 0:
            raise ValueError('x must be >= 0')
        elif y < 0:
            raise ValueError('y must be >= 0')
        else:
            self.size = size
            self.x = x
            self.y = y

    def __str__(self):
        """ Returns [Square] (id) x/y - size """
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.size}')
