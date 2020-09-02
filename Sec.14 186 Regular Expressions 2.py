#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 186. Regular Expressions

# https://docs.python.org/3/howto/regex.html
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

import re


string = 'search inside this text please! this, this, this Ha-Ha-Ha?'

a = re.search(r'[a-zA-Z]', string)
print('a: ', a)
b = re.findall(r'([a-zA-Z]).([H])', string)
print('b: ', b)


# 187. Exercises: Interactive RegEx
# https://regexone.com/


# 188. Regular Expressions 3

# E-mail validation
# https://emailregex.com/

string = 'ssasdcdfgf@erfbfd.dsf'

a = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", string)
print('a: ', a)
