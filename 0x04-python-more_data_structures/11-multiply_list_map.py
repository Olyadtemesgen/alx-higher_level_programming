#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda a, b: a * b, my_list.copy(), [number] * len(my_list.copy())))
