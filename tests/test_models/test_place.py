#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
import os


class TestPlaceClass(unittest.TestCase):
    """class TestPlaceClass to test Place class"""

    my_place = Place()

    def test_instance_place(self):
        self.assertIsInstance(self.my_place, Place)

    def test_inheritance_place(self):
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertTrue(issubclass(type(self.my_place), BaseModel))

    def test_types_place(self):
        self.assertTrue(type(self.my_place.name) is str)
        self.assertTrue(type(self.my_place.city_id) is str)
        self.assertTrue(type(self.my_place.user_id) is str)
        self.assertTrue(type(self.my_place.description) is str)
        self.assertTrue(type(self.my_place.number_rooms) is int)
        self.assertTrue(type(self.my_place.number_bathrooms) is int)
        self.assertTrue(type(self.my_place.max_guest) is int)
        self.assertTrue(type(self.my_place.price_by_night) is int)
        self.assertTrue(type(self.my_place.latitude) is float)
        self.assertTrue(type(self.my_place.longitude) is float)
        self.assertTrue(type(self.my_place.amenity_ids) is list)
        for items in self.my_place.amenity_ids:
            self.assertTrue(type(items) is str)

    def test_des_serialization_place(self):
        place_dict = self.my_place.to_dict()
        self.assertTrue(type(place_dict) is dict)

if __name__ == '__main__':
    unittest.main()
