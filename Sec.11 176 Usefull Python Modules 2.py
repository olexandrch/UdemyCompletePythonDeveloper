#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 176. Useful Modules 2
# This is standard Python Library https://docs.python.org/3/py-modindex.html

import datetime
from array import array  # create an array with exact type of the elements

print(datetime.time())
print(datetime.time(15, 45, 2))
print(datetime.date.today())


arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1, 2, 3, 4, 5, 6])

print(arr1)
print(arr2)
print(arr1[2], arr2[2])
