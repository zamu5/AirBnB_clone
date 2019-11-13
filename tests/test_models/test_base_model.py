#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from uuid import uuid4
import json
import os


class TestBaseClass(unittest.TestCase):
    """class TestBaseClass to test BaseModel class"""

    model = BaseModel()
    model_2 = BaseModel()

    def test_instance_id(self):
        self.assertTrue(self.model.id != self.model_2.id)
        self.assertTrue(isinstance(self.model.id, str))
        self.assertTrue(isinstance(self.model_2.id, str))

    def test_datetime(self):
        self.assertTrue(isinstance(self.model.created_at, datetime))
        self.assertTrue(isinstance(self.model_2.created_at, datetime))

    def test_str(self):
        self.assertEqual(str(self.model), "[{}] ({}) {}".format(
            self.model.__class__.__name__, self.model.id, self.model.__dict__))
        self.assertEqual(str(self.model_2), "[{}] ({}) {}".format(
            self.model_2.__class__.__name__, self.model_2.id,
            self.model_2.__dict__))

    def test_todict(self):
        dictionary = self.model.to_dict()
        self.assertTrue(type(dictionary) is dict)
        self.assertIn('id', dictionary)
        self.assertIn('created_at', dictionary)
        self.assertIn('updated_at', dictionary)
        self.assertIn('__class__', dictionary)

    def test_obj_to_json(self):
        self.model_2.name = "Basename"
        self.model_2.number = 89
        dictionary_2 = self.model_2.to_dict()
        self.assertTrue(type(dictionary_2['id']) is str)
        self.assertTrue(type(dictionary_2['created_at']) is str)
        self.assertTrue(type(dictionary_2['updated_at']) is str)
        self.assertTrue(type(dictionary_2['__class__']) is str)
        self.assertTrue(type(dictionary_2['number']) is int)

    def test_save(self):
        prev_date = self.model.updated_at
        self.model.save()
        self.assertTrue(self.model.updated_at != prev_date)
        os.remove("file.json")

    def test_from_dictionary(self):
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        self.assertTrue(isinstance(my_model.created_at, datetime))
        my_model_json = my_model.to_dict()
        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertTrue(isinstance(my_new_model.created_at, datetime))
        self.assertFalse(my_model is my_new_model)

if __name__ == '__main__':
    unittest.main()
