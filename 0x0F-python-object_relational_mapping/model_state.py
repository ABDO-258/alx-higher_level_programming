#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys
Base = declarative_base()


class State(Base):
    """ class of state """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
