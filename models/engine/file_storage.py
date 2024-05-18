#!/usr/bin/python3
import json
"""define the FileStorage Class"""


class FileStorage():
    """
    defines the FileStorage Class to serialize
    and deserializes the objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dict __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in the __objects the instance obj with the key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serialize objects to json files"""

        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(json_dict, json_file)

    def reload(self):
        """deserializes the JSON file"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as json_file:
                from models.base_model import BaseModel
                myLoader = json.load(json_file)

                for key, value in myLoader.items():
                    cls = value["__class__"]
                    obj = eval(cls + "(**value)")
                    FileStorage.__objects[key] = obj

        except IOError:
            pass
