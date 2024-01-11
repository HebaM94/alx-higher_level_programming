#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cpy_dictionary = a_dictionary.copy()
    for i in cpy_dictionary.keys():
        cpy_dictionary[i] *= 2
    return cpy_dictionary
