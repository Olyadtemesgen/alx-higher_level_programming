#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for a, b in a_dictionary.items():
        new[a] = b * 2
    return new
