#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for s in range(len(str)):
        if s < n:
            new_str += str[s]
        elif s > n:
            new_str += str[s]
        else:
            pass
    return '{}'.format(new_str)
