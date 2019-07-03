#!/usr/bin/python3
"""Base Model"""

import json
import models
import uuid
from datetime import datetime

cronos = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
        """BaseModel for other classes"""

        def __init__(self, *args, **kwargs):
                """public instance attr"""
                if kwargs:
                    self.__dict__ = kwargs
                    if "created_at" in kwargs:
                        self.created_at = datetime.strptime(kwargs.get("created_at"),
                                                            cronos)
                    if "updated_at" in kwargs:
                        self.updated_at = datetime.strptime(kwargs.get("updated_at"),
                                                            cronos)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    models.storage.new(self)

        def __str__(self):
                """String rep of the BaseModel"""
                return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                                 self.id, self.__dict__)

        def save(self):
                """updates the attr updated_at"""
                self.updated_at = datetime.now()
                models.storage.save()

        def to_dict(self):
                """returns a dictionary with created_at and updated_at"""
                s_dict = self.__dict__.copy()
                s_dict["__class__"] = type(self).__name__
                for key, value in s_dict.items():
                    if isinstance(value, datetime):
                        s_dict[key] = value.strftime(cronos)
                return s_dict
