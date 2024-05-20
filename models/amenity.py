#!/usr/bin/env python3
"""
Amenity Model for the HBNB Project
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity Model that inherits from the BaseModel
    """
    name = ""

    def __init__(self, *args, *kwargs):
        """Amenity Constructor"""
        super().__init__(**kwargs)
