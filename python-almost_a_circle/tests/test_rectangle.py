import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    """ Testing width conditions """

    def test_width(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.width, 2)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            rec3 = Rectangle(-4, 1)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(0, 5)

    def test_string_width(self):
        with self.assertRaises(TypeError):
            rec = Rectangle("2", 10)

    """ Testing height conditions """

    def test_height(self):
        rectangle = Rectangle(2, 4)
        self.assertEqual(rectangle.height, 4)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(5, -2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 0)

    def test_str_height(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(35, "15")

    """ Testing x conditions """
    def test_x(self):
        rectangle = Rectangle(10, 2, 3, 5)
        self.assertEqual(rectangle.x, 3)

    """ Testing area """

    def test_area(self):
        rectangle = Rectangle(3, 3)
        self.assertEqual(rectangle.area(), 9)
