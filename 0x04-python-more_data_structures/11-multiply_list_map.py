def multiply_list_map(my_list=[], number=0):
    new = my_list.copy()
    return list(map(lambda a, b: a * b, new, [number] * len(new)))