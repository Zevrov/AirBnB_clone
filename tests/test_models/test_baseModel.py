#!/usr/bin/python3
"""BaseModel tests"""


import unittest
import io
from models.base_model import BaseModel
from datetime import datetime, timedelta
from time import sleep
from contestlib import redirect_stdout


class TestBaseModel(unittest.TestCase):
    """BaseModel tests"""

    def test_Correctid(self):
        """test for unique id"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertTrue((type(my_model1.id) is str))
        self.assertNotEqual(model1.id, model2.id)

    def test_updateDif(self):
        """Test if update changes"""
        model = BaseModel()
        self.assertEqual(model.created_at.second, model.updated_at.second)
        s1 = model.created_at.second
        sleep(1)
        model.name = "Holberton"
        s2 = model.updated_at.second
        self.assertEqual(s1, s2)

    def test_saveArgs(self):
        """Test save args"""
        model = BaseModel()
        self.assertRaises(TypeError, model.save, "Test")

    def test_correctStr(self):
        """test that str words"""
        model = BaseModel()
        f = io.StringIO()
        s = "[BaseModel] ({}) {}\n".format(model.id, model.__dict__)
        with redirect_stdout(f):
            print(model)
        self.assertEqual(f.getvalue(), s)

    def test_toDictArgs(self):
        """Test passing args"""
        model = BaseModel()
        self.assertRaises(TypeError, model.to_dict, "Test")
