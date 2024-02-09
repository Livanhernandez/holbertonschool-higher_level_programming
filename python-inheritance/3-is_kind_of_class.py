#!/usr/bin/python3
"""Function that returns True if obj is
instance"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if obj is
    instance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
