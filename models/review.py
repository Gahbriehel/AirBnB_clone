#!/usr/bin/env python3
"""
Review Model for the HBNB Project
"""

from base_model import BaseModel

class Review(BaseModel):
    """
    Review Model that inherits from the BaseModel
    """
    
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *arg, **kwargs):
        """
        Constructor for the Review Model
        """
        super()__init__(**kwargs)
