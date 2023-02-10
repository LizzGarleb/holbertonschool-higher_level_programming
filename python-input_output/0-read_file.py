#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as fd:
        for line in fd:
            print(line, end="")
