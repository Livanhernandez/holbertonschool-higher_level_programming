#!/usr/bin/python3
"""Provide a class that map to state table"""
# Module for Connecting to MySQL database
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class mapping table"""
    __tablename__ = 'States'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
        )

    name = Column(
        String(128),
        nullable=False
        )
