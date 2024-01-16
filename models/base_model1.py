#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence


Base = declarative_base()

class BaseModel(Base):
	