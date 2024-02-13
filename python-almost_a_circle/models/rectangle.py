#!/usr/bin/python3
"""
Class Rectangle inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Class renctangle from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init my class"""
        super().__init__(id)
        self.validator("width", width)
        self.validator("height", height)
        self.validator("x", x)
        self.validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validator(self, attribute, value):
        """Int validator"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "width" or attribute == "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(attribute))
        else:
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
    
    def area(self):
        """returns area value"""
        return self.__width * self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validator("y", value)
        self.__y = value
