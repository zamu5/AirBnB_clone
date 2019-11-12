#!/usr/bin/python3
"""Module that have the clas users"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User class have the data:
    email, password, first_name, last_name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
