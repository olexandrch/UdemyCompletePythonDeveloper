#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 112. OOP. creating objects

class PlayerCharacter:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run, ', self.name)


player1 = PlayerCharacter("Sas", 16)
player2 = PlayerCharacter("Mas", 27)

print(player1)
print(player1.name, player1.age)
player1.run()
print(player2.name, player2.age)
