#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
    value = 0
    prev = 0
    for i in roman_string[::-1]:
        char = roman_num[i]
        if char >= prev:
            value += char
        else:
            value -= char
        prev = char
    return value
