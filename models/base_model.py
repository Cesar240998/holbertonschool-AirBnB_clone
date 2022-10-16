#!/usr/bin/python3
"""This is the base model class for AirBnB"""
from uuid import uuid4
import os
from datetime import datetime
import models


class BaseModel:
    """This class will defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Constructor of Base Model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            from models import storage
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()


    def __str__(self):
        """Returns a string representation of BaseModel
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Save the new changes with the actual time
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    
    def to_dict(self):
        """Representation in a dictionary of an instance
        """
        rep = dict(self.__dict__)
        rep["__class__"] = self.__class__.__name__
        rep["created_at"] = rep["created_at"].isoformat()
        rep["updated_at"] = rep["updated_at"].isoformat()
        return (rep)
