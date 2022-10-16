#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import models


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is not None:
            dic_class = {}
            for key, value in FileStorage.__objects.items():
                if value.__class__ == cls:
                    dic_class[key] = value
            return dic_class
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            # temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                FileStorage.__objects = json.load(f)
                for key, val in FileStorage.__objects.items():
                    # class_name = val["__class__"]
                    # class_name = models.classes[class_name]
                    # FileStorage.__objects[key] = class_name(**val)
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
    
    def delete(self, obj=None):
        """ delete obj from __objects"""
        for key, value in FileStorage.__objects.items():
            if obj is value:
                del FileStorage.__objects[key]
                self.save()
                break
Footer

