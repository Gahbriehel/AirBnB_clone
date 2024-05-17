#!/usr/bin/env python3
""" Tests for the FileStorage class """

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


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
