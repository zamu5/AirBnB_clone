#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models import storage
import os


class TestStateClass(unittest.TestCase):
    """class TestStateClass to test State class"""

    my_state = State()
    my_state.name = "Felicidonia"

    def test_instance(self):
        self.assertTrue(isinstance(self.my_state, State))

    def test_inheritance(self):
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(issubclass(type(self.my_state), BaseModel))

    def test_types(self):
        self.assertTrue(type(self.my_state.name) is str)

    def test_des_serialization(self):
        state_dict = self.my_state.to_dict()
        self.assertTrue(type(state_dict) is dict)
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.my_state.save()
        self.assertTrue(os.path.exists("file.json"))
        state_obj = storage.all()
        for each_obj_key in state_obj:
            self.assertIsInstance(state_obj[each_obj_key], State)
        os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
