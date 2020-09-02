#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 131. MRO Method Resolution Order
# http://www.srikanthtechnologies.com/blog/python/mro.aspx


class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


print("D.num: ", D.num)

print("D.mro(): ", D.mro())
