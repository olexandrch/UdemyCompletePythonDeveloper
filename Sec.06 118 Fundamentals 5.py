#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 118. Developer Fundamentals 5

class PlayerCharacter:
    """ Example Class """

    def __init__(self, name, age):
        """ Example Setup """
        self.name = name
        self.age = age

    def run(self):
        """ Run """
        return(self)


player1 = PlayerCharacter("Sas", 99)

print(player1.run())
