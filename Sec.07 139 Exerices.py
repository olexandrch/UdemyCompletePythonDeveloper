#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# Exercise map(), filter(), zip(), reduce()

from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def upper_str(ss):
    return ss.upper()


print(list(map(upper_str, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

my_numbers.sort()
print("tuple(zip(my_strings, my_numbers)):  ",
      tuple(zip(my_strings, my_numbers)))

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_50(item):
    if item > 50:
        return True
    else:
        return False


print("list(filter(over_50, scores)): ", list(filter(over_50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def add_numm(num1, num2):
    return num1+num2


all_numbers = my_numbers + scores

print("reduce(add_num,all_numbers):", reduce(add_numm, (my_numbers + scores)))
