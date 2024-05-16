#!/usr/bin/env python3
"""File storage engine"""

import json

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
        class_dict = obj.to_dict()
        key = f"{class_dict.__class__}.{class_dict.id}"
        FileStorage.__objects[key] = class_dict


    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, mode='w+', encoding='UTF-8') as my_file:
            json.dump(FileStorage.__objects, my_file)


    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        + otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, encoding='UTF-8') as my_file:
                file_dict = json.load(my_file)
                FileStorage.__objects = file_dict.copy()
        except:
            pass

