#!/usr/bin/python3
"""module for FileStorage class"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """class to store and return obejects using JSON"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the __objects dictionary"""
        return self.__objects

    def new(self, obj):
        """creates dictionary of object to __objects"""
        if obj is not None:
            k = obj.__class__.__name__ + "." + obj.id
            self.__objects[k] = obj

    def reload(self):
        """retreive objects from a JSON file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                j_ob = json.load(file)
            for k in json_ob:
                self.__objects[k] = classes[j_ob[k]["__class__"]](**j_ob[k])
        except:
            pass

    def save(self):
        """save to JSON storage file"""
        new_dict = {}
        for key in FileStorage.__objects.keys():
            new_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, mode="w",
                  encoding="UTF-8") as to_file:
            (json.dump(new_dict, to_file))
