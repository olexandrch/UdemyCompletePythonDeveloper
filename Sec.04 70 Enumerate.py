#!/usr/bin/python

# Python 3
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 70. Enumerate

for i, char in enumerate('Hello!'):
    print (i, char)

print()

for i, N in enumerate((1,2,3,4)):
    print (i, N)

print()

for i, N in enumerate(list(range(100))):
    if N==50:
        print (f'index of 50 is: {i}')
