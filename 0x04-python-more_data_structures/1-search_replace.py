#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for x in range(len(my_list)):
        if my_list[x] != search:
            new.append(my_list[x])
        else:
            new.append(replace)            
    return new
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
