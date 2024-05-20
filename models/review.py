#!/usr/bin/env python3
"""
Review Model for the HBNB Project
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review Model that inherits from the BaseModel
    """

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review Constructors"""
        super().__init__(**kwargs)
