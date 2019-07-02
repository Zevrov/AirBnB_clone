#!/usr/bin/python3
"""The console"""

import cmd
from datetime import datetime
import models


class HBNBCommand(cmd.Cmd):
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

if __name__ == '__main__':
        HBNBCommand().cmdloop()
