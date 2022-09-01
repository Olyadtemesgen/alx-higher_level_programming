#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    number = 0
    if len(my_list) == 0:
        return 0
    for x in range(len(my_list)):
        sum += my_list[x][0] * my_list[x][1]
        number += my_list[x][1]
        result = sum / number
    return result
