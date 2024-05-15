#!/usr/bin/env python3
""" Tests for the BaseModel class """

import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def setUp(self):
        """Instances to test BaseModel class"""
        self.obj_1 = BaseModel()
        self.obj_2 = BaseModel()

    def test_class_attributes(self):
        """Tests for the BaseModel class attributes"""
        self.assertTrue(hasattr(self.obj_1, "id"))
        self.assertTrue(hasattr(self.obj_1, "created_at"))
        self.assertTrue(hasattr(self.obj_1, "updated_at"))
        self.assertFalse(hasattr(self.obj_1, "kwargs"))
