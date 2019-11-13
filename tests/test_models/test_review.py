#!/usr/bin/python3
"""
Unittest module for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage
import os


class TestReviewClass(unittest.TestCase):
    """class TestReviewClass to test Review class"""

    my_review = Review()

    def test_instance_rev(self):
        self.assertIsInstance(self.my_review, Review)

    def test_inheritance_rev(self):
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertTrue(issubclass(type(self.my_review), BaseModel))

    def test_types_rev(self):
        self.assertTrue(type(self.my_review.place_id) is str)
        self.assertTrue(type(self.my_review.user_id) is str)
        self.assertTrue(type(self.my_review.text) is str)

    def test_des_serialization_rev(self):
        review_dict = self.my_review.to_dict()
        self.assertTrue(type(review_dict) is dict)

if __name__ == '__main__':
    unittest.main()
