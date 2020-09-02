#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 119. Encapsulation
# https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

# Encapsulation is achieved when each object keeps its state private, inside a class. Other objects don’t have direct access to this state. Instead, they can only call a list of public functions — called methods.
# So, the object manages its own state via methods — and no other class can touch it unless explicitly allowed. If you want to communicate with the object, you should use the methods provided. But (by default) you can’t change the state.


class PlayerCharacter:
    """ Example Class """

    def __init__(self, name, age):
        """ Example Setup """
        self.name = name
        self.age = age

    def run(self):
        """ Run """
        print("Run")

    def speak(self):
        """ Print name and age """
        print(f'May name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter("Sas", 99)

player1.run()
player1.speak()
