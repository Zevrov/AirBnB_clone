#!/usr/bin/python3
"""The console"""

import cmd
from datetime import datetime
import models


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
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
				keys = arguments[0] + "." + arguments[1]
				if keys in models.storage.all():
					print(models.storage.all()[keys])
				else:
					print("** no instance found **")
			else:
				print("** instance id missing **")
		else:
			print("** class doesn't exist **")
=======
        """HBNB console"""
        classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
                   "Place": Place, "Review": Review,
                   "State": State, "User": User}
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

        def do_update(self, args):
                """update or add attribute to instance passed in"""
                if line == '':
                        self.__print("** class name missing **")
                        return
                line = line.split(maxsplit=4)
                if line[0] not in self.__classes:
                        self.__print("** class doesn't exist **")
                        return
                if len(line) < 2:
                        self.__print("** instance id missing **")
                        return
                key = line[0] + '.' + line[1]
                if key not in self.__storage.all():
                        self.__print("** no instance found **")
                        return
                if len(line) < 3:
                        self.__print("** attribute name missing **")
                        return
                if len(line) < 4:
                        self.__print("** value missing **")
                        return
                obj = self.__storage.all()[key]
                value = eval(line[3])
                if line[2] in obj:
                        value = type(obj[line[2]])(value)
                obj[line[2]] = value
                self.__storage.save()
>>>>>>> 592709ed8483ce76f4bf9210fbb36fb451aef498

	def do_destroy(self, arg):
		"""deletes an instance based on class/id"""
		arguments = arg.split()
		if len(arguments) == 0:
			print("** class name missing **")
		elif arguments[0] in classes:
			if len(arguments) > 1:
				keys = arguments[0] + "." + arguments[1]
				if keys in models.storage.all()
				models.storage.all().pop(keys)
				models.storage.save()
				else:
					print("** no instance found **")
			else:
				print("** instance id missing **")
		else:
			print("** class doesn't exist **")

	def do_all(self, arg):
		"""prints all instances if they exist"""
		instances = storage.all()
		class_arg = "empty"
		if arg in self.classes:
			for keys, value in instances.items():
				if arg in key:
					print(value)
					class_arg = "instances exist"
				if class_arg == "empty":
					print("[]")
			else:
				print("** class doesn't exist **")
		else:
			for value in instances.values():
				print(value)

	def do_update(self, arg):
		"""updates instance based on class/id"""
		arguments = arg.split()
		float = ["latitude", "longitude"]
		int = ["number_rooms", "number_bathrooms", "max_guest", "price_by_night"]
		if len(arguments) == 0:
			print("** class name missing **")
		elif arguements[0] in classes:
			if len(arguments) > 1:
				keys = arguments[0] + "." + arguments[1]
				if keys in models.storage.all():
					if len(arguments) > 2:
						if len(arguments) > 3:
							if arguments[0] == "Place":
								if arguments[2] in int:
									try:
										arguments[3] = int(arguments[3])
									except:
										arguments[3] = 0
								elif arguments[2] in float:
									try:
										arguments[3] = float(arguments[3])
									except:
										arguments[3] = 0.0
							setattr(models.storage.all()[keys], arguments[2], arguemnts[3])
							models.storage.all()[keys].save()
						else:
							print("** value missing **")
					else:
						print("** attribute name missing **")
				else:
					print("** no instance found **")
			else:
				print("** instance id missing **")
		else:
			print("** class doesn't exist **")
if __name__ == '__main__':
        HBNBCommand().cmdloop()
