#!/usr/bin/env python3
""" Tests for the FileStorage class """

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import tempfile

class TestFileStorage(unittest.TestCase):
    """ Tests for the FileStorage class """

    def setUp(self):
        """Instances to test FileStorage class"""
        FileStorage._FileStorage__objects = {}
        self.storage = FileStorage()
        self.obj_1 = BaseModel()
        self.obj_1.id = "1234"
        self.obj_dict = self.obj_1.to_dict()

    def test_new(self):
        """ Tests for the new method"""
        self.storage.new(self.obj_1)
        key = "BaseModel.1234"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.obj_1)

     def test_save(self):
        self.storage.new(self.obj_1)
        self.storage.save()
        with open(self.temp_file.name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        key = "BaseModel.1234"
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], self.obj_dict['id'])
        self.assertEqual(data[key]['created_at'], self.obj_dict['created_at'])
        self.assertEqual(data[key]['updated_at'], self.obj_dict['updated_at'])


