from models.base import Base
import unittest

class TestBase(unittest.TestCase):
    """ Testing  initialization """
    def test_init(self):
        new_obj = Base()
        self.assertEqual(new_obj._Base__nb_objects, 1)
        self.assertEqual(new_obj.id, 1)
        new_obj_2 = Base()
        self.assertEqual(new_obj_2._Base__nb_objects, 2)
        self.assertEqual(new_obj_2.id, 2)
        new_obj_3 = Base(89)
        self.assertEqual(new_obj_3._Base__nb_objects, 2)
        self.assertEqual(new_obj_3.id, 89)

if __name__ == '__main__':
    unittest.main()
