#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 135. map() function
# https://www.w3schools.com/python/ref_func_map.asp


# map(), filter(), zip(), reduce()
# map() function returns a map object(which is an iterator) of the results after applying
# the given function to each item of a given iterable (list, tuple etc.)


def multiply_by2(item):
    return item*2


print(list(map(multiply_by2, [1, 2, 3, 4])))
