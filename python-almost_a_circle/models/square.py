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
