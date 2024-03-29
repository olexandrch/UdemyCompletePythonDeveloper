#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 150. Decorators
# https://www.programiz.com/python-programming/decorator

from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'it took {t2-t1} s')
        return result
    return wrap_func


@performance
def long_time():
    for i in range(100000000):
        i*5


long_time()
