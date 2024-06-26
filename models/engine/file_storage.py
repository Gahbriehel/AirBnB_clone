#!/usr/bin/env python3
"""File storage engine"""

import json
import os


class FileStorage:
    """
    This class serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    # __class_list = ["BaseModel", "User"]

    def __init__(self):
        pass

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = type(obj).__name__ + "." + obj.to_dict()["id"]
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        file_name = FileStorage.__file_path
        with open(file_name, mode="w", encoding="UTF-8") as my_file:
            new_dict = {}
            for key, value in FileStorage.__objects.items():
                new_value = value.to_dict()
                new_dict[key] = new_value

            json.dump(new_dict, my_file, indent=4, sort_keys=True)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        + otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        class_list = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }

        file_name = FileStorage.__file_path
        new_dict = {}

        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                try:
                    new_obj = json.load(file)
                    for key, value in new_obj.items():
                        class_model = class_list[value["__class__"]]
                        new_dict[key] = class_model(**value)
                except json.JSONDecodeError:
                    pass

        FileStorage.__objects = new_dict.copy()
