#!/usr/bin/python3
"""Module that have The class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """This class is the base of the console objects"""

    def __init__(self, *args, **kwargs):
        """
        the constructor init have the attributes
        id, created_at, updated_at
        """
        if (kwargs):
            for key, value in kwargs.items():
                if key != '__class__':
                    if (key == 'created_at') or (key == 'updated_at'):
                        value = datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return a string with the output
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the current modificated date"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """class public method that returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        dictionary = {}
        obj_dict = self.__dict__
        dictionary['__class__'] = self.__class__.__name__
        for k in obj_dict:
            if k == "created_at" or k == "updated_at":
                dictionary[k] = obj_dict[k].isoformat()
            else:
                dictionary[k] = obj_dict[k]
        return dictionary
