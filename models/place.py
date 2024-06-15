#!/usr/bin/python3
from models.base_model import BaseModel


"""define the Place class"""


class Place(BaseModel):
    """
    define A Place class that inherits from
    the BaseModel
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
