#!/usr/bin/python
# https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 185. Regular Expressions

# https://docs.python.org/3/howto/regex.html
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

import re


string = 'search inside this text please! this, this, this Ha-Ha-Ha?'

print("'search' in string: ", 'search' in string)

a = re.search('this', string)
aa = a.group()

print('a: ', a)
print('a.span(): ', a.span())
print('string[a.start(): a.end()]: ', string[a.start(): a.end()])
print("aa: ", aa)

print("="*40)

pattern = re.compile('this')
aaa = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)

print("aaa: ", aaa)
print("b: ", b)
print("c: ", c)
print("d: ", d)
