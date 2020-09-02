#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 136. filter() function
# https://www.w3schools.com/python/ref_func_filter.asp


# map(), filter(), zip(), reduce()
# The filter() function returns an iterator were the items are filtered
# through a function to test if the item is accepted or not.


def multiply_by2(item):
    return item*2


def if_odd(item):
    return item % 2 != 0


def if_even(item):
    return item % 2 == 0


print("map multiply_by2:", list(map(multiply_by2, [1, 2, 3, 4, 5, 6, 7, 8])))

print("filter odd:  ", list(filter(if_odd, [1, 2, 3, 4, 5, 6, 7, 8])))

print("filter even: ", list(filter(if_even, [1, 2, 3, 4, 5, 6, 7, 8])))
