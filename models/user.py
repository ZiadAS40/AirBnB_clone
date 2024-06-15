#!/usr/bin/python3
from models.base_model import BaseModel

"""create the user class that inhertits from BaseModel"""


class User(BaseModel):
    """define the User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
