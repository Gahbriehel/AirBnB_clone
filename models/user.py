#!/usr/bin/env python3
"""User Model derived from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for HBNB Project"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
        """
        User Constructor
        """
        super().__init__()
