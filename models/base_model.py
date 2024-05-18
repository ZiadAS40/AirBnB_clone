#!/usr/bin/python3
import uuid
from datetime import datetime
from models import storage
""" the base modele"""


class BaseModel():
    """the base model(class) for the upcomming classes"""

    def __init__(self, *args, **kwargs):
        """
        initiate the instance with the attrs ->
        id - a unique id to the instance.
        created_at - the time that was created in.
        updated_at - the last time that was updated in.
        """
        for key in kwargs:
            if key == '__class__':
                continue

            if (key == "created_at" or key == "updated_at"):
                sestr = "%Y-%m-%dT%H:%M:%S.%f"
                kwargs[key] = datetime.strptime(kwargs[key], sestr)

            setattr(self, key, kwargs[key])

        if "id" not in kwargs.keys():
            self.id = str(uuid.uuid4())
        if "created_at" not in kwargs.keys():
            self.created_at = datetime.now()
        if "updated_at" not in kwargs.keys():
            self.updated_at = datetime.now()

        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self):
        """
        disply the class on a certain format
        """
        clsN = self.__class__.__name__
        return ("[{}] ({}) {}".format(clsN, self.id, self.__dict__))

    def save(self):
        """
        apdate the attr 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        convert the instance to a dict
        """
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
