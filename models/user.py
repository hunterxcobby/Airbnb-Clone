#!/usr/bin/python3

from models.basemodel import BaseModel

class User(BaseModel):

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""