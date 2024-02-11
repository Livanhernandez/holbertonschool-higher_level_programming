#!/usr/bin/python3
"""comentario modulo"""
import json


def save_to_json_file(my_obj, filename):
    """comment definicion"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
