#!/usr/bin/env bash
"""
A module that for the BaseModel class
"""


from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:

    """
    BaseModel: A class that defines all common attributes/methods for
    other classes
    """

    def __init__(self, *args, **kwargs):

        """
        Initializing the BaseModel class
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        prints the string representation of BaseModel.
         [<class name>] (<self.id>) <self.__dict__>
        """
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current date and time
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        dict_1["created_at"] = dict_1["created_at"].isoformat()
        dict_1["updated_at"] = dict_1["updated_at"].isoformat()
        return dict_1
