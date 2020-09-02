#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 175. Useful Modules
# This is standard Python Library https://docs.python.org/3/py-modindex.html

from collections import Counter, defaultdict, OrderedDict

list1 = [1, 2, 3, 4, 5, 6, 7, 7, 3, 3, 3, 3, 3, 3]
sentence = "blah blah blah thinking about pythonnnnnn"

print(Counter(list1))
print(Counter(sentence))


dictionary1 = {'a': 111, 'b': 222}
dictionary2 = defaultdict(lambda: 999, {'a': 111, 'b': 222})
dictionary3 = defaultdict(lambda: "Doesn't exist", {'a': 111, 'b': 222})

print(dictionary1['a'])
# print(dictionary1['c']) - this will give an error, because 'c' doesn't exist

print(dictionary2['b'])
print(dictionary2['c'])
print(dictionary3['c'])


dict1 = OrderedDict()
dict1['a'] = 11
dict1['b'] = 22

dict2 = OrderedDict()
dict2['a'] = 11
dict2['b'] = 22

dict3 = OrderedDict()
dict3['b'] = 22
dict3['a'] = 11

print("dict1==dict2:  ", dict1 == dict2)  # True, because the same order
print("dict1==dict3:  ", dict1 == dict3)  # False, because a different order

# Now dictionary are ordered, no need to use OrderedDict()

# https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/en/

# Changed in version 3.7: Dictionary order is guaranteed to be insertion order.
# This behavior was an implementation detail of CPython from 3.6.
