#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        from math import sqrt
        try:
            sqrt(size)
            self.__size = size
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
