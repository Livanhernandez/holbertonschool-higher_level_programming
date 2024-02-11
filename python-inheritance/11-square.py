#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle
    (9-rectangle.py). (task based on 10-square.py)."""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self._Square__size = size

    def __str__(self):
        return f'[Square] {self._Square__size}/{self._Square__size}'
