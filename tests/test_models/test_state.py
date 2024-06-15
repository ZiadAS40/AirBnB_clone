#!/usr/bin/env python3


"""test the State class"""


import unittest
from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    """testing the properties of State class"""

    def setUp(self):
        self.State = State()
        self.base = BaseModel()

    def tearDown(self):
        del self.State
        del self.base

    def test_State(self):
        self.assertIsInstance(self.State, BaseModel)
        self.assertTrue(hasattr(self.State, "name"))

    def test_attrs(self):
        self.assertTrue(isinstance(self.State.name, str))


if __name__ == "__main__":
    unittest.main()
