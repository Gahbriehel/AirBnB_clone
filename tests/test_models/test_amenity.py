#!/usr/bin/env python3
""" Tests for the Amenity class """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """ Tests for the Amenity class """

    def setUp(self):
        """ Instances to test Amenity class """
        self.obj_1 = Amenity()

    def test_inheritance(self):
        """ Test that Amenity is a subclass of BaseModel """
        self.assertIsInstance(self.obj_1, BaseModel)

    def test_class_attributes(self):
        """ Tests for the Amenity class attributes """
        self.assertTrue(hasattr(self.obj_1, "name"))
        self.assertEqual(self.obj_1.name, "")

    def test_attribute_assignment(self):
        """ Test assigning and retrieving 'name' attribute """
        self.obj_1.name = "Gabriel"
        self.assertEqual(self.obj_1.name, "Gabriel")


if __name__ == "__main__":
    unittest.main()
