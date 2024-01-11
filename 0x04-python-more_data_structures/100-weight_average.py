#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    numer = 0
    denom = 0
    for tuples in my_list:
        numer += tuples[0] * tuples[1]
        denom += tuples[1]
    ave = numer/denom
    return ave
