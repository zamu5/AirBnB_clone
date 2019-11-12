#!/usr/bin/python3
"""Module that have the class Review"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class have the data:
    name
    """
    place_id = ""
    user_id = ""
    text = ""
