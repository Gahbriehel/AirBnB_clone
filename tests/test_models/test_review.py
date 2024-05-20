#!/usr/bin/env python3
""" Module for: Tests for the Review class """

import unittest
from models.base_model import BaseModel
from models.review import Review


class Test_Review(unittest.TestCase):
    """ Tests for the Review class """

    def setUp(self):
        """ Instances to test Review class """
        self.obj_1 = Review()

    def test_inheritance(self):
        """ Test that Review is a subclass of BaseModel """
        self.assertIsInstance(self.obj_1, BaseModel)

    def test_class_attributes(self):
        """ Tests for the Review class attributes """
        self.assertTrue(hasattr(self.obj_1, "place_id"))
        self.assertTrue(hasattr(self.obj_1, "user_id"))
        self.assertTrue(hasattr(self.obj_1, "text"))
        self.assertEqual(self.obj_1.place_id, "")
        self.assertEqual(self.obj_1.user_id, "")
        self.assertEqual(self.obj_1.text, "")

    def test_attribute_assignment(self):
        """ Test assigning and retrieving 'name' attribute """
        self.obj_1.place_id = "Gabriel"
        self.assertEqual(self.obj_1.place_id, "Gabriel")
        self.obj_1.user_id = "Lagos-12345"
        self.obj_1.text = "random text"

        self.assertEqual(self.obj_1.user_id, "Lagos-12345")
        self.assertEqual(self.obj_1.text, "random text")


if __name__ == "__main__":
    unittest.main()
