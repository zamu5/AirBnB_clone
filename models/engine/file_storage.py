#!/usr/bin/python3
"""FileStorage Module"""

from ..base_model import BaseModel
import json

class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        with open(self.__file_path, 'a') as f:
            dic = {}
            for key, value in self.__objects.items():
                dic.uptade({key: value.to_dict()})
            f.write(json.dumps(dic))

    def reload(self):
        try:
            with open(self.__file_path) as f:
                objs_json = json.loads(f.read())
                print(objs_json)
                #self.__objects["{}.{}".format(self.__objects['__class__'], self.__objects['id'])] = objs_json
        except IOError:
            pass
