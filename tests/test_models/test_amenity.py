#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
import os


class TestAmenityClass(unittest.TestCase):
    """class TestAmenityClass to test Amenity class"""

    my_amenity = Amenity()
    my_amenity.name = "BBQ"

    def test_instance_amenity(self):
        self.assertIsInstance(self.my_amenity, Amenity)

    def test_inheritance_amenity(self):
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(type(self.my_amenity), BaseModel))

    def test_types_amenity(self):
        self.assertTrue(type(self.my_amenity.name) is str)

    def test_des_serialization_amenity(self):
        amenity_dict = self.my_amenity.to_dict()
        self.assertTrue(type(amenity_dict) is dict)

if __name__ == '__main__':
    unittest.main()
