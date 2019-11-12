#!/usr/bin/python3
"""FileStorage Module"""

from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review
import json


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    com_list = {"BaseModel" : BaseModel, "User" : User, "Place": Place,
                "State": State, "City": City, "Amenity": Amenity,
                "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        objs_dict = {}
        for obj_elem in self.__objects:
            objs_dict[obj_elem] = self.__objects[obj_elem].to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(objs_dict))

    def reload(self):
        try:
            with open(self.__file_path) as f:
                o_json = json.loads(f.read())
                for obj_elem in o_json:
                    obj_class = obj_elem.split(".")
                    self.__objects[obj_elem] = FileStorage.com_list[obj_class[0]](**(o_json[obj_elem]))
        except IOError:
            pass
