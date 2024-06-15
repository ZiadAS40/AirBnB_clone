#!/usr/bin/env python3


"""test the User class"""


import unittest
from models.base_model import BaseModel
from models.user import User


class Test_user(unittest.TestCase):
    """testing the properties of User class"""

    def setUp(self):
        self.user = User()
        self.base = BaseModel()

    def tearDown(self):
        del self.user
        del self.base

    def test_user(self):
        self.assertIsInstance(self.user, BaseModel)
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
    
    def test_attrs(self):
        self.assertTrue(isinstance(self.user.email, str))
        self.assertTrue(isinstance(self.user.first_name, str))
        self.assertTrue(isinstance(self.user.last_name, str))
        self.assertTrue(isinstance(self.user.password, str))


if __name__ == "__main__":
    unittest.main()
