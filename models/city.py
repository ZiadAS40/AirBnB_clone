#!/usr/bin/python3
from models.base_model import BaseModel


"""define the City class"""


class City(BaseModel):
    """
    define A City class that inherits from
    the BaseModel and have extra attrs:
    state_id: ->str
    name: ->str
    """
    state_id = ""
    name = ""
