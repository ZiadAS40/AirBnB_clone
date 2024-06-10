#!/usr/bin/env python3


"""the unittest for the base model"""

import unittest
from models.base_model import BaseModel


class Test_base_module(unittest.TestCase):

    def setUp(self):
        self.base = BaseModel()

    def tear_down(self):
        del self.base

    def test_init(self):
        self.assertIsInstance(self.base, BaseModel)
        self.assertTrue(hasattr(self.base, 'id'))
        self.assertTrue(hasattr(self.base, 'created_at'))
        self.assertTrue(hasattr(self.base, 'updated_at'))

    def test_str(self):
        str_rpr = str(self.base)
        self.assertIn("[BaseModel]", str_rpr)
        self.assertIn("id", str_rpr)
        self.assertIn("created_at", str_rpr)
        self.assertIn("updated_at", str_rpr)

    def test_save(self):
        update = self.base.updated_at
        self.base.save()
        self.assertNotEqual(update, self.base.updated_at)

    def test_todict(self):
        Mydict = self.base.to_dict()
        self.assertIsInstance(Mydict, dict)
        self.assertEqual(Mydict['__class__'], 'BaseModel')
        self.assertIn('id', Mydict)
        self.assertIn('created_at', Mydict)
        self.assertIn('updated_at', Mydict)


if __name__ == '__main__':
    unittest.main()
