#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 158. Generators
# https://realpython.com/introduction-to-python-generators/
# Generator functions are a special kind of function that return a lazy iterator.
# These are objects that you can loop over like a list.
# However, unlike lists, lazy iterators do not store their contents in memory.

# 158.

print(range(100))

print("158. ", "*" * 30)
print(list(range(20)))

print("158. ", "*" * 40)


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result


print(make_list(20))

# 159.

print("159. ", "*" * 40)


def generator_function():
    for i in range(10):
        yield i*2           # pause the function and return when it's time to work on the next item


for item in generator_function():
    print(item)

print("159. ", "*" * 50)

g = generator_function()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
