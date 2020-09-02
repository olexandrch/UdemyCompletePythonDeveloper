#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 134. Pure Functions
# https://www.pythoninformer.com/programming-techniques/functional-programming/pure-functions/


# The basic definition of a pure function is a function that doesn't cause or rely on side effects.
# The output of a pure function should only depend on its inputs.

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list


print(multiply_by2([1, 2, 3, 4]))
