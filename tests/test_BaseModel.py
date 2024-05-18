#!/usr/bin/python
import unittest
from datetime import datetime
from models.base_model import BaseModel
"""
testing the BaseMode class
"""


class TestModel(unittest.TestCase):
    def setUp(self):
        self.to_base = BaseModel()
        self.my_dict = self.to_base.to_dict()
        self.my_dict["name"] = "Ziad"
        self.from_base = BaseModel(**self.my_dict)
        cestr = "2017-06-14T22:31:03.285259"
        self.base = BaseModel(**{"id": 34, "created_at": cestr})

    def test_certain_id(self):
        self.assertEqual(self.base.id, 34)

    def test_certain_created_at(self):
        cestr = "2017-06-14T22:31:03.285259"
        sestr = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(self.base.created_at, datetime.strptime(cestr, sestr))

    def test_normal_id(self):
        self.assertEqual(self.to_base.id, self.from_base.id)

    def test_normal_created_at(self):
        self.assertEqual(self.to_base.created_at, self.from_base.created_at)

    def test_dict_attrs(self):
        self.assertEqual(self.from_base.name, "Ziad")


if __name__ == '__main__':
    unittest.main()
