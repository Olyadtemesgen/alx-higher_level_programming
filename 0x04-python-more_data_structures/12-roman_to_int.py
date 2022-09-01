#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [data[x] for x in roman_string] + [0]
    result = 0
    for num in range(len(roman_string) - 1):
        if numbers[num] >= numbers[num + 1]:
            result += numbers[num]
        else:
            result -= numbers[num]
    result += numbers[len(roman_number) - 1]
    return result
