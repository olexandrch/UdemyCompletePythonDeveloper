#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 170 sys Python Built-in Modules.py
# https://docs.python.org/3/library/sys.html#module-sys

import sys

fname = sys.argv[0]
first = sys.argv[1]
last = sys.argv[2]

print(f'Hi {first} {last} from "{fname}"')
