#!/usr/bin/python3


def call_counter(func):
    def helper():
        helper.calls += 1
        return func()
    helper.calls = 0

    return helper


@call_counter
def magic_string():
    return 'BestSchoolssss, ' * (magic_string.calls - 1) + 'BestSchool'
