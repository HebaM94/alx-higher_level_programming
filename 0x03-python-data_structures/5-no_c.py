#!/usr/bin/python3
def no_c(my_string):
    exclude = {ord('c'): None, ord('C'): None}
    new_string = my_string.translate(exclude)
    return new_string
