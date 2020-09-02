#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 128. Dunder Methods
# https://docs.python.org/3/reference/datamodel.html#special-method-names


class Toy():
    def __init__(self, color, age):
        self.color=color
        self.age = age

    # we can redifine dunder methods
    #def __str__(self):
    #    return f'{self.color}'

    def __call__(self):
        return("method __call_ is causing to run ()")

action_figure = Toy('red', 0)

print(action_figure.__str__())
print(str(action_figure))
print(action_figure())
