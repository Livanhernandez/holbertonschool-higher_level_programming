#!/usr/bin/python3
"""comment Mudoule"""


class Student():
    """comment class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        obj_dict = {}
        if attrs is None:
            attrs = dir(self)
        for i in attrs:
            if i in dir(self):
                obj_dict[i] = getattr(self, i)
            return obj_dict
