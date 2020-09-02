#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 122. Inheritance
# https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

# It means that you create a (child) class by deriving from another (parent) class. This way, we form a hierarchy.
# The child class reuses all fields and methods of the parent class (common part) and can implement its own (unique part).


class User:
    """ User Class. Don't have __init__ method, because there are no variables to init """

    def sign_in(self):
        """ sign in """
        print(f"User {self} is logged in")


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')



class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
wizard1.attack()
archer1.attack()

print("isinstance(wizard1, Wizard): ", isinstance(wizard1, Wizard))
print("isinstance(wizard1, User):   ", isinstance(wizard1, User))
print("isinstance(wizard1, object): ", isinstance(wizard1, object))