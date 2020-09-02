#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 144. Exercise comprehension
# https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3


# Exercise!
# Find duplicates and crete a LIST with the duplicates

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'n', 'n', 'b']

duplicates = list({char for char in some_list if some_list.count(char) > 1})

print(duplicates)
