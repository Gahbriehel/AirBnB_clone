#!/usr/bin/env python3
"""BaseModel module"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    This class defines all common attributes or methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Base Model Constructor
        """

        if kwargs:
            # print(kwargs)
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    setattr(self, key, datetime.fromisoformat(value))
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        String format for BaseModel
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

        """
        if BaseModel.__isnewinstance is True:
            storage.new(self)
        storage.save()
        """

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__

        for key, value in obj_dict.items():
            if key in ["created_at", "updated_at"]:
                obj_dict[key] = value.isoformat()

        return obj_dict
