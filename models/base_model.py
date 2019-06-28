#!/usr/bin/python3
"""Base Model"""

import models
import json
import uuid
from datetime import datetime


class BaseModel:
	"""BaseModel for other classes"""
	def __init__(self, *args, **kwargs):
		"""public instance attr"""
		time = '%Y-%m-%dT%H:%M:%S.%f'
		if kwargs:
			for key, value in kwargs.items():
				if key != '__class__':
					setattr(self, key, value)
		if 'id' in kwargs.keys():
			self.id = kwargs['id']
			if 'created_at' in kwargs.keys():
				self.created_at = datetime.strptime(kwargs['created_at'],
													time)
			if 'updated_at' in kwargs.keys():
				self.updated_at = datetime.strptime(kwargs['updated_at'],
													time)
		else:
			self.id = str(uuid.uuid4())
			self.created_at = datetime.now()
			self.updated_at = self.created_at

	def __str__(self):
		"""String rep of the BaseModel"""
		return '[{:s}] ({:s}) {}'.format(self.__class__.__name__, self.id,
										 self.__dict__)

	def save(self):
		"""updates the attr updated_at"""
		self.updated_at = datetime.now()

	def to_dict(self):
		"""returns a dictionary with created_at and updated_at in iso format"""
		s_dic = self.__dict__.copy()
		s_dic['created_at'] = self.created_at.isoformat()
		s_dic['updated_at'] = self.updated_at.isoformat()
		s_dic['__class__'] = self.__class__.__name__
		return s_dic
