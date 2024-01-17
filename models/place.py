#!/usr/bin/env python3
"""place Module"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String, Integer, Float
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """Represents a Place for MySQL database
    Inherits from BaseModel and Base (in this order)
    Attributes:-
        __tablename__(str): Represents Table name Places
        city_id(sqlalchemy String): Represents city id, fkey to cities.id
        user_id(sqlalchemy String): Represents user id, fkey to users.id
        name(sqlalchemy String): Represents city name
        description(sqlalchemy String): Represents city description
        number_rooms(sqlalchemy Integer): Represents number of rooms
        number_bathrooms(sqlalchemy Integer): Represents number of bathrooms
        max_guest(sqlalchemy Integer): Represents number of maximum guests
        price_by_night(sqlalchemy Integer): Represents price by night
        Latitude(sqlalchemy Float): Represents Latitude
        Longitude(sqlalchemy Float): Represents Longitude
    fkey -- Foriegn key    
    """

    __tablename__ = "places"
    city_id = Column(String(60),ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60),ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float) 
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")

