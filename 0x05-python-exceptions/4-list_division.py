#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [None] * list_length
    for x in range(list_length):
        res = 0
        try:
            res = my_list_1[x] / my_list_2[x]
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by zero")
        except TypeError:
            print("wrong type")
        finally:
            result[x] = res
    return result
