#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# is means the same object in memory

print(True is True)
print('1' is '1')
print('2' is '2')
print([] is [])
print(() is ())
print(10 is 10.0)
print(10 is 10)
print([1,2,3] is [1,2,3])

print()

print([1,2,3] == [1,2,3])