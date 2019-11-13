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

    def test_instance(self):
        self.assertTrue(isinstance(self.my_amenity, Amenity))

    def test_inheritance(self):
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(issubclass(type(self.my_amenity), BaseModel))

    def test_types(self):
        self.assertTrue(type(self.my_amenity.name) is str)

    def test_des_serialization(self):
        amenity_dict = self.my_amenity.to_dict()
        self.assertTrue(type(amenity_dict) is dict)
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.my_amenity.save()
        self.assertTrue(os.path.exists("file.json"))
        amenity_obj = storage.all()
        for each_obj_key in amenity_obj:
            self.assertIsInstance(amenity_obj[each_obj_key], Amenity)
        os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
