#!/usr/bin/python3
"""Function returns True if onj is instance
of a class that inherited from specified class"""


def inherits_from(obj, a_class):
    """Function returns True if onj is instance
    of a class that inherited from specified class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
