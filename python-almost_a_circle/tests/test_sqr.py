from models.square import Square
import unittest

class TestSquare(unittest.TestCase):

    """ Testing id """
    def test_id(self):
        sqr = Square(1)
        self.assertEqual(sqr.id, 1)

    """ Testing size """
    def test_size(self):
        sqr = Square(1, 2)
        self.assertEqual(sqr.size, 1)

    """ Testing width """
    def test_width(self):
        sqr = Square(1, 2, 3)
        self.assertEqual(sqr.width, 1)

    """ Testing a str as argument """
    def test_str_1_arg(self):
        with self.assertRaises(TypeError):
            sqr = Square("1")

    def test_str_2_arg(self):
        with self.assertRaises(TypeError):
            sqr = Square(1, "2")

    def test_str_3_arg(self):
        with self.assertRaises(TypeError):
            sqr = Square(1, 2, "3")

    """ Testing Negative Arguments """
    def test_neg_arg_1(self):
        with self.assertRaises(ValueError):
            sqr = Square(-1)

    def test_neg_arg_2(self):
        with self.assertRaises(ValueError):
            sqr = Square(1, -2)

    def test_neg_arg_3(self):
        with self.assertRaises(ValueError):
            sqr = Square(1, 2, -3)

    """ Testing __str__ method """
    def test_str_method(self):
        sqr = Square(5)
        self.assertEqual(sqr.__str__(), "[Square] (9) 0/0 - 5")

    """ Testing to_dictionary method """
    def test_to_dic(self):
        sqr = Square(10, 2, 1, 6)
        result = {'id': 6, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(sqr.to_dictionary(), result)
