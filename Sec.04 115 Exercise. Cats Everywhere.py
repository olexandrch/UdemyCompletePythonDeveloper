#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 115. Exercise: Cats Everywhere

# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat("Murka", 9)
cat2 = Cat("Marik", 11)
cat3 = Cat("Durik", 3)

# 2 Create a function that finds the oldest cat


def find_oldest(*args):
    ages = []
    for arg in args:
        ages.append(arg.age)
    return max(ages)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f"The oldest cat is {find_oldest(cat1, cat2, cat3)} years old.")
