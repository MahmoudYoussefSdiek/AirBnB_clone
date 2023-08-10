#!/usr/bin/python3
"""A module that defines a base class for all other classes"""

import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods
    for other classes

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The timestamp indicating when
        the instance was created.
        updated_at (datetime): The timestamp indicating when
        the instance was last updated.

    Methods:
        __init__(): Initializes a new instance of the BaseModel class.
        __str__(): Returns a string representation of the instance.
        save(): Updates the updated_at attribute with the current datetime.
        to_dict(): Returns a dictionary representation of the instance.
    """

    def __init__(self):
        """Initialize a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result
