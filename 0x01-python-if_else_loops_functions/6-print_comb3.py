#!/usr/bin/python3
for x in range(10):
    for y in range(x + 1, 10):
        if str(x) + str(y) != '89':
            print('{}{}'.format(x,y), end=', ')
        else:
            print('89')
