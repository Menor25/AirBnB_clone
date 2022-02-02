#!/usr/bin/python
"""class that inherit from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class that inherit from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
