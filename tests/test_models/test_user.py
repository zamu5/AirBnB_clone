#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage
import os
import datetime


class TestUserClass(unittest.TestCase):
    """class TestUserClass to test User class"""

    my_user = User()
    my_user.first_name = "Betty"
    my_user.last_name = "Holberton"
    my_user.email = "airbnb@holbertonshool.com"
    my_user.password = "root"

    def test_instance(self):
        """test instance"""
        self.assertTrue(isinstance(self.my_user, User))

    def test_inheritance(self):
        """test inherit from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(issubclass(type(self.my_user), BaseModel))

    def test_attr(self):
        """test attributes"""
        self.assertTrue(hasattr(self.my_user, 'first_name'))
        self.assertTrue(hasattr(self.my_user, 'last_name'))
        self.assertTrue(hasattr(self.my_user, 'email'))
        self.assertTrue(hasattr(self.my_user, 'password'))

    def test_types(self):
        """test attributes types"""
        self.assertTrue(type(self.my_user.email) is str)
        self.assertTrue(type(self.my_user.password) is str)
        self.assertTrue(type(self.my_user.first_name) is str)
        self.assertTrue(type(self.my_user.last_name) is str)
        self.assertIsInstance(self.my_user.created_at, datetime.datetime)
        self.assertIsInstance(self.my_user.updated_at, datetime.datetime)

    def test_des_serialization(self):
        """test seriarization and deserialization"""
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
