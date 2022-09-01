def roman_to_int(roman_string):
    dict1 = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1, 'A':0}
    roman = "MDCLXVI"
    number = 0
    list_roman = list(roman_string)
    final = list_roman[len(list_roman) - 1]
    for chars in list_roman[:len(list_roman) - 1]:
        if roman.index(chars) - roman.index(list_roman[list_roman.index(chars) + 1]) >= 1:
            number = number - dict1[chars] + dict1[list_roman[list_roman.index(chars) + 1]]
            list_roman[list_roman.index(chars):list_roman.index(chars) + 2] = 'A'
        else:
            number += dict1[chars]
    if len(list_roman) > 2 or len(list_roman) == 1:
        number += dict1[final]
    return number
roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))