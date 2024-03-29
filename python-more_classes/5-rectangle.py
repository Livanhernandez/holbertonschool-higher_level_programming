#!/usr/bin/python3
"""my class"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        my_str = ""
        for _ in range(0, self.height):
            my_str += "#" * self.__width
            my_str += "\n"
        return my_str.strip()

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
