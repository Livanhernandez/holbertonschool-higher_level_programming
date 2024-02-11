#!/usr/bin/python3
"""
Write a class BaseGeometry
(based on 6-base_geometry.py).
"""


class BaseGeometry:
    """
    Write a class BaseGeometry
    (based on 6-base_geometry.py).
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):

    """Write a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
