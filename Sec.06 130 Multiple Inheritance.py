#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 130. Multiple Inheritance


class User():
    """ User Class. Don't have __init__ method, because there are no variables to init """

    def sign_in(self):
        """ sign in """
        print(f"User {self} is logged in")


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Wizard attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'arrows left - {self.num_arrows}')

    def run(self):
        print(f'{self.name}  run really fast ')


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, num_arrows)


wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
hb1 = HybridBorg("Borgyyy", 300, 400)


hb1.run()
hb1.attack()
hb1.check_arrows()
hb1.sign_in()
