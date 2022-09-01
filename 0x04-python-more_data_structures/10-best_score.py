#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None or len(a_dictionary) == 0:
        return None
    for a in a_dictionary:
        value = a
    for key, val in a_dictionary.items():
        if a_dictionary[value] < val:
            value = key
    return value
