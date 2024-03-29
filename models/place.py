#!/usr/bin/python3
"""
Module that contains a class
Place that inherits from BaseModel
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class Place that containts the attributes listed
    below

    Attributes:
    city_id: empty string: it will be the City.id
    user_id: empty string: it will be the User.id
    name: empty string
    description: empty string
    number_rooms: integer
    number_bathrooms: integer
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of string - empty list:
        it will be the list of Amenity.id later
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
