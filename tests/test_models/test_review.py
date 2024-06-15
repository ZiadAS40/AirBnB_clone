#!/usr/bin/env python3


"""test the Review class"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """testing the properties of Review class"""

    def setUp(self):
        self.Review = Review()
        self.base = BaseModel()

    def tearDown(self):
        del self.Review
        del self.base

    def test_Review(self):
        self.assertIsInstance(self.Review, BaseModel)
        self.assertTrue(hasattr(self.Review, "place_id"))
        self.assertTrue(hasattr(self.Review, "user_id"))
        self.assertTrue(hasattr(self.Review, "text"))

    def test_attrs(self):
        self.assertTrue(isinstance(self.Review.place_id, str))
        self.assertTrue(isinstance(self.Review.user_id, str))
        self.assertTrue(isinstance(self.Review.text, str))


if __name__ == "__main__":
    unittest.main()
