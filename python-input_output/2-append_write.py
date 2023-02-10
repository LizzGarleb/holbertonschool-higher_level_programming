#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    This function appends a tring at the
    end of a text file and return the number
    of characters added
    """
    with open(filename, 'a') as fd:
        return fd.write(text)
