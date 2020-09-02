#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 85. *args **kwargs
# Rule: params, *args, default parameters, **kwargs
# https://www.geeksforgeeks.org/args-kwargs-python/

def super_func(*args, **kwargs):
    '''
    Info: this function tests and prints param a
    '''
    print(*args)
    print(args)
    print(kwargs)
    total_kwargs = 0
    for items in kwargs.values():
        total_kwargs += items
    return sum(args) + total_kwargs


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))
