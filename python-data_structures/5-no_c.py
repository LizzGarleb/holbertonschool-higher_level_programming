#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.tranlate({ord('cC'):None})
    return(new_str)
