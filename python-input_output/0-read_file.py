#!/usr/bin/python3
"""
write a function that reads a text file
(UFT8) and prints it to stdout
"""


def read_file(filename=""):
    """
    write a function that reads a text file
    (UFT8) and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        a = f.read()
    print(a, end="")
