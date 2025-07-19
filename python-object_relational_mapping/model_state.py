#!/usr/bin/python3
"""
This module defines the State class and Base instance for SQLAlchemy ORM.

The State class is mapped to the 'states' table in a MySQL database.
It includes an integer primary key 'id' and a string column 'name'.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Defines the 'states' table structure."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
