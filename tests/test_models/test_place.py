#!/usr/bin/env python3


"""test the Place class"""


import unittest
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """testing the properties of Place class"""

    def setUp(self):
        self.Place = Place()
        self.base = BaseModel()

    def tearDown(self):
        del self.Place
        del self.base

    def test_Place(self):
        self.assertIsInstance(self.Place, BaseModel)
        self.assertTrue(hasattr(self.Place, "city_id"))
        self.assertTrue(hasattr(self.Place, "user_id"))
        self.assertTrue(hasattr(self.Place, "description"))
        self.assertTrue(hasattr(self.Place, "number_rooms"))
        self.assertTrue(hasattr(self.Place, "number_bathrooms"))
        self.assertTrue(hasattr(self.Place, "max_guest"))
        self.assertTrue(hasattr(self.Place, "price_by_night"))
        self.assertTrue(hasattr(self.Place, "latitude"))
        self.assertTrue(hasattr(self.Place, "latitude"))
        self.assertTrue(hasattr(self.Place, "longitude"))

    def test_attrs(self):
        self.assertTrue(isinstance(self.Place.city_id, str))
        self.assertTrue(isinstance(self.Place.user_id, str))
        self.assertTrue(isinstance(self.Place.description, str))
        self.assertTrue(isinstance(self.Place.number_rooms, int))
        self.assertTrue(isinstance(self.Place.number_bathrooms, int))
        self.assertTrue(isinstance(self.Place.max_guest, int))
        self.assertTrue(isinstance(self.Place.price_by_night, int))
        self.assertTrue(isinstance(self.Place.latitude, float))
        self.assertTrue(isinstance(self.Place.longitude, float))
        self.assertTrue(isinstance(self.Place.amenity_ids, list))


if __name__ == "__main__":
    unittest.main()
