#!/usr/bin/env python3
"""File storage engine"""

import json
import os


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

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
        key = type(obj).__name__ + "." + obj.id
        value = obj.to_dict()
        FileStorage.__objects[key] = value

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, mode="w", encoding="UTF-8") as my_file:
            json.dump(FileStorage.__objects, my_file, indent=4, sort_keys=True)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        + otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """

        from models.base_model import BaseModel
        file_name = FileStorage.__file_path
        new_dict = {}

        if os.path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as file:
                try:
                    new_obj = json.load(file)
                    for key, value in new_obj.items():
                        new_dict[key] = value
                except json.JSONDecodeError:
                    pass

        FileStorage.__objects = new_dict
