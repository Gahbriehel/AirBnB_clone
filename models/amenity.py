#!/usr/bin/env python3
"""
Amenity Model for the HBNB Project
"""

from base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity Model that inherits from the BaseModel
    """
    name = ""

    def __init__(self, *arg, **kwargs):
        """
        Constructor for the Amenity Model
        """
        super()__init__(**kwargs)
