#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 140. Lambda Expression
# https://www.w3schools.com/python/python_lambda.asp


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

from functools import reduce

print("map lambda item: item *2:",
      list(map(lambda item: item * 2, [1, 2, 3, 4, 5, 6, 7, 8])))

print("filter odd:  ", list(filter(lambda item: item %
                                   2 != 0, [1, 2, 3, 4, 5, 6, 7, 8])))

# zip()
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

# use the tuple() function to display a readable version of the result:
print(tuple(x))


# reduce()


print("reduce(do_sum, [1, 2, 3, 4]): ", reduce(
    lambda item1, item2: item1 + item2, [1, 2, 3, 4]))

fact = reduce(lambda item1, item2: item1 * item2, range(1, 10))
print('Factorial of 9: ', fact)
