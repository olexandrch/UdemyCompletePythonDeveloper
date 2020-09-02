#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 142. list, set, dictionary comprehension
# https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3


# List comprehensions offer a succinct way to create lists based on existing lists.
# When using list comprehensions, lists can be built by leveraging any iterable, including strings and tuples.
# Syntactically, list comprehensions consist of an iterable containing an expression followed by a for clause.
# This can be followed by additional for or if clauses, so familiarity with for loops
# and conditional statements will help you understand list comprehensions better.
# List comprehensions provide an alternative syntax to creating lists and other sequential data types.
# While other methods of iteration, such as for loops, can also be used to create lists,
# list comprehensions may be preferred because they can limit the number of lines used in your program.

# For loop to create a new list
my_list1 = []

for char in 'hello':
    my_list1.append(char)

print("my_list1: ", my_list1)


# List comprehension to create a new list
my_list2 = [char for char in 'hello']
print("my_list2: ", my_list2)

my_list3 = [num for num in range(0, 20)]
print("my_list3: ", my_list3)

my_list4 = [num**2 for num in range(0, 20)]
print("my_list4: ", my_list4)

my_list5 = [num**2 for num in range(0, 20) if num % 2 == 0]
print("my_list5: ", my_list5)
