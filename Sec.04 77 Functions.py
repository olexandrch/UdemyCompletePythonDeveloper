#!/usr/bin/python
# Python 3          # https://www.udemy.com/course/complete-python-developer-zero-to-mastery/

# 77. Functions     # https://www.w3schools.com/python/python_functions.asp

def hello_function():
    print("Hello from a function") 
    
hello_function()

# 78. Parameters and Arguments
# name and emoji - parameters
def say_hello(name, emoji):
    print(f"Hello {name} from a function. Here is your {emoji}") 

# "Alex", ";-)" - arguments
say_hello("Alex", ";-)")
say_hello("Max", ";-)")


# 79. Default Parameters and Keyword Arguments
# keyword arguments
say_hello(emoji=':-O', name='WikiPedia')

# default parameters
def say_by(name='Darth Vader', emoji = ':-('):
    print(f"By-By {name} {emoji}") 

say_by()
say_by("Lllll")

# 80. Return

def sum(num1, num2):
    return num1+num2 

print (sum(2,3))
