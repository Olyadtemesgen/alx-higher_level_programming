#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for x in range(len(my_list)):
        if my_list[x] != search:
            new.append(my_list[x])
        else:
            new.append(replace)            
    return new
