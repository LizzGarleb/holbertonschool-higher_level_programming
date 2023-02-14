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

    def __str__(self):
        """ Returns [Square] (id) x/y - size """
        return (f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}')

    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, size):
        self.width = size

    def update(self, *args, **kwargs):

        if args is not None:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1

        for key, elem in kwargs.items():
            if key == "id":
                self.id = elem
            if key == "size":
                self.width = elem
            if key == "x":
                self.x = elem
            if key == "y":
                self.y = elem
