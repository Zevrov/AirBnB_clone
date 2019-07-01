#!/usr/bin/python3
"""The console"""

import cmd
from datetime import datetime
import models


class HBNBCommand(cmd.Cmd):
	"""HBNB console"""
	prompt = '(hbnb)'

	def do_quit(self, arg):
		"""command to exit the program"""
		return True

	def do_EOF(self, arg):
		"""command to exit the console"""
		return True

	def emptyline(self):
		"""when line is empty do nothing"""
		return False

if __name__ == '__main__':
	HBNBCommand().cmdloop()
