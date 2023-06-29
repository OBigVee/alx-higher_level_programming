#!/usr/bin/python3
"""a State class
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """
    Class reps a state with it object
    corresponding instance name and and id
    for each object instantiated
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
