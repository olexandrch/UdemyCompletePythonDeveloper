#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 122. Polymorphism
# https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

# Simply put, polymorphism gives a way to use a class exactly like its parent so there’s no confusion with mixing types. But each child class keeps its own methods as they are.
# This typically happens by defining a (parent) interface to be reused. It outlines a bunch of common methods. Then, each child class implements its own version of these methods.
# Any time a collection (such as a list) or a method expects an instance of the parent (where common methods are outlined), the language takes care of evaluating the right implementation of the common method — regardless of which child is passed.

class User:
    """ User Class. Don't have __init__ method, because there are no variables to init """

    def sign_in(self):
        """ sign in """
        print(f"User {self} is logged in")

    def attack(self):
        print("Do Nothing for User")

class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


def player_attack(char):
    char.attack()

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)

player_attack(wizard1)
player_attack(archer1)

for char in (wizard1, archer1):
    char.attack()
