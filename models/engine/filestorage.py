#!/usr/bin/python3

import json
from models.basemodel import BaseModel
from models.user import User


class filestorage:

    __file__path = "file.json"
    __objects = {}

    CLASSES = {
        'baseModel' : BaseModel,
        'User' : User 
    }

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized_object = {}
        for key, obj in self.__objects.items():
            serialized_object[key] = obj.to_dict()

        with open(self.__file__path, "w") as file:
            json.dump(serialized_object, file)

