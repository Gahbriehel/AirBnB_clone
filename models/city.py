#!/usr/bin/env python3
"""
City Model for the HBNB Project
"""

from base_model import BaseModel

class City(BaseModel):
    """
    City Model that inherits from the BaseModel
    """
    state_id = ""
    name = ""

    def __init__(self, *arg, **kwargs):
        """
        Constructor for the City Model
        """
        super()__init__(**kwargs)
