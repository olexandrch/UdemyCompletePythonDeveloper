#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 126. super()
# https://realpython.com/python-super/
# https://stackoverflow.com/questions/222877/what-does-super-do-in-python

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
print(wizard1.email)
