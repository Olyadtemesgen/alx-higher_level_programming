#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    number = 0
    for x in range(len(my_list)):
        sum += my_list[x][0] * my_list[x][1]
        number += my_list[x][1]
    answer = sum / number
    return answer
