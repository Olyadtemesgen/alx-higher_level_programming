#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for char in my_string:
        if char not in "cC":
            a += char
    return '{}'.format(a)
