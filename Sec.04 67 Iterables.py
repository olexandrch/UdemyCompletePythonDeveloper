#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 66. Iterable
# https://www.w3schools.com/python/python_iterators.asp

# iterable  - list, dictionary, tuple, set, string

user = {
    'name': 'Golem',
    'age': 5555,
    'can_swim': False
}

print(user)

for item in user.items():  # Iterate through keys:value pairs
    print (item)

for key, value in user.items():  # Iterate through keys:value pairs
    print (key, value)

for item in user:  # Iterate through keys
    print (item)

for item in user.keys():  # Iterate through keys
    print (item)


for item in user.values():   # Iterate through values
    print (item)
