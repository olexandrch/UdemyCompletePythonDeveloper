#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 121. Private vs Public Variables
# https://www.freecodecamp.org/news/object-oriented-programming-concepts-21bb035f7260/

# Private variables in a class
# in Python there are no private variables

# Convention is to put _ before the _variable

class PlayerCharacter:
    """ Example Class """

    def __init__(self, name, age):
        """ Example Setup """
        self._name = name
        self._age = age

    def run(self):
        """ Run """
        print(f"Run, {self._name}")

    def speak(self):
        """ Print name and age """
        print(f'May name is {self._name}, and I am {self._age} years old')


player1 = PlayerCharacter("Sas", 99)
player1.name = "!!!! Changed Name !!!"

player1.run()
player1.speak()

print(player1.name)
