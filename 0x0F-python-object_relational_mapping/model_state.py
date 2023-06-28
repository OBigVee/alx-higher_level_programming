#!/usr/bin/python3

"""
a State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import URL

# import MySQLdb

# conn = MySQLdb.connect(
#     host="localhost",
#     port=3036,

# )

url_object = URL.create(
    "mysql+mysqldb",
    username="root",
    password="thisme",
    host="localhost",
    database="hbtn_0e_6_usa",
)

Base = declarative_base()


class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


# engine = create_engine(url_object)
