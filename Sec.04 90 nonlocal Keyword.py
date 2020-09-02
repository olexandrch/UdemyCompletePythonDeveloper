#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 90. Scope. nonlocal Keyword


total = 0


def outer():
    '''
    Function to demonstrate nonlocal keyword
    '''
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("in the function inner, x = : ", x)

    print("in the function outer, before running inner(), x = : ", x)
    inner()
    print("in the function outer, x = : ", x)


outer()

x = 300


def my_func():
    global x
    x = 200


print("x before my_funct(): ", x)
my_func()
print("x after  my_funct(): ", x)
