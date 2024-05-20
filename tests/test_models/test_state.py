#!/usr/bin/env python3
""" Module for: Tests for the State class """

import unittest
from models.base_model import BaseModel
from models.state import State


class Test_State(unittest.TestCase):
    """ Tests for the State class """

    def setUp(self):
        """ Instances to test State class """
        self.obj_1 = State()

    def test_inheritance(self):
        """ Test that State is a subclass of BaseModel """
        self.assertIsInstance(self.obj_1, BaseModel)

    def test_class_attributes(self):
        """ Tests for the State class attributes """
        self.assertTrue(hasattr(self.obj_1, "name"))

        self.assertEqual(self.obj_1.name, "")

    def test_attribute_assignment(self):
        """ Test assigning and retrieving 'name' attribute """
        self.obj_1.name = "Gabriel"

        self.assertEqual(self.obj_1.name, "Gabriel")


if __name__ == "__main__":
    unittest.main()
