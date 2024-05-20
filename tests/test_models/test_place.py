#!/usr/bin/env python3
""" Tests for the Place class """

import unittest
from models.base_model import BaseModel
from models.place import Place


class Test_Place(unittest.TestCase):
    """ Tests for the Place class """

    def setUp(self):
        """ Instances to test class Place """
        self.obj_1 = Place()

    def test_inheritance(self):
        """ Test that Place is a subclass of BaseModel """
        self.assertIsInstance(self.obj_1, BaseModel)

    def test_class_attributes(self):
        """ Tests for the Place class attributes """
        self.assertTrue(hasattr(self.obj_1, "user_id"))
        self.assertTrue(hasattr(self.obj_1, "city_id"))
        self.assertTrue(hasattr(self.obj_1, "name"))
        self.assertTrue(hasattr(self.obj_1, "description"))
        self.assertTrue(hasattr(self.obj_1, "number_rooms"))
        self.assertTrue(hasattr(self.obj_1, "number_bathrooms"))

    def test_class_attributes2(self):
        """ More tests for the attributes of class Place """
        self.assertTrue(hasattr(self.obj_1, "max_guest"))
        self.assertTrue(hasattr(self.obj_1, "price_by_night"))
        self.assertTrue(hasattr(self.obj_1, "latitude"))
        self.assertTrue(hasattr(self.obj_1, "longitude"))
        self.assertTrue(hasattr(self.obj_1, "amenity_ids"))

    def test_equality_class_attributes(self):
        """ Tests for the equality of Place class attributes """
        self.assertEqual(self.obj_1.name, "")
        self.assertEqual(self.obj_1.city_id, "")
        self.assertEqual(self.obj_1.user_id, "")
        self.assertEqual(self.obj_1.description, "")
        self.assertEqual(self.obj_1.number_rooms, 0)
        self.assertEqual(self.obj_1.number_bathrooms, 0)
        self.assertEqual(self.obj_1.max_guest, 0)
        self.assertEqual(self.obj_1.price_by_night, 0)
        self.assertEqual(self.obj_1.latitude, 0.0)
        self.assertEqual(self.obj_1.longitude, 0.0)
        self.assertEqual(self.obj_1.amenity_ids, [])

    def test_attribute_assignment(self):
        """ Test assigning and retrieving 'name' attribute """
        self.obj_1.city_id = "Lagos-12345"
        self.assertEqual(self.obj_1.city_id, "Lagos-12345")
        self.obj_1.name = "Gabriel"
        self.assertEqual(self.obj_1.name, "Gabriel")
        self.obj_1.user_id = "Gabriel-12345"
        self.assertEqual(self.obj_1.user_id, "Gabriel-12345")
        self.obj_1.description = "Big room"
        self.assertEqual(self.obj_1.description, "Big room")


if __name__ == "__main__":
    unittest.main()
