#!/usr/bin/env python3


"""the unittest for the base model"""


import unittest
from models.base_model import BaseModel
from datetime import datetime
import time

class TestBaseModel(unittest.TestCase):
    """test the base model"""
    def test_initialization(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
    
    def test_save(self):
        model = BaseModel()
        old_updated_at = model.updated_at
        time.sleep(1)
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == "__main__":
    unittest.main()
