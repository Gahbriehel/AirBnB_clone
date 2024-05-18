#!/usr/bin/env python3
"""
Place Model for the HBNB Project
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place Model that inherits from the BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []
