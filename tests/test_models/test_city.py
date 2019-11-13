#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models import storage
import os


class TestCityClass(unittest.TestCase):
    """class TestCityClass to test City class"""

    my_city = City()
    my_city.state_id = "123567890987654"
    my_city.name = "Felicidonia"

    def test_instance_city(self):
        self.assertTrue(isinstance(self.my_city, City))

    def test_inheritance_city(self):
        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(issubclass(type(self.my_city), BaseModel))

    def test_types_city(self):
        self.assertTrue(type(self.my_city.name) is str)
        self.assertTrue(type(self.my_city.state_id) is str)

    def test_des_serialization_city(self):
        city_dict = self.my_city.to_dict()
        self.assertTrue(type(city_dict) is dict)
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.my_city.save()
        self.assertTrue(os.path.exists("file.json"))
        city_obj = storage.all()
        for each_obj_key in city_obj:
            class_n = each_obj_key.split(".")
            if class_n[0] == "City":
                self.assertIsInstance(city_obj[each_obj_key], City)
        os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
