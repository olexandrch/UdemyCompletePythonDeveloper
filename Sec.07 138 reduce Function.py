#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 138. reduce() function
# https://thepythonguru.com/python-builtin-functions/reduce/
#


# map(), filter(), zip(), reduce()
# The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
# iterator is paired together, and then the second item in each passed iterator are paired together etc.
# If the passed iterators have different lengths, the iterator with the least items decides
# the length of the new iterator.


from functools import reduce


def multiply_by2(item):
    return item*2


def if_odd(item):
    return item % 2 != 0


print("map multiply_by2:", list(map(multiply_by2, [1, 2, 3, 4, 5, 6, 7, 8])))

print("filter odd:  ", list(filter(if_odd, [1, 2, 3, 4, 5, 6, 7, 8])))

# zip()
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)

# use the tuple() function to display a readable version of the result:
print(tuple(x))


# reduce()


def do_sum(x1, x2):
    return x1 + x2


print("reduce(do_sum, [1, 2, 3, 4]): ", reduce(do_sum, [1, 2, 3, 4]))


def mult(x, y):
    print("x=", x, " y=", y)
    return x*y


fact = reduce(mult, range(1, 10))
print('Factorial of 9: ', fact)
