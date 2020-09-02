#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 171. Exercise: Guessing Game
# program take two arguments - first and the last number and ask to guess the number in between

import sys
from random import randint

if len(sys.argv) < 3:
    print('usage is: python "Sec.11 171 Exercise. Guessing Game.py" 1 5')
    sys.exit(1)

min_num = int(sys.argv[1])
max_num = int(sys.argv[2])

number = randint(min_num, max_num)

while True:
    guess_str = input(f"Try to guess a number from {min_num} to {max_num}: ")
    try:
        guess = int(guess_str)
        if min_num <= guess <= max_num:
            if guess == number:
                print("That's right. Good Job!")
                break
        else:
            print(f"Number should be from {min_num} to {max_num} ")
    except ValueError:
        print(f"You have to guess numbers, not a string")


"""
alex:$ python "Sec.11 171 Exercise. Guessing Game.py" 1 5
Try to guess a number from 1 to 5: 1
Not exactly. Let's try again
Try to guess a number from 1 to 5: 2
Not exactly. Let's try again
Try to guess a number from 1 to 5: 3
That's right. Good Job!
"""
