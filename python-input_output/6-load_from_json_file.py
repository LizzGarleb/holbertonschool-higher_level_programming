#!/usr/bin/python3
import json
"""
Function that creates an Object
from a JSON file
"""


def load_from_json_file(filename):
    """Creates an Object from a JSON file """
    with open(filename, 'r') as fd:
        return json.loads(fd.read())
