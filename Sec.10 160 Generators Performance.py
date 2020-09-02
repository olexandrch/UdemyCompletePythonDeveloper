#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 160. Generators Performance

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
    print('1')
    for i in range(10**8):
        i*5


@performance
def long_time2():
    print('2')
    for i in list(range(10**8)):
        i*5


long_time()
long_time2()
