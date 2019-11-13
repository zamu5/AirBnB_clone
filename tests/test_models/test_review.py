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
    my_review.place_id = "123456765432"
    my_review.user_id = "124567543456"
    my_review.text = "Very Cool Place"

    def test_instance_rev(self):
        self.assertTrue(isinstance(self.my_review, Review))

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
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.my_review.save()
        self.assertTrue(os.path.exists("file.json"))
        review_obj = storage.all()
        for each_obj_key in review_obj:
            class_n = each_obj_key.split(".")
            if class_n[0] == "Review":
                self.assertIsInstance(review_obj[each_obj_key], Review)
        os.remove("file.json")

if __name__ == '__main__':
    unittest.main()
