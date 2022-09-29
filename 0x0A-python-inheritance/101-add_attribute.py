#!/usr/bin/python3
"""It is a method that add an attribute"""


def add_attribute(obj, att, value):
    """it adds attribute
    Args:
        obj (any):it is an object.
        att (str): the attribute we want to add.
        value (any): the value we assign to an attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
