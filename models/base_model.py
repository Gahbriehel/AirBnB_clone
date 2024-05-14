#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    This defines all common attributes or methods for other classes
    """
    def __init__(self):
        """
        Base Model Instructor
        """
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String format for BaseModel
        """

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        obj_dict = self.__dict__
        return obj_dict
