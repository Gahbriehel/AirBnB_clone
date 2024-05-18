#!/usr/bin/env python3
"""
City Model for the HBNB Project
"""

from models.base_model import BaseModel

class City(BaseModel):
    """
    City Model that inherits from the BaseModel
    """
    state_id = ""
    name = ""
