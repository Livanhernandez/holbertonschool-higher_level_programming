#!/usr/bin/python3
"""Provide a class that map to state table"""

import sys
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class mapping table"""
    __tablename__ = 'States'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
