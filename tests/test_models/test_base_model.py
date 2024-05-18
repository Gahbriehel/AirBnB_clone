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
#        self.assertTrue(hasattr(self.obj_1, "created_at"))
#        self.assertTrue(hasattr(self.obj_1, "updated_at"))
        self.assertFalse(hasattr(self.obj_1, "kwargs"))

    def test_obj_types(self):
        """Tests for the data types of attributes"""
        self.assertIsInstance(self.obj_1.id, str)
        self.assertIsInstance(self.obj_1.created_at, datetime)
        self.assertIsInstance(self.obj_2.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test for the save method"""
        old_updated_at = self.obj_1.updated_at
        self.obj_1.save()
        new_updated_at = self.obj_1.updated_at

        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_returns_dict(self):
        obj_dict = self.obj_1.to_dict()

        self.assertIsInstance(obj_dict, dict)

        for key, value in self.obj_1.__dict__.items():
            if isinstance(value, datetime):
                value = value.isoformat()
            self.assertIn(key, obj_dict)
            self.assertEqual(obj_dict[key], value)

        self.assertIn("__class__", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")

        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertIsInstance(obj_dict["created_at"], str)
        self.assertIsInstance(obj_dict["updated_at"], str)


if __name__ == '__main__':
    unittest.main()
