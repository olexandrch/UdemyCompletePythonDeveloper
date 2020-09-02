#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 127. introspection
# https://book.pythontips.com/en/latest/object_introspection.html

# introspection is the ability to determine the type of an object at runtime. It is one of Python’s strengths. Everything in Python is an object and we can examine those objects. Python ships with a few built-in functions and modules to help us.

# dir function

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        """ sign in """
        print(f"User {self} is logged in")


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
print(dir(wizard1))
