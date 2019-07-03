#!/usr/bin/python3
"""module for FileSorage class"""

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
            with open(self.__file_path, 'r') as file:
                json_object = json.load(file)
            for keys in json_obj:
                self.__objects[keys] = classes[json_object[key]["__class__"]]
                (**json_obj[key])
        except:
            pass

    def save(self):
        """save to JSON storage file"""
        json_obj = {}
        for keys in self.__objects:
            json_obj[keys] = self.__objects[keys].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)
