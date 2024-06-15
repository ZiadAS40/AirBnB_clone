#!/usr/bin/env python3


"""test the City class"""


import unittest
from models.base_model import BaseModel
from models.city import City


class Test_city(unittest.TestCase):
    """testing the properties of User class"""

    def setUp(self):
        self.user = City()
        self.base = BaseModel()

    def tearDown(self):
        del self.user
        del self.base

    def test_user(self):
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "name"))
        self.assertTrue(hasattr(self.user, "state_id"))

    def test_attrs(self):
        self.assertTrue(isinstance(self.user.name, str))
        self.assertTrue(isinstance(self.user.state_id, str))


if __name__ == "__main__":
    unittest.main()
