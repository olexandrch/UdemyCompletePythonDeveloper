#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 141. Exercise Lambda Expression
# https://www.w3schools.com/python/python_lambda.asp


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


# Square
my_list = [5, 4, 3, 2]

print(list(map(lambda item: item ** 2, my_list)))


# List Sorting
a = [(0, 2), (4, 5), (9, 9), (10, -1), (5, 4)]

a.sort(key=lambda item: item[1])
print(a)
