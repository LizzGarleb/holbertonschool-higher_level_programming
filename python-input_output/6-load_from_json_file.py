#!/usr/bin/python
import json
def load_from_json_file(filename):
    with open(filename, 'r') as fd:
        return json.loads(fd.read())

