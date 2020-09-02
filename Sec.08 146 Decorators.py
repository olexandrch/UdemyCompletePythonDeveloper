#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 146. Decorators
# https://www.programiz.com/python-programming/decorator

def hello():
    print('Helllloooooooo!')


greet = hello

del hello

greet()


# 148. Decorators 2

def my_decorator(func):
    def wrap_func():
        print('*'*10)
        func()
        print('*'*10)
    return wrap_func


@my_decorator
def hello():
    print('Hellooo!')


@my_decorator
def bye():
    print('Byeeeee!')


hello()
bye()

# It is the same as
hello2 = my_decorator(hello)
hello2()


# 148. Decorators 3


def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('*'*10)
        func(*args, **kwargs)
        print('*'*10)
    return wrap_func


@my_decorator2
def hello3(greeting, emoji=':-('):
    print(greeting, emoji)


hello3('Hi there!!!!!!!')
hello3('Hi there!!!!!!!', ":-)")
