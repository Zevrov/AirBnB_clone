#!/usr/bin/python3
"""module for FileSorage class"""

import os.path
import json


class FileStorage:
	"""class to store and return obejects using JSON"""

        __file_path = "storage.json"
        __objects = {}

        def all(self):
            """return the __objects dictionary"""

            return type(self).__objects

        def new(self, obj):
            """creates dictionary of object to __objects"""

            value = obj.to_dict()
            key = '{}.{}'.format(obj.__class__.name__, obj.id)
            type(self).__objects[key] = value

        def reload(self):
            """retreive objects from a JSON file"""

            if not os.path.isfile(FileStorage.__file_path):
                return
            with open(FileStorage.__file_path, 'rt') as file:
                FileStorage.__objects = json.load(file)

        def save(self):
            """save to JSON storage file"""

            with open(FileStorage.__file_path, 'wt') as file:
                json.dump(FileStorage.__objects, file)
