#!/usr/bin/env python3
"""
State Model for the HBNB Project
"""

from base_model import BaseModel

class State(BaseModel):
    """
    State Model that inherits from the BaseModel
    """
    name = ""

    def __init__(self, *arg, **kwargs):
        """
        Constructor for the State Model
        """
        super()__init__(**kwargs)
