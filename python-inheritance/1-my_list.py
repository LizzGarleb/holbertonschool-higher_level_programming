#!/usr/bin/python3
"""
This module contains a child class
named MyList that inherit from list.
"""


class MyList(list):
    """
    This class inherts from list,
    it containd also a function that print
    a sorted list
    """
    def print_sorted(self):
        """
        This function prints a list sorted
        in ascending order of integers
        """
        list_sorted = []
        for num in self:
            list_sorted.append(num)
        list_sorted.sort()
        print(list_sorted)
