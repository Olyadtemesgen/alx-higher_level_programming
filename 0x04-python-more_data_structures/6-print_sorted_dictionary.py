#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = []
    for x in a_dictionary:
        new.append(x)
    new.sort()
    for x in range(len(new)):
        print('{0}: {1}'.format(new[x], a_dictionary[new[x]]))
