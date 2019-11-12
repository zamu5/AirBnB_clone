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


class TestFileStorage(unittest.TestCase):
    """class TestFileStorage to test FileStorage class"""

    model_3 = BaseModel()
    model_4 = BaseModel()

    def test_all(self):
        all_objs = storage.all()
        self.assertTrue(type(all_objs) is dict)
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(isinstance(obj, BaseModel))

    def test_new(self):
        storage.new(self.model_3)
        all_objs = storage.all()
        self.assertTrue("{}.{}".format(self.model_3.__class__.__name__,
                                       self.model_3.id) in all_objs)
        self.assertTrue(isinstance(all_objs[
            "{}.{}".format(self.model_3.__class__.__name__, self.model_3.id)],
                                   BaseModel))

    def test_save(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.save()
        self.assertTrue(os.path.exists("file.json"))
        os.remove("file.json")

    def test_reload(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        storage.save()
        storage.reload()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(isinstance(obj, BaseModel))
        os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
