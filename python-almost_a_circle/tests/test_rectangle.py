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

    def test_x_negative(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(5, 5, -9)

    def test_x_zero(self):
        rectangle = Rectangle(3, 2, 0, 1)
        self.assertEqual(rectangle.x, 0)

    def test_x_str(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(5, 5, "1")

    """ Testing y conditions """
    def test_y(self):
        rectangle = Rectangle(2, 3, 2, 2)
        self.assertEqual(rectangle.y, 2)

    def test_y_negative(self):
        with self.assertRaises(ValueError):
            rec = Rectangle(10, 2, 3, -1)

    def test_y_zero(self):
        rectangle = Rectangle(3, 2, 1, 0)
        self.assertEqual(rectangle.y, 0)

    def test_y_str(self):
        with self.assertRaises(TypeError):
            rec = Rectangle(4, 6, 2, "2")

    """ Testing area """
    def test_area(self):
        rectangle = Rectangle(3, 3)
        self.assertEqual(rectangle.area(), 9)

    def test_area_2(self):
        rec = Rectangle(2, 10)
        self.assertEqual(rec.area(), 20)

    def test_area_3(self):
        rec = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(rec.area(), 56)

    """ Testing display """

    """ Testing __str__ """
    def test_str_method(self):
        rec = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rec.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    """ Testing update method """

    """  Testing to_dictionary method """

