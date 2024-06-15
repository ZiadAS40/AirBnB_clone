#!/usr/bin/python3
from models.base_model import BaseModel


"""define the state class"""


class State(BaseModel):
    """
    define A State class that inherits from
    the BaseModel and have extra attrs:
    name: ->str
    """
    name = ""
