#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import os


class TestUserClass(unittest.TestCase):
    """class TestUserClass to test User class"""

    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Holberton"
    my_user.email = "airbnb@holbertonshool.com"
    my_user.password = "root"

    def test_instance(self):
        self.assertTrue(isinstance(self.my_user, User))

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(type(self.my_user), BaseModel))

    def test_types(self):
        self.assertTrue(type(self.my_user.email) is str)
        self.assertTrue(type(self.my_user.password) is str)
        self.assertTrue(type(self.my_user.first_name) is str)
        self.assertTrue(type(self.my_user.last_name) is str)

    def test_des_serialization(self):
        user_dict = self.my_user.to_dict()
        self.assertTrue(type(user_dict) is dict)
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.my_user.save()
        self.assertTrue(os.path.exists("file.json"))
        user_obj = storage.all()
        for each_obj_key in user_obj:
            self.assertIsInstance(user_obj[each_obj_key], User)
        os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
