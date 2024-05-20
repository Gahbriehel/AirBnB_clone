#!/usr/bin/env python3
""" Module for: Tests for the User class """


import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests for the User class"""

    def setUp(self):
        """Set up an instance for testing"""
        self.user = User()
        self.user1 = User().email
        self.user2 = User().first_name


    def test_inheritance(self):
        """Test that User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_class_attributes_initialization(self):
        """Test that User attributes are initialized correctly"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_class_attribute1(self):
        """ Test for email attribute """
        self.assertEqual(self.user1, "")


        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")

        self.assertEqual(self.user1, "")

        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        """Test assigning and retrieving attributes"""
        self.user.email = "user@example.com"
        self.user.password = "securepassword"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


if __name__ == "__main__":
    unittest.main()
