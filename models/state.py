#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column,String
from sqlalchemy.orm import relationship 
import models 
from os import getenv  


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") =="db": 
        name = Column(String(128),nullabe=False)
        cities = relationship("Cities", backref="state", cascade="all,delete,delete-orphan")
    else:
        name =""

    @property
    def cities(self):
        state_list =[]
        dic = models.storage.all("City")
        for city in dic.items():
            if city.state_id == self.id:
                state_list.append(city)
        return state_list 
