#!/usr/bin/python3
""""""
class MyInt(int):
    """it inverts """

    def __eq__(self, x):
        """Inverse == to !="""
        return self.real != x

    def __ne__(self, x):
        """inverse != to =="""
        return self.real == x
