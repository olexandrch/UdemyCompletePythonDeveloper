#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 83. Docstrings - description of functions.

def test(a):
    '''
    Info: this function tests and prints param a
    '''
    print(a)


test('Aasqwed')

help(test)
print()
print()
print (test.__doc__)
