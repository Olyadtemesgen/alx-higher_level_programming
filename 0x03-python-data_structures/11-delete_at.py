#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    a = len(my_list) - 1
    if idx > len(my_list) - 1 or idx < 0:
        return my_list
    else:
        for x in range(len(my_list)):
            if x < idx:
                new_list.append(my_list[x])
            elif x > idx:
                new_list.append(my_list[x])
    del my_list[idx]
    my_list = new_list.copy()
    return my_list
