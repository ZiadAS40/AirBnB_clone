#!/usr/bin/env python3


"""test the Amenity class"""


import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """testing the properties of Amenity class"""

    def setUp(self):
        self.Amenity = Amenity()
        self.base = BaseModel()

    def tearDown(self):
        del self.Amenity
        del self.base

    def test_Amenity(self):
        self.assertIsInstance(self.Amenity, BaseModel)
        self.assertTrue(hasattr(self.Amenity, "name"))

    def test_attrs(self):
        self.assertTrue(isinstance(self.Amenity.name, str))


if __name__ == "__main__":
    unittest.main()
