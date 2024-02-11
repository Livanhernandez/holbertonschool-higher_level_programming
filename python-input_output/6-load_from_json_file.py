#!/usr/bin/python3
"""Comment Module"""
import json


def load_from_json_file(filename):
    """comment function"""
    with open(filename, 'r') as f:
        return json.load(f)
