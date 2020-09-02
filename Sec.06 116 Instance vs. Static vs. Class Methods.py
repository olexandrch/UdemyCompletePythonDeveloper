#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 116. Instance vs. Static vs. Class Methods in Python: The Important Differences
# https://www.makeuseof.com/tag/python-instance-static-class-methods/

# Instance Methods: The most common method type. Able to access data and properties unique to each instance.
# Static Methods: Cannot access anything else in the class. Totally self-contained code.
# Class Methods: Can access limited methods in the class. Can modify class specific details.

print("-"*80)
# Instance Methods


class DecoratorExample1:
    """ Example Class 1"""

    def __init__(self):
        """ Example Setup 1"""
        print('Hello, World! 1')
        self.name = 'Decorator_Example 1'

    def example_function(self):
        """ This method is an instance method! 1"""
        print('I\'m an instance method! 1')
        print('My name  1  is ' + self.name)


de = DecoratorExample1()
de.example_function()
print("-"*80)

# Static Methods


class DecoratorExample2:
    """ Example Class 2"""

    def __init__(self):
        """ Example Setup 2"""
        print('Hello, World!  2')

    @staticmethod
    def example_function():
        """ This method is a static method! 2"""
        print('I\'m a static method!  2')


de = DecoratorExample2.example_function()
print("-"*80)


# Class Methods
class DecoratorExample3:
    """ Example Class 3"""

    def __init__(self):
        """ Example Setup 3"""
        print('Hello, World! 3')

    @classmethod
    def example_function(cls):
        """ This method is a class method! 3"""
        print('I\'m a class method! 3')
        cls.some_other_function()

    @staticmethod
    def some_other_function():
        print('Hello!  3')


de = DecoratorExample3()
de.example_function()
print("-"*80)
