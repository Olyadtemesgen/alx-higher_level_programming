#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = my_list[0]
    if len(my_list) == 0 or not my_list:
        return None
    for x in my_list[:1]:
        if x > largest:
            largest = x
    return largest
