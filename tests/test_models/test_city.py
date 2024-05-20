#!/usr/bin/env python3
""" Tests for the City class """

import unittest
from models.base_model import BaseModel
from models.city import City


class Test_City(unittest.TestCase):
    """ Tests for the City class """

    def setUp(self):
        """ Instances to test City class """
        self.obj_1 = City()

    def test_inheritance(self):
        """ Test that City is a subclass of BaseModel """
        self.assertIsInstance(self.obj_1, BaseModel)

    def test_class_attributes(self):
        """ Tests for the City class attributes """
        self.assertTrue(hasattr(self.obj_1, "name"))
        self.assertTrue(hasattr(self.obj_1, "state_id"))
        self.assertEqual(self.obj_1.name, "")
        self.assertEqual(self.obj_1.state_id, "")

    def test_attribute_assignment(self):
        """ Test assigning and retrieving 'name' attribute """
        self.obj_1.name = "Gabriel"
        self.assertEqual(self.obj_1.name, "Gabriel")
        self.obj_1.state_id = "Lagos-12345"
        self.assertEqual(self.obj_1.state_id, "Lagos-12345")


if __name__ == "__main__":
    unittest.main()
