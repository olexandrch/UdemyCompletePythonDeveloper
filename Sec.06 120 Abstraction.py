#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 120. Abstraction
# https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

# Applying abstraction means that each object should only expose a high-level mechanism for using it.
# This mechanism should hide internal implementation details. It should only reveal operations relevant for the other objects.


class PlayerCharacter:
    """ Example Class """

    def __init__(self, name, age):
        """ Example Setup """
        self.name = name
        self.age = age

    def run(self):
        """ Run """
        print(f"Run, {self.name}")

    def speak(self):
        """ Print name and age """
        print(f'May name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter("Sas", 99)

player1.run()
player1.speak()
