#!/usr/bin/env python3
"""
State Model for the HBNB Project
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State Model that inherits from the BaseModel
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """State Constructor"""
        super().__init__(**kwargs)
