#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 143. list, set, dictionary comprehension
# https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3


# List comprehensions offer a succinct way to create lists based on existing lists.
# When using list comprehensions, lists can be built by leveraging any iterable, including strings and tuples.
# Syntactically, list comprehensions consist of an iterable containing an expression followed by a for clause.
# This can be followed by additional for or if clauses, so familiarity with for loops
# and conditional statements will help you understand list comprehensions better.
# List comprehensions provide an alternative syntax to creating lists and other sequential data types.
# While other methods of iteration, such as for loops, can also be used to create lists,
# list comprehensions may be preferred because they can limit the number of lines used in your program.

# Set comprehension
my_set2 = {char for char in 'hello'}
print("my_set2: ", my_set2)

my_set3 = {num for num in range(0, 20)}
print("my_set3: ", my_set3)

my_set5 = {num**2 for num in range(0, 20) if num % 2 == 0}
print("my_set5: ", my_set5)

# Dictionary comprehension
simple_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
my_dict1 = {key: value**2 for key, value in simple_dict.items()}
print("my_dict1: ", my_dict1)

my_dict2 = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print("my_dict2: ", my_dict2)

my_dict3 = {num: num**2 for num in range(0, 9)}
print("my_dict3: ", my_dict3)
