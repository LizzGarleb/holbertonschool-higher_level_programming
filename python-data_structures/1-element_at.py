#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return(None)
    list_len = len(my_list)
    if idx > list_len:
        return(None)
    print("Element at index {:d} is {:d}".format(idx, my_list[idx]))
