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

    def test_instance_user(self):
        """test instance"""
        self.assertEqual(isinstance(self.my_user, User), True)

    def test_inheritance_user(self):
        """test inherit from BaseModel"""
        self.assertEqual(issubclass(User, BaseModel), True)
        self.assertEqual(issubclass(type(self.my_user), BaseModel), True)

    def test_attr_user(self):
        """test attributes"""
        self.assertEqual(hasattr(self.my_user, 'first_name'), True)
        self.assertEqual(hasattr(self.my_user, 'last_name'), True)
        self.assertEqual(hasattr(self.my_user, 'email'), True)
        self.assertEqual(hasattr(self.my_user, 'password'), True)

    def test_types_user(self):
        """test attributes types"""
        self.assertEqual(type(self.my_user.email) is str, True)
        self.assertEqual(type(self.my_user.password) is str, True)
        self.assertEqual(type(self.my_user.first_name) is str, True)
        self.assertEqual(type(self.my_user.last_name) is str, True)
        self.assertIsInstance(self.my_user.created_at, datetime.datetime)
        self.assertIsInstance(self.my_user.updated_at, datetime.datetime)

    def test_des_serialization_user(self):
        """test seriarization and deserialization"""
        user_dict = self.my_user.to_dict()
        self.assertEqual(type(user_dict) is dict, True)

if __name__ == '__main__':
    unittest.main()
