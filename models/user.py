#!/usr/bin/env python3
"""User Model derived from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for HBNB Project"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *arg, **kwargs):
        """
        User Constructor
        """
        super().__init__(arg, kwargs)
