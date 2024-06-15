#!/usr/bin/python3
from models.base_model import BaseModel


"""define the Review class"""


class Review(BaseModel):
    """
    define A Review class that inherits from
    the BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
