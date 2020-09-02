#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 169. Python Built-in Modules
# https://docs.python.org/3/py-modindex.html

import random

# help(random)
# dir(random.)

print(random.random())
print(random.randint(1, 10))

print(random.choice([101,102,103,104,105]))


my_list=[101,102,103,104,105]
random.shuffle(my_list)
print(my_list)
