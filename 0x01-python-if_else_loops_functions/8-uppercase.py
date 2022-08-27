#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for x in str:
        if ord(x) < 91 and ord(x) > 64:
            new_str += x
        elif ord(x) < 123 and ord(x) >96:
            x = chr(ord(x) - 32)
            new_str += x
        else:
            new_str += x
    print('{}'.format(new_str))
