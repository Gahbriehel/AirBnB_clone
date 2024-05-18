#!/usr/bin/env python3
""" Tests for the FileStorage class """

import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class """

    def setUp(self):
        """ Instances to test FileStorage class """
        FileStorage._FileStorage__objects = {}
        self.storage = FileStorage()
        self.obj_1 = BaseModel()
        self.obj_1.id = "1234"
        self.obj_dict = self.obj_1.to_dict()
        self.file_path = "test_file.json"
        FileStorage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """ Cleaning up any created files """
        FileStorage._FileStorage__objects = {}
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """ Tests for the all method """
        self.storage.new(self.obj_1)
        all_objects = self.storage.all()
        key = "BaseModel.1234"
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], self.obj_1)

    def test_new(self):
        """ Tests for the new method"""
        self.storage.new(self.obj_1)
        key = "BaseModel.1234"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.obj_1)

    def test_save(self):
        """ Tests for the save method """
        self.storage.new(self.obj_1)
        self.storage.save()
        with open(self.file_path, "r") as file:
            data = json.load(file)
        key = "BaseModel.1234"
        self.assertIn(key, data)
        self.assertEqual(data[key], self.obj_dict)

    def test_reload(self):
        """ Tests for the reload method """
        self.storage.new(self.obj_1)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = "BaseModel.1234"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key].to_dict(), self.obj_dict)


if __name__ == "__main__":
    unittest.main()
