#!/usr/bin/python3
"""The console"""

import cmd
from datetime import datetime
import models


class HBNBCommand(cmd.Cmd):
	"""HBNB console"""
	classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
			   "Place": Place, "Review": Review, "State": State, "User": User}
	prompt = '(hbnb) '
	storage = models.storage

	def do_quit(self, arg):
		"""command to exit the program"""
		return True

	def do_EOF(self, arg):
		"""command to exit the console"""
		return True

	def emptyline(self):
		"""when line is empty do nothing"""
		return False

	def do_create(self, arg):
		"""creates a new class instance"""
		arguments = arg.split()
		if len(arguments) == 0:
			print("** class name missing **")
			return False
		else:
			if len(arguments) == 1 and arguments[0] in self.classes:
				instace = self.classes.get(arguments[0])()
				print(instance.id)
			else:
				print("** class doesn't exist **")
		storage.save()
	def do_show(self, arg):
		"""shows string rep of an instance
		class name and id
		"""
		arguments = arg.split()
		if len(arguments) == 0:
			print("** class name missing **")
			return False
		if arguments[0] in classes:
			if len(arguments) > 1:
				key = arguments[0] + "." + arguments[1]
				if key in models.storage.all():
					print(models.storage.all()[key])
				else:
					print("** no instance found **")
			else:
				print("** instance id missing **")
		else:
			print("** class doesn't exist **")

if __name__ == '__main__':
	HBNBCommand().cmdloop()
