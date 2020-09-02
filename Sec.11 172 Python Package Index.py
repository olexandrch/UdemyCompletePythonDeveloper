#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 172. Python Package Index
# https://pypi.org/
# The Python Package Index (PyPI) is a repository of software for the Python programming language.
# This is standard Python Library https://docs.python.org/3/py-modindex.html

# 173. pip install
# Let's install a module. https://pypi.org/project/pyjokes/

"""
alex:$ pip -V
pip 20.1.1 from /usr/lib/python3.8/site-packages/pip (python 3.8)
[~]
alex:$ pip install pyjokes
Defaulting to user installation because normal site-packages is not writeable
Collecting pyjokes
  Using cached pyjokes-0.6.0-py2.py3-none-any.whl (26 kB)
Installing collected packages: pyjokes
Successfully installed pyjokes-0.6.0
[~]
alex:$ pyjoke
To understand recursion you must first understand recursion.
[~]
alex:$ pyjoke -c all
Old C programmers don't die, they're just cast into void.
"""


import pyjokes

print(pyjokes.get_joke('en', 'all'))
