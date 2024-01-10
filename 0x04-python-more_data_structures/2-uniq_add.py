#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list_set = set(my_list)
    unq_sum = 0
    for i in my_list_set:
        unq_sum += i
    return unq_sum
